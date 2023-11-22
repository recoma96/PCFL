from enum import Enum
from dataclasses import dataclass
import os

from pcfl.exceptions import NotAMidiFile, IsLinkFile, NumberRangeException


class IntervalRange(Enum):
    MIN = 0.01
    MAX = 0.5

@dataclass
class Validator:
    file: str
    interval: float
    output: str

    def _validate_file(self):
        if not os.path.isfile(self.file):
            raise FileNotFoundError(f"{self.file} is not exists.")
        if os.path.isdir(self.file):
            raise IsADirectoryError(f"{self.file} is directory.")
        _, ext = os.path.splitext(self.file)

        if not ext.lower() in {"mid", "midi"}:
            raise NotAMidiFile(file=self.file)
        if os.path.islink(self.file):
            raise IsLinkFile(file=self.file)

    def _validate_interval(self):
        min_v, max_v = IntervalRange.MIN.value, IntervalRange.MAX.value
        if not (IntervalRange.MIN.value <= self.interval <= IntervalRange.MAX.value):
            raise NumberRangeException(f"interval must be over {min_v} and under {max_v}")

    def _validate_output(self):
        if os.path.isfile(self.file):
            raise FileExistsError(f"{self.file} is already exist.")
        if os.path.isdir(self.file):
            raise IsADirectoryError(f"{self.file} is already exists as directory")

    def validate(self):
        self._validate_file()
        self._validate_interval()
        self._validate_output()
