from setuptools import setup, find_packages

setup(
    name="speech-translator-rushikesh",   # choose unique name
    version="0.1.0",
    author="Rushikesh Jagtap",
    description="Real-time speech translator using SpeechRecognition",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition",
        "pydub",
        "mtranslate",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "speech-translator=speech_translator.cli:main"
        ]
    },
    python_requires=">=3.8",
)
