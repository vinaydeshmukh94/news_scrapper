import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape news from BBC News
def scrape_bbc_news():
    url = "https://www.bbc.com/news"  # BBC News homepage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all news articles on the page (both london-card and edinburgh-card)
    articles = soup.find_all("div", {"data-testid": ["london-card", "edinburgh-card"]})

    news_data = []

    # Extract headline, summary, and link for each article
    for article in articles:
        headline = article.find("h2", {"data-testid": "card-headline"})
        summary = article.find("p", {"data-testid": "card-description"})
        link = article.find("a", {"data-testid": "internal-link"})

        if headline and summary and link:
            news_data.append({
                "Headline": headline.text.strip(),
                "Summary": summary.text.strip(),
                "Link": "https://www.bbc.com" + link["href"]
            })

    return news_data



def save_to_csv(news_data, filename="news_aggregator.csv"):
    """
    Args:
        news_data (list of dict): List of dictionaries containing news data.
        filename (str): Name of the CSV file to save the data.
    """
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(news_data)
    
    # Rename columns to match the desired CSV header
    df.rename(columns={
        "Headline": "Headline",
        "Summary": "Summary",
        "Link": "Link"
    }, inplace=True)
    
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False, encoding="utf-8")

# Main function
if __name__ == "__main__":
    print("Scraping news from BBC...")
    news_data = scrape_bbc_news()

    if news_data:
        print(f"Found {len(news_data)} articles.")
        save_to_csv(news_data)
        print("News data saved to 'news_aggregator.csv'.")
    else:
        print("No articles found.")