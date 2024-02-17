#!/bin/bash

# install ollama
curl -fsSL https://ollama.com/install.sh | sh

# pull local model
ollama pull orca-mini

# setup virtual enviroment
python3 -m venv venv
source venv/bin/activate

# download prequisities
pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface
