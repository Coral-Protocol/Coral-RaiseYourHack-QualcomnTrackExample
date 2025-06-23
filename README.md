# Personal Finance Advisor

This project is a comprehensive personal finance advisor system that combines the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) and [Monzo Agent](https://github.com/Coral-Protocol/Coral-Monzo-Agent) to provide secure, intelligent, and privacy-preserving financial management through natural language interaction. The Monzo Agent enables users to safely access and analyze their Monzo banking data using a local LLM, ensuring sensitive information never leaves their device. By integrating with Monzo’s official API and customized toolkits, the system supports conversational account balance checks, transaction history queries, and personalized financial advice. All agents in this project are part of the [Awesome Agents for Multi-Agent Systems](https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems) collection.


## 🚀 Quick Start Guide

### Step 1: Install and Run Ollama (for Local LLM)
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

### Step 2: Setup Coral Server

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

### Step 3: Environment Setup

You'll need to set up **two separate terminals** for each component:

<details>
<summary>Click to see setup instructions for each component</summary>

#### Terminal 1: Coral Interface Agent
```bash
cd Coral-Interface-Agent
uv sync
```

#### Terminal 2: Monzo Agent  
```bash
cd Coral-Monzo-Agent
uv sync
```

</details>

### Step 4: Environment Configuration

<details>
<summary>Click to see configuration instructions</summary>

#### For Coral Interface Agent
Get the API Key: [OpenAI](https://platform.openai.com/api-keys).

Create a `.env` file in the `Coral-Interface-Agent` directory based on the `.env_sample` file:
```bash
cd Coral-Interface-Agent
cp -r .env_sample .env
# Edit .env with your specific configuration
```

#### For Monzo Agent
Get the `MONZO_ACCESS_TOKEN` and `MONZO_ACCOUNT_ID`:[Monzo Developer Portal](https://developers.monzo.com/).

Create a `.env` file in the `Restaurant-Voice-Agent` directory based on the `.env.example` file:
```bash
cd Coral-Monzo-Agent
cp -r env_example .env
# Edit .env with your specific configuration
```

</details>

### Step 5: Running the Application

<details>
<summary>Click to see running instructions</summary>

Start all three components in their respective terminals:

#### Terminal 1: Start Coral Interface Agent
```bash
cd Coral-Interface-Agent
uv run 0-langchain-interface.py
```

#### Terminal 2: Start Monzo Agent
```bash
cd Coral-Monzo-Agent
uv run langchain-monzo-agent.py.
```

</details>

## Example

<details>
<summary>Click to see example</summary>

```bash
# Input:
Question: Help me check my transections of monzo for the last 2 months and give me some personal finance advice.

# Output:
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


## 📚 Additional Resources

<details>
<summary>Click to see additional resources</summary>

For more detailed information about the individual components:

- **Interface Agent**: [https://github.com/Coral-Protocol/Coral-Interface-Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
- **Monzo Agent**: [https://github.com/Coral-Protocol/Coral-Monzo-Agent](https://github.com/Coral-Protocol/Coral-Monzo-Agent)
- **Coral Server**: [https://github.com/Coral-Protocol/coral-server](https://github.com/Coral-Protocol/coral-server)
- **Awesome Agents Collection for Multi-Agent-System**: [https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems](https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems)

</details>
