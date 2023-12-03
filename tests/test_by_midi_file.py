import pytest
import os

from pcfl import pcfl_by_file
from pcfl.core.exceptions import NotAMidiFile, MidiParseFailedException


def test_file_is_not_exists():
    with pytest.raises(FileNotFoundError):
        pcfl_by_file(os.path.join(os.getcwd(), "tests", "assets", "aaaa.mid"), "output.mid")


def test_not_a_midi_file():
    with pytest.raises(NotAMidiFile):
        pcfl_by_file(os.path.join(os.getcwd(), "tests", "assets", "not-midi-file.txt"), "output.mid")


def test_midi_file_is_crashed():
    with pytest.raises(MidiParseFailedException):
        pcfl_by_file(os.path.join(os.getcwd(), "tests", "assets", "error.mid"), "output.mid")


def test_output_file_is_already_exists():
    with pytest.raises(FileExistsError):
        pcfl_by_file(
            os.path.join(os.getcwd(), "tests", "assets", "mido-practice.mid"),
            os.path.join(os.getcwd(), "tests", "assets", "error.mid")
        )
