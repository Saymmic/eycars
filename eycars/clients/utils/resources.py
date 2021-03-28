from marshmallow import Schema


class Resource:
    """Base class for Resources."""

    url: str = None
    schema_class: Schema = None
