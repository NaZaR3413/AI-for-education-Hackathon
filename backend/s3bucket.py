import boto3
import os
def download_folder_from_s3(bucket_name, folder_prefix, local_directory):
    """
    Download all objects from a folder in Amazon S3 to a local directory.

    Args:
    - bucket_name: The name of the S3 bucket.
    - folder_prefix: The prefix of the folder in the bucket.
    - local_directory: The local directory where the objects will be saved.
    """
    # Create a new S3 client
    s3 = boto3.client('s3')

    try:
        # List all objects in the specified folder
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)

        # Iterate through each object in the folder
        for obj in response.get('Contents', []):
            # Extract the object key
            object_key = obj['Key']
            # Construct the local file path
            local_path = os.path.join(local_directory, os.path.basename(object_key))
            # Download the object
            s3.download_file(bucket_name, object_key, local_path)
            print(f"Object downloaded successfully: {object_key}")

        print("All objects downloaded successfully.")
    except Exception as e:
        print(f"Error downloading objects: {e}")

if __name__ == "__main__":
    # Set the S3 bucket name
    bucket_name = 'educationbucket1'

    # Set the folder prefix (path to the folder within the bucket)
    folder_prefix = 'CS BS Resume/'

    # Set the local directory where the objects will be saved
    local_directory = '/Users/quadr/Documents/Shibi/S3Bucket'

    # Download all objects from the folder
    download_folder_from_s3(bucket_name, folder_prefix, local_directory)