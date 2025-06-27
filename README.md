# AI Judge Agent

**Developed by VARMETA**  


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


- <img src="image/seraphina_1750218300.webp" alt="Seraphina " width="60"/> **Seraphina Sera Veritas (Ethical Judge):** Deeply analyzes ethics, fairness, and reasoning, always maintaining objectivity and strong principles.
- <img src="image/evenlyn_1750218300.webp" alt="Evenlyn" width="60"/> **Evelyn Evie Reed (Audience Judge):** Evaluates clarity, persuasiveness, and accessibility for general audiences, prioritizing clear communication and connection.
- <img src="image/unit_734_1750218300.webp" alt="Unit 734" width="60"/> **Seven (Data Judge):** Checks logic, factual accuracy, and evidence, strictly objective and unaffected by emotions.
- <img src="image/spark_1750218300.webp" alt="Spark" width="60"/> **Spark (Creative Judge):** Values creativity, originality, and breakthrough ideas, always encouraging out-of-the-box thinking.
- <img src="image/elias_1750821275.webp" alt="Elias" width="60"/> **Elias Thorne (Pragmatic Judge):** Focuses on practicality, effectiveness, and real-world applicability, judging based on results and tangible impact.


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
