import pytest

from schema_registry.client import schema as schema_loader
from tests import data_gen


@pytest.mark.asyncio
async def test_getters(client):
    subject = "test-basic-schema"
    parsed_basic = schema_loader.AvroSchema(data_gen.BASIC_SCHEMA)
    await client.register(subject, parsed_basic)
    schema = await client.get_by_id(1)
    assert schema is not None

    subject = "subject-does-not-exist"
    latest = await client.get_schema(subject)
    assert latest is None

    schema_id = await client.register(subject, parsed_basic)
    latest = await client.get_schema(subject)
    fetched = await client.get_by_id(schema_id)

    assert fetched == parsed_basic


@pytest.mark.asyncio
async def test_get_subjects(client, user_schema_v3, country_schema):
    subject_user = "test-user-schema"
    subject_country = "test-country"

    await client.register("test-user-schema", user_schema_v3)
    await client.register("test-country", country_schema)

    subjects = await client.get_subjects()

    assert subject_user in subjects
    assert subject_country in subjects
