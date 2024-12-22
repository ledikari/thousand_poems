from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langhcina.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PrompTemplate
from langchain.chains import LLMChain
import time

start = time.time()
llm = Ollama(model="llama3.1", callback_manager = CallbackManager(StreamingStdOutCallbackHandler()))

prompt = PrompTemplate(
    input_variables = ["topic"],
    template = "Give me 3 stanza poem about {topic}"
)

chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
print(chain.run("dog in grass"))

end = time.time()
print(f"{end - start} time elapsed")


# llm("tell me 5 facts about Philippines history")