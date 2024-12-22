from langchain_ollama import OllamaLLM

import time
start = time.time()

llm = OllamaLLM(model="llama3.2:1b",
                max_tokens=100,
                )
result = llm.invoke("Tell me a 2 stanza poem about dogs in grass")
print(result)

end = time.time()
print(f"{end - start} time elapsed")
