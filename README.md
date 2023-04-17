## Installation

### Create a .venv

```bash
python3 -m virtualenv -p Python39 .venv
```

### Activate the .venv

```bash
#For Windows
source .venv/Scripts/activate
#For Mac
source .venv/bin/activate
```

## Important!

Inside your .venv:

- `<venv-name>/lib/<python-path>/site-packages/presidio_analyzer/analyzer_engine.py`

In order to use the score_threshold different for each entity, you need to add changes in:

- `line 3`:

  ```python
  from typing import List, Optional
  ```

  to

  ```python
  from typing import List, Optional, Union, Dict
  ```

- `line 131`:

  ```python
  score_threshold: Optional[float] = None,
  ```

  to

  ```python
  score_threshold: Optional[Union[float, Dict[str, float]] ] = None,
  ```

- `line 296`:

  ```python
  def __remove_low_scores(self, results: List[RecognizerResult], score_threshold: float = None) -> List[RecognizerResult]:
  ```

  to

  ```python
  def __remove_low_scores(
          self, results: List[RecognizerResult], score_threshold: Union[float, Dict[str, float]] = None
      ) -> List[RecognizerResult]:
  ```

- `line 309`:

  ```python
    new_results = [result for result in results if result.score >= score_threshold]
    return new_results
  ```

  to

  ```python
  if isinstance(score_threshold, dict):
            new_results: List[RecognizerResult] = []
            for result in results:
                if result.entity_type in score_threshold and result.score >= score_threshold[result.entity_type]:
                    new_results.append(result)
        elif isinstance(score_threshold, float):
            new_results = [result for result in results if result.score >= score_threshold]
        return new_results
  ```

## Using

Run the `presidio.ipynb` notebook.

## For more context:

- See the [Presidio documentation](https://microsoft.github.io/presidio/).
- See the [Explanation Document](https://docs.google.com/document/d/1QFF-VG1q9iyZAukwo-GnYcXIz_BW7Rl62G3rMbWru2U/edit?usp=sharing)
- See in HuggingFace the [Model used with Presidio (obi/deid_roberta_i2b2)](https://huggingface.co/obi/deid_roberta_i2b2)
