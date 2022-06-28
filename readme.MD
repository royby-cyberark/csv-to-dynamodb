# Load csv to dynamodb

* this project uses pipenv
* `pipenv shell`
* `pipenv sync --dev`
* run with: `python csv_to_dynamodb.py -t <table name> -c <csv file>`
* IMPORTANT! Make sure your dynamodb table partition key type matches the type from the csv (string/numeric) and optionally the sort key if you have one
