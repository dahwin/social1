text = 'who is the boyfriend of kim dahyun from twice'

# Replace spaces with plus (+)
d_text = text.replace(' ', '+')

# Print the modified text
print(d_text)

import requests
from bs4 import BeautifulSoup

# URL of the webpage
# url = "https://deepmind.google/discover/blog/transforming-the-future-of-music-creation/"
# url = "https://www.google.com/search?q=gpt4+v+openai&oq=gpt4+v&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgKGIAEMgcIAhAAGIAEMgkIAxAAGAoYgAQyBwgEEAAYgAQyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgyMDYzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
url= "https://www.google.com/search?q=kim+dahyun&oq=&gs_lcrp=EgZjaHJvbWUqCQgBECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQoyNzM3NDlqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8"
# url = f"https://www.bing.com/search?pglt=673&q={d_text}&cvid=bfc98c93c97e4eac84cedef81f2793e4&gs_lcrp=EgZjaHJvbWUqBggAEAAYQDIGCAAQABhAMgcIARDrBxhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQg1NDY4ajBqMagCALACAA&FORM=ANSPA1&PC=U531"
# url = "https://www.bing.com/search?pglt=673&q=who+is+the+boyfriend+of+kim+dahyun+from+twice&cvid=2b3d586c249d45a2b0af46bc771b78c2&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgxMTM0ajBqMagCALACAA&FORM=ANSPA1&PC=U531"
url = f"https://www.google.com/search?q={d_text}&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMhgIARAuGEMYgwEYxwEYsQMY0QMYgAQYigUyDggCEEUYJxg7GIAEGIoFMgcIAxAAGIAEMgYIBBBFGDwyBggFEEUYPDIGCAYQRRg8MgYIBxBFGD3SAQg0MTI2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags (links) in the HTML
    all_links_elements = soup.find_all('a')

    # Extract href attributes from the links
    all_links = [link.get('href') for link in all_links_elements]
    
    # Print or use the links as needed

    # Print each link on a new line
    for link in all_links:
        if 'https://' in link:
            if 'google' not in link:
                # Find the index of the first occurrence of 'https://'
                start_index = link.find('https://')

                # Extract the substring starting from 'https://'
                result = link[start_index:]
                #print(result)
                # Find the index of "&sa="
                sa_index = result.find("&sa=")

                # Extract the substring before "&sa="
                result = result[:sa_index]

                # Print the result
                print(result)

                
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
