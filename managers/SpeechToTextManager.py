import speech_recognition as sr

class SpeechToTextManager:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_speech_to_text_file(self, audio_file_path=None):
        try:
            if audio_file_path:
                with sr.AudioFile(audio_file_path) as source:
                    audio_data = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(audio_data)
            else:
                raise ValueError("You should select an audio file.")

            return text
        except sr.UnknownValueError:
            return "It was not possible to understand the speech."
        except sr.RequestError as e:
            return f"Error in the request to speech recognition service: {str(e)}"

    def convert_speech_to_text_microphone(self, microphone_input=False):
        try:
            if microphone_input:
                with sr.Microphone() as source:
                    print("Please say something...")
                    audio = self.recognizer.listen(source, phrase_time_limit=10)
                    text = self.recognizer.recognize_google(audio, language="pt-BR")
            else:
                raise ValueError("You should activate your microphone.")

            return text
        except sr.UnknownValueError:
            return "It was not possible to understand the speech."
        except sr.RequestError as e:
            return f"Error in the request to speech recognition service: {str(e)}"