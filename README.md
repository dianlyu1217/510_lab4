# 510_lab4

# How to Run
Open the terminal and run the following commands:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

# What's include
app.py - main running application.  
db.py - dal layer, include definition of books table and functions to operate database.
scraper.py - scrape data from internet and save into database.
.gitignore - tells Git which files or directories to ignore in a project.  
requirements.txt - list all the dependencies that the project needs to run correctly.  
README.md - includes the text info of the basic introduction of this GitHub Repository, how to run, what's included, lessons learned, questions / uncertainties.  

# Lesson Learned
Importance of URL Encoding:
I learned how to use the urllib.parse.quote function in Python to encode special characters in URLs, which is crucial for constructing web requests and handling URLs with special characters to ensure their correctness and transferability.
Web Scraping Techniques:
I gained knowledge on how to use regular expressions and BeautifulSoup for extracting and parsing web content. This is essential for data collection and automating the process of handling web data.
Handling Time Series Data:
I understood the basics of time series data such as sensor data, event data, and stock price data. I learned how to store, query, and analyze these types of data using both SQL and NoSQL databases.
Using Python’s datetime Module:
I learned how to utilize Python’s datetime module for handling date and time data, including formatting and parsing time, which is very useful for processing and analyzing data involving timestamps.
Real-Time Data Handling Techniques:
I discovered two main techniques for real-time data handling: Websockets and polling. These techniques are crucial in applications that require real-time updates of data.

# questions
How can we effectively scale databases or data warehouses to support high-frequency data writing and querying for large-scale time series data? Especially when using traditional SQL databases, are there specific strategies or technologies for scaling?
While using Websockets for true bidirectional communication can provide a better user experience, it may increase the complexity and cost of the system. How can we balance the need for real-time data processing with the use of system resources, especially in resource-limited situations? Are there more cost-effective alternatives?
