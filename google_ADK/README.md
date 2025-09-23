# Get started with Agent Development Kit (ADK)

### Overview: Benefits of Agent Development Kit

Agent Development Kit offers several key advantages for developers building agentic applications:

* Multi-Agent Systems: Build modular and scalable applications by composing multiple specialized agents in a hierarchy. Enable complex coordination and delegation.

* Rich Tool Ecosystem: Equip agents with diverse capabilities: use pre-built tools (Search, Code Execution, etc.), create custom functions, integrate tools from third-party agent frameworks (LangChain, CrewAI), or even use other agents as tools.

* Flexible Orchestration: Define workflows using workflow agents (SequentialAgent, ParallelAgent, and LoopAgent) for predictable pipelines, or leverage LLM-driven dynamic routing (LlmAgent transfer) for adaptive behavior.

* Integrated Developer Experience: Develop, test, and debug locally with a powerful CLI and an interactive dev UI. Inspect events, state, and agent execution step-by-step.

* Built-in Evaluation: Systematically assess agent performance by evaluating both the final response quality and the step-by-step execution trajectory against predefined test cases.

* Deployment Ready: Containerize and deploy your agents anywhere – run locally, scale with Vertex AI Agent Engine, or integrate into custom infrastructure using Cloud Run or Docker.


#### While other Gen AI SDKs or agent frameworks also allow you to query models and even empower them with tools, dynamic coordination between multiple models requires a significant amount of work on your end.

#### Agent Development Kit offers a higher-level framework than these tools, allowing you to easily connect multiple agents to one another for complex but easy-to-maintain workflows.

<img width="988" height="460" alt="image" src="https://github.com/user-attachments/assets/a39f22ea-3bec-4418-8e9f-2d58847332bf" />

__Additionally, it allows you to deploy these complex systems of agents to a fully-managed endpoint in Agent Engine, so you can focus on the agents' logic while infrastructure is allocated and scaled for you__


## Core Concepts of Agent Development Kit

Google ADK is built around a few core concepts that make it powerful and flexible:

* **Agent:** Agents are core building blocks designed to accomplish specific tasks. They can be powered by LLMs to reason, plan, and utilize tools to achieve goals, and can even collaborate on complex projects.
* **Tools:** Tools give agents abilities beyond conversation, letting them interact with external APIs, search information, run code, or call other services.
* **Session Services:** Session services handle the context of a single conversation (Session), including its history (Events) and the agent's working memory for that conversation (State).
* **Callbacks:** Custom code snippets you provide to run at specific points in the agent's process, allowing for checks, logging, or behavior modifications.
* **Artifact Management:** Artifacts allow agents to save, load, and manage files or binary data (like images or PDFs) associated with a session or user.
* **Runner:** The engine that manages the execution flow, orchestrates agent interactions based on Events, and coordinates with backend services.
