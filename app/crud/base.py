from typing import TypeVar, Generic
from pydantic import BaseModel

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCRUD(Generic[CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model):
        self.model = model

    def get_sa_model(self):
        model = self.model.sa
        return model

    def create(self, obj_in: CreateSchemaType):
        try:
            obj_in_data = obj_in.dict()
            obj = self.model.objects.create(**obj_in_data)
            return obj
        except:
            return None

    def update(self, obj_id, obj_in: UpdateSchemaType):
        try:
            obj_in_data = obj_in.dict(exclude_unset=True)
            self.model.objects.filter(pk=obj_id).update(**obj_in_data)
            return self.get_by_id(obj_id)
        except:
            return None

    def delete(self, obj):
        try:
            return obj.delete()
        except:
            return None

    def get_by_id(self, obj_id):
        try:
            return self.model.objects.get(id=obj_id)
        except:
            return None
