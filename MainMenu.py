import tkinter as tk
from tkinter import *
from tkinter import filedialog
from managers.SpeechToTextManager import SpeechToTextManager
from managers.TranslatorManager import TranslatorManager
import time
import os

def withoutCommand():
    print("")

def select_file():
     root = tk.Tk()
     root.withdraw()

     # Open a dialog window to select the text file and read it
     file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
     return file_path

def create_destination_directory():
    destination_directory = 'text_files(translated)/'
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    return destination_directory

def save_translation_to_file(translation, source_file_path, destination_directory):
    output_file_name = os.path.splitext(os.path.basename(source_file_path))[0] + "_translated.txt"
    full_path = os.path.join(destination_directory, output_file_name)

    with open(full_path, 'w', encoding='utf-8') as translated_file:
        translated_file.write(translation)
    return full_path

def final_print(original_text, translated_text, full_path):
    print(f"Original text: {original_text}\n")
    print(f"Translated: {translated_text}\n")
    print(f"Translation completed and saved in '{full_path}'.\n")

def speechToTextFile():
    initial_time = time.time()
    stt = SpeechToTextManager()
    filename = "audio_file_1.wav"
    text = stt.convert_speech_to_text_file(audio_file_path=filename)
    print("Recognized text: ", text)

    mainTraductor = TranslatorManager()
    mainTranslate = mainTraductor.translate(text, language_destiny='pt')
    final_time = time.time()
    print(f"Original text: {text}")
    print(f"Translated: {mainTranslate}")
    print(f"The processing time was {int(final_time - initial_time)} seconds")

def speechToTextMicrophone():
    stt = SpeechToTextManager()
    text = stt.convert_speech_to_text_microphone(microphone_input=True)
    print("Recognized text: ", text)

    mainTraductor = TranslatorManager()
    mainTranslate = mainTraductor.translate(text, language_destiny='en')
    print(f"Original text: {text}")
    print(f"Translated: {mainTranslate}")

def translatorEnglishTextFile():
        file_path = select_file()

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        
        mainTraductor = TranslatorManager()
        mainTranslate = mainTraductor.translate(text, language_destiny='pt')
               
        destination_directory = create_destination_directory()

        # Call the function to save the translation in a file and store the full name of the file in a variable.
        full_path = save_translation_to_file(mainTranslate, file_path, destination_directory)

        final_print(text, mainTranslate, full_path)

def translatorPortugueseTextFile():
        file_path = select_file()

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        
        mainTraductor = TranslatorManager()
        mainTranslate = mainTraductor.translate(text, language_destiny='en')
               
        destination_directory = create_destination_directory()

        # Call the function to save the translation in a file and store the full name of the file in a variable.
        full_path = save_translation_to_file(mainTranslate, file_path, destination_directory)

        final_print(text, mainTranslate, full_path)

app = Tk()
app.title("NExT-2023 - M01 Audio To Text")
app.geometry("500x300")
app.configure(background="#dde")

menu = Menu(app)
menuSpeechToText = Menu(menu, tearoff=0)
menuSpeechToText.add_command(
    label="From Audio File (wav)", command=speechToTextFile)
menuSpeechToText.add_command(
    label="From Microphne", command=speechToTextMicrophone)
menuSpeechToText.add_separator()
menuSpeechToText.add_command(label="Close", command=app.quit)
menu.add_cascade(label="Speech To Text", menu=menuSpeechToText)

menuTranslator = Menu(menu, tearoff=0)
menuTranslator.add_command(
    label="Text file (english to portuguese)", command=translatorEnglishTextFile)
menuTranslator.add_command(
    label="Text file (portuguese to english)", command=translatorPortugueseTextFile)
menu.add_cascade(label="Translation", menu=menuTranslator)

menuAbout = Menu(menu, tearoff=0)
menuAbout.add_command(label="Speech to Text/Translator",
                      command=withoutCommand)
menu.add_cascade(label="About", menu=menuAbout)

app.config(menu=menu)
app.mainloop()