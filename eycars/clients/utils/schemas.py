from marshmallow import Schema, post_load


class BaseSchema(Schema):
    model = None

    @post_load
    def make_object(self, data, **kwargs) -> model:
        return self.model(**data)


