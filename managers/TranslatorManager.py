from googletrans import Translator

class TranslatorManager:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, language_origin='auto', language_destiny='en'):
        try:
            traductor = self.translator.translate(
                text, src=language_origin, dest=language_destiny)
            return traductor.text
        except Exception as e:
            return f"Error in translation: {str(e)}"