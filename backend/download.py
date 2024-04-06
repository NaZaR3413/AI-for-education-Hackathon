import requests
import time
import random
import json
from reciever import file
reference_num = random.randint(1, 100000)
reference = str(reference_num)
url = "https://api.hrflow.ai/v1/profile/parsing/file"
pdf_file_path = "/Users/quadr/Documents/Shibi/S3Bucket/Jacob-Hakopian.pdf"
payload = {'source_key': 'f5be79cba2be5a230eaa867185f946302d8ec528',
'reference': reference,
'sync_parsing': '0',
'sync_parsing_indexing': '1'}

headers = {
  'X-USER-EMAIL': 'quadratic149@gmail.com',
  'X-API-KEY': 'ask_e8f97e9583b6246cc158a35f57b725df',
  'Cookie': 'AWSALB=XKZOvKL7MAvlncALShpG1CFPyva9RXzq//+WUEerYqRqUJ/5phBP5j57TemmLVmH82tIfDmMeGKFhSQ+gOd7EITyO8IYRmxzDhawt26F5Fgw6k7JWAbXJBt5xK7B; AWSALBCORS=XKZOvKL7MAvlncALShpG1CFPyva9RXzq//+WUEerYqRqUJ/5phBP5j57TemmLVmH82tIfDmMeGKFhSQ+gOd7EITyO8IYRmxzDhawt26F5Fgw6k7JWAbXJBt5xK7B'
}
#with open(pdf_file_path, 'rb') as file:
    #files = [('file', ('resume.pdf', file, 'application/pdf'))]
files = file  
response = requests.request("POST", url, headers=headers, data=payload, files=files)
    



#print(response.text)
time.sleep(5)
url = "https://api.hrflow.ai/v1/profile/parsing?source_key=f5be79cba2be5a230eaa867185f946302d8ec528&reference=" + reference

payload = {}
headers = {
  'X-USER-EMAIL': 'quadratic149@gmail.com',
  'X-API-KEY': 'ask_e8f97e9583b6246cc158a35f57b725df',
  'Cookie': 'AWSALB=XKZOvKL7MAvlncALShpG1CFPyva9RXzq//+WUEerYqRqUJ/5phBP5j57TemmLVmH82tIfDmMeGKFhSQ+gOd7EITyO8IYRmxzDhawt26F5Fgw6k7JWAbXJBt5xK7B; AWSALBCORS=XKZOvKL7MAvlncALShpG1CFPyva9RXzq//+WUEerYqRqUJ/5phBP5j57TemmLVmH82tIfDmMeGKFhSQ+gOd7EITyO8IYRmxzDhawt26F5Fgw6k7JWAbXJBt5xK7B'
}

response = requests.request("GET", url, headers=headers, data=payload)
parsed_data = response.json().get('data')
    
    # Print the 'data' subfield
#print(parsed_data)
#json_document = json.loads(response.text)
#print(response.text)

