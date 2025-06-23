# Restaurant Agentic System Webapp

This project is a comprehensive restaurant voice agent system that combines [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) and [Restaurant Voice Agent](https://github.com/Coral-Protocol/Restaurant-Voice-Agent) to connect via coral protocol to provide an intelligent conversational experience for restaurant interactions. The agents used in this project are part of the [Awesome Agents for Multi-Agent Systems](https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems) collection.



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

#### Terminal 3: UI Frontend
```bash
cd UI
npm install
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
cp -r .env.example .env
# Edit .env with your specific configuration
```

#### For UI Frontend
Create a `.env.local` file in the `UI` directory:
```bash
cd UI

# Create .env.local with these variables:

# LiveKit Configuration
LIVEKIT_API_KEY=your_livekit_api_key_here  ([Get LiveKit API Key](https://cloud.livekit.io/))
LIVEKIT_API_SECRET=your_livekit_api_secret_here  ([Get LiveKit API Secret Key](https://cloud.livekit.io/))
LIVEKIT_URL=your_livekit_url_here  ([Get LiveKit Url](https://cloud.livekit.io/))

# API Endpoint Configuration (for Interface Agent)
NEXT_PUBLIC_CONN_DETAILS_ENDPOINT=/api/connection-details

# Interface Agent API Endpoint (default: http://localhost:8000)
NEXT_PUBLIC_INTERFACE_AGENT_API_ENDPOINT=http://localhost:8000
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
cd Restaurant-Voice-Agent
uv run main.py dev
```

#### Terminal 3: Start UI Frontend
```bash
cd UI
npm run dev
```

</details>

## 🎯 Usage

<details>
<summary>Click to see usage instructions</summary>

1. **Access the Application**: Open your browser and navigate to the UI application (typically `http://localhost:3000`)

2. **Try Now Button**: Click the "Try Now" button to be directed to the main page

3. **Start Conversation**: On the main page, press the "Start Conversation" button for the restaurant agent

4. **Interact**: You can now chat with the agentic system for restaurant-related queries and interactions

</details>


## 📚 Additional Resources

<details>
<summary>Click to see additional resources</summary>

For more detailed information about the individual components:

- **Restaurant Voice Agent**: [https://github.com/Coral-Protocol/Restaurant-Voice-Agent](https://github.com/Coral-Protocol/Restaurant-Voice-Agent)
- **Voice Interface Agent**: [https://github.com/Coral-Protocol/Voice-Interface-Agent](https://github.com/Coral-Protocol/Voice-Interface-Agent)
- **Coral Server**: [https://github.com/Coral-Protocol/coral-server](https://github.com/Coral-Protocol/coral-server)
- **Awesome Agents Collection for Multi-Agent-System**: [https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems](https://github.com/Coral-Protocol/awesome-agents-for-multi-agent-systems)

</details>

## 📋 Prerequisites

Before setting up this project, ensure you have the following installed:

- **Python 3.8+** with `uv` package manager
- **Node.js 18+** with npm
- **Git** for cloning repositories

## Check the Demo video:
[Demo](https://drive.google.com/file/d/1LtUfTUzV9MPEPY7b4alElDiJoml7E089/view)