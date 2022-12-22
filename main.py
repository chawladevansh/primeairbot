from bs4 import BeautifulSoup
import requests
from pprint import pprint
import schedule
import time


def getJobs():
    # create url
    url = "https://www.amazon.jobs/en/teams/prime-air"
    # define headers
    headers = { 'User-Agent': 'Generic user agent' }
    # get page
    page = requests.get(url, headers=headers)
    # let's soup the page
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        try:
            # get definition
            jobs = soup.find('h2', {'class': 'subtitle'}).text
            return jobs
        except:
            return 'Jobs not found!'
    except:
        return 'Something went wrong...'


def send_to_telegram():
    
    apiToken = '5633268737:AAHJ4-XYrDbhWOsfYrRN_RjUKHBTM6QG_Ik'
    chatID = '5330764792'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': getJobs()})
        print(response.text)
    except Exception as e:
        print(e)
        
schedule.every().day.at("11:11").do(send_to_telegram)

while True:
    schedule.run_pending()
    time.sleep(18000)