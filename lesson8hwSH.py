import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

def parser():
    # функция парсинга интеллекта
    super_hero = []
    for item in requests.get(url).json():
        if item['name'] == 'Hulk':
            super_hero.append({
            'name': item['name'],
            'intelligence': item['powerstats']['intelligence'],
        })
        if item['name'] == 'Captain America':
            super_hero.append({
            'name': item['name'],
            'intelligence': item['powerstats']['intelligence'],
        })
        if item['name'] == 'Thanos':
            super_hero.append({
            'name': item['name'],
            'intelligence': item['powerstats']['intelligence'],
        })

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_hero:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f'Самый умный {name}, его интеллект: {intelligence_super_hero}')

parser()
