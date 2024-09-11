from langchain.chains import LLMChain
from langchain.chains.base import Chain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

from typing import Dict, List

class ConcatenateChain(Chain):
    chain_1: LLMChain
    chain_2: LLMChain

    @property
    def input_keys(self) -> List[str]:
        all_input_vars = set(self.chain_1.input_keys).union(set(self.chain_2.input_keys))
        return list(all_input_vars)
    
    @property
    def output_keys(self) -> List[str]:
        return ['concat_output']
    
    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        output_1 = self.chain_1.invoke(inputs)
        output_2 = self.chain_2.invoke(inputs)
        return {'concat_output': output_1 + "\n" + output_2}
    

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
prompt_1 = PromptTemplate(
    input_variables=["job"],
    template="{job}に一番おすすめのプログラミング言語は？\nプログラミング言語:",
)
chain_1 = prompt_1 | llm

prompt_2 = PromptTemplate(
    input_variables=["job"],
    template="{job}の平均年収は？\n平均年収:",
)
chain_2 = prompt_2 | llm

concat_chain = ConcatenateChain(chain_1=chain_1, chain_2=chain_2)
print(concat_chain.invoke("データサイエンティスト"))