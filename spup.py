import requests
from bs4 import BeautifulSoup
import gzip
import os
from urllib.parse import urljoin
import re

api_key = input("Enter an API-key for the shodan account where the download file has been generated:")
service = input("Enter query name:")
current_directory = os.path.abspath(os.path.dirname(__file__))
url = f"https://www.shodan.io/download?key={api_key}&query={service}"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
download_link = soup.find("a", href=lambda href: href and href.startswith("/download/"))
if download_link:
    download_url = urljoin(url, download_link["href"])
    download_response = requests.get(download_url, params={"key": api_key})
    with open("shodan_results.json.gz", "wb") as file:
        file.write(download_response.content)
    print("Download completed!")
    with gzip.open("shodan_results.json.gz", "rb") as tar_ref:
        with open("file.json", "wb") as f_out:
            f_out.write(tar_ref.read())
    print(f"File unzipped at {current_directory}!")
    os.remove("shodan_results.json.gz")
    print("Zip file deleted!")
with open("file.json", "r") as f:
    content = f.read()
    ips = []
    ports = []
    for match in re.finditer(r'"host": "([^"]+)', content):
        ips.append(match.group(1))
    for match in re.finditer(r'"port": (\d+)', content):
        ports.append(match.group(1))
    
    with open("output.txt", "w") as f:
        for i in range(len(ips)):
            f.write(ips[i] + ":" + ports[i] + "\n")
os.remove("file.json")
with open("output.txt", 'r') as input_file:
    lines = input_file.readlines()
    lines = list(set(lines))
    output_file_name = "unique_" + input_file.name
    with open(output_file_name, 'w') as output_file:
        output_file.writelines(lines)
    print(f"Duplicate lines removed and written to {output_file_name} and {input_file.name} has been deleted")
os.remove("output.txt")
