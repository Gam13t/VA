import logging
from va import VAInterface

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    voice_assistant = VAInterface()
    while True:
        try:
            voice_assistant.listen_for_input()
        except Exception as e:
            logger.exception(
                f"An exception has occured while trying to listen for an input, the detailed exception: {e}"
            )
