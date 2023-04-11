from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
import pandas as pd
from typing import List


class DocxIngestor(IngestorInterface):

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.verify(path):
            raise ValueError(f"File Type not supported : {path}")

        doc = docx.Document(docx=path)
        quotes = []
        for paragraph in doc.paragraphs:
            paragraph.text and quotes.append(
                QuoteModel(*paragraph.text.split(" - ")))
        return quotes
