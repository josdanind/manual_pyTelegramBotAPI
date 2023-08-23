import os, re

# Commands
from .start import start_command
from .photo import photo_command
from .audio import audio_command
from .video import video_command
from .location import location_command
from .venue import venue_command
from .poll import poll_command
from .document import document_command
from .sticker import sticker_command
from .dice import dice_command
from .group import group_command

command_names = os.listdir("bot/message_handler/commands")
commands = []

ignored_names = ["main.py", "__pycache__"]

for command in command_names:
    if command not in ignored_names:
        command = re.sub(r"\.py$", "", command)
        commands.append(command)
