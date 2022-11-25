import os

from dataclasses import dataclass
from dotenv import load_dotenv

# TODO: rework this in a more propper venv approach
@dataclass
class Config:
    login: str
    password: str
    api_key: str
    email: str
    hardware_provider_credentials: dict
    debug: bool = False
    network_tests: bool = True

    va_name: str = "Маша"

    def __init__(self):
        load_dotenv()

        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.email = os.getenv("EMAIL")
        self.api_key = os.getenv("API_KEY")

        self.network_tests = os.getenv("NETWORK_TESTS")

        self.hardware_provider_credentials = {
            "login": self.login,
            "password": self.password,
            "email": self.email,
            "api_key": self.api_key,
        }

        self.va_name = os.getenv("VA_NAME").lower()


filled_config = Config()
