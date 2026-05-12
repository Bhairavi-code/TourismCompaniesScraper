Tourism Companies Scraper
-------------------------

## Overview
This project scrapes tourism company data from the [Yellow Pages Business Directory](https://www.yellowpages.org.in/tours-And-travels/56) using Python.

Regarding implementing an automation trigger: since a simple “Scheduled Run” would not add meaningful value (the data is not dynamic like weather data), I designed the scraper to trigger automatically when data from the source changes.  
This ensures that scraping happens only when relevant updates occur.

The **Tourism Companies Scraper** can be useful for Yellow Pages Business Directory owners to implement automatic extraction of “Tours & Travels companies” data whenever their backend updates.  
I implemented the automation trigger in a Streamlit app, with timestamped Excel/CSV outputs to help directory owners keep track of datasets with precise date and time.

---

## Tools Used
- Python: requests, BeautifulSoup, pandas
- Streamlit: interactive interface and automation logic

---

## Features
- Automated scraping of tourism company data (Name, Phone, Location).
- Automatic sample email Generation for all the companies. 
- Automation trigger designed around **data changes**, not just scheduled runs.  
- Timestamped Excel/CSV outputs for version tracking.  
- Streamlit UI with 'Update' button and success messages.  
- Screenshots included for demonstration.

---

## Outputs
- **Excel file**: leads_<timestamp>.xlsx
- **CSV file**: downloaded via Streamlit  
- **Screenshots**: app interface and sample outputs  

---

## How to Run
1. Clone the repository:
   git clone https://github.com/username/TourismCompaniesScraper.git
   cd TourismCompaniesScraper
   
2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run scraper_app.py

---

## Screenshots
   Screenshots of the Streamlit app and sample outputs are available in the screenshots/ folder.
