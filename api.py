from bs4 import BeautifulSoup
import requests

url = "https://www.ippbonline.com/web/ippb/current-openings"

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract headings, paragraphs, or job entries
        for job in soup.find_all('li'):
            print(job.get_text(strip=True))
    else:
        print(f"Failed to fetch page. Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
