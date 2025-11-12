import os
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import HTML, display
import pandas as pd
from io import StringIO

load_dotenv('.env', override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)

def get_llm_response(prompt):
    llm_response = client.responses.create(
        model='gpt-5',
        reasoning={"effort": "high"},
        instructions="As a helpful AI assistant, you possess expertise in data analysis and machine learning.",
        input=prompt,
    )
    return llm_response.output_text

def display_table(data):
    df = pd.read_csv(StringIO(data))
    display(HTML(df.to_html(index=False)))

def display_csv(data):
    df = pd.read_csv(data)
    display(HTML(df.to_html(index=False)))

def write_to_csv(data, filename):
    csv_buffer = StringIO(data)
    df = pd.read_csv(csv_buffer)
    df.to_csv(filename, index=False)
