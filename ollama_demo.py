# -*- coding: utf-8 -*-
# @Time    : 2025/4/3 22:11
# @Author  : Gritty
# @File    : kg_metadata_build.py
# @Software: PyCharm
import os
# You must choose the DIR to put your logs,json and so on ,Do not choose the root, it is chaos
WORKING_DIR = "./test"

api_key=""
os.environ["OPENAI_API_KEY"] = api_key
base_url=""
os.environ["OPENAI_API_BASE"]=base_url
from PathRAG import PathRAG, QueryParam
from PathRAG.llm import gpt_4o_mini_complete,ollama_model_complete


if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = PathRAG(
    working_dir=WORKING_DIR,
    # llm_model_func=gpt_4o_mini_complete,
    llm_model_func=ollama_model_complete,
)
# Input Your Data and Question!
data_file="./demo.txt"
question=""
with open(data_file, encoding='utf-8') as f:
    rag.insert(f.read())

print(rag.query(question, param=QueryParam(mode="hybrid")))














