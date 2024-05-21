from bs4 import BeautifulSoup
import requests

def analyze_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting title
    title = soup.title.string if soup.title else 'No title found'
    
    # Extracting meta description
    description = soup.find('meta', attrs={'name': 'description'})
    description = description['content'] if description else 'No description found'
    
    # Extracting keywords
    keywords = soup.find('meta', attrs={'name': 'keywords'})
    keywords = keywords['content'] if keywords else 'No keywords found'
    
    return {
        'title': title,
        'description': description,
        'keywords': keywords
    }

if __name__ == "__main__":
    url = 'https://example.com'
    print(analyze_seo(url))
