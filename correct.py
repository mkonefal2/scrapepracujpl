#Correct Scrape PracujPL
import os
import pandas as pd
import re
from datetime import datetime

def convert_salary(salary):
    if isinstance(salary, str):
        if salary == 'None':
            return salary, 'None'
        netto = 'net' in salary.lower()
        salary = salary.split('/')[0]
        salary = re.sub(r'\s+', '', salary)
        salary = re.sub(r'[^\d.–]+', '', salary)
        if '–' in salary:
            salary_range = salary.split('–')
            try:
                min_salary = float(salary_range[0])
                max_salary = float(salary_range[1])
                if netto:
                    min_salary *= 1.23
                    max_salary *= 1.23
                if min_salary < 1000:
                    min_salary *= 40
                if max_salary < 1000:
                    max_salary *= 40
                return min_salary, max_salary
            except ValueError:
                return None, 'None'
        else:
            try:
                min_salary = float(salary)
                if netto:
                    min_salary *= 1.23
                if min_salary < 1000:
                    min_salary *= 40
                return min_salary, 'None'
            except ValueError:
                return None, 'None'
    else:
        return None, 'None'


df = pd.read_csv('job_offers.csv')
df[['MIN', 'MAX']] = df['Salary'].apply(convert_salary).apply(pd.Series)
df.drop(columns=['Salary'], inplace=True)
df['Date'] = datetime.now().strftime('%Y-%m-%d')
df.to_csv('job_offers_salary.csv', index=False)
os.system('python3 add_group_col.py')
