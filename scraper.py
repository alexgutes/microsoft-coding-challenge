import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def scrape_wikipedia_page(num_words=10, exclude_words=None):
    if exclude_words is None:
        exclude_words = []
    
    try:
        URL_TO_CRAWL = 'https://en.wikipedia.org/wiki/Microsoft'
        response = requests.get(URL_TO_CRAWL)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            content = soup.find('div', class_='mw-parser-output')
            text = " ".join(paragraph.get_text() for paragraph in content.find_all('p'))
            
            words = re.findall(r'\b\w+\b', text.lower())
            
            words = [word for word in words if word not in exclude_words]
            
            word_counts = Counter(words)
            
            most_common_words = word_counts.most_common(num_words)
            
            print(f"Top {num_words} Most Common Words (Excluding {', '.join(exclude_words)}):")
            for word, count in most_common_words:
                print(f"{word}: {count}")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    num_words = int(input("Enter the number of words to return (default: 10): ") or 10)
    exclude_words = input("Enter words to exclude (comma-separated): ").split(',')
    
    exclude_words = [word.strip().lower() for word in exclude_words]
    
    scrape_wikipedia_page(num_words, exclude_words)
