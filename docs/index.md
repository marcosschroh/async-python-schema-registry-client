# Async Python Rest Client Schema Registry

**This work has been overtaken by the python-schema-registry-client project:** https://github.com/marcosschroh/python-schema-registry-client

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

## When to use this library

Usually, we have a situacion in which we have producers/consumers that serialize/deserialize events to send/receive from Kafka topics. In this picture, we can imagine a `Faust` or `Flink` application receiving/sending messages (encoded with an Avro schema)

![Confluent Architecture](docs/img/confluent_architecture.png)

`Avro schemas` have to be maintained and also need to be used to encode/decode events. On those situation this library is convenient to use.

*Summary*:

* When we want to build an application to administrate `Avro Schemas` (register, update compatibilities, delete old schemas, etc.)
* When we have a process that needs to serialize/deserialize events to send/receive to/from a kafka topics

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
