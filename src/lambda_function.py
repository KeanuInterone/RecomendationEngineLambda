def lambda_handler(event, context):
    """
    Lambda function entry point.
    """
    message = event.get('message', 'Hello, Keanu')
    return {
        'statusCode': 200,
        'body': message
    }