from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions}
)

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
_input = prompt.format(subject="Programming Language")
output = llm.invoke(_input)
print(output)
print(output_parser.parse(output))