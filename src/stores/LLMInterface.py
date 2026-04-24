from abc import ABC , abstractmethod

class LLMInterface(ABC):

    @classmethod
    @abstractmethod
    def llm_model(self,llm_model_id:str):
        pass

    @classmethod
    @abstractmethod
    def select_embedding_model(self,model_id:str,embedding_size:int):
        pass

    @classmethod
    @abstractmethod   
    def text_generator(self,prompt:str,max_tokens:int,temp:float=None):
        pass

    @classmethod
    @abstractmethod    
    def embedding_text(self,text:str,doc_type:str):
        pass

    @classmethod
    @abstractmethod
    def model_prompt(self,prompt:str,role:str):
        pass
