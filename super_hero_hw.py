import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
data = response.json()

def best_super_hero(hero_1,hero_2,hero_3):
    all_heroes = {}
    x = 0
    for i in range(len(data)):
        hero = data[x]['name']
        if hero == hero_1 or hero == hero_2 or hero == hero_3:
            intelligen = data[x]['powerstats']['intelligence']
            all_heroes[hero] = intelligen
        x += 1
    max_value = max(all_heroes.values())
    best = {key: values for key, values in all_heroes.items() if values == max_value}
    result = []
    for key, values in best.items():
        result.append(f'Самый умный супергерой это {key}: {values} очков интеллекта.')
    return result

if __name__ == "__main__":
    print(best_super_hero(hero_1="Hulk", hero_2="Thanos", hero_3="Captain America"))
