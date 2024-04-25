import requests
import time
import random
import json

reference_num = random.randint(-10000, 100000)
reference = str(reference_num)
url = "https://api.hrflow.ai/v1/profile/parsing/file"
pdf_file_path = "/Users/quadr/Documents/Shibi/S3Bucket/Jacob-Hakopian.pdf"
payload = {'source_key': 'f5be79cba2be5a230eaa867185f946302d8ec528',
'reference': "1e46dsgr",
'sync_parsing': '1',
'sync_parsing_indexing': '1'}

headers = {
  'X-USER-EMAIL': 'quadratic149@gmail.com',
  'X-API-KEY': 'ask_e8f97e9583b6246cc158a35f57b725df',
  'Cookie': 'AWSALB=XKZOvKL7MAvlncALShpG1CFPyva9RXzq//+WUEerYqRqUJ/5phBP5j57TemmLVmH82tIfDmMeGKFhSQ+gOd7EITyO8IYRmxzDhawt26F5Fgw6k7JWAbXJBt5xK7B; AWSALBCORS=XKZOvKL7MAvlncALShpG1CFPyva9RXzq//+WUEerYqRqUJ/5phBP5j57TemmLVmH82tIfDmMeGKFhSQ+gOd7EITyO8IYRmxzDhawt26F5Fgw6k7JWAbXJBt5xK7B'
}
#file_pa = upload_file_and_text()
with open(pdf_file_path, 'rb') as file:
    files = [('file', ('resume.pdf', file, 'application/pdf'))]
    
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    

parsed_json = json.loads(response.text)

# Extract the 'data' field
parsed_data = parsed_json['data']
output_file_name = "extracted_data.json"

# Open the file in write mode and write the data into it
with open(output_file_name, 'w') as json_file:
    # Use json.dump to write the data into the new file
    json.dump(parsed_data, json_file, indent=4)  # Indentation for pretty-printing

#print(parsed_data)

