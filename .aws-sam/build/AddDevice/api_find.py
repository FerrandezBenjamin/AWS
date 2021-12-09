import boto3
import json
import os
import uuid
from boto3.dynamodb.conditions import Key, Attr
DEVICES_TABLE = os.environ['DEVICE_TABLE']
dynamodb = boto3.resource('dynamodb')

def get_devices(context, event):
    if dynamodb:
        table = dynamodb.Table(DEVICES_TABLE)
        result = table.scan()
        return {
            "statusCode": 400,
            "body": {'result' : result},
            "headers": {'Access-Control-Allow-Origin': '*'}
        }
    else:
        print('rate bb')

def add_device(context, event):
    if dynamodb:
        table = dynamodb.Table(DEVICES_TABLE)
        params = context['multiValueQueryStringParameters']
        # print(params)
        result = table.put_item(
            Item= {
                'DeviceId': uuid.uuid4().hex,
                'DeviceName':str(params['DeviceName'][0]),
                'DeviceType':str(params['DeviceType'][0])
                }
            )  
        return {
            "statusCode": 400,
            "body": {'ajoutOK' : json.dumps(result)},
            "headers": {'Access-Control-Allow-Origin': '*'}
        }
    else:
        print('rate bb')