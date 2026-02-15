import argparse
from speech_translator.core import speech_to_text


def main():
    parser = argparse.ArgumentParser(description="Speech Translator CLI")
    parser.add_argument("--mic", type=int, default=None, help="Microphone index")
    parser.add_argument("--lang", type=str, default="en", help="Target language (en, hi, fr, etc)")

    args = parser.parse_args()

    print(f"Calling speech_to_text with mic={args.mic}, lang={args.lang}")

    speech_to_text(mic_index=args.mic, target_lang=args.lang)



