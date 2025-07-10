
# COVID-19 Global Data Tracker

# 1. Import necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt

# 2. Fetch data from the COVID-19 API
url = "https://api.covid19api.com/summary"
response = requests.get(url)

# 3. Check if the API call was successful
if response.status_code == 200:
    data = response.json()
    countries = data['Countries']

    # 4. Create a DataFrame
    df = pd.DataFrame(countries)

    # 5. Sort the data by Total Confirmed Cases
    top10 = df.sort_values(by='TotalConfirmed', ascending=False).head(10)

    # 6. Plot the top 10 countries
    plt.figure(figsize=(12, 6))
    plt.bar(top10['Country'], top10['TotalConfirmed'], color='coral')
    plt.title('Top 10 Countries by Total Confirmed COVID-19 Cases')
    plt.xlabel('Country')
    plt.ylabel('Total Confirmed Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Failed to fetch data from API.")
