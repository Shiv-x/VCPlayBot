from os import listdir
from os import mkdir

if 'raw_files' not in listdir():
    mkdir('raw_files')

from VCPlayBot.services.converter.converter import convert

__all__ = ["convert"]
