import pandas as pd
from Config import Config
# import multiprocessing as mp
import json
from process_review import process_review2 
import time 
import torch 
import torch.multiprocessing as mp

# def chunked_data(data, chunk_size):
#     """Yield chunks of data with the specified chunk size."""
#     print(f"Chunking data into chunks of size {chunk_size}...")
#     print(f"Total number of chunks: {len(data) // chunk_size}")
#     print(f"Total number of reviews: {len(data)}")
#     for i in range(0, len(data), chunk_size):
#         yield data[i:i+chunk_size]


def model_results_parallel(input_path, output_path):
    
    # Read input data
    df = pd.read_csv(input_path, encoding="ISO-8859-1", header=0, names=Config.columns)
    # Extract the review column
    all_values = df["REVIEW"].tolist()
    # Create pool of worker processes
    # num_workers = mp.cpu_count() - 6
    pool = mp.Pool(Config.num_workers)


    print(f"Getting results for the NER model and Presidio Analyzer using {Config.num_workers} workers...")
    start_time = time.time()
     # Create a pool of worker processes
    with pool:
        # Map the process_data function to chunks of the input data
        results = pool.map(process_review2, all_values)
    print(f'end of run: {time.time()-start_time}')
    print("Saving results to json file...")
    with open(output_path, 'w', encoding="ISO-8859-1") as fp:
        json.dump(results, fp)
    print("Done!")

if __name__ == "__main__":
  model_results_parallel("testing-data/sentences_from_db.csv", "testing-data/testing.json")