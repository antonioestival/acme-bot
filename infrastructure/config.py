from typing import List

from starlette.config import Config

config = Config('.env')


class Environments:
    # Discord integration
    DISCORD_TOKEN: str = config("DISCORD_TOKEN", cast=str, default=None)  # noqa
    DISCORD_PREFIX: str = config("DISCORD_PREFIX", cast=str, default="?")  # noqa

    # ViaCep API
    VIACEP_URL: str = config("VIACEP_URL", cast=str, default='http://www.viacep.com.br')  # noqa

