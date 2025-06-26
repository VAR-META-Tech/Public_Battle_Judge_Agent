from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from datetime import datetime
import re 
from openai import OpenAI

from prompt import *

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

def judgement(topic, discussion, prompt_judge, bot1, bot2):

    # Create a prompt template for query rewriting
    query_rewrite_template = """
You are a judge of a debating competition with this prompt: {prompt_judge}
This is the name of two debaters: {bot1} and {bot2}

Now, evaluate the following discussion:
    **{topic}: topic
    **{discussion}: this is the conversation of two debaters
    Your mission is evaluating the discussion and chose who win the debate
    your response MUST BE less than 1000 characters and in format:
        1. 'Comments about discussion': comment
        2. 'Name of the winner': just name of the winner, no additional text
    REMEMBER THAT YOU MUST CHOOSE A WINNER 
    """

    prompt = PromptTemplate(
        input_variables=["topic", "discussion","prompt_judge", "bot1", "bot2"],
        template=query_rewrite_template
    )
    
    prompt = query_rewrite_template.format(
        topic = topic,
        discussion = discussion,
        prompt_judge = prompt_judge,
        bot1 = bot1,
        bot2 = bot2,
    )
    # Create an LLMChain for query rewriting
    response = get_response(prompt = prompt)  
    # print(response)
    if response is None:
        return None,None
    return parse_text(response)

def parse_text(text):
    # Biểu thức regex để tách từng mục dạng "1. <key>: <value>"
    pattern = r'(\d+)\.\s*([^:]+):\s*(.+)'
    
    comment, name = None, None  # Khởi tạo biến
    
    # Lặp qua từng dòng và trích xuất thông tin
    for match in re.finditer(pattern, text):
        key = match.group(2).strip().lower()  # Lấy phần "key" và chuyển thành chữ thường
        value = match.group(3).strip()  # Lấy phần "value"
        
        if "comment" in key:
            comment = value
        elif "name" in key:
            name = value
    
    return comment, name

def get_response(prompt: str=None, model: str="gpt-4o", temperature: float=0.7, top_p: float=1.0):
    api_key = os.getenv("OPENAI_API_KEY").split(',')[0]
    content="You are a helpful assistant who provides clear and concise answers to any query."
    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model=model, messages=[{"role": "system", "content": content}, {"role": "user", "content": prompt}],
            temperature=temperature, top_p=top_p,
        )
    except Exception as e:
        print('Error key 1 ----> swap to back-up key')
        api_key = os.getenv("OPENAI_API_KEY").split(',')[1]
        client = OpenAI(api_key=api_key)
        try:
            response = client.chat.completions.create(
                model=model, messages=[{"role": "system", "content": content}, {"role": "user", "content": prompt}],
                temperature=temperature, top_p=top_p,
            )
        except Exception as  e:
            print('---->     ERROR BACKUP KEY :',e)
            return None
    collected_response = response.choices[0].message.content.strip()
    return collected_response 


if __name__ == "__main__":
    topic = "Is AI beneficial for society?"
    discussion = """Debater1: No, AI poses significant risks to privacy and employment.
    Debater2: I disagree, AI can enhance productivity and create new job opportunities.  
    """
    comment, winner = judgement(topic, discussion, ethical_prompt, "Debater1", "Debater2")
    print("Comment:", comment)
    print("Winner:", winner)