from bs4 import BeautifulSoup
import requests

# https://www.google.com/search?q=rfr+gjcvjnhtnm+gjujle+d+google&rlz=1C1GCEU_ruRU1054RU1054&sxsrf=APwXEdemtockRlfijSxD2hwRieySPYdCHg%3A1682366751615&ei=H-FGZJicJaGnrgTF2YQI&ved=0ahUKEwjYp_LEqMP-AhWhk4sKHcUsAQEQ4dUDCA8&uact=5&oq=rfr+gjcvjnhtnm+gjujle+d+google&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIICCEQFhAeEB06BAgjECc6DgguEIAEELEDEIMBENQCOgsIABCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAgAEIAEELEDOgoIABCABBAUEIcCOgUIABCABDoJCC4QgAQQChABOgkIABCABBAKEAE6CAguEIAEENQCOgcIABCABBAKOgsIABCKBRCxAxCDAToMCC4QgAQQ1AIQChABOgoIABCABBCxAxAKOg0IABCABBCxAxCDARAKOgcILhCABBAKOgoIABCABBAKEMsBOggIABCKBRCxAzoJCAAQgAQQChAqOgsIABCABBAKEAEQKjoICAAQFhAeEAo6CwgAEBYQHhDxBBAKOgcIABANEIAEOgYIABAeEA06CAgAEAgQHhANOgYIABAWEB5KBAhBGABQAFiDMWDHM2gAcAF4AIABrAGIAccbkgEEMC4zMJgBAKABAcABAQ&sclient=gws-wiz-serp

def weather_check(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', 
        headers=headers
    )
    
    soup = BeautifulSoup(res.text, 'lxml')
    
    time = soup.select('#wob_dts')[0].getText().strip()
    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    wind = soup.select('#wob_ws')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    # humidity = soup.find('span', id = 'wob_hm').text.strip()
    probability_of_precipitation = soup.select('#wob_pp')[0].getText().strip()
    
    print(f'''День недели и время: {time}
Информация об осадках: {precipitation}
Температура воздуха: {weather}°C
Ветер: {wind}
Влажность: {humidity}
Вероятность осадков: {probability_of_precipitation}''')


if __name__ == '__main__':
    city_input = input('Введите название города: ')
    weather_check(f'{city_input} погода')