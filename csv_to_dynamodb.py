
import argparse
import json

import boto3
import pandas as pd


def load_csv_to_dynamodb(table: str, csv_file: str):
    print(f'Table: {table}')
    print(f'CSV Files: {csv_file}')

    df = pd.read_csv(csv_file, skipinitialspace=True)
    json_output = json.loads(df.to_json(orient='records'))

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    for item in json_output:
        table.put_item(Item=item)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv-file')    
    parser.add_argument('-t', '--table')    
    args = parser.parse_args()

    load_csv_to_dynamodb(table=args.table, csv_file=args.csv_file)



if __name__ == '__main__':
    main()
