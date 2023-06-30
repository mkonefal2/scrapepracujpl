# scrapepracujpl

The purpose of this project is to collect data from the Pracuj.pl website and save it in csv format for further analysis.
 **Data is collected for educational purposes only**


Script uses libraries : os, csv, requests, BeautifulSoup, glob, pandas, re, and datetime.


## scrapepracujpl.py
This script starts by removing all the CSV files in the current directory. Then it defines a function called scrape_jobs that takes a URL as an argument. The function sends an HTTP request to the URL and parses the HTML content using BeautifulSoup. It then extracts job offers from the HTML content and writes them to a CSV file. Finally, it calls the scrape_jobs function for each page of job offers on the website.
Finally, the script runs add_group_col.py with os.system(‘python3 correct.py’).

## correct.py
The python script is intended to process a CSV file containing job offers. It then defines the convert_salary() function that converts the salary values ​​in job postings. This function checks if the salary value is a string and contains the word "net". Then it removes spaces and characters that are not numbers or decimal points. If the salary value is a range, the function divides it into two values ​​and multiplies them by 1.23 (VAT). If the minimum value is less than 1000, it multiplies it by 40. The function returns the minimum and maximum salary values.
The script then imports a CSV file containing job offers and processes the Salary column using the convert_salary() function. The results are stored in the MIN and MAX columns. The Salary column is removed from the dataframe. The script also adds a Date column containing the current date in the YYYY-MM-DD format. The results are saved to a CSV file named job_offers_salary.csv.
Finally, the script runs add_group_col.py with os.system(‘python3 add_group_col.py’).

## add_group_col.py
This script is written in Python and uses the pandas library. It reads a CSV file called job_offers_salary.csv into a pandas DataFrame. 
It then applies the apply method to the Title column of the DataFrame to create a new column called Groups. The apply method applies a lambda function to each value in the Title column to determine the group that the job offer belongs to. The lambda function uses a series of if-else statements to check for keywords in the job title and assign the appropriate group. Finally, it writes the modified DataFrame to a new jobs.csv file.

### Usage 

```bash 
python3 scrapepracujpl.py
```
Personally I am using it from crontab and uploading data to mysql

```bash
20 12 * * * mysqlimport  --ignore-lines=1 --fields-terminated-by=',' --fields-optionally-enclosed-by='"' --silent --local -u datauser  PRACUJ_PL /home/valkyrie/scrape_jobs/jobs.csv
00 12 * * * python3 /home/valkyrie/scrape_jobs/scrapepracujpl.py
```
