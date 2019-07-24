import pytest

from schema_registry.client import schema, errors
from schema_registry.client.client import requests

from tests import data_gen


@pytest.mark.asyncio
async def test_compatibility(client, user_schema_v3):
    """
    Test the compatibility of a new User Schema against the User schema version 2.
    """
    subject = "test-user-schema"
    version_2 = schema.AvroSchema(data_gen.USER_V2)
    await client.register(subject, version_2)

    compatibility = await client.test_compatibility(subject, user_schema_v3)
    assert compatibility


@pytest.mark.asyncio
async def test_update_compatibility_for_subject(client):
    """
    The latest User V2 schema is  BACKWARD and FORWARDFULL compatibility (FULL).
    So, we can ipdate compatibility level for the specified subject.
    """
    assert await client.update_compatibility("FULL", "test-user-schema")


@pytest.mark.asyncio
async def test_update_global_compatibility(client):
    """
    The latest User V2 schema is  BACKWARD and FORWARDFULL compatibility (FULL).
    So, we can ipdate compatibility level for the specified subject.
    """
    assert await client.update_compatibility("FULL")


@pytest.mark.asyncio
async def test_update_compatibility_fail(client, response_klass, async_mock):
    http_code = 404
    mock = async_mock(
        requests.sessions.Session, "request", returned_value=response_klass(http_code)
    )

    with mock:
        with pytest.raises(errors.ClientError) as excinfo:
            await client.update_compatibility("FULL", "test-user-schema")

            assert excinfo.http_code == http_code


@pytest.mark.asyncio
async def test_get_compatibility_for_subject(client):
    """
    Test latest compatibility for test-user-schema subject
    """
    assert await client.get_compatibility("test-user-schema") == "FULL"


@pytest.mark.asyncio
async def test_get_global_compatibility(client):
    """
    Test latest compatibility for test-user-schema subject
    """
    assert await client.get_compatibility() is not None
