import boto3

client = boto3.client('s3')

# list of buckets in s3
response = client.list_buckets()

# Loop through each bucket
# get(val1 if it exists, val2 if it does not)
for b in response.get("Buckets", None):
    print(b.get("Name", None))

# boto3 closes automatically