import requests
from bs4 import BeautifulSoup
import json

def get_locations():
    url = 'https://dentalia.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    locations = []

    location_elements = soup.find_all('div', class_='''elementor-section elementor-inner-section elementor-element
                                       elementor-element-f9012da elementor-section-boxed elementor-section-height-default elementor-section-height-defaul''')

    for location_element in location_elements:
        name = location_element.find('h3', class_='class="elementor-heading-title elementor-size-default').text.strip()
        address = location_element.find('div', class_='jet-listing-dynamic-field__content').text.strip()
        coordinates = location_element['data-coordinates']
        phones = [phone.text.strip() for phone in location_element.find_all('div', class_='jet-listing-dynamic-field__content')]
        working_hours_element = location_element.find('div', class_='jet-listing-dynamic-field__content')
        working_hours = working_hours_element.get_text(separator='\n').strip()

        location = {
            'name': name,
            'address': address,
            'coordinates': coordinates,
            'phones': phones,
            'working_hours': working_hours
        }
        locations.append(location)

    return locations

locations_data = get_locations()

with open('locations.json', 'w', encoding='utf-8') as file:
    json.dump(locations_data, file, indent=4, ensure_ascii=False)

print('Информация о локациях сохранена в locations.json')






