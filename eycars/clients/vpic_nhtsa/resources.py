import requests

from eycars.clients.utils.resources import Resource
from eycars.clients.vpic_nhtsa.dataclasses import CarModel
from eycars.clients.vpic_nhtsa.schemas import ModelsForMakeResponseSchema


class ModelsForMakeResource(Resource):
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
    schema_class = ModelsForMakeResponseSchema

    def list(self, make: str) -> list[CarModel]:
        schema = self.schema_class()

        raw_response = requests.get(url=self.url.format(make=make))
        response = schema.load(raw_response.json())

        return response.Results
