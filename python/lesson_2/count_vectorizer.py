from typing import Iterable, List
import re


class CountVectorizer():
    """Covert text corpus to a matrix of tocken occurances."""

    def __init__(self):
        self._vocabulary = None

    @staticmethod
    def preprocess_document(doc: str) -> str:
        """Conver document to lower case, remove special characters,
        digits and double spaces.
        """
        doc = doc.lower()
        doc = re.sub(r'[^\w\s]', '', doc)
        doc = re.sub(' +', ' ', doc)
        return doc

    def fit_transform(self, corpus: Iterable[str]) -> List[List[int]]:
        """Transform text corpus into a document-term matrix."""
        count_dict = {}
        for i, doc in enumerate(corpus):
            doc = self.preprocess_document(doc)
            for term in doc.split(' '):
                if term not in count_dict:
                    count_dict[term] = [0 for i in range(len(corpus))]
                count_dict[term][i] += 1
        self._vocabulary = list(count_dict.keys())
        count_matrix = [list(x) for x in zip(*count_dict.values())]
        return count_matrix

    def get_feature_names(self) -> List[str]:
        """Get vocabulary of transformation's terms"""
        if self._vocabulary is None:
            raise ValueError('CountVectorizer should be fitted first')
        return self._vocabulary
