## Prompt Evaluation Workflow for AWS Tasks

Building a custom prompt evaluation workflow starts with creating a solid prompt and then generating test data to see how well it performs. This guide walks through setting up an evaluation system for a prompt that helps users write AWS-specific code.

### Goal
Our prompt should assist users in producing one of three outputs for AWS use cases:

- **Python code**
- **JSON configuration files**
- **Regular expressions**

**Key requirement**: When a user requests help with a task, the output must be a clean artifact in one of the formats above — with no extra explanations, headers, or footers.

### Starting Prompt (v1)
```python
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

### Creating an Evaluation Dataset
An evaluation dataset contains inputs that we'll feed into our prompt. For each combination of prompt and input, we'll run the prompt and analyze the results.

Our dataset will be an array of JSON objects, where each object contains a `"task"` describing what we want the model to accomplish. We can either create this dataset by hand or generate it automatically using Claude.

Since we're generating test data, this is a perfect opportunity to use a **faster model like Haiku** instead of a more expensive model.

## Generating Test Data with Code

### Helper Functions
```python
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    response = client.messages.create(**params)
    return response.content[0].text
```

### Dataset Generation Function
```python
def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing a task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
  {
    "task": "Description of task"
  }
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""

    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

### Why Prefilling and Stop Sequences?

```python
def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        # if stop_sequences is provided, the model will stop generating tokens when it encounters any of the stop sequences
        # "stop_sequences": stop_sequences,
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    response = client.messages.create(**params)
    return response.content[0].text
```

To properly parse the JSON response, we prefill the assistant with `````json```` and add a stop sequence of ````` ``` ````` so the model stops at the end of the JSON block. This reliably yields valid JSON that can be parsed.

### Test the Dataset Generation

```python
dataset = generate_dataset()
print(dataset)
```

This should return three different test cases covering our target outputs: Python functions, JSON configurations, and regular expressions for AWS-specific tasks.

### Save the Dataset
```python
import json

with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)
```

This creates a `dataset.json` file containing your list of tasks ready for prompt evaluation.

---

With this foundation in place, you now have a systematic way to generate test data for evaluating how well your prompts perform across different types of AWS-related coding tasks.