from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
keywords = ["essential oil"]
results = []

def fetch_articles(keyword):
    try:
        driver.get("https://pubmed.ncbi.nlm.nih.gov/")
        time.sleep(2)
        
        search_box = driver.find_element("name", "term")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        articles = soup.find_all('article', class_='full-docsum')
        keyword_results = []

        for article in articles:
            title_elem = article.find('a', class_='docsum-title')
            title = title_elem.get_text(strip=True) if title_elem else "No title available"
            
            authors_elem = article.find('span', class_='docsum-authors')
            authors = authors_elem.get_text(strip=True) if authors_elem else "No authors available"
            
            journal_elem = article.find('span', class_='docsum-journal-citation')
            journal = journal_elem.get_text(strip=True) if journal_elem else "No journal information available"
            
            abstract_link = "https://pubmed.ncbi.nlm.nih.gov" + title_elem['href'] if title_elem else None
            
            if abstract_link:
                try:
                    driver.get(abstract_link)
                    time.sleep(3)
                    
                    abstract_soup = BeautifulSoup(driver.page_source, 'html.parser')
                    abstract_section = abstract_soup.find('div', class_='abstract-content')
                    
                    abstract = abstract_section.get_text(strip=True) if abstract_section else "No abstract available"
                except Exception as e:
                    abstract = "Abstract unavailable"
            else:
                abstract = "Abstract link missing"

            keyword_results.append({
                'keyword': keyword,
                'title': title,
                'authors': authors,
                'journal': journal,
                'abstract': abstract
            })

        results.extend(keyword_results)
        return keyword_results

    except Exception as e:
        return []

for keyword in keywords:
    print(f"Processing keyword: {keyword}")
    keyword_results = fetch_articles(keyword)
    print(f"Found {len(keyword_results)} results for '{keyword}'")
    for result in keyword_results:
        print(f"- {result['title'][:50]}...")

driver.quit()

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'pubmed_results.json')
with open(desktop_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"\nSaved to: {desktop_path}")