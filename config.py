from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings """
    
    app_name:str  = "Inventery Management System"
    debug:bool  = True
    database_url: str = "sqlite:///./inventery.db"    


    class Config:
        env_file = "venv"


settings = Settings()