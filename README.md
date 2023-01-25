# Shodan-Parse-Using-Python
Downloads and Parses shodan results and gives a proper list of unique ip:port found from specific searches.

A simple python script that downloads the results of a query from SHODAN and extracts IP:Port information from the results, removing duplicates and writing the unique IP:Port combinations to a new file.

# Usage:
# Clone the repository to your local machine

`git clone https://github.com/HackerPrat/Shodan-Parse-Using-Python/`

-Navigate to the root directory of the project

`cd Shodan-Parse-Using-Python`

-Run the script using python

`python spup.py`

**Enter the required details for the SHODAN API-Key and the query name**

The script will download the results from SHODAN, extract IP:Port information from the results, remove duplicates and write the unique IP:Port combinations to a new file named "unique_output.txt"

# Requirements

Python 3.x

requests

BeautifulSoup

gzip

GeckoDriver: [Download](https://github.com/mozilla/geckodriver/releases)

# Note:
The script will remove the intermediate files "shodan_results.json.gz" and "file.json" and "output.txt" after the process.

Happy Parsing!
