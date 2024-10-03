from pydantic import BaseModel


class LLMResponseModel(BaseModel):
    function_to_call: str
    function_kwargs: dict
