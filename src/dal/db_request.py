import boto3


class DBRequest:
    def __init__(self, ac: str, sc: str):
        self.__access_key = ac
        self.__secret_key = sc

    def create_table(self, primary_key_name: str, primary_key_type: str, table_name: str):
        client = boto3.client(
            'dynamodb',
            region_name="eu-west-1",
            aws_access_key_id=self.__access_key,
            aws_secret_access_key=self.__secret_key
        )
        params = {
            'TableName': table_name,
            'KeySchema': [
                {'AttributeName': primary_key_name, 'KeyType': 'HASH'}
            ],
            'AttributeDefinitions': [
                {'AttributeName': primary_key_name, 'AttributeType': primary_key_type}
            ],
            'BillingMode': 'PAY_PER_REQUEST'
        }
        response = client.create_table(**params)
        print(response)


if __name__ == "__main__":

    db_request = DBRequest('accessKey', 'secretKey')
    db_request.create_table('dog_id', 'N', 'Doggies')
