# AI Judge Agent

**Developed by VARMETA**  
**Client: 0GLAB**

## Project Overview

The AI Judge Agent is an advanced, modular system designed to evaluate and moderate debates between AI agents. It leverages large language models and a panel of specialized virtual judges, each with unique evaluation criteria, to ensure fair, insightful, and multi-dimensional assessments of AI debates.

## Key Features

- **Multi-Perspective Judging:**  
  Includes ethical, audience, data-driven, creative, and pragmatic virtual judges, each with distinct personalities and evaluation frameworks.
- **Automated Debate Evaluation:**  
  Objectively analyzes debate transcripts and determines a winner based on configurable judging criteria.
- **LLM Integration:**  
  Utilizes OpenAI’s GPT models for natural language understanding and evaluation.
- **Customizable Prompts:**  
  Easily extend or modify judge personas and evaluation logic via prompt templates.

## Judge Personas

- **Ethical Judge:** Focuses on moral reasoning, fairness, and justice.
- **Audience Judge:** Evaluates clarity, persuasiveness, and accessibility for general audiences.
- **Data Judge:** Assesses logical consistency, factual accuracy, and evidence-based arguments.
- **Creative Judge:** Rewards originality, innovation, and out-of-the-box thinking.
- **Pragmatic Judge:** Prioritizes feasibility, real-world impact, and operational efficiency.

## How It Works

1. **Input:**  
   Provide a debate topic, transcript, and select the desired judge persona.
2. **Evaluation:**  
   The system generates a structured prompt and queries an LLM to evaluate the debate.
3. **Output:**  
   Returns concise comments and declares a winner, ensuring every debate has a clear outcome.

## Usage

1. Clone the repository.
2. Install dependencies (see `requirements.txt`).
3. Set your OpenAI API key in the environment variables.
4. Run `main.py` to start the evaluation process.

## Example

```python
from main import judgement, ethical_prompt

topic = "Is AI beneficial for society?"
discussion = "Debater1: ... Debater2: ..."
comment, winner = judgement(topic, discussion, ethical_prompt, "Debater1", "Debater2")
print("Comment:", comment)
print("Winner:", winner)
```

## About

- **Developed by:** VARMETA  
- **Client:** 0GLAB
