


import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init

init(autoreset=True)


def translate_audio(text, target_lang='en'):
    try:
        return translate(text, target_lang)
    except Exception as e:
        return f"Translation error: {e}"


def speech_to_text(mic_index=None, target_lang="en"):
    print("Mic Index:", mic_index)
    print("Target Language:", target_lang)
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    print(Fore.GREEN + "Speech Translator Started (Ctrl+C to stop)")
    print(f"Using Microphone Index: {mic_index}")
    print(f"Target Language: {target_lang}")

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            while True:
                try:
                    print(Fore.YELLOW + "\nListening...")
                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=8
                    )

                    print("Recognizing...")
                    text = recognizer.recognize_google(audio)

                    print(Fore.CYAN + f"Original: {text}")

                    translated = translate_audio(text, target_lang)
                    print(Fore.BLUE + f"Translated: {translated}")

                except sr.WaitTimeoutError:
                    print(Fore.RED + "No speech detected")

                except sr.UnknownValueError:
                    print(Fore.RED + "Could not understand audio")

                except sr.RequestError as e:
                    print(Fore.RED + f"Google API error: {e}")

    except KeyboardInterrupt:
        print(Fore.RED + "\nStopped by user")
