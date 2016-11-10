import httplib2
import mechanize
import calendar
from bs4 import BeautifulSoup, SoupStrainer

base_url = 'https://www.google.co.in/search?q='
keyword = 'iphone 8'
keyword += ' Release Date'
start = "&start="
start_val = 0
search_url = base_url + keyword.replace(' ', '+')

def get_page_source(url_link):# Do the Google URL search as browser
    chrome = mechanize.Browser()
    chrome.set_handle_robots(False)
    chrome.addheaders = [('User-agent',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]
    return chrome.open(search_url).read()

links = []
while (start_val < 100):
    htmltext = get_page_source(search_url + start + str(start_val))
    soup = BeautifulSoup(htmltext, "html.parser")
    for link in soup.find_all('a'):
        url_link = str(link.get("href"))
        if "http" in url_link and "/search" not in url_link and "release" in url_link:
            if url_link.startswith('/'):
                links.append('https://google.com' + url_link)
            else:
                links.append(url_link)
    start_val += 10

links = set(links)

months = calendar.month_name
year_dict = {'2016' : 0, '2017' : 0, '2018' : 0, '2019' : 0, '2020' : 0}
month_dict = {'February': 0, 'October': 0, 'March': 0, 'August': 0, 'May': 0, 'January': 0, 'June': 0, 'September': 0, 'April': 0, 'July': 0, 'November': 0}
for link in links:
    print(link)
    text = get_page_source(link)
    for year in year_dict.keys():
        year_dict[year] += text.count(year)
    for month in month_dict.keys():
        month_dict[month] += text.count(month)
print(year_dict)
print(month_dict)
