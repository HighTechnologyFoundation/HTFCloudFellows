## Databricks                                                                      
### Test one 1.00 resolution file:
- Function 'access_one_file' with ('nomads', 1.0) took: 2.76757 sec
- Function 'access_one_file' with ('az', 1.0) took: 1.48937 sec
- Function 'access_one_file' with ('aws', 1.0) took: 1.95945 sec
- Function 'access_one_file' with ('gcs', 1.0) took: 1.58927 sec

### Test one 0.25 resolution file:
- Function 'access_one_file' with ('nomads', 0.25) took: 5.73593 sec
- Function 'access_one_file' with ('az', 0.25) took: 10.20825 sec
- Function 'access_one_file' with ('aws', 0.25) took: 27.80119 sec
- Function 'access_one_file' with ('gcs', 0.25) took: 6.12976 sec

### Test 25 1.00 resolution files:
- Function 'access_twentyfive_files' with ('nomads', 1.0) took: 80.75929 sec
- Function 'access_twentyfive_files' with ('az', 1.0) took: 39.56601 sec
- Function 'access_twentyfive_files' with ('aws', 1.0) took: 56.08287 sec
- Function 'access_twentyfive_files' with ('gcs', 1.0) took: 48.14089 sec

### Test 25 0.25 resolution files:
- Function 'access_twentyfive_files' with ('nomads', 0.25) took: 358.19809 sec
- Function 'access_twentyfive_files' with ('az', 0.25) took: 345.88915 sec
- Function 'access_twentyfive_files' with ('aws', 0.25) took: 346.08751 sec
- Function 'access_twentyfive_files' with ('gcs', 0.25) took: 180.89464 sec

## Local
### Test one 1.00 resolution file:
- Function 'access_one_file' with ('nomads', 1.0) took: 7.65472 sec
- Function 'access_one_file' with ('az', 1.0) took: 5.08072 sec
- Function 'access_one_file' with ('aws', 1.0) took: 4.11747 sec
- Function 'access_one_file' with ('gcs', 1.0) took: 4.13002 sec

### Test one 0.25 resolution file:
- Function 'access_one_file' with ('nomads', 0.25) took: 41.95155 sec
- Function 'access_one_file' with ('az', 0.25) took: 49.56345 sec
- Function 'access_one_file' with ('aws', 0.25) took: 43.02189 sec
- Function 'access_one_file' with ('gcs', 0.25) took: 49.02692 sec

### Test 25 1.00 resolution files:
- Function 'access_twentyfive_files' with ('nomads', 1.0) took: 104.55930 sec
- Function 'access_twentyfive_files' with ('az', 1.0) took: 120.06952 sec
- Function 'access_twentyfive_files' with ('aws', 1.0) took: 109.00529 sec
- Function 'access_twentyfive_files' with ('gcs', 1.0) took: 105.30327 sec

### Test 25 0.25 resolution files:
- Function 'access_twentyfive_files' with ('nomads', 0.25) took: 1061.68678 sec
- Function 'access_twentyfive_files' with ('az', 0.25) took: 1245.69442 sec
- Function 'access_twentyfive_files' with ('aws', 0.25) took: 1130.79429 sec
- Function 'access_twentyfive_files' with ('gcs', 0.25) took: 1122.52406 sec