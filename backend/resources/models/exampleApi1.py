from pydantic import BaseModel
from pydantic.class_validators import List


# region Class
class Pagination(BaseModel):
    total: int
    page: int
    pageSize: int


class Data(BaseModel):
    id: int
    name: str
    description: str
    isActive: bool


class DataGetEnabled(BaseModel):
    id: int
    name: str
# endregion


# region Models
class ExampleModelGetId(BaseModel):
    data: Data
    isSuccessfull: bool


class ExampleModelGetAll(BaseModel):
    data: List[Data]
    isSuccessfull: bool
    pagination: Pagination


class ExampleModelGetEnabled(BaseModel):
    data: List[DataGetEnabled]
    isSuccessfull: bool
    pagination: Pagination


class ExampleModelPostCreate(BaseModel):
    isSuccessfull: bool


class ExampleModelPutUpdate(BaseModel):
    isSuccessfull: bool


class ExampleModelPatchEnabled(BaseModel):
    isSuccessfull: bool


class ExampleModelNotFound(BaseModel):
    isSuccessfull: bool
    message: str
# endregion
