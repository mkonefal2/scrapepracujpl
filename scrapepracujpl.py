import os
import csv
import requests
from bs4 import BeautifulSoup
import glob

for file in glob.glob("*.csv"):
    os.remove(file)

def scrape_jobs(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_offers = soup.find_all('div', class_='listing_c7z99rl')

    for offer in job_offers:
        title = offer.find('h2', class_='listing_buap3b6').text
        company = offer.find('h4', class_='listing_eiims5z size-caption listing_t1rst47b').text
        salary_element = offer.find('span', class_='listing_sug0jpb')
        if salary_element:
            salary = salary_element.text
        else:
            salary = 'None'
    #print(f'{title}, {company}, {salary}')
        csv_writer.writerow([title, company, salary])


with open('job_offers.csv', mode='w', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Title', 'Company', 'Salary'])

    base_url = 'https://www.pracuj.pl/praca/praca%20zdalna;wm,home-office?cc=5015%2C5016&pn='
    for page_number in range(1, 60): 
        url = base_url + str(page_number)
        scrape_jobs(url)

os.system('python3 correct.py')
