import boto3

# setting up the S3 client
client = boto3.client('s3')
bucket_name = "tkh-nyc-education"
file_path = "data\Math_Test_Results_2013-2023_20240512.csv"


# adding objects
with open(file_path, 'rb') as f:
    data = f.read()
    response = client.put_object(
        Body=data,
        Bucket=bucket_name,
        # S3 object name
        Key='data\Math_Test_Results_2013-2023_20240512.csv'  
    )

print("Uploaded CSV file:", response)

### GETTING OBJECTS FROM A BUCKET ###
# Get the list of objects in s3
response = client.list_objects(
    Bucket=bucket_name
)
print("objects currently in Bucket:")
# iterate over names
for i in response.get("Contents", None):
    print(i.get("Key", None))


### DELETING OBJECTS FROM A BUCKET ###
# response = client.delete_object(
#    Bucket=bucket_name,
#    Key="tux-image"
#)

# print("Result of deleting object", response)
