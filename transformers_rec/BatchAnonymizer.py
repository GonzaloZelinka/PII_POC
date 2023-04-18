from typing import List, Dict, Union, Iterable
from presidio_analyzer import RecognizerResult, DictAnalyzerResult
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import EngineResult
import collections


class BatchAnonymizer(AnonymizerEngine):
    """
    Class inheriting from the AnonymizerEngine and adding additional functionality
    for anonymizing lists or dictionaries.
    """

    def anonymize_list(
        self,
        texts: List[Union[str, bool, int, float]],
        recognizer_results_list: List[List[RecognizerResult]],
        **kwargs
    ) -> List[EngineResult]:
        """
        Anonymize a list of strings.

        :param texts: List containing the texts to be anonymized (original texts)
        :param recognizer_results_list: A list of lists of RecognizerResult,
        the output of the CustomAnalyzerEngine on each text in the list.
        :param kwargs: Additional kwargs for the `AnonymizerEngine.anonymize` method
        """
        return_list = []
        if not recognizer_results_list:
            recognizer_results_list = [[] for _ in range(len(texts))]
        for text, recognizer_results in zip(texts, recognizer_results_list):
            if type(text) in (str, bool, int, float) and len(recognizer_results) > 0:
                resp = self.anonymize(
                    text=str(text), analyzer_results=recognizer_results, **kwargs
                )
                resp = sorted(resp.items, key=lambda x: x.start)
                ents = []
                for res in resp:
                    ents.append(
                        {
                            "start": res.start,
                            "end": res.end,
                            "label": res.entity_type,
                            "text": res.text,
                        }
                    )
                return_list.append({"text": text, "entities": ents})
            else:
                return_list.append(text)

        return return_list

    def anonymize_dict(self, analyzer_results: Iterable[DictAnalyzerResult], **kwargs):
        """
        Anonymize values in a dictionary.

        :param analyzer_results: Iterator of `DictAnalyzerResult`
        containing the output of the CustomAnalyzerEngine.analyze_dict on the input text.
        :param kwargs: Additional kwargs for the `AnonymizerEngine.anonymize` method
        """

        return_dict = {}
        for result in analyzer_results:
            if isinstance(result.value, dict):
                resp = self.anonymize_dict(
                    analyzer_results=result.recognizer_results, **kwargs
                )
                return_dict[result.key] = resp

            elif isinstance(result.value, str):
                resp = self.anonymize(
                    text=result.value,
                    analyzer_results=result.recognizer_results,
                    **kwargs
                )
                resp = sorted(resp.items, key=lambda x: x.start)
                ents = []
                for res in resp:
                    ents.append(
                        {
                            "start": res.start,
                            "end": res.end,
                            "label": res.entity_type,
                            "text": res.text,
                        }
                    )
                return_dict[result.key] = {"text": result.value, "entities": ents}

            elif isinstance(result.value, collections.abc.Iterable):
                anonymize_responses = self.anonymize_list(
                    texts=result.value,
                    recognizer_results_list=result.recognizer_results,
                    **kwargs
                )
                return_dict[result.key] = anonymize_responses
            else:
                return_dict[result.key] = resp
        return return_dict
