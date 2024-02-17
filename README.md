# eve-ai

general framework for AI agent deployment

___

- setup a virtual python enviroment

`python3 -m venv venv`

`source /venv/bin/activate`

- local setup with Ollama and HuggingFace embeddings

`pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface`

- download ollama for local llm

`curl -fsSL https://ollama.com/install.sh | sh`

`ollama pull orca-mini`

- local llm can be prompted with: `ollama run orca-mini`

