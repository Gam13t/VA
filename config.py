import os

from typing import Optional, Tuple, Dict
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path


@dataclass
class ChatGPTConfig:
    """
    Config for handling Chat GPT API credentials
    """

    chat_gpt_org_key: str
    chat_gpt_api_key: str

    def __init__(self):
        self.chat_gpt_api_key = os.getenv("CHAT_GPT_API_KEY")
        self.chat_gpt_org_key = os.getenv("CHAT_GPT_ORG_KEY")


@dataclass
class VADesiredBehaviorConfig:
    """
    Config for Voice Assistant config handling to custom Voice Assistant instance behaviour.
    """

    va_name: Optional[Tuple[str]] = "Маша"
    base_reply: Optional[Tuple[str]] = "ОК"

    def __init__(self):
        load_dotenv()

        self.base_reply = os.getenv("BASE_REPLY").split(",")
        self.va_name = os.getenv("VA_NAME").split(",")


@dataclass
class ActionSpecConfig:
    """
    Config for Voice Assistant config handling to custom action providers(like browsers, links, paths)
    """

    working_directory: Optional[Tuple[str]]
    music_provider_link: str
    video_provider_link: str
    web_explorer_link: str
    application_path: Path
    media_folder: Path

    def __init__(self):
        load_dotenv()

        self.working_directory = os.getenv("WORKING_DIRECTORY").split(",")
        self.music_provider_link = os.getenv("MUSIC_PROVIDER_LINK")
        self.video_provider_link = os.getenv("VIDEO_PROVIDER_LINK")
        self.web_explorer_link = os.getenv("WEB_EXPLORER_LINK")
        self.application_path = os.getenv("APPLICATION_PATH")
        self.media_folder = os.getenv("MEDIA_FOLDER")


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
        self.gpt_credentials = ChatGPTConfig()
        self.debug = os.getenv("DEBUG")

        self.hardware_provider_credentials = {
            "login": self.login,
            "password": self.password,
            "email": self.email,
            "api_key": self.api_key,
        }

        self.va_name = os.getenv("VA_NAME").lower()


filled_config = Config()
