Api docs for sbp data : https://easydata.sbp.org.pk/apex/f?p=10:22:16561895085421:

## Ollama:

Ollama should be installed and running:

```curl -fsSL https://ollama.com/install.sh | sh```

Pull a model to use with the library:  

```
ollama pull gemma3
ollama run gemma3

```
Ollama’s API is served by default at (locally):
```http://localhost:11434/api```

then :
```pip install ollama```


| Command                  | What it installs              | Purpose                                   |
| ------------------------ | ----------------------------- | ----------------------------------------- |
| **Install Ollama**       | The Ollama application/server | Runs LLMs locally on your machine         |
| **`pip install ollama`** | The Python client library     | Lets Python code talk to an Ollama server |



