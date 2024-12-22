from langchain_ollama import OllamaLLM


class Ai_chat(object):

    llm=None

    def __init__(self):
        llm = OllamaLLM(model="llama3.2:1b", prepend_text='')
        self.llm = llm
    
    def generate_poem(self, poem_of):
        return self.llm.invoke(f"Tell me two stanza poem about {poem_of}. Poem only no other propts")
