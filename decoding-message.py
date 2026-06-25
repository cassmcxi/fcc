import requests
import json

url = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'


def decode_secret_message(url):
    #fetch content and split into lines
    response = requests.get(url)
    lines = response.text.strip().splitlines()
    data = response.json()
    #process data and populate a 2D list for the grid
    positions = []

    if response == url:
        #retrieve/parse the data and print characters
        for x in range(url):
            print(json.url)



print(decode_secret_message('https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'))



