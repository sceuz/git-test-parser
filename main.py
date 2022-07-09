import csv
import json
import os
import random
import re
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
    req = requests.get(url,headers)
    req.encoding = 'utf-8'
    # with open ('project1.html','a', encoding='utf-8') as f:
    #     f.write(req.text)
    # with open('project1.html', encoding='utf-8') as file:
    #     src = file.read()
    soup = BeautifulSoup(req, 'lxml')
    divs = soup.find_all('div', class_='fusion-post-content post-content')
    print(divs)

    # project_urls = []
    # for div in divs:
    #     project_url = 'https://www.freelancejob.ru' + div.find('a').get('href')
    #     project_urls.append(project_url)
    # project_data = []
    #
    # for project_url in project_urls:
    #     req = requests.get(project_url)
    #     req.encoding = 'utf-8'
    #     project_name = project_url.split("/")[-2]
    #
    #     # with open (f"data/{project_name}.html", 'a', encoding='utf-8') as f:
    #     #     f.write(req.text)
    #
    #     with open (f"data/{project_name}.html", encoding='utf-8') as f:
    #         src = f.read()
    #     spec_divs = []
    #     soup = BeautifulSoup(src,"lxml" )
    #     project_data = soup.find('div', class_ ='col-xs-12 col-sm-9 col-md-8 x1')
    #     name = project_data.find_all('span', class_='h1')
    #     spec_div = project_data.find_all('div', class_ = 'x42')
    #     names = []
    #     for i in range(len(spec_div)):
    #         spec_divs.append(spec_div[i].text)
    #     project_skill = soup.find_all('div', class_ = 'col-xs-12 x1R')
    #     project_skills = []
    #     for i in range(len(name)):
    #         names.append(name[i].text)
    #
    #     for i in range(2,len(project_skill)):
    #         project_skills.append(project_skill[i].text)
    #     for i in names:
    #         with open('file.csv', 'w') as f:
    #             writer = csv.writer(f)
    #             writer.writerow(i)
    #     print(len(names))
    # #     spec6 = project_data.find_all('p')
    # #
    # #
    # #     specs,specs1,spec2,spec3 = [], [], [], []
    # #     for i in range(23, len(project_data5)-460,3):
    # #         spec3.append(project_data5[i].text)
    # #
    # #     for i in range(0, len(spec6)):
    # #         spec2.append(spec6[i].text)
    # #
    # #
    # #     for i in range(2,len(spec), 3):
    # #         specs.append(spec[i].text)
    # #
    # #     for i in range(3,len(spec), 3):
    # #         specs1.append(spec[i].text)
    #


get_data("URL")

