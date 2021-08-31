# indeed scrape

import requests
import bs4
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import os
from webdriver_manager.chrome import ChromeDriverManager
import time

# Data Analyst

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

max_page = 670

jobs11 = []
companies11 = []
locations11 = []
summaries11 = []

print("Running Data Analyst Scrape ...")

for start in range(0, max_page, 10):
    indeed_url = 'http://www.indeed.com/jobs?q=data%20analyst&l=California&start=' + str(start)
    browser.visit(indeed_url)
    time.sleep(5)  
    html = browser.html
    soup = bs(html, "html.parser")
    #print(indeed_url)  
    
    #grabbing job title
    #for div in soup.find_all(name='div', attrs={'class':'job_seen_beacon'}):
    for td in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div in td.find_all(name='div', attrs={'class':'heading4 color-text-primary singleLineTitle tapItem-gutter'}):
            for span in div.find_all(name='span'):
                if span.text.strip() != 'new':
                    jobs11.append(span.text.strip())  

    #grabbing company name
    for td2 in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div2 in td2.find_all(name='div', attrs={'class':'heading6 company_location tapItem-gutter'}):
            for span2 in div2.find_all(name='span', attrs={'class':'companyName'}):
                companies11.append(span2.text.strip())      

    #grabbing location
    for td3 in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div3 in td3.find_all(name='div', attrs={'class':'heading6 company_location tapItem-gutter'}):
            for div4 in div3.find_all(name='div'):
                locations11.append(div4.text.strip())   

    #grabbing summary text
    divs = soup.findAll('div', attrs={'class': 'job-snippet'})
    for div5 in divs:
        summaries11.append(div5.text.strip())

print("Done with Data Analyst Scrape")

browser.quit()

# remove \n from summaries
summaries11_noreturn = [word.replace('\n',' ') for word in summaries11]

# create dataframe
job_list_analyst_df = pd.DataFrame(list(zip(jobs11, companies11, locations11, summaries11_noreturn)),
               columns = ['job_title', 'company_name', 'location', 'summary'])

# add column for the source of this data
job_list_analyst_df['job_search'] = pd.Series(["data analyst" for x in range(len(job_list_analyst_df.index))])

# Data Scientist

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

max_page = 710

jobs12 = []
companies12 = []
locations12 = []
summaries12 = []

print("Running Data Scientist Scrape ...")

for start in range(0, max_page, 10):
    indeed_url2 = 'http://www.indeed.com/jobs?q=data%20scientist&l=California&start=' + str(start)
    browser.visit(indeed_url2)
    time.sleep(5)  
    html = browser.html
    soup = bs(html, "html.parser")
    #print(indeed_url2)  
    
    #grabbing job title
    #for div in soup.find_all(name='div', attrs={'class':'job_seen_beacon'}):
    for td in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div in td.find_all(name='div', attrs={'class':'heading4 color-text-primary singleLineTitle tapItem-gutter'}):
            for span in div.find_all(name='span'):
                if span.text.strip() != 'new':
                    jobs12.append(span.text.strip())  

    #grabbing company name
    for td2 in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div2 in td2.find_all(name='div', attrs={'class':'heading6 company_location tapItem-gutter'}):
            for span2 in div2.find_all(name='span', attrs={'class':'companyName'}):
                companies12.append(span2.text.strip())      

    #grabbing location
    for td3 in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div3 in td3.find_all(name='div', attrs={'class':'heading6 company_location tapItem-gutter'}):
            for div4 in div3.find_all(name='div'):
                locations12.append(div4.text.strip())   

    #grabbing summary text
    divs = soup.findAll('div', attrs={'class': 'job-snippet'})
    for div5 in divs:
        summaries12.append(div5.text.strip())

print("Done with Data Scientist Scrape")

browser.quit()

# remove \n from summaries
summaries12_noreturn = [word2.replace('\n',' ') for word2 in summaries12]

# create dataframe
job_list_sci_df = pd.DataFrame(list(zip(jobs12, companies12, locations12, summaries12_noreturn)),
               columns = ['job_title', 'company_name', 'location', 'summary'])

# add column for the source of this data
job_list_sci_df['job_search'] = pd.Series(["data scientist" for y in range(len(job_list_sci_df.index))])

# Data Engineer

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

max_page = 340

jobs14 = []
companies14 = []
locations14 = []
summaries14 = []

print("Running Data Engineer Scrape ...")

for start in range(0, max_page, 10):
    indeed_url3 = 'http://www.indeed.com/jobs?q=data%20engineer&l=California&start=' + str(start)
    browser.visit(indeed_url3)
    time.sleep(5)  
    html = browser.html
    soup = bs(html, "html.parser")
    #print(indeed_url3)  
    
    #grabbing job title
    #for div in soup.find_all(name='div', attrs={'class':'job_seen_beacon'}):
    for td in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div in td.find_all(name='div', attrs={'class':'heading4 color-text-primary singleLineTitle tapItem-gutter'}):
            for span in div.find_all(name='span'):
                if span.text.strip() != 'new':
                    jobs14.append(span.text.strip())  

    #grabbing company name
    for td2 in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div2 in td2.find_all(name='div', attrs={'class':'heading6 company_location tapItem-gutter'}):
            for span2 in div2.find_all(name='span', attrs={'class':'companyName'}):
                companies14.append(span2.text.strip())      

    #grabbing location
    for td3 in soup.find_all(name='td', attrs={'class':'resultContent'}):
        for div3 in td3.find_all(name='div', attrs={'class':'heading6 company_location tapItem-gutter'}):
            for div4 in div3.find_all(name='div'):
                locations14.append(div4.text.strip())   

    #grabbing summary text
    divs = soup.findAll('div', attrs={'class': 'job-snippet'})
    for div5 in divs:
        summaries14.append(div5.text.strip())

print("Done with Data Engineer Scrape")

browser.quit()

# remove \n from summaries
summaries14_noreturn = [word3.replace('\n',' ') for word3 in summaries14]

# create dataframe
job_list_eng_df = pd.DataFrame(list(zip(jobs14, companies14, locations14, summaries14_noreturn)),
               columns = ['job_title', 'company_name', 'location', 'summary'])

# add column for the source of this data
job_list_eng_df['job_search'] = pd.Series(["data engineer" for z in range(len(job_list_eng_df.index))])

# Full Job List

job_list_all = [job_list_analyst_df, job_list_sci_df, job_list_eng_df]
job_list_all_df = pd.concat(job_list_all)
job_list_all_df.to_csv('job_list_all.csv', index=False)

print("---Done---")
