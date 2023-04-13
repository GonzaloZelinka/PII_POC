from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer import RecognizerResult
from typing import List
from presidio_anonymizer.entities import OperatorConfig

class Anonymizer:
  def anonymize(self, text: str, analyze_results: List[RecognizerResult]):
    """Anonymize identified input using Presidio Anonymizer.
    :param text: Full text
    :param analyze_results: list of results from presidio analyzer engine
    """
    operator_config = {"lambda": lambda x: x}
    operator = "custom"
    res = AnonymizerEngine().anonymize(
        text,
        analyze_results,
        operators={"DEFAULT": OperatorConfig(operator, operator_config)},
    )
    return res