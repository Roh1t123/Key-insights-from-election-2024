import requests
import csv
from bs4 import BeautifulSoup
#bjp
#URL = "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm"
#congres
URL = "https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm"
page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")
if page.status_code == 200:
    html_content = page.text
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('div', class_="table-responsive")

#Array to print the data on console for verification
data = []
#Array to print the data on csv for insight generation
datacsv = []

# Check if the table is found
if table:
    # Extract data from each row (skipping the header row)
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip the first row (header)
        cells = row.find_all('td')
        if cells:
            No = cells[0].text.strip()
            Const = cells[1].text.strip()
            win = cells[2].text.strip()
            Total = cells[3].text.strip()
            Margin = cells[4].text.strip()
            data.append({'S.No': No, 'Const': Const, 'win': win, 'Total': Total, 'Margin': Margin})
            datacsv.append([No,Const,win,Total,Margin])
            print(data)

#define a python function to save it on CSV file
def print_save(data):
    csv_file = 'extracted_data.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['S.No', 'Parliament Constituency', 'Winning Candidate', 'Total Votest', 'Margin'])
        writer.writerows(data)
# Print the extracted data
        #for item in data:
            #writer.writerows(data)
            #print(f"S.No: {item['S.No']}, Const: {item['Const']}, win: {item['win']}, Total: {item['Total']}, Margin: {item['Margin']}")
        print(f'Extracted data has been saved to {csv_file}')

#Invoke the python function to save the data in CSV
print_save(datacsv)
