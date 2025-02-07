# BBC News Scraper

A Python-based web scraper to extract news headlines, summaries, and links from the BBC News homepage. The scraped data is saved to a CSV file for further analysis or use.

---

## Features

- Extracts news headlines, summaries, and links from `bbc.com/news`.
- Handles multiple types of news cards (e.g., `london-card`, `edinburgh-card`).
- Saves the scraped data to a CSV file using `pandas`.
- Easy to set up and use.

---

## Prerequisites

Before running the scraper, ensure you have the following installed:

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`, and `pandas`.

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

__Step 1__ : Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/bbc-news-scraper.git
cd bbc-news-scraper
```

__Step 2__ : Run the Scraper
Run the scraper script:

```bash
python bbc_scraper.py
```

This will:
Scrape the latest news articles from the BBC News homepage.

Save the data to a CSV file named bbc_news.csv.

__Step 3__ : Check the Output
The scraped


