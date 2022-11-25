from va import VAInterface

if __name__ == "__main__":
    voice_assistant = VAInterface()
    while True:
        voice_assistant.listen_for_input()
