#!/bin/bash

# setup virtual enviroment
python3 -m venv venv
source venv/bin/activate

# download modules
pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface
