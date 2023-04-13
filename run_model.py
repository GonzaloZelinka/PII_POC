import pandas as pd
from Config import Config
import multiprocessing as mp
import json
from process_review import process_review2 
import time 
import psutil
import os

def model_results_parallel(input_path, output_path):
    # Read input data
    df = pd.read_csv(input_path, encoding="ISO-8859-1", header=0, names=Config.columns)
    # Extract the review column
    all_values = df.values.tolist()

    # Create pool of worker processes
    # num_workers = mp.cpu_count() - 6
    pool = mp.Pool(Config.num_workers)


    print(f"Getting results for the NER model and Presidio Analyzer using {Config.num_workers} workers...")
    start_time = time.time()
    with pool as p:
        results = p.map(process_review2, all_values)
    print(f'end of run: {time.time()-start_time}')
    print("Saving results to json file...")
    with open(output_path, 'w', encoding="ISO-8859-1") as fp:
        json.dump(results, fp)
    print("Done!")

if __name__ == "__main__":
  model_results_parallel("testing-data/sentences_from_db copy.csv", "testing-data/testing.json")