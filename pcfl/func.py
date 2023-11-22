import os

from pcfl.validator import Validator


def pcfl(file: str, interval: float, output: str) -> str:
    """
    PCFL Function

    :param file: input filepath
    :param interval: interval between CC64s
    :param output: result root
    :return: result filepath
    """
    Validator(file=file, interval=interval, output=output).validate()

    return ""
