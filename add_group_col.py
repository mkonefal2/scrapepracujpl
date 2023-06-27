import pandas as pd

df = pd.read_csv('job_offers_salary.csv')

df['Groups'] = df['Title'].apply(lambda x: "Developer" if "Developer" in x else ("Engineer" if "Engineer" in x else ("Analyst" if "Analyst" in x or "Analityk" in x else ("Architect" if "Architect" in x else ("Administrator" if "Admin" in x or "Linux" in x or " IT" in x else ("Manager" if "Manager" in x or "Head" in x or "Kierownik" in x or "lead" in x or "Lead" in x else ("Consultant" if "Consultant" in x or "Konsultant" in x or "consultant" in x else ("Cybersec" if "cyber" in x.lower() or "bezpie" in x.lower() or "Cyber" in x or "sec" in x.lower() or "Sec" in x else ("Tester" if "test" in x.lower() or "Test" in x else ("UX/UI" if "UX" in x.upper() or "UI" in x.upper() else ("Other")))))))))))

df.to_csv('jobs.csv', index=False)
