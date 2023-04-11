from typing import List
from .ingestor_interface import IngestorInterface
from .QuoteModel import QuoteModel
from .docx_ingestor import DocxIngestor
from .text_ingestor import TextIngestor
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor


class Ingestor(IngestorInterface):

    ingestors = [DocxIngestor, TextIngestor,
                 CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.verify(path):
                return ingestor.parse(path)
