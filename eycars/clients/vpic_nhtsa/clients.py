from eycars.clients.vpic_nhtsa.resources import ModelsForMakeResource


class NHTSAvPICApiClient:
    def __init__(self) -> None:
        self.models_for_make = ModelsForMakeResource()


client = NHTSAvPICApiClient()
