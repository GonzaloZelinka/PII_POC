class Config: 
  entities = ["PERSON", "LOCATION", "PHONE_NUMBER", "EMAIL_ADDRESS","CREDIT_CARD", "US_SSN"]
  threshold = 0.5
  check_overlaps = True
  columns = ["SITE_URL","ITEM_GROUP_ID","PVID","REVIEW"]
  BATCH_SIZE = 2000
