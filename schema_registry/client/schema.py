import json
import typing

import aiofiles
import fastavro


class AvroSchema:
    def __init__(self, schema: str):
        if isinstance(schema, str):
            schema = json.loads(schema)
        self.schema = fastavro.parse_schema(schema, _force=True)
        self.generate_hash()

    def generate_hash(self):
        self._hash = hash(json.dumps(self.schema))

    @property
    def name(self) -> str:
        return self.schema.get("name")

    def __hash__(self) -> int:
        return self._hash

    def __str__(self) -> str:
        return str(self.schema)

    def __eq__(self, other: typing.Any) -> bool:
        if not isinstance(other, AvroSchema):
            return NotImplemented
        return self.__hash__() == other.__hash__()


async def load(fp: str) -> AvroSchema:
    """Parse a schema from a file path"""
    async with aiofiles.open(fp, mode="r") as f:
        content = await f.read()
        return AvroSchema(content)
