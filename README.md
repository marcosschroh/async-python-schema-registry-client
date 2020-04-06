# Async Python Rest Client Schema Registry

[![Build Status](https://travis-ci.org/marcosschroh/async-python-schema-registry-client.svg?branch=master)](https://travis-ci.com/marcosschroh/async-python-schema-registry-client.svg?branch=master)
[![GitHub license](https://img.shields.io/github/license/marcosschroh/async-python-schema-registry-client.svg)](https://github.com/marcosschroh/async-python-schema-registry-client/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/marcosschroh/async-python-schema-registry-client/branch/master/graph/badge.svg)](https://codecov.io/gh/marcosschroh/async-python-schema-registry-client)
[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)

Async Python Rest Client to interact against [schema-registry](https://docs.confluent.io/current/schema-registry/index.html) confluent server to manage [Avro Schemas](https://docs.oracle.com/database/nosql-12.1.3.1/GettingStartedGuide/avroschemas.html) resources.

## Requirements

python 3.6+, fastavro, requests-async, aiofiles

## Installation

```sh
pip install async-python-schema-registry-client
```

## Client API, Serializer and Schema Server description

**Documentation**: [https://marcosschroh.github.io/async-python-schema-registry-client.io](https://marcosschroh.github.io/async-python-schema-registry-client)

## When use this library?

Usually, we have a situacion like this:

![Confluent Architecture](docs/img/confluent_architecture.png)

So, our producers/consumers have to serialize/deserialize messages every time that they send/receive from Kafka topics. In this picture, we can imagine a `Faust` application receiving messages (encoded with an Avro schema) and we want to deserialize them, so we can ask the `schema server` to do that for us. In this scenario, the `MessageSerializer` is perfect.

Also, could be a use case that we would like to have an Application only to administrate `Avro Schemas` (register, update compatibilities, delete old schemas, etc.), so the `SchemaRegistryClient` is perfect.

## Development

The tests are run against the `Schema Server` using `docker compose`, so you will need
`Docker` and `Docker Compose` installed.

```sh
./scripts/test
```

Lint code:

```sh
./scripts/lint
```
