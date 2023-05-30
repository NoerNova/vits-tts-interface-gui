"""
An interface gui for vits (Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech)
"""
import os
import datetime
import pygame
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .ttsmms import TTS
from pathlib import Path


class VitsTTS(toga.App):
    def generate_audio(self, widget):
        # get model path
        model = "./models/shn"
        self.current_path = Path(__file__).resolve().parent
        self.models_dir = self.current_path.joinpath(model).resolve()
        tts = TTS(self.models_dir)

        # get user input
        input_text = self.input_text.value

        # set time stemp audio file name
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.output_path = self.current_path.joinpath("./output").resolve()
        filename = f"{self.output_path}/output_{timestamp}.wav"

        # generate tts
        tts.synthesis(input_text, wav_path=filename)

        self.audio_file = filename
        self.play_button.enabled = True

    def play_audio(self, widget):
        audio_file = self.audio_file
        if os.path.isfile(audio_file):
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.input_text = toga.MultilineTextInput(style=Pack(flex=1))
        self.generate_button = toga.Button("Generate", on_press=self.generate_audio)
        self.play_button = toga.Button("Play", on_press=self.play_audio, enabled=False)

        spacing = toga.Box(style=Pack(width=20))
        button_box = toga.Box(
            children=[self.generate_button, spacing, self.play_button],
            style=Pack(direction=ROW),
        )

        main_box = toga.Box(
            children=[self.input_text, button_box],
            style=Pack(direction=COLUMN, padding=20),
        )

        self.main_window.content = main_box
        self.main_window.show()


def main():
    return VitsTTS()
