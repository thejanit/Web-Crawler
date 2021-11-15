# Importing Required Libraries..
from bs4 import BeautifulSoup
import requests
import csv

# Creating function for our program which finds job for us.
def crawl_for_finding_job():

    # Requesting url to get desired response back
    content = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+&txtLocation=').text

    # Parsing the response with lxml parser
    soup = BeautifulSoup(content, 'lxml')       # Creating object for parsing

    # Finding all jobs by 'tag' and filter by class name
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    # Creating CSV file
    csv_file = open('jobs.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Comapany', 'Required Skills', 'Details', 'Posted']) # Adding columns name

    # Iterating over job to extract other detail
    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')   # Getting company name
        key_skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')  # Getting Required Skills
        details = job.header.a['href']      # Getting 'link' for more information regarding specific job
        posted_date = job.find('span', class_ = 'sim-posted').span.text   # Getting date of posting of job

        # Writing in csv file
        csv_writer.writerow([company_name, key_skills, details, posted_date])

    csv_file.close()


if __name__ == '__main__':
    crawl_for_finding_job()
