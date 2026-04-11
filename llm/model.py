from transformers import pipeline

class LLM:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            max_new_tokens=300
        )

    def invoke(self, prompt):
        response = self.generator(prompt)[0]["generated_text"]
        return response