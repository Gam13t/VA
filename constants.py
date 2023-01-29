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
action = {"tbr": ("скажи", "расскажи", "покажи", "сколько", "произнеси")}
command = {
    "command": {
        "current_time": ("текущее время", "сейчас времени", "который час"),
        "radio": ("включи музыку", "воспроизведи радио", "включи радио"),
        "stupid1": ("расскажи анекдот", "рассмеши меня", "ты знаешь анекдоты"),
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
            "протокол работа",
        ),
        "open_apple_music": (
            "открой Apple Music",
            "что послушать",
            "запусти музыку",
            "мне скучно",
        ),
    }
}

action_linker = PredefinedVocabularity(name, action, command)
