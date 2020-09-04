from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

AUTH_APP_VERSION = "1.0.2"
LOGSTASH_VERSION = "7.8.0"
MYSQL_SOURCE_CONNECTOR_VERSION = "1.0.1"

config = {
    "add": {
        "AWS_ACCESS_KEY": "!! PUT THE AWS ACCESS KEY HERE !!",
        "AWS_SECRET_KEY": "!! PUT THE AWS SECRET KEY HERE !!",

        "APM_SERVER_URL": "!! PUT THE APM SERVER URL HERE !!",
        "APM_SECRET_TOKEN": "!! PUT THE APM SECRET TOKEN HERE !!",

        "SERVER_IDENTIFIER": "!! PUT THE SERVER IDENTIFIER HERE !!",

        "LOGSTASH_CLOUD_ID": "!! PUT THE ELASTIC CLOUD ID HERE !!",
        "LOGSTASH_CLOUD_AUTH_USER": "!! PUT THE ELASTICSEARCH USER HERE !!",
        "LOGSTASH_CLOUD_AUTH_PASS": "!! PUT THE ELASTICSEARCH PASS HERE !!",
        "LOGSTASH_ELASTICSEARCH_HOST": "!! PUT THE ELASTICSEARCH HOST HERE !!",

        "AUTH_APP_API_SECRET_KEY": "{{ 20|random_string }}"
    },
    "defaults": {
        "VERSION": __version__,

        "DEFAULT_THEME": "open-edx-engaged-theme",
        "DEFAULT_TIMEZONE": "America/Sao_Paulo",

        "AWS_REGION": "sa-east-1",

        "OPEN_EDX_MYSQL_HOST": "{{ MYSQL_HOST }}",
        "OPEN_EDX_MYSQL_DATABASE": "openedx",
        "OPEN_EDX_MYSQL_USERNAME": "{{ MYSQL_ROOT_USERNAME }}",
        "OPEN_EDX_MYSQL_PASSWORD": "{{ MYSQL_ROOT_PASSWORD }}",

        "LOGSTASH_VERSION": LOGSTASH_VERSION,
        "LOGSTASH_SERVICE_NAME": "engaged-logstash",
        "LOGSTASH_DOCKER_IMAGE": "docker.elastic.co/logstash/logstash:{{ ENGAGED_LOGSTASH_VERSION }}",

        "MYSQL_SOURCE_CONNECTOR_VERSION": MYSQL_SOURCE_CONNECTOR_VERSION,
        "MYSQL_SOURCE_CONNECTOR_ENV": "production",
        "MYSQL_SOURCE_CONNECTOR_AWS_EVENTBRIDGE_BUS_NAME": "open-edx-event-bus",
        "MYSQL_SOURCE_CONNECTOR_AWS_EVENTBRIDGE_PRODUCER_NAME": "open-edx-mysql-source-connector",
        "MYSQL_SOURCE_CONNECTOR_DOCKER_IMAGE": "{{ DOCKER_REGISTRY}}engagedu/open-edx-mysql-source-connector:{{ ENGAGED_MYSQL_SOURCE_CONNECTOR_VERSION }}",
        "MYSQL_SOURCE_CONNECTOR_DOCKER_SERVICE_NAME": "engaged-mysql-source-connector",
        "MYSQL_SOURCE_CONNECTOR_LOGSTASH_PORT": 5001,
        "MYSQL_SOURCE_CONNECTOR_LOGSTASH_INDEX_NAME": "open-edx-mysql-source-connector-{{ ENGAGED_SERVER_IDENTIFIER }}",

        "AUTH_APP_VERSION": AUTH_APP_VERSION,
        "AUTH_APP_ENV": "production",
        "AUTH_APP_API_SERVER_PORT": 3000,
        "AUTH_APP_HOST": "engaged-auth.{{ LMS_HOST }}",
        "AUTH_APP_DOCKER_IMAGE": "{{ DOCKER_REGISTRY}}engagedu/open-edx-engaged-auth-integration:{{ ENGAGED_AUTH_APP_VERSION }}",
        "AUTH_APP_DOCKER_SERVICE_NAME": "engaged-auth",
        "AUTH_APP_LOGSTASH_PORT": 5000,
        "AUTH_APP_LOGSTASH_INDEX_NAME": "open-edx-engaged-auth-integration-api-{{ ENGAGED_SERVER_IDENTIFIER }}",
    }
}

hooks = {
    "remote-image": {
        "engaged-auth": "{{ ENGAGED_AUTH_APP_DOCKER_IMAGE }}",
        "engaged-logstash": "{{ ENGAGED_LOGSTASH_DOCKER_IMAGE }}",
        "engaged-mysql-source-connector": "{{ ENGAGED_MYSQL_SOURCE_CONNECTOR_DOCKER_IMAGE }}"
    },
}


def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
