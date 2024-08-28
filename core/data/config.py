from dataclasses import dataclass
from typing import Type, List, TypeVar
from environs import Env

T = TypeVar('T')

@dataclass
class Bots:
    bot_token: str
    admin_ids: List[int]

@dataclass
class Api:
    api_url: str
    api_code: str

@dataclass
class Settings:
    bots: Bots

@dataclass
class SettingsAPI:
    api: Api

def load_settings(config_class: Type[T], path: str = ".env") -> T:
    env = Env()
    env.read_env(path)

    env_vars = {
        'bot_token': env.str('TOKEN'),
        'admin_ids': [int(admin) for admin in env.list('ADMINS')],
        'api_url': env.str('API_URL'),
        'api_code': env.str('API_CODE'),
    }

    if config_class == Settings:
        return Settings(bots=Bots(bot_token=env_vars['bot_token'], admin_ids=env_vars['admin_ids']))
    elif config_class == SettingsAPI:
        return SettingsAPI(api=Api(api_url=env_vars['api_url'], api_code=env_vars['api_code']))


settings = load_settings(Settings)
settings_api = load_settings(SettingsAPI)
