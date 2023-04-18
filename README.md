# Installation

## Create a .venv

```bash
python3 -m virtualenv -p Python39 .venv
```

## Activate the .venv

```bash
#For Windows
source .venv/Scripts/activate
#For Mac
source .venv/bin/activate
```

# Install dependencies

```bash
pip install -r requirements.txt
```

# Using

You have some examples in the `presidio.ipynb` notebook.

## Run model with csv data

- It is necessary to run the `utils/run_model.py` script in the presidio notebook or in the terminal, for this function, the model must always be run in `batch mode` (below is only an optimized n-call method).
- At the moment, the available models are `obi/deid_roberta_i2b2` from HuggingFace and a `custom-bert-model`.
- Initially (but you could change the function to accept another type of csv), The input csv file should have the following order:

```csv
"["id1", "id2"]","This product is awesome!"
"["id3", "id4"]","This product is bad..."
```

The first column is a list representing the IDs (e.g. PVIDs) associated with the review (second column).

- For improved performance, you can run the model with a [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) device.

# For more context:

- See the [Presidio documentation](https://microsoft.github.io/presidio/).
- See the [Explanation Document](https://docs.google.com/document/d/1QFF-VG1q9iyZAukwo-GnYcXIz_BW7Rl62G3rMbWru2U/edit?usp=sharing)
- See in HuggingFace the [Model used with Presidio (obi/deid_roberta_i2b2)](https://huggingface.co/obi/deid_roberta_i2b2)
