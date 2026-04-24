from ...LLMInterface import LLMInterface
from google import genai
from ...LLMEnums import GeminiEnums
from google.genai import types
import logging

class GeminiProvider(LLMInterface):

    def __init__(self, api_key: str , url: str=None,
                default_max_input_characters: int=750,
                default_max_output_tokens: int=1000,
                default_temperature:int=0.1):
        super().__init__()

        self.api_key = api_key
        self.url = url

        self.default_max_input_characters = default_max_input_characters
        self.default_max_output_tokens = default_max_output_tokens
        self.default_temperature = default_temperature

        self.generation_model_id = None
        self.embedding_model_id = None


        self.client = genai.Client(api_key=self.api_key)

        self.logger = logging.getLogger(__name__)


    @classmethod
    def llm_model(self, model_id:str):
        self.llm_model_id = model_id
        
    

    @classmethod
    def select_embedding_model(self, model_id:str, embedding_size):
        self.embdding_model_id = model_id
        self.embedding_size = embedding_size
        
    def procces_text(self,text:str):
        return text[:self.default_max_input_characters].strip()
    
    @classmethod
    def text_generator(self, prompt:str,max_tokens:int=None, temp = None):

        if not self.client:
            self.logger.error("Gemini client was not set")
            return None
        
        if not self.llm_model_id:
            self.logger.error("Gemini model was not set")
            return None

        max_tokens = max_tokens if max_tokens else  self.default_max_output_tokens 
        temp = temp if temp else self.default_temperature

        response = self.client.models.generate_content(
            model =  self.llm_model_id,
            config= types.GenerateContentConfig(system_instruction = GeminiEnums.SYSTEM_INSTRUCTION.value,
                                                temperature=temp,
                                                max_output_tokens=max_tokens),
                                                contents = self.procces_text(prompt),
        )
        
        if not response or not response.text or len(response.text) == 0 :
            self.logger.error("Error while generation text with Gemini")
            return None

        return response.text
    @classmethod
    def embedding_text(self, text:str, doc_type:str = None):
        
        if not self.client:
            self.logger.error("Gemini client was not set")
            return None
    
        if not self.embdding_model_id:
            self.logger.error("embdding model for Gemini was not set")
            return None

        result = self.client.embed_content(
            model = self.embdding_model_id,
            contents = text,
        )

        if not result or not result.embeddings or len(result.embeddings) == 0 :
            self.logger.error("Error while embedding text with Gemini")
            return None
        
        return result.embeddings
    
    