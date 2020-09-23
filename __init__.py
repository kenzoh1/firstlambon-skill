from mycroft import MycroftSkill, intent_file_handler


class Firstlambon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('firstlambon.intent')
    def handle_firstlambon(self, message):
        self.speak_dialog('firstlambon')


def create_skill():
    return Firstlambon()

