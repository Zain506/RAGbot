"""
Author: Zain Nomani
Description: Hold conversation with LLM with this class by calling .speak()
"""
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
class Conversation:
    """
    Hold conversation with language model
    """
    def __init__(self, model = "microsoft/DialoGPT-small"):
        # Load model directly

        tokenizer = AutoTokenizer.from_pretrained(model)
        model = AutoModelForCausalLM.from_pretrained(model)
        self.pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=200
        )
        self.messages = []
        return None
    
    def speak(self, query: str) -> list: # speak to LLM
        self.messages.append({"role": "user", "content": query})
        response = self.pipe(self.messages)
        self.messages = response[0]["generated_text"]
        return None