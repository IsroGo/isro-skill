from mycroft import MycroftSkill, intent_file_handler


class Isro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('isro.intent')
    def handle_isro(self, message):
        self.speak_dialog('isro')


def create_skill():
    return Isro()

