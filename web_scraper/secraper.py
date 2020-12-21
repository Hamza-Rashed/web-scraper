import requests
from bs4 import BeautifulSoup
import json

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(URL): 
    resultOfPage = requests.get(URL)
    soup = BeautifulSoup(resultOfPage.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")
    return results

def get_citations_needed_report(URL): 
    resultOfPage = requests.get(URL)
    soup = BeautifulSoup(resultOfPage.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    paragraphs  = []
    lines = []

    resultsss = results.find_all('p') # get all paragraphs
    for res in resultsss:
            all_para = res.find_all('span', string = 'citation')
            if all_para:
                for hamza in range(len(all_para)):
                        paragraphs.append(res.text) 
                        poset = res.text.index('citation') 
                        line = res.text[poset].split(". ")
                        lines.append(line[-1])
