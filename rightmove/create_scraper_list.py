import json
import os
import requests

url = "https://api.minexa.ai/scraper/"
api_key = "YOUR_API_KEY"

# Your JSON data for the request body
data = {
    # Copy paste the data from the website directly without any modification to train the scraper
    # or Write a short description of your required data, for example: "clinical trials results"
    "look_for": """|
1/42
FEATURED PROPERTY
£3,750,000
Kensington Church Street, W8
Flat
4
3
Reduced on 03/12/2024
Call
Contact
Save

|
1/15
£80,000,000
Guide Price
The Knightsbridge Apartments, 199 Knightsbridge, London, SW7
Penthouse
5
5
Added on 02/09/2024
Call
Contact
Save

1/6
£60,000,000
One Hyde Park, Knightsbridge
Apartment
5
5
Added on 05/07/2024
Call
Contact
Save

1/24
£59,950,000
PREMIUM LISTING
Avenue Road, St John's Wood, London, NW8, United Kingdom
House
10
8
Added on 25/11/2024
Call
Contact
Save

|
1/12
£49,500,000
Guide Price
FREEHOLD
Balfour Place, Mayfair, London, W1K
End of Terrace
7
8
Added on 04/09/2024
Call
Contact
Save

|
1/34
£47,000,000
Guide Price
Whistler Square, London, SW1W
Town House
7
8
NEW HOME
Added on 10/09/2024
Call
Contact
Save

|
1/16
£47,000,000
Whistler Square, Chelsea Barracks, London, SW1W, United Kingdom
House
6
6
Added on 09/09/2024
Call
Contact
Save

1/5
£47,000,000
One Hyde Park, Knightsbridge
Apartment
5
5
Added on 21/02/2025
Call
Contact
Save

|
1/29
£44,000,000
Wilton Crescent, Belgravia, London, SW1X, United Kingdom
House
7
7
Added on 29/01/2025
Call
Contact
Save

1/14
£42,000,000
Guide Price
Bayswater Road, London, W2
Apartment
5
4
NEW HOME
Added on 06/06/2025
Call
Contact
Save""",

    # Provide a single url corresponding to pages with listed data
    "urls":
    [
    "https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=London&useLocationIdentifier=true&locationIdentifier=REGION%5E87490&radius=0.0&_includeSSTC=on"
    ],

    # uncomment if you need to recrawl the HTML again from scratch by ignoring cached data (like its the first time you scrape it)
    #"reset": True,

    # Unocomment and set it when manaully detecting your container after first try
    # No need to use for creating scraper for a particular page for the first time
    # "xpath": "/html/body/div/div/div[3]/div[1]/div[2]",

    "mode": "list" #  Use list if the data you're scraping is in form of an itemized collection
}



headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

print("Creating scraper.. This may take up to 2 minutes")

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
if response.status_code == 200:
    print("Please confirm container is well located:", response.json()['response']['web_app'])

    # Create and save the file
    scraper_id = response.json()["response"]["id"]
    file_path = f"{os.path.dirname(os.path.abspath(__file__))}/scraper_id_{scraper_id}.json"

    # Save the scraper.json
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False, indent=4)

    print("Full scraper json saved at: {}".format(file_path))
else:
    print("Error status code {} occurred ".format(response.status_code))
    try:
        print(response.status_code)
        print(response.json())
    except Exception as e:
        print("{} in showing error".format(e))
