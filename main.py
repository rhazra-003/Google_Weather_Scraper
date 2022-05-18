from requests_html import HTMLSession

s = HTMLSession()

query = 'XYZ' #Enter the name of the city here
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'})
# user-agent is used to avoid "Are you a bot?" question

temperature = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
description = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
# tags taken by inspecting the google webpage

print(query, temperature, unit, description)
