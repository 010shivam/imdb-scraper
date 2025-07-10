# 🎬 IMDb Movie Reviews Scraper (2015–2024)

This repository contains the Python code used to scrape **featured IMDb reviews** for popular movies from **2015 to 2024** using `Selenium` and `BeautifulSoup`.

The scraper:
- Extracts movie reviews from IMDb based on a provided list of IMDb IDs
- Expands **spoiler sections** in featured reviews
- Captures the **review title**, **body**, **star rating**
- Outputs structured data in CSV/JSON formats for further analysis
- The dataset contains about 5.2K rows of reviews

---

## 📁 Files

- `scrape_movies.py`: Script to extract top movies of 10 years i.e 2014-2025
- `scrape_reviews.py` : Script to extract the featured reviews and user rating for each movie
- `imdb_list.csv`: List of IMDb movie IDs (input)
- `data/`: Output folder for scraped reviews

---

## 🖥️ Tech Stack

- Python 3
- Selenium (ChromeDriver)
- BeautifulSoup
- pandas

---

## 🚀 How to Use

1. Install requirements:
   ```bash
   pip install -r requirements.txt

