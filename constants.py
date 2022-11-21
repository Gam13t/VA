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

name = {"va": ("Маша", "Машик", "Машкинс")}
action = {"tbr": ("скажи", "расскажи", "покажи", "сколько", "произнеси")}
command = {
    "ctime": ("текущее время", "сейчас времени", "который час"),
    "radio": ("включи музыку", "воспроизведи радио", "включи радио"),
    "stupid1": ("расскажи анекдот", "рассмеши меня", "ты знаешь анекдоты"),
}

action_linker = PredefinedVocabularity(name, action, command)
