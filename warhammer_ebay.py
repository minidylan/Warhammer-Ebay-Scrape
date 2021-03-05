# Ebay shop Warhammer mini scrape

# This script is for Warhammer Age of Sigmar

#TODO
#1. Make a request to Ebay.com and get a page
#2. Collect data from eatch page
#3. Collect all links to detaul page of each product
#4. Write scrapped data to a csv file

import csv
import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup  = BeautifulSoup(response.text, 'lxml')
    return soup

    

def get_detail_data(soup):
    # Title
    # Price
    

    try:
        title = soup.find('h1', id='itemTitle').text
    except:
        title = ''
    

    try:
        price = soup.find('span', id='prcIsum').text
    except:
        price = ''
    
    data = {
        'title': title,
        'price': price,
    }

    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href')for item in links]
    
    return urls

def write_csv(data, url):
    with open('output.csv','a') as csvfile:
        writer = csv.writer(csvfile)

        row = [data['title'], data['price'], url]

        writer.writerow(row)


    


def main():
    url = "https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=warhammer+age+of+sigmar&_pgn=1"
    get_page(url)

    product = get_index_data(get_page(url))

    for link in product:
        data = get_detail_data(get_page(link))
        write_csv(data, link)
        

   





if __name__ == '__main__':
    main()