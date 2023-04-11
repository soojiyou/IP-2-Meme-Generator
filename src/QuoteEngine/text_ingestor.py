from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
import pandas as pd
from typing import List


class TextIngestor(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        if not cls.verify(path):
            raise ValueError(f"File Type not supported : {path}")
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        return [QuoteModel(*quote.rstrip("\n").split(" - ")) for quote in lines]
