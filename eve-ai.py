from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

data_corpus_directory = SimpleDirectoryReader("../data").load_data()

# bge-m3 embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="orca-mini", request_timeout=30.0)

index = VectorStoreIndex.from_documents(
    data_corpus_directory,
)