from typing import List
from pydantic import BaseModel, Field

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.output_parsers import PydanticOutputParser

class Job(BaseModel):
    name: str = Field(description="Name of the job")
    skill_list: List[str] = Field(description="List of skills required for that job")

parser = PydanticOutputParser(pydantic_object=Job)
prompt = PromptTemplate(
    template="{query}\n\n{format_instructions}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

_input = prompt.format_prompt(query="Tell me the skills required for frontend engineer.")
print(_input)

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
output = llm.invoke(_input.to_string())
print(output)

print(parser.parse(output))