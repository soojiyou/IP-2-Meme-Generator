from typing import List
from .QuoteModel import QuoteModel

extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface:
    @classmethod
    def verify(cls, file_extension):
        return file_extension in extensions.values()

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
