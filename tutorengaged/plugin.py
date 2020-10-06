from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

AUTH_APP_VERSION = "1.0.2"

config = {
    "add": {
        "APM_SERVER_URL": "!! PUT THE APM SERVER URL HERE !!",
        "APM_SECRET_TOKEN": "!! PUT THE APM SECRET TOKEN HERE !!",
        "SERVER_IDENTIFIER": "!! PUT THE SERVER IDENTIFIER HERE !!",

        "AUTH_APP_API_SECRET_KEY": "{{ 20|random_string }}",

        "CORE_API_SECRET_KEY": "!! PUT THE ENGAGED CORE API SECRET KEY HERE !!"
    },
    "defaults": {
        "VERSION": __version__,

        "DEFAULT_THEME": "open-edx-engaged-theme",
        "DEFAULT_TIMEZONE": "America/Sao_Paulo",

        "OPEN_EDX_MYSQL_HOST": "{{ MYSQL_HOST }}",
        "OPEN_EDX_MYSQL_DATABASE": "openedx",
        "OPEN_EDX_MYSQL_USERNAME": "{{ MYSQL_ROOT_USERNAME }}",
        "OPEN_EDX_MYSQL_PASSWORD": "{{ MYSQL_ROOT_PASSWORD }}",

        "AUTH_APP_VERSION": AUTH_APP_VERSION,
        "AUTH_APP_ENV": "production",
        "AUTH_APP_API_SERVER_PORT": 3000,
        "AUTH_APP_HOST": "engaged-auth.{{ LMS_HOST }}",
        "AUTH_APP_DOCKER_IMAGE": "{{ DOCKER_REGISTRY}}engagedu/open-edx-engaged-auth-integration:{{ ENGAGED_AUTH_APP_VERSION }}",
        "AUTH_APP_DOCKER_SERVICE_NAME": "engaged-auth",

        "CMS_FEATURE_ENABLE_CONTENT_LIBRARIES": "true",
        "CMS_FEATURE_DISABLE_COURSE_CREATION": "false",

        "CORE_API_EMIT_CERTIFICATE_URL": "https://core.engaged.com.br/internal/ead/certificate/emit"
    }
}

hooks = {
    "remote-image": {
        "engaged-auth": "{{ ENGAGED_AUTH_APP_DOCKER_IMAGE }}"
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
