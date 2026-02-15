import speech_recognition as sr


def list_microphones():
    print("Available Microphones:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")
