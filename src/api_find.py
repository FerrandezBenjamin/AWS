import boto3
import json
import os
from boto3.dynamodb.conditions import Key, Attr
DEVICES_TABLE = os.environ['DEVICE_TABLE']
dynamodb = boto3.resource('dynamodb')

def get_devices(context, event):
    if dynamodb:
        print('coiffeur')
        table = dynamodb.Table(DEVICES_TABLE)
        result = table.scan()
        return {
            "statusCode": 400,
            "body": {'result' : result},
            "headers": {'Access-Control-Allow-Origin': '*'}
            }


def add_device(event, context):
    if dynamodb:
        table = dynamodb.Table(DEVICES_TABLE)
        print(table.table_status)
        table.put_item(Item= {'DeviceId': '5','DeviceName':  'cccpasmoi', 'DeviceType': 'jesuisuneformuleun'})  
        return {
            "statusCode": 400,
            "body": {'ajoutOK' : 'ajoutOK' },
            "headers": {'Access-Control-Allow-Origin': '*'}
        }
    else:
        print('rate bb')