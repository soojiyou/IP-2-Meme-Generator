from .QuoteModel import QuoteModel
from .ingestor_interface import IngestorInterface
import pandas as pd
from typing import List


class CSVIngestor(IngestorInterface):

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.verify(path):
            raise ValueError(f"File Type not supported : {path}")
        return pd.read_csv(path).apply(lambda x: QuoteModel(body=x.body, author=x.author), axis=1).to_list()
