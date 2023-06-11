from pydantic import BaseModel
from pydantic.class_validators import List


class ErrorModel(BaseModel):
    isSuccessfull: bool
    message: str
    errors: List[str]
