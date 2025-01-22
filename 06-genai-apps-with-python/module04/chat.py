from langchain_core import utils
from langchain_community.llms import VLLMOpenAI
from torch.cuda import temperature

model="ibm-granite/granite-3.1-2b-instruct"

openai_api_key = 'EMPTY'
openai_api_base = 'http://127.0.0.1:8000/v1'
llm = VLLMOpenAI(model_name=model, openai_api_base=openai_api_base, openai_api_key=openai_api_key)

print(llm.invoke("How many feet are there in a yard?"))
