from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

from dotenv import load_dotenv

load_dotenv()


class AWSSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="AWS_")
    access_key_id: str = Field(alias="AWS_ACCESS_KEY_ID", default="test")
    secret_access_key: str = Field(alias="AWS_SECRET_ACCESS_KEY", default="test")
    region_name: str = Field(alias="AWS_REGION_NAME", default="us-east-1")


class SpotifySettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SPOTIFY_")
    username: str = Field(alias="SPOTIFY_USERNAME", default="test")
    password: str = Field(alias="SPOTIFY_PASSWORD", default="test")


class Settings(BaseSettings):
    queue_url: str = Field(alias="QUEUE_URL")
    aws: AWSSettings = AWSSettings()
    spotify: SpotifySettings = SpotifySettings()


settings = Settings()
