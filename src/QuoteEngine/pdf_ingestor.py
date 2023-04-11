from typing import List
import subprocess
import pandas as pd
import os
from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
from .text_ingestor import TextIngestor


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        if not cls.verify(path):
            raise ValueError(f"File Type not supported : {path}")

        text_file = './pdf_to_text.txt'
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(text_file)
        os.remove(text_file)
        return quotes
