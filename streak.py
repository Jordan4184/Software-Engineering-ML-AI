#Code Architecture

#Plan: Open LOG.md and read lines, extract date line, target date line to calculate streak

import datetime as datetime

with open('LOG.md', 'r', encoding = 'utf-8') as file: 
    for line in file: 
        clean_line = line.strip()
        if clean_line.startswith('##'): 
            date_str = '2026-04-14'
            dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            extracted_date = dt.date()
            print(extracted_date)

#If date from yesterday is not equal to 0 and datetime equals today: 
    #then increase streak counter by 1 
#Else streak = 1 


