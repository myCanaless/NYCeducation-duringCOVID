import boto3
import pandas as pd
from io import StringIO, BytesIO


# create s3 client
s3 = boto3.client('s3')

# specify the bucket & folder you'd like to interact with

name = 'tkh-nyc-education'
folder = 'data/'

# view all objects within this folder
response = s3.list_objects_v2(Bucket=name, Prefix=folder)

print("\n Multiple object retrieval \n")
####
# NOTE: The below code is for when you have multiple objects

# Example code: concatenate all files together
concat_list = []

# Interacting with multiple objects
# loop through all objects, handle them as a data frame
for file in response['Contents']:
    fname = file['Key']

    # if this is a csv file...
    if fname.endswith('.csv') or fname.endswith('.xlsx'):
        # get csv object
        object = s3.get_object(Bucket=name, Key=fname)
        print(fname)
        
        if fname.endswith('.csv'):
            df = pd.read_csv(object['Body'],low_memory=False)
            concat_list.append(df)
        elif fname.endswith('.xlsx'):
            object = s3.get_object(Bucket=name, Key=fname)
            excel_data = object['Body'].read()  
            excel_file = BytesIO(excel_data)    
            excel = pd.ExcelFile(excel_file)
                
            for sheet_name in excel.sheet_names:
                df = pd.read_excel(excel,sheet_name=sheet_name,engine='openpyxl')
                csv_file = f'{sheet_name}.csv'
                df = df.to_csv(csv_file,index=False)
                
                concat_list.append(df)
            #print(concat_list)
        


# concatenate all files together
hpot_data = pd.concat(concat_list)

# verify columns
#print(hpot_data.columns)
# verify shape
#print(hpot_data.shape)
####

# print("\n Single object retrieval \n")
####
# NOTE: Alternatively, we can also load one object at a time
# name = "tkh-nyc-education"
# file = "data/"
# single_object = s3.get_object(Bucket=name, Key=file)
# single_df = pd.read_csv(single_object['Body'])
# print(single_df.head())
####

# Lastly, after we are done performing our transformations, we load this data back into our bucket

# create an empty buffer to prepare our data push
buffer = StringIO()

# load our dataframe into this placeholder
# single_df.to_csv(buffer, index=False)

# push this buffer to our s3 data store
s3.put_object(
    Bucket='tkh-nyc-education',
    Key='transformed_file.csv',
    Body=buffer.getvalue()
)
