#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface

curl -fsSL https://ollama.com/install.sh | sh

ollama pull orca-mini

