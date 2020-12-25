import requests
from bs4 import BeautifulSoup
    
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(URL)
def get_citations_needed_count(soup):
    page = requests.get(URL)
    results = BeautifulSoup(page.content, 'html.parser').find(id="bodyContent").find_all('a', title='Wikipedia:Citation needed')
    return len(results)

def get_citations_needed_report(soup):
    all_paragraphs = BeautifulSoup(page.content, 'html.parser').find(id="bodyContent").find_all('p')

    all_paragraph=[]
    for paragraph in all_paragraphs:
        result_paragraph = paragraph.find('a', { "title" : "Wikipedia:Citation needed"})
        if result_paragraph:
            all_paragraph.append(paragraph.text)
    return all_paragraph
    
def get_citations_needed_by_section(soup):
    all_sections = BeautifulSoup(page.content, 'html.parser').find(id="bodyContent").find_all('section')

    all_section=[]
    for section in all_sections:
        result_section = section.find('a', { "title" : "Wikipedia:Citation needed"})
        if result_section:
            all_section.append(section.text)
    return all_section
    

if __name__ == "__main__":

    soup = BeautifulSoup(page.content, 'html.parser')

    print ("citations needed: ", get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
    print(get_citations_needed_by_section(URL))