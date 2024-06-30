#This program extracts all links from the 2024 election result page
import requests
from bs4 import BeautifulSoup

URL = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
#URL = "https://results.eci.gov.in/"
page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")
if page.status_code == 200:
    html_content = page.text
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Example: Extract all the links (anchor tags) from the page
links = soup.find_all('a')
#links = soup.find_all("div", class_="rslt-table teble-responsive")

# Print all the URLs
for link in links:
    print(link.get('href'))

#for job_element in links:
#    print(job_element, end="\n"*2)
