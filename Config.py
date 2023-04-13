class Config: 
  number_column_review = 2
  entities = ["PERSON", "LOCATION", "PHONE_NUMBER", "EMAIL_ADDRESS","CREDIT_CARD", "US_SSN"]
  threshold = 0.5
  check_overlaps = True
  columns = ["SITE_URL", "PVID", "REVIEW"]
  num_workers = 5
  # Define the chunk size and number of processes
  CHUNK_SIZE = 100
