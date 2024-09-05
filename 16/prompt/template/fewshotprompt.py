from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
from langchain_openai import OpenAI

examples = [
    {"fruit": "りんご", "color": "赤"},
    {"fruit": "キウイ", "color": "緑"},
    {"fruit": "ぶどう", "color": "紫"},
]

example_formatter_template = """
フルーツ: {fruit}
色: {color}\n
"""

example_prompt = PromptTemplate(
    template=example_formatter_template,
    input_variables=["fruit", "color"]
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="フルーツの色を漢字で教えて。",
    suffix="フルーツ: {input}\n色:",
    input_variables=["input"],
    example_separator="\n\n",
)

prompt_text = few_shot_prompt.format(input="オレンジ")
print(prompt_text)

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
# print(llm(prompt_text))
print(llm.invoke(prompt_text))