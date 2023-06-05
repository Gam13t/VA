import os

from typing import Optional, Tuple, Dict
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path


@dataclass
class VADesiredBehaviorConfig:
    base_reply: Optional[Tuple[str]] = "ОК"

    def __init__(self):
        load_dotenv()

        self.base_reply = os.getenv("BASE_REPLY")


@dataclass
class ActionSpecConfig:
    working_directory: Optional[Tuple[str]]
    music_provider_link: str
    video_provider_link: str
    web_explorer_link: str
    application_path: Path

    def __init__(self):
        load_dotenv()

        self.working_directory = os.getenv("WORKING_DIRECTORY")
        self.music_provider_link = os.getenv("MUSIC_PROVIDER_LINK")
        self.video_provider_link = os.getenv("VIDEO_PROVIDER_LINK")
        self.web_explorer_link = os.getenv("WEB_EXPLORER_LINK")
        self.application_path = os.getenv("APPLICATION_PATH")


@dataclass
class Config:
    language: str
    login: str
    password: str
    api_key: str
    email: str
    hardware_provider_credentials: Dict
    action_spec_config: ActionSpecConfig
    va_behavior_config: VADesiredBehaviorConfig

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
        self.language = os.getenv("LANGUAGE")
        self.action_spec_config = ActionSpecConfig()
        self.va_behavior_config = VADesiredBehaviorConfig()
        self.debug = os.getenv("DEBUG")

        self.hardware_provider_credentials = {
            "login": self.login,
            "password": self.password,
            "email": self.email,
            "api_key": self.api_key,
        }

        self.va_name = os.getenv("VA_NAME").lower()


filled_config = Config()
