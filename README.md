# Coral Raise Your Hack Guide

## About Raise Your Hack 💻
This is your chance to push boundaries, solve real-world challenges, and create impact at the official hackathon of the [RAISE Summit 2025](https://www.raisesummit.com/) at one of Paris's most iconic venues: Le Carrousel du Louvre. RAISE Summit 2025 is a premier event convening the brightest minds across industries to accelerate innovation and drive the future of entrepreneurship, AI, and technology.

## About Coral Protocol 🪸

The [Coral Protocol](https://www.coralprotocol.org/) is an initiative to create an open, standardized infrastructure for AI agent coordination. It builds on the MCP framework to enable multiple AI agents to work together collaboratively, addressing the limitation of isolated AI systems that lack mechanisms for interconnected workflows. The Coral Protocol focuses on:

- Agent Collaboration: Allowing AI agents to communicate, share tasks, and coordinate in a structured way.

- Messaging Layer: Providing a system for agents to exchange messages, similar to human messaging platforms, with features like threads and mentions.

- Scalability and Openness: Designing an extensible, open-source solution that can support a wide range of AI applications, from customer support to project management.

We released the [Coral Server](https://github.com/Coral-Protocol/coral-server) as an open-source MCP server to serve as the backbone for this vision. The server acts as a messaging hub where AI agents can register, communicate via threads, and coordinate tasks by mentioning each other. The protocol aims to foster a community-driven ecosystem, encouraging developers to experiment, contribute, and build collaborative AI systems.

## About the Tracks 🎯

Coral Protocol is encouraged for teams interested in multi-agent systems, allowing them to integrate open-source agents from any framework. With its thread-based agent architecture, Coral enables scalable and predictable multi-agent interactions, making it a powerful tool for innovative applications. Build on one of the below tracks using Coral Protocol.

### Qualcomm Track

🧠 Edge AI Consumer Utility Application

<details>

Build a powerful, AI-driven utility app for everyday users—right at the edge.
In this track, you'll will develop a consumer-facing utility application that runs entirely on-device using the Snapdragon X Elite platform. The challenge is to harness the power of Edge AI to create a tool that is both useful and accessible to a broad audience—without relying on cloud connectivity.

🔍 What We’re Looking For:

• Consumer-Oriented: The app should appeal to a wide range of users and offer clear, everyday value.
• Utility-Focused: It must help users accomplish a task—whether it's organizing, creating, assisting, or enhancing their experience.
• Edge AI-Powered: The core functionality should include a probabilistic AI component (e.g., computer vision, audio processing, or generative AI) that runs locally in a resource-constrained environment.
• Cross-Platform: While the app targets Snapdragon X Elite, it should be compatible with Windows, macOS, and Linux.
• Developer-Ready: Submissions should include a GitHub repository with setup and run instructions. A polished consumer UI is not required—focus on functionality and innovation.

🛠️ Tech Flexibility:

• Use any programming language or framework.
• Combine multiple AI modalities (CV, audio, Gen AI) as needed.
• No internet connection should be required for core functionality.

Qualcomm will directly ship the Copilot+ PC with the Snapdragon® X Elite (loaner devices) to selected participants and collect them at the conclusion of the hackathon.

The hardware will be shipped on June 30th with next-day delivery.

</details>


## Coral Example Usage 🎮

Checkout: [How to Build a Multi-Agent System with Awesome Open Source Agents using Coral Protocol](https://github.com/Coral-Protocol/existing-agent-sessions-tutorial-private-temp) to get started on building on Coral Protocol, set-up as per the given instructions and choose/ create agents as per your requirement.

### Qualcomm Track: Personal Finance Advisor

- Personal finance advisor system that  to provides secure, intelligent, and privacy-preserving financial management through natural language interaction using Coral Monzo Agent.
- The Monzo Agent enables users to safely access and analyze their Monzo banking data using a local LLM, ensuring sensitive information never leaves their device. By integrating with Monzo’s official API and customized toolkits, the system supports conversational account balance checks, transaction history queries, and personalized financial advice.
- Agents: [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) | [Monzo Agent](https://github.com/Coral-Protocol/Coral-Monzo-Agent)
- [Demo Video](https://drive.google.com/file/d/11A0sDDd2bpit54RNpXSNKxJfJOpatDkU/view?usp=sharing)


<details>

### 1. How to set up local model:

<details>

<summary>Click to expand Ollama instructions</summary>

Monzo Agent uses Ollama to run local LLM. Please make sure you have Ollama installed and the desired model downloaded before running the agent.

**1. Install Ollama**

- **Linux/macOS:**
  Follow the official instructions: [https://ollama.com/download](https://ollama.com/download)
  Or run:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```
- **Windows:**
  Download the installer from [Ollama's website](https://ollama.com/download).

**2. Download Local model**

```bash
ollama pull qwen3:latest
```

**3. Start Ollama Service**

Ollama usually starts automatically. If not, start it manually:
```bash
ollama serve
```

**4. Verify the model is running**

```bash
ollama list
```
Make sure no errors occur and Ollama is running at `http://localhost:11434`.

</details>

### 2. How to run:

<details>

<summary>Option 1: Agents running on docker without orchestrator:</summary>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system

#### 1. Git clone and pull docker image

```bash
# Clone the repository
git clone https://github.com/Coral-Protocol/Qualcomn-Track-use-case-example----Personal-finance-advisor.git

# Pull docker images
docker pull coralprotocol/coral-interface-agent
docker pull coralprotocol/coral-monzo-agent
```

#### 2. Environment Configuration

##### For Coral Interface Agent:
Get the API Key: [OpenAI](https://platform.openai.com/api-keys).

Create a `.env` file in the `Coral-Interface-Agent` directory based on the `.env_sample` file:
```bash
cd Coral-Interface-Agent
cp -r .env_sample .env
# Edit .env with your specific configuration
```

##### For Monzo Agent:
Get the `MONZO_ACCESS_TOKEN` and `MONZO_ACCOUNT_ID`:[Monzo Developer Portal](https://developers.monzo.com/).

Create a `.env` file in the `Coral-Monzo-Agent` directory based on the `.env.example` file:
```bash
cd Coral-Monzo-Agent
cp -r env_example .env
# Edit .env with your specific configuration
```

#### 3. Run Agents in Separate Terminals

##### For Coral Interface Agent:

```bash
cd Coral-Interface-Agent
docker run --network host --env-file .env -it coralprotocol/coral-interface-agent
```

##### For Monzo Agent:

```bash
cd Coral-Monzo-Agent
docker run --network host --env-file .env -it coralprotocol/coral-monzo-agent
```

</details>

<details>

<summary>Option 2: Agents running on docker with orchestrator:</summary>

#### 1. Follow the steps in [How to Build a Multi-Agent System with Awesome Open Source Agents using Coral Protocol](https://github.com/Coral-Protocol/existing-agent-sessions-tutorial-private-temp)

#### 2. Pull the docker image

```bash
docker pull coralprotocol/coral-interface-agent
docker pull coralprotocol/coral-monzo-agent
```

#### 3. Update the config by updating the "application.yml" file

```bash
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
      - name: "OPENAI_API_KEY"
        type: "string"
        description: "OpenAI API Key"
      - name: "HUMAN_RESPONSE"
        type: "string"
        description: "Human response to be used in the interface agent"

    runtime:
      type: "docker"
      image: "coralprotocol/coral-interface-agent:latest"
      environment:
        - name: "API_KEY"
          from: "OPENAI_API_KEY"
        - name: "HUMAN_RESPONSE"
          from: "HUMAN_RESPONSE"

  monzo:
    options:
      - name: "MONZO_ACCESS_TOKEN"
        type: "string"
        description: "monzo access token"
      - name: "MONZO_ACCOUNT_ID"
        type: "string"
        description: "monzo account id"

    runtime:
      type: "docker"
      image: "coralprotocol/coral-monzo-agent:latest"
      environment:
        - name: "MONZO_ACCESS_TOKEN"
          from: "MONZO_ACCESS_TOKEN"
        - name: "MONZO_ACCOUNT_ID"
          from: "MONZO_ACCOUNT_ID"
```


</details>

<details>

<summary>Option 3: Agents running on executable with orchestrator:</summary>

#### 1. Follow the steps in [How to Build a Multi-Agent System with Awesome Open Source Agents using Coral Protocol](https://github.com/Coral-Protocol/existing-agent-sessions-tutorial-private-temp)

#### 2. Git clone the repository

```bash
# Clone the repository
git clone https://github.com/Coral-Protocol/Qualcomn-Track-use-case-example----Personal-finance-advisor.git
cd Qualcomn-Track-use-case-example----Personal-finance-advisor
```
#### 3. Update the config by updating the "application.yml" file

```bash
applications:
  - id: "app"
    name: "Default Application"
    description: "Default application for testing"
    privacyKeys:
      - "default-key"
      - "public"
      - "priv"

# Registry of agents we can orchestrate
registry:
  interface-local:
      options:
        - name: "OPENAI_API_KEY"
          type: "string"
          description: "OpenAI API Key"
        - name: "HUMAN_RESPONSE"
          type: "string"
          description: "Human response to be used in the interface agent"
  
      runtime:
        type: "executable"
        command:
          [
            "bash",
            "-c",
            "cd ../Coral-Interface-Agent && uv sync && uv run 0-langchain-interface.py",
          ]
        environment:
          - name: "API_KEY"
            from: "OPENAI_API_KEY"
          - name: "HUMAN_RESPONSE"
            from: "HUMAN_RESPONSE"

  Monzo:
      options:
        - name: "MONZO_ACCESS_TOKEN"
          type: "string"
          description: "monzo access token"
        - name: "MONZO_ACCOUNT_ID"
          type: "string"
          description: "monzo account id"
  
      runtime:
        type: "executable"
        command:
          [
            "bash",
            "-c",
            "cd ../Coral-Monzo-Agent && uv sync && uv run langchain-monzo-agent.py",
          ]
        environment:
          - name: "MONZO_ACCESS_TOKEN"
            from: "MONZO_ACCESS_TOKEN"
          - name: "MONZO_ACCOUNT_ID"
            from: "MONZO_ACCOUNT_ID"
```


</details>

<details>

<summary>Option 4: Agents running without docker or orchestrator:</summary>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system

#### 1. Git clone the repository and install dependencies

```bash
# Clone the repository
git clone https://github.com/Coral-Protocol/Qualcomn-Track-use-case-example----Personal-finance-advisor.git

# Install `uv`:
pip install uv
```

##### For Coral Interface Agent
```bash
# Navigate to the interface agent agent directory
cd Coral-Interface-Agent

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

##### For Monzo Agent
```bash
# Navigate to the monzo agent directory
cd Coral-Monzo-Agent

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

#### 2. Environment Configuration

##### For Coral Interface Agent
Get the API Key: [OpenAI](https://platform.openai.com/api-keys).

Create a `.env` file in the `Coral-Interface-Agent` directory based on the `.env_sample` file:
```bash
cd Coral-Interface-Agent
cp -r .env_sample .env
# Edit .env with your specific configuration
```

##### For Monzo Agent
Get the `MONZO_ACCESS_TOKEN` and `MONZO_ACCOUNT_ID`:[Monzo Developer Portal](https://developers.monzo.com/).

Create a `.env` file in the `Coral-Monzo-Agent` directory based on the `.env.example` file:
```bash
cd Coral-Monzo-Agent
cp -r env_example .env
# Edit .env with your specific configuration
```

#### 3. Run Agents in Separate Terminals

###### For Coral Interface Agent:

```bash
cd Coral-Interface-Agent
uv run 0-langchain-interface.py
```

###### For Monzo Agent:

```bash
cd Coral-Monzo-Agent
uv run langchain-monzo-agent.py
```

</details>

### 3. How to use:

<details>

<summary>Click to expand sample input/output</summary>

#### 1. Input

```bash
Help me check my transections of monzo for the last 2 months and give me some personal finance advice.
```

#### 2. Output

```bash
Answer: Here is a summary of your Monzo transactions for the past 2 months:
- May 1: -£22.00 (University, bills)
- May 14: -£120.00 (Person A, general)
- May 14: -£20.81 (Mobile Provider, bills)
- May 18: -£16.00 (Person A, general)
- May 19: +£9.00 (Person B, income)
- June 2: -£22.00 (University, bills)
- June 6: +£6.66 (From Person C, income)
- June 12: -£20.81 (Mobile Provider, bills)
- June 17: +£100.00 (From Person C, income)

Notable spending patterns:
- Regular bills to University and Mobile Provider.
- Significant general spending to "Person A."
- Income from Person B and Person C.

Personalized financial advice:
1. **Track Recurring Bills:** Your regular payments to University and Mobile Provider are predictable. Consider setting up automated budgeting for these to ensure you always have funds allocated.
2. **Review Large Expenses:** The £120 payment to "Person A" stands out. Review such large transactions to ensure they are necessary and look for ways to reduce or avoid them if possible.
3. **Increase Savings:** Try to set aside a portion of your income (even small amounts) right after you receive it. Automating savings can help build a financial cushion.
4. **Monitor Cash Flow:** Your income is irregular. Consider ways to stabilize your income or reduce discretionary spending during lower-income months.
5. **Analyze General Spending:** Categorize your general expenses to identify areas where you can cut back.

Would you like more detailed budgeting tips or help setting up a savings plan?

Is there anything else I can help you with?
```
</details>

</details>
