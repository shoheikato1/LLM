#py -m pip install llama-index pypdf python-dotenv pandas

from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str
from note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI

load_dotenv()

population_path = os.path.join("data","population.csv")
population_df = pd.read_csv(population_path)

#print(population_df.head())

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})


tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine, 
        metadata=ToolMetadata(
            name='population_data',
            description='this gives information at the world population and demographics',
    ),
),
]

llm = OpenAI(model='gpt-3.5-turbo-0613')
agent = ReActAgent.from_tools(tools,llm=llm, verbose=True, context=context)

while (prompt := input('Enter prompt (q to quit):')) !="q":
    result = agent.query(prompt)
    print(result)