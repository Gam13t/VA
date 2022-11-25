class PredefinedVocabularity:
    def __init__(self, name, action, command):
        self.base_dct = {}
        self.name = name
        self.action = action
        self.command = command

    @property
    def base_dct_filled(self):
        for item in (self.name, self.action, self.command):
            self.base_dct.update(item)

        return self.base_dct


# TODO: change in a more preferable way

name = {"va": ("Маша")}
action = {"tbr": ("расскажи")}
command = {
    "command": {
        "current_time": ("текущее время", "сейчас времени", "который час"),
        "open_google": (
            "открой google",
            "запусти google",
            "открой гугл",
            "запусти гугл",
            "поиск",
        ),
        "open_command_communications": (
            "открой чаты",
            "покажи сообщения",
            "проверь почту",
            "мне кто-то писал",
        ),
        "open_apple_music": (
            "открой Apple Music",
            "что послушать",
            "запусти музыку",
            "мне скучно",
        ),
        "sadness": ("меня не любят", "я ненужный"),
        "working_protocol": ("за работу", "протокол работа", "работать"),
        "joke_question": ("ты любишь подчиняться", "я люблю рабов"),
    }
}

action_linker = PredefinedVocabularity(name, action, command)
