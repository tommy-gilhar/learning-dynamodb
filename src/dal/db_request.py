class DBRequest:
    def __init__(self, ac: str, sc: str):
        self.__access_key = ac
        self.__secret_key = sc

    def create_table(self, primary_key_name: str, primary_key_type: str, table_name: str):
        params = {
            'TableName': table_name,
            'KeySchema': [
                {'AttributeName': primary_key_name, 'KeyType': 'HASH'}
            ],
            'AttributeDefinitions': [
                {'AttributeName': primary_key_name, 'AttributeType': primary_key_type}
            ]
        }
        print(params)
        # TODO: call boto3 create table


if __name__ == "__main__":
    pass
    # db_request = DBRequest('sexrdctfn', 'drcftbhunj')
    # db_request.create_table('dog_id', 'N', 'Doggies')
