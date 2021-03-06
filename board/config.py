import os

from dynaconf import Dynaconf

current_directory = os.path.dirname(os.path.realpath(__file__))

settings = Dynaconf(
    envvar_prefix="ENV", settings_files=[
        f"{current_directory}/settings.toml"
    ],
)
