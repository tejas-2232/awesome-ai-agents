# Empower ADK agents with tools

### Overview

This lab covers the use of tools with Agent Development Kit agents.

From powerful tools provided by Google, like Google Search and Vertex AI Search, to the rich variety of tools available in the LangChain and CrewAI ecosystems, there are many tools to get started with.

Additionally, creating your own tool from a function only requires writing a good docstring!

> This lab assumes you are familiar with the basics of ADK covered in the lab1: _Get started with Agent Development Kit (ADK)._


## Objective
In this lab, you will learn about the ecosystem of tools available to ADK agents. You will also learn how to provide a function to an agent as a custom tool.

After this lab, you will be able to:

* Provide prebuilt Google, LangChain, or CrewAI tools to an agent
* Discuss the importance of structured docstrings and typing when writing functions for agent tools
* Write your own tool functions for an agent

## Tool use with the Agent Developer Kit

Leveraging tools effectively is what truly distinguishes intelligent agents from basic models. A tool is a block of code, like a function or a method, that executes specific actions such as interacting with databases, making API requests, or invoking other external services.

Tools empower agents to interact with other systems and perform actions beyond their core reasoning and generation capabilities. It's crucial to note that these tools operate independently of the agent's LLM, meaning that tools do not automatically possess their own reasoning abilities.

Agent Development Kit provides developers with a diverse range of tool options:

1. Pre-built Tools: Ready-to-use functionalities such as Google Search, Code Execution, and Retrieval-Augmented Generation (RAG) tools.

2. Third-Party Tools: Seamless integration of tools from external libraries like LangChain and CrewAI.

3. Custom Tools: The ability to create custom tools tailored to specific requirements, by using language specific constructs and Agents-as-Tools. The SDK also provides asynchronous capabilities through Long Running Function Tools.

In this lab, you will explore these categories and implement one of each type.


## Available Pre-Built Tools from Google

Google provides several useful tools for your agents. They include:

__Google Search (google_search):__ Allows the agent to perform web searches using Google Search. You simply add google_search to the agent's tools.

__Code Execution (built_in_code_execution):__ This tool allows the agent to execute code, to perform calculations, data manipulation, or interact with other systems programmatically. You can use the pre-built VertexCodeInterpreter or any code executor that implements the BaseCodeExecutor interface.

__Retrieval (retrieval):__ A package of tools designed to fetch information from various sources.

__Vertex AI Search Tool (VertexAiSearchTool):__ This tool integrates with Google Cloud's Vertex AI Search service to allow the agent to search through your AI Applications data stores.

