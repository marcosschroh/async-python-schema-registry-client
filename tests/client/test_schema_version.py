import pytest


@pytest.mark.asyncio
async def test_version_does_not_exists(client, country_schema):
    assert await client.check_version("test-schema-version", country_schema) is None


@pytest.mark.asyncio
async def test_get_versions(client, country_schema):
    subject = "test-schema-version"
    await client.register(subject, country_schema)
    versions = await client.get_versions(subject)

    assert versions


@pytest.mark.asyncio
async def test_get_versions_does_not_exist(client):
    assert not await client.get_versions("random-subject")


@pytest.mark.asyncio
async def test_check_version(client, country_schema):
    subject = "test-schema-version"
    schema_id = await client.register(subject, country_schema)
    result = await client.check_version(subject, country_schema)

    assert subject == result.subject
    assert schema_id == result.schema_id


@pytest.mark.asyncio
async def test_delete_version(client, country_schema):
    subject = "test-schema-version"
    await client.register(subject, country_schema)
    versions = await client.get_versions(subject)
    latest_version = versions[-1]

    assert latest_version == await client.delete_version(subject, latest_version)


@pytest.mark.asyncio
async def test_delete_version_does_not_exist(client, country_schema):
    subject = "test-schema-version"
    await client.register(subject, country_schema)

    assert not await client.delete_version("random-subject")
    assert not await client.delete_version(subject, "random-version")
