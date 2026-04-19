import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from sympy.physics.units import temperature

deepseek_api_key = os.getenv["DEEPSEEK_API_KEY"]

model = init_chat_model(
    model="deepseek",
    api_key = deepseek_api_key,
    temperature=0.0)

prompt = ChatPromptTemplate.from_template(
    []

)