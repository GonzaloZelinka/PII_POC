from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from .custom_analyzer_engine import CustomAnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider

from .configuration import BERT_DEID_CONFIGURATION, BERT_PII_CONFIGURATION
from .transformers_recognizer import TransformersRecognizer
from .BatchAnalyzer import BatchAnalyzer


class Analyzer:
    def __init__(self, model_path, type):
        """Return CustomAnalyzerEngine or BatchAnalyzerEngine.
        :param model_path: Which model to use for NER:
            "obi/deid_roberta_i2b2",
            "en_core_web_lg"
        :param type: "batch" or "simple".
        """
        self._analyzer = None
        self._engine = None

        registry = RecognizerRegistry()
        registry.load_predefined_recognizers()
        if model_path == "en_core_web_lg":
            nlp_configuration = {
                "nlp_engine_name": "spacy",
                "models": [{"lang_code": "en", "model_name": "en_core_web_lg"}],
            }
        else:
            # Using a small spaCy model + a HF NER model
            transformers_recognizer = TransformersRecognizer(model_path=model_path)
            if model_path == "obi/deid_roberta_i2b2":
                transformers_recognizer.load_transformer(**BERT_DEID_CONFIGURATION)
            elif model_path == "gonzazelinka/custom-bert-model-PII":
                transformers_recognizer.load_transformer(**BERT_PII_CONFIGURATION)
            # Use small spaCy model, no need for both spacy and HF models
            # The transformers model is used here as a recognizer, not as an NlpEngine
            nlp_configuration = {
                "nlp_engine_name": "spacy",
                "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}],
            }
            registry.add_recognizer(transformers_recognizer)

        nlp_engine = NlpEngineProvider(
            nlp_configuration=nlp_configuration
        ).create_engine()

        analyzer = CustomAnalyzerEngine(nlp_engine=nlp_engine, registry=registry)
        if type == "batch":
            self._engine = BatchAnalyzer(analyzer_engine=analyzer)
        else:
            self._engine = analyzer

    def get_engine(self):
        """Return CustomAnalyzerEngine."""
        return self._engine

    def analyze(self, **kwargs):
        """Analyze input using Analyzer engine and input arguments (kwargs).
        :param input_dict: The input dictionary for analysis in batch mode, executed with analyze_dict method of BatchAnalyzer
        :param keys_to_skip: Keys to ignore during analysis in batch mode with input_dict argument.
        :param texts: The list of texts for analysis in batch mode, executed with analyze_iterator method of BatchAnalyzer
        :param text: The text for analysis in simple mode, executed with analyze method of CustomAnalyzerEngine

        :param language: Input language"""
        if "entities" not in kwargs or "All" in kwargs["entities"]:
            kwargs["entities"] = None
        if isinstance(self._engine, BatchAnalyzer) and "input_dict" in kwargs:
            return self._engine.analyze_dict(**kwargs)
        elif isinstance(self._engine, BatchAnalyzer) and "texts" in kwargs:
            return self._engine.analyze_iterator(**kwargs)
        elif isinstance(self._engine, CustomAnalyzerEngine) and "text" in kwargs:
            return self._engine.analyze(**kwargs)
        else:
            raise ValueError("Invalid input arguments.")
