from bs4 import BeautifulSoup as bs
import requests as req
import json

url = 'https://www.nature.com/articles/nclimate2124'

response = req.get(url)

if response.status_code == 200:
    soup = bs(response.text, 'html.parser')

    script_tags = soup.find('script', type='application/ld+json')

    with open('output.txt', 'w') as file:
        if script_tags:
            json_cont = json.loads(script_tags.string)
            headline = json_cont['mainEntity']['headline']
            desc = json_cont['mainEntity']['description']

            file.write(f'Headline: {headline}\n')
            file.write(f'Description: {desc}\n\n')

            for sc in script_tags:
                file.write(sc + '\n')

else:
    print('Err or:', response.status_code)