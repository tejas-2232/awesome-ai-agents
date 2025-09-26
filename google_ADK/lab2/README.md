# Connect to Remote Agents with ADK and the Agent2Agent (A2A) SDK

### Overview: Agent2Agent (A2A)

* The Agent2Agent (A2A) protocol addresses a critical challenge in the AI landscape: enabling gen AI agents, built on diverse frameworks by different companies running on separate servers, to communicate and collaborate effectively - as agents, not just as tools.

* A2A aims to provide a common language for agents, fostering a more interconnected, powerful, and innovative AI ecosystem.

* A2A is built around a few core concepts that make it powerful and flexible:

* Standardized Communication: JSON-RPC 2.0 over HTTP(S).
* Agent Discovery: Agent Cards detail an agent's capabilities and connection info, so agents can discover each other and learn about each other's capabilities
* Rich Data Exchange: Handles text, files, and structured JSON data.
* Flexible Interaction: Supports synchronous request/response, streaming (SSE), and asynchronous push notifications.
* Enterprise-Ready: Designed with security, authentication, and observability in mind

### Objective

In this lab, you will:

* Deploy an ADK agent as an A2A Server
* Prepare a JSON Agent Card to describe an A2A agent's capabilities
* Enable another ADK agent to read the Agent Card of your deployed A2A agent and use it as a sub-agent

