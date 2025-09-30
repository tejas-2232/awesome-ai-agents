# Build multi-agent systems with ADK

### Overview

This lab covers orchestrating multi-agent systems within the Google Agent Development Kit (Google ADK).

This lab assumes that you are familiar with the basics of ADK and tool use as covered in the labs:

* Get started with Google Agent Development Kit (ADK)
* Empower ADK agents with tools

## Objective
In this lab, you will learn about multi-agent systems using the Agent Development Kit.

After this lab, you will be able to:

* Create multiple agents and relate them to one another with parent to sub-agent relationships.
* Build content across multiple turns of conversation and multiple agents by writing to a session's state dictionary
* Instruct agents to read values from the session state to use as context for their responses
* Use workflow agents to pass the conversation between agents directly

## Multi-Agent Systems

* The __Agent Development Kit__ empowers developers to get more reliable, sophisticated, multi-step behaviors from generative models. 

* Instead of writing long, complex prompts that may not deliver results reliably, you can construct a flow of multiple, simple agents that can collaborate on complex problems by dividing tasks and responsibilities.

This architectural approach offers several key advantages such as:

* __Easier to design:__ You can think in terms of agents with specific jobs and skills.
* __Specialized functions with more reliable performance:__ Specialized agents can learn from clear examples to become more reliable at their specific tasks.
* __Organization:__ Dividing the workflow into distinct agents allows for a more organized, and therefor easier to think about, approach.
* __Improvability and maintainability:__ It is easier to improve or fix a specialized component rather than make changes to a complex agent that may fix one behavior but might impact others.
* __Modularity:__ Distinct agents from one workflow can be easily copied and included in other similar workflows.

## The Hierarchical Agent Tree

![alt text](image.png)  