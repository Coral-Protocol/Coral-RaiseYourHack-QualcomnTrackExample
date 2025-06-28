import urllib.parse
from dotenv import load_dotenv
import os, json, asyncio, traceback
from langchain.chat_models import init_chat_model
from langchain.prompts import ChatPromptTemplate
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import Tool
import logging
import traceback

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

base_url = os.getenv("CORAL_SSE_URL")
agentID = os.getenv("CORAL_AGENT_ID")

coral_params = {
    "agentId": agentID,
    "agentDescription": "An agent that takes the user's input and interacts with other agents to fulfill the request"
}

query_string = urllib.parse.urlencode(coral_params)

def get_tools_description(tools):
    return "\n".join(
        f"Tool: {tool.name}, Schema: {json.dumps(tool.args).replace('{', '{{').replace('}', '}}')}"
        for tool in tools
    )

async def ask_human_tool(question: str) -> str:
    print(f"Agent asks: {question}")
    response = input("Your response: ")
    return response

async def create_agent(coral_tools, agent_tools, runtime):
    coral_tools_description = get_tools_description(coral_tools)
    
    if runtime == "docker" or runtime == "executable":
        agent_tools_for_description = [
            tool for tool in coral_tools if tool.name in agent_tools
        ]
        agent_tools_description = get_tools_description(agent_tools_for_description)
        combined_tools = coral_tools + agent_tools_for_description
        user_interaction_tool = "request_question"
        print(agent_tools_description)
    else:
        # For other runtimes (e.g., devmode), agent_tools is a list of Tool objects
        agent_tools_description = get_tools_description(agent_tools)
        combined_tools = coral_tools + agent_tools
        user_interaction_tool = "ask_human"

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            f"""You are an agent interacting with the tools from Coral Server and using your own `{user_interaction_tool}` tool to communicate with the user. **You MUST NEVER finish the chain**

            Follow these steps in order:
            1. Use tool `{user_interaction_tool}` to ask: "How can I assist you today?" and wait for the response.
            2. Use `list_agents` to list all connected agents and get their descriptions.
            3. Understand the user's intent and decide which agent(s) are needed based on their descriptions.
            4. If the user requests Coral Server information (e.g., agent status, connection info), use your tools to retrieve and return the information directly to the user, then go back to Step 1.
            5. If fulfilling the request requires multiple agents, then call
            `create_thread ('threadName': , 'participantIds': [ID of all required agents, including yourself])` to create conversation thread.
            6. For each selected agent:
            * **If the required agent is not in the thread, add it by calling `add_participant(threadId=..., 'participantIds': ID of the agent to add)`.**
            * Construct a clear instruction message for the agent.
            * Use **`send_message(threadId=..., content="instruction", mentions=[Receive Agent Id])`.** (NEVER leave `mentions` as empty)
            * Use `wait_for_mentions(timeoutMs=60000)` to receive the agent's response up to 5 times if no message received.
            * Record and store the response for final presentation.
            7. After all required agents have responded, take 2 seconds and think about the content to ensure you have executed the instruction to the best of your ability and the tools. Make this your response as "answer".
            9. Always respond back to the user with the "answer" or error occurred even if you have no answer or error.
            10. Repeat the process from Step 1.
            
            These are the list of coral tools: {coral_tools_description}
            These are the list of agent tools: {agent_tools_description}"""
        ),
        ("placeholder", "{agent_scratchpad}")
    ])
    print(prompt)

    model = init_chat_model(
        model=os.getenv("MODEL"),
        model_provider=os.getenv("LLM_MODEL_PROVIDER"),
        api_key=os.getenv("API_KEY"),
        temperature=0.3,
        max_tokens=16000
    )
    agent = create_tool_calling_agent(model, combined_tools, prompt)
    return AgentExecutor(agent=agent, tools=combined_tools, verbose=True)

async def main():
    CORAL_SERVER_URL = f"{base_url}?{query_string}"
    logger.info(f"Connecting to Coral Server: {CORAL_SERVER_URL}")

    client = MultiServerMCPClient(
        connections={
            "coral": {
                "transport": "sse",
                "url": CORAL_SERVER_URL,
                "timeout": 600,
                "sse_read_timeout": 600,
            }
        }
    )
    logger.info("Coral Server Connection Established")

    coral_tools = await client.get_tools(server_name="coral")
    logger.info(f"Coral tools count: {len(coral_tools)}")

    runtime = os.getenv("CORAL_ORCHESTRATION_RUNTIME", "devmode")
    
    if runtime == "docker" or runtime == "executable":
        required_tools = ["request-question", "answer-question"]
        available_tools = [tool.name for tool in coral_tools]

        for tool_name in required_tools:
            if tool_name not in available_tools:
                error_message = f"Required tool '{tool_name}' not found in coral_tools. Please ensure that while adding the agent on Coral Studio, you include the tool from Custom Tools."
                logger.error(error_message)
                raise ValueError(error_message)        
        agent_tools = required_tools

    else:
        agent_tools = [
            Tool(
                name="ask_human",
                func=None,
                coroutine=ask_human_tool,
                description="Ask the user a question and wait for a response."
            )
        ]
    
    agent_executor = await create_agent(coral_tools, agent_tools, runtime)

    while True:
        try:
            logger.info("Starting new agent invocation")
            await agent_executor.ainvoke({"agent_scratchpad": []})
            logger.info("Completed agent invocation, restarting loop")
            await asyncio.sleep(1)
        except Exception as e:
            logger.error(f"Error in agent loop: {str(e)}")
            logger.error(traceback.format_exc())
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())