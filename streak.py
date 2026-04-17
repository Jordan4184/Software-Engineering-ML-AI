#Code Architecture

#Plan: Open LOG.md and read lines, extract date line, split and parese line, then append and target date to streak list

import datetime as datetime

with open('LOG.md', 'r', encoding = 'utf-8') as file: 
    streak = []
    for line in file: 
        clean_line = line.strip()
        if clean_line.startswith('##'): 
            date_str = '## Day 0 - 2026-4-14'
            partial_str = line.split(' - ') 
            just_date = partial_str[-1]
            just_date = just_date.strip()
            dt = datetime.datetime.strptime(just_date, '%Y-%m-%d')
            extracted_date = dt.date()
            streak.append(extracted_date)
    print(f'Streak = {len(streak)}')