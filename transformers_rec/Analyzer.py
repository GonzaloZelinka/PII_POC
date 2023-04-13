from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngineProvider

from .configuration import BERT_DEID_CONFIGURATION
from .transformers_recognizer import TransformersRecognizer


class Analyzer:

  def __init__(self, model_path):
    """Return AnalyzerEngine.
      :param model_path: Which model to use for NER:
          "obi/deid_roberta_i2b2",
          "en_core_web_lg"
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
      # Use small spaCy model, no need for both spacy and HF models
      # The transformers model is used here as a recognizer, not as an NlpEngine
      nlp_configuration = {
        "nlp_engine_name": "spacy",
        "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}],
      }
      registry.add_recognizer(transformers_recognizer)

    nlp_engine = NlpEngineProvider(nlp_configuration=nlp_configuration).create_engine()

    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, registry=registry)
    self._engine = analyzer

  def get_engine(self):
    """Return AnalyzerEngine."""
    return self._engine
    
  def analyze(self, **kwargs):
    """Analyze input using Analyzer engine and input arguments (kwargs)."""
    if "entities" not in kwargs or "All" in kwargs["entities"]:
        kwargs["entities"] = None
    return self._engine.analyze(**kwargs)
