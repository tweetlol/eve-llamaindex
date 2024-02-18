# eve-llamaindex

## llamaindex RAG setup

- will access .pdf files saved in `../data` directory (default) and extract knowledge in attemt to answer a query
- uses localy running llm model (from [ollama.com/library](https://ollama.com/library))
- huggingface embedding model

## install-ollama.sh script

- download ollama to run a local llm instance

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

```sh
ollama pull orca-mini
```

- **note:** local llm can be prompted in terminal with following command:

```sh
ollama run orca-mini
```

## env-setup.sh script

- make sure you have venv installed, setup a virtual python environment

```sh
sudo apt install python3.10-venv
```

```sh
python3 -m venv venv
```

```sh
source /venv/bin/activate
```

- install required modules

```sh
pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface
```

- proceed to edit the eve-lammaindex.py script variables

## eve-lammaindex.py script

```py
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
```

- specify the `data_corpus_directory` variable for ai to access

```py
# directory with data accessible to ai
data_corpus_directory = "../data"
print(f"    > loading data corpus from:    {data_corpus_directory}")
data_corpus = SimpleDirectoryReader(data_corpus_directory).load_data()
```

- specify the `ebedding_model` to be used

```py
# embedding model
embedding_model = "local:BAAI/bge-small-en-v1.5"
print(f"    > loading embedding model:     {embedding_model}")
Settings.embed_model = resolve_embed_model(embedding_model)
```

- specify the `language_model` to be used
- specify `request_timeout` (default is usually too low for CPU-running llms)

```py
# ollama language model
language_model = "orca-mini"
print(f"    > loading language model:      {language_model}")
Settings.llm = Ollama(model=language_model, request_timeout=3600.0)
```

- customize the user interface for optimal experience

```py
# user interface
print(f"[ eve ] Hello, this is {language_model} over dataset embedded with {embedding_model} contained at {data_corpus_directory}, at your service.")
query = input(f">>> \n")
response = query_engine.query(query)
print("-" * 100)
print("[ eve ] " + response)
```

## useful resources

[llamaindex docs](https://docs.llamaindex.ai/en/stable/index.html)
