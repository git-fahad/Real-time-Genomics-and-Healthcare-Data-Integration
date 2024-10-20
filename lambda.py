import json
import boto3

kinesis = boto3.client('kinesis')

def lambda_handler(event, context):
    healthcare_data = json.loads(event['body'])
    
    if 'patient_id' not in healthcare_data or 'diagnosis_code' not in healthcare_data:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid data: missing required fields.')
        }
    
    transformed_data = {
        'patient_id': healthcare_data['patient_id'],
        'diagnosis_code': healthcare_data['diagnosis_code'],
        'visit_date': healthcare_data['visit_date'],
        'doctor': healthcare_data.get('doctor', 'Unknown')
    }
    
    response = kinesis.put_record(
        StreamName='healthcare',
        Data=json.dumps(transformed_data),
        PartitionKey=transformed_data['patient_id']  # Use patient_id as the partition key
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed and sent to Kinesis successfully.')
    }
