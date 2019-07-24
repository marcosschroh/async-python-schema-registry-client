import os

import pytest
import requests_async as requests

from schema_registry.client import SchemaRegistryClient, schema

from tests import data_gen


@pytest.mark.asyncio
async def test_context(client):
    async with client as c:
        parsed = schema.AvroSchema(data_gen.BASIC_SCHEMA)
        schema_id = await c.register("test-basic-schema", parsed)
        assert schema_id > 0
        assert len(c.id_to_schema) == 1


def test_cert_no_key():
    with pytest.raises(ValueError):
        SchemaRegistryClient(
            url="https://127.0.0.1:65534", cert_location="/path/to/cert"
        )


def test_cert_with_key():
    client = SchemaRegistryClient(
        url="https://127.0.0.1:65534",
        cert_location="/path/to/cert",
        key_location="/path/to/key",
    )

    assert ("/path/to/cert", "/path/to/key") == client.session.cert


def test_custom_headers():
    extra_headers = {"custom-serialization": "application/x-avro-json"}

    client = SchemaRegistryClient(
        url="https://127.0.0.1:65534", extra_headers=extra_headers
    )
    assert extra_headers == client.extra_headers


@pytest.mark.asyncio
async def test_override_headers(client, deployment_schema, response_klass, async_mock):
    extra_headers = {"custom-serialization": "application/x-avro-json"}
    client = SchemaRegistryClient(
        url=os.getenv("SCHEMA_REGISTRY_URL"), extra_headers=extra_headers
    )

    assert (
        client.prepare_headers().get("custom-serialization")
        == "application/x-avro-json"
    )

    subject = "test"
    override_header = {"custom-serialization": "application/avro"}

    mock = async_mock(
        requests.sessions.Session,
        "request",
        returned_value=response_klass(200, content={"id": 1}),
    )

    with mock:
        await client.register(subject, deployment_schema, headers=override_header)

        prepare_headers = client.prepare_headers(body="1")
        prepare_headers["custom-serialization"] = "application/avro"

        mock.assert_called_with(headers=prepare_headers)


def test_cert_path():
    client = SchemaRegistryClient(
        url="https://127.0.0.1:65534", ca_location="/path/to/ca"
    )

    assert "/path/to/ca" == client.session.verify


def test_init_with_dict():
    client = SchemaRegistryClient(
        {
            "url": "https://127.0.0.1:65534",
            "ssl.certificate.location": "/path/to/cert",
            "ssl.key.location": "/path/to/key",
        }
    )
    assert "https://127.0.0.1:65534" == client.url_manager.url


def test_empty_url():
    with pytest.raises(AssertionError):
        SchemaRegistryClient({"url": ""})


def test_invalid_type_url():
    with pytest.raises(AttributeError):
        SchemaRegistryClient(url=1)


def test_invalid_type_url_dict():
    with pytest.raises(AttributeError):
        SchemaRegistryClient({"url": 1})


def test_invalid_url():
    with pytest.raises(AssertionError):
        SchemaRegistryClient({"url": "example.com:65534"})


def test_basic_auth_url():
    client = SchemaRegistryClient(
        {"url": "https://user_url:secret_url@127.0.0.1:65534"}
    )

    assert ("user_url", "secret_url") == client.session.auth


def test_basic_auth_userinfo():
    client = SchemaRegistryClient(
        {
            "url": "https://user_url:secret_url@127.0.0.1:65534",
            "basic.auth.credentials.source": "user_info",
            "basic.auth.user.info": "user_userinfo:secret_userinfo",
        }
    )
    assert ("user_userinfo", "secret_userinfo") == client.session.auth


def test_basic_auth_sasl_inherit():
    client = SchemaRegistryClient(
        {
            "url": "https://user_url:secret_url@127.0.0.1:65534",
            "basic.auth.credentials.source": "SASL_INHERIT",
            "sasl.mechanism": "PLAIN",
            "sasl.username": "user_sasl",
            "sasl.password": "secret_sasl",
        }
    )
    assert ("user_sasl", "secret_sasl") == client.session.auth


def test_basic_auth_invalid():
    with pytest.raises(ValueError):
        SchemaRegistryClient(
            {
                "url": "https://user_url:secret_url@127.0.0.1:65534",
                "basic.auth.credentials.source": "VAULT",
            }
        )
