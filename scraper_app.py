import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# --- SCRAPING SECTION ---
def scrape_yellowpages():
    url = "https://www.yellowpages.org.in/tours-And-travels/56"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    companies = soup.select("div.listing-info.listpopular")

    scraped_data = []
    email_joining_words = ["info", "contactus", "support", "enquiry", "tourism"]
    index = 0

    for company in companies:
        phone = company.select_one("li.float-sm-right a").text.strip() if company.select_one("li.float-sm-right a") else "N/A"
        name = company.select_one("h3 a").text.strip() if company.select_one("h3 a") else "N/A"
        location = company.select_one("li.place-location a").text.strip() if company.select_one("li.place-location a") else "N/A"
        
        email = ""

        email += email_joining_words[index]

        name_in_email = ""
        for i in range(len(name)):
            if name[i].isalpha() or name[i].isdigit():
                name_in_email += name[i]
            else:
                continue

        email += '@' + name_in_email.lower() + '.com'
        
        scraped_data.append({
            "Name": name,
            "Location": location,
            "Phone": phone,
            "Email": email
        })

        if index < len(email_joining_words)-1:
            index += 1
        else:
            index = 0

    df = pd.DataFrame(scraped_data, columns=["Name", "Phone", "Location", "Email"])
    df.drop_duplicates(inplace=True)
    df.fillna("N/A", inplace=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"leads_{timestamp}.xlsx"
    df.to_excel(filename, index=False)

    return df, filename

# --- AUTOMATION TRIGGER SECTION ---
# Triggers the scraper automatically when the data on the website is updated.
# For demonstration purpose, we have used a button 'Update Site Data' to trigger the scraper.

st.title("Tourism Companies Scraper")
st.markdown(
    """
    <h4 style='margin-left:255px;'>
        <span style='color:grey;'><i>SOURCE - </i></span>
        <a href='https://www.yellowpages.org.in/tours-And-travels/56' 
           style='color:yellow; text-decoration:none;' target='_blank'> 
        <i>Yellow Pages Business Directory</i></a>
    </h4>
    """,
    unsafe_allow_html=True
)
if st.button("Update Site Data"):
    df, filename = scrape_yellowpages()
    st.success(f"Success! Site data has been updated and saved to {filename}")
    st.dataframe(df)
