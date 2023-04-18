from typing import List, Optional, Dict, Union, Iterable

from presidio_analyzer import DictAnalyzerResult, RecognizerResult
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
from .BatchAnonymizer import BatchAnonymizer


class Anonymizer:
    def __init__(self, type: str = "simple"):
        if type == "simple":
            self._engine = AnonymizerEngine()
        elif type == "batch":
            self._engine = BatchAnonymizer()
        else:
            raise ValueError("type must be either 'simple' or 'batch'")

    def anonymize(
        self,
        analyze_results: Union[List[RecognizerResult], Iterable[DictAnalyzerResult]],
        operator_config: Dict[str, OperatorConfig] = {"lambda": lambda x: x},
        operator: str = "custom",
        text: Optional[str] = None,
    ):
        """Anonymize identified input using Presidio Anonymizer.
        :param text: Full text to be anonymized
        :param analyze_results: list of results from presidio analyzer engine
        :param operator_config: configuration for the operator
        :param operator: operator to use for anonymization
        """
        if isinstance(self._engine, AnonymizerEngine) and text is not None:
            res = self._engine.anonymize(
                text,
                analyze_results,
                operators={"DEFAULT": OperatorConfig(operator, operator_config)},
            )
            return res
        elif isinstance(self._engine, BatchAnonymizer):
            res = self._engine.anonymize_dict(
                analyze_results,
                operators={"DEFAULT": OperatorConfig(operator, operator_config)},
            )
            return res
