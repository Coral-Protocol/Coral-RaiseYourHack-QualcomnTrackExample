# Personal Finance Advisor

This project is a comprehensive personal finance advisor system that combines the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) and [Monzo Agent](https://github.com/Coral-Protocol/Coral-Monzo-Agent) to provide secure, intelligent, and privacy-preserving financial management through natural language interaction. The Monzo Agent enables users to safely access and analyze their Monzo banking data using a local LLM, ensuring sensitive information never leaves their device. By integrating with Monzo’s official API and customized toolkits, the system supports conversational account balance checks, transaction history queries, and personalized financial advice. All agents in this project are part of the [Awesome Agents for Multi-Agent Systems](https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems) collection.


## 🚀 Quick Start Guide

### Step 1: Setup Coral Server

<details>
<summary>Click to expand setup instructions</summary>

First, you need to run the Coral server which will serve as a communication channel for our agents:

1. Clone and setup the Coral server:
```bash
git clone https://github.com/Coral-Protocol/coral-server
cd coral-server
# Follow the setup instructions in the coral-server repository
```

2. Start the Coral server (follow the specific instructions in the coral-server repository)

</details>

### Step 2: Environment Setup

You'll need to set up **three separate terminals** for each component:

<details>
<summary>Click to see setup instructions for each component</summary>

#### Terminal 1: Coral Interface Agent
```bash
cd Coral-Interface-Agent
uv sync
```

#### Terminal 2: Restaurant Voice Agent  
```bash
cd Restaurant-Voice-Agent
uv sync
```

</details>

### Step 3: Environment Configuration

<details>
<summary>Click to see configuration instructions</summary>

#### For Coral Interface Agent
Create a `.env` file in the `Coral-Interface-Agent` directory based on the `.env_sample` file:
```bash
cd Coral-Interface-Agent
cp -r .env_sample .env
# Edit .env with your specific configuration
```

#### For Restaurant Voice Agent
Create a `.env` file in the `Restaurant-Voice-Agent` directory based on the `.env.example` file:
```bash
cd Restaurant-Voice-Agent  
cp -r env_example .env
# Edit .env with your specific configuration
```

</details>

### Step 4: Running the Application

<details>
<summary>Click to see running instructions</summary>

Start all three components in their respective terminals:

#### Terminal 1: Start Coral Interface Agent
```bash
cd Coral-Interface-Agent
uv run 0-langchain-interface.py
```

#### Terminal 2: Start Restaurant Voice Agent
```bash
cd Coral-Monzo-Agent
uv run langchain-monzo-agent.py.
```

</details>


## 📚 Additional Resources

<details>
<summary>Click to see additional resources</summary>

For more detailed information about the individual components:

- **Interface Agent**: [https://github.com/Coral-Protocol/Coral-Interface-Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
- **Monzo Agent**: [https://github.com/Coral-Protocol/Coral-Monzo-Agent](https://github.com/Coral-Protocol/Coral-Monzo-Agent)
- **Coral Server**: [https://github.com/Coral-Protocol/coral-server](https://github.com/Coral-Protocol/coral-server)
- **Awesome Agents Collection for Multi-Agent-System**: [https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems](https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems)

</details>
