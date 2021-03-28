from marshmallow import fields

from eycars.clients.utils.schemas import BaseSchema
from eycars.clients.vpic_nhtsa.dataclasses import ModelsForMakeResponse, CarModel, BaseResponse


class BaseResponseSchema(BaseSchema):
    model = BaseResponse

    Count = fields.Integer()
    Message = fields.String()
    SearchCriteria = fields.String()


class CarModelSchema(BaseSchema):
    model = CarModel

    Make_ID = fields.Integer()
    Make_Name = fields.String()
    Model_ID = fields.Integer()
    Model_Name = fields.String()


class ModelsForMakeResponseSchema(BaseResponseSchema):
    model = ModelsForMakeResponse

    Results = fields.Nested(CarModelSchema(many=True))
