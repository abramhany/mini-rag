from abc import ABC , abstractmethod

class LLMInterface(ABC):

    @classmethod
    @abstractmethod
    def select_llm_model(self,model_name:str):
        pass

    @classmethod
    @abstractmethod
    def select_embedding_model(self,model_name:str):
        pass

    @classmethod
    @abstractmethod   
    def text_generator(self,prompt:str,max_tokens:int,temp:float=None):
        pass

    @classmethod
    @abstractmethod    
    def embeding_text(self,text:str,doc_type:str):
        pass

    @classmethod
    @abstractmethod
    def model_prompt(self,prompt:str,role:str):
        pass
