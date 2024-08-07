from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    POSTGRE_SERVER: str
    POSTGRE_PORT: int = 5432
    POSTGRE_USER: str
    POSTGRE_PASSWORD: str
    POSTGRE_DB: str

    @property
    def db_url(self):
        return MultiHostUrl.build(
            scheme='postgresql+asyncpg',
            host=self.POSTGRE_SERVER,
            username=self.POSTGRE_USER,
            password=self.POSTGRE_PASSWORD,
            port=self.POSTGRE_PORT,
            path=self.POSTGRE_DB
        )


setting = Setting()

if __name__ == "__main__":
    setting = Setting()
    from pprint import pprint
    pprint(setting.json())
    pprint(setting.db_url)
