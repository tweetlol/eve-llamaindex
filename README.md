# eve-llamaindex

## llamaindex RAG setup

- will access .pdf files saved in `../data` directory (default) and extract knowledge in attemt to answer a query
- uses localy running llm model (from [ollama.com/library](https://ollama.com/library))
- huggingface embedding model


## env-setup.sh script

- download ollama and the local llm

```sh
curl -fsSL https://ollama.com/install.sh | sh

ollama pull orca-mini
```

- **note:** local llm can be prompted with following command:

```sh
ollama run orca-mini
```

- setup a virtual python enviroment

```sh
python3 -m venv venv

source /venv/bin/activate
```

- install prequisites

```sh
pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface
```

- proceed to edit the eve-lammaindex.py script variables

## eve-lamma.py script

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
print(f"# hello, this is {language_model} over dataset embedded with {embedding_model} contained at {data_corpus_directory}, at your service")
query = input(f"# ask a question:\n")
response = query_engine.query(query)
print("-" * 100)
print(response)
```

## useful resources

[llamaindex docs](https://docs.llamaindex.ai/en/stable/index.html)