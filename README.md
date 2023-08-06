## Python Script: Web Scraping and Data Processing from Pracuj.pl
The Python script that scrapes the data from Pracuj.pl processes the data and saves it to a CSV file.

## How it works?
The script first deletes all existing CSV files in the directory.
Then he scrapes job offers from pracuj.pl for remote work. Data such as job title, company name, and salary are saved to a CSV file.
The script then loads the CSV file and processes the salary column, converting the values ​​to minimum and maximum salary.
Finally, the script ranks the jobs based on the title and adds that classification as a new column to the DataFrame, then saves the resulting DataFrame to a new CSV file.
