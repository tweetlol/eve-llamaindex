#!/bin/bash

# install ollama
curl -fsSL https://ollama.com/install.sh | sh

# donload local language model
ollama pull orca-mini
