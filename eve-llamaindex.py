from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

# directory with data accessible to ai
data_corpus_directory = "../data"
print(f"    > loading data corpus from:    {data_corpus_directory}")
data_corpus = SimpleDirectoryReader(data_corpus_directory).load_data()

# embedding model
embedding_model = "local:BAAI/bge-small-en-v1.5"
print(f"    > loading embedding model:     {embedding_model}")
Settings.embed_model = resolve_embed_model(embedding_model)

# ollama language model
language_model = "orca-mini"
print(f"    > loading language model:      {language_model}")
Settings.llm = Ollama(model=language_model, request_timeout=3600.0)

# create a vector database object from accessible data
index = VectorStoreIndex.from_documents(
    data_corpus,
)
print(f"    > loading vector database:     {index}")

# create a Q&A engine over dataset
query_engine = index.as_query_engine()
print(f"    > loading query engine:        {query_engine}")

# user interface
print(f"# hello, this is {language_model} over dataset embedded with {embedding_model} contained at {data_corpus_directory}, at your service")
query = input(f"# ask a question:\n")
response = query_engine.query(query)
print("-" * 100)
print(response)

