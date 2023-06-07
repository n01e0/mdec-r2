import openai
import os

from mdecbase import Service

MODEL = "gpt-4"
GENERAL_PROMPT = """
Please explain provided script and deobfuscate when if that are obfuscated
"""
openai.api_key = os.getenv('OPENAI_API_KEY')

class GptService(Service):
    """
    GPT Script Decompiler as a service
    """

    def decompile(self, path: str) -> str:
        """
        Decompile the obfuscated script with using OpenAI API
        """
        try:
            with open(path) as f:
                script = f.read()
                resp = openai.ChatCompletion.create(
                    model=MODEL,
                    messages=[
                        {'role': 'system', 'content': GENERAL_PROMPT},
                        {'role': 'user', 'content': script}
                    ],
                    temperature=0,
                )
                return resp['choices'][0]['message']['content']
        except Exception as e:
            return f'failed: {e}'
    def version(self) -> str:
        return MODEL 

