from typing import List

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain.output_parsers import (
    PydanticOutputParser,
    OutputFixingParser,
)

class Job(BaseModel):
    name: str = Field(description="Name of the job")
    skill_list: List[str] = Field(description="List of skills required for that job")

misformatted = "{'name': 'Frontend Engineer', 'skill_list': ['HTML', 'CSS', 'JS', 'TS']}"

parser = PydanticOutputParser(pydantic_object=Job)

new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI(model_name="gpt-3.5-turbo"))
print(new_parser.parse(misformatted))