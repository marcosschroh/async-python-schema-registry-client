from collections import namedtuple

SchemaVersion = namedtuple("SchemaVersion", "subject schema_id schema version")

BACKWARD = "BACKWARD"
BACKWARD_TRANSITIVE = "BACKWARD_TRANSITIVE"
FORWARD = "FORWARD"
FORWARD_TRANSITIVE = "FORWARD_TRANSITIVE"
FULL = "FULL"
FULL_TRANSITIVE = "FULL_TRANSITIVE"
NONE = "NONE"

VALID_LEVELS = (BACKWARD, BACKWARD_TRANSITIVE, FORWARD, FORWARD_TRANSITIVE, FULL, FULL_TRANSITIVE, NONE)
VALID_METHODS = ("GET", "POST", "PUT", "DELETE")
VALID_AUTH_PROVIDERS = ("URL", "USER_INFO", "SASL_INHERIT")

HEADERS = "application/vnd.schemaregistry.v1+json"
HEADER_AVRO = "application/avro"
HEADER_AVRO_JSON = "application/x-avro-json"
HEADER_APPLICATION_JSON = "application/json"
HEADER_SCHEMA_REGISTRY_V1 = "application/vnd.schema_registry.v1+json"
HEADER_SCHEMA_REGISTRY = "application/vnd.schema_registry+json"

ACCEPT_HEADERS = f"{HEADER_SCHEMA_REGISTRY_V1}, {HEADER_SCHEMA_REGISTRY}, {HEADER_APPLICATION_JSON}"

URL = "url"
SSL_CA_LOCATION = "ssl.ca.location"
SSL_CERTIFICATE_LOCATION = "ssl.certificate.location"
SSL_KEY_LOCATION = "ssl.key.location"
SSL_KEY_PASSWORD = "ssl.key.password"
