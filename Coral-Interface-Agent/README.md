## [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
 
User Interaction Agent is the main interface for receiving user instructions, coordinating multi-agent tasks, and logging conversations via the terminal.

## Responsibility
User Interaction Agent acts as the main interface for coordinating user instructions and managing multi-agent tasks. It interacts with the user via terminal and orchestrates requests among various agents, ensuring seamless workflow and conversation logging.

## Details
- **Framework**: LangChain
- **Tools used**: Coral MCP Tools, ask_human Tool (human-in-the-loop)
- **AI model**: GPT-4.1
- **Date added**: June 4, 2025
- **License**: MIT

## Use the Agent in Orchestration

### 1. Executable Agent Definition

<details>

For Linux or MAC:

```bash
# PROJECT_DIR="/PATH/TO/YOUR/PROJECT"

applications:
  - id: "app"
    name: "Default Application"
    description: "Default application for testing"
    privacyKeys:
      - "default-key"
      - "public"
      - "priv"

registry:
  interface:
    options:
      - name: "API_KEY"
        type: "string"
        description: "API key for the service"
    runtime:
      type: "executable"
      command: ["bash", "-c", "${PROJECT_DIR}/run_agent.sh main.py"]
      
      environment:
        - name: "API_KEY"
          from: "API_KEY"
        - name: "MODEL"
          value: "gpt-4.1"
        - name: "LLM_MODEL_PROVIDER"
          value: "openai"
```

For Windows, create a powershell command and run:

```bash
command: ["powershell","-ExecutionPolicy", "Bypass", "-File", "${PROJECT_DIR}/run_agent.ps1","main.py"]
```

</details>

## Use the Agent in Dev Mode

### 1. Clone & Install Dependencies


<details>  

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. If you are trying to run Interface agent and require coordination with other agents, you can run additional agents that communicate on the coral server.

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Coral-Interface-Agent.git

# Navigate to the project directory:
cd Coral-Interface-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>
 

### 2. Configure Environment Variables

<details>
 
Get the API Key:
[OpenAI](https://platform.openai.com/api-keys)


```bash
# Create .env file in project root
cp -r .env_sample .env
```
</details>


### 3. Run Agent

<details>

```bash
# Run the agent using `uv`:
uv run python 0-langchain-interface.py
```
</details>


### 4. Example

<details>


```bash
# Input:
Agent: How can I assist you today?

#Output:
The agent will interact with you directly in the console and coordinate with other agents as needed.
```
</details>


## Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)
