import requests
import time

cookies = {
    'qrator_jsr': '1727453661.096.aPcfAQJtHk7wWeQ6-8o575p3d0skjfibkivjdr5ae7ckf8h1t-00',
    'qrator_ssid': '1727453661.386.MOvVYHp8JhF5FLNr-qd9dct2c436f90rro84bn3ds810mgig9',
    'qrator_jsid': '1727453661.096.aPcfAQJtHk7wWeQ6-pi2httmc5ac8h61k5o6dvoibvbofvsv6',
    'ab_spa': '%7B%22home-presearch-test%22%3A%22main_search_4%22%7D',
    'lang': 'ru',
    'phonesIdentV2': 'bfc1f7e1-36c5-428f-97ba-d4b7857d07e2',
    'cartUserCookieIdent_v3': '5e2fedce56dc6fae5e456557f0155fc75b17a2ea9c1127941d67658c7975cebca%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22e818f10f-21e5-3da1-a66b-a6a4503dd58e%22%3B%7D',
    '_ga': 'GA1.1.1915417375.1727453662',
    'tmr_lvid': 'd5191c5738f0d48c3a3b3bdc87eddbf0',
    'tmr_lvidTS': '1727453662375',
    '_ym_uid': '1727453662338059554',
    '_ym_d': '1727453662',
    '_ym_isad': '2',
    'domain_sid': 'trrg-5LHTioMs6Li8ACHF%3A1727453662539',
    '_ym_visorc': 'b',
    'city_path': 'moscow',
    'current_path': '605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'rrpvid': '996767739813389',
    'rcuid': '66e6075e870b48bf18295dee',
    '_ab_': '%7B%22discount-online%22%3A%22discount_online_3%22%7D',
    'PHPSESSID': '19b9019cdfaa6458f5ed9e7f6ae14862',
    '_csrf': '9501ce5589c7825eba0992c10ecded1625ad50baeab67c92cb4190004d392e50a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22HLHYu_uQ316dcdg-3WudUn4xcbWkX9bj%22%3B%7D',
    '_gcl_au': '1.1.257896413.1727453687',
    'tmr_detect': '0%7C1727453689652',
    'chatNewMessage': '0',
    '_ga_FLS4JETDHW': 'GS1.1.1727453662.1.1.1727453703.19.0.645838918',
    'rr-testCookie': 'testvalue',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'qrator_jsr=1727453661.096.aPcfAQJtHk7wWeQ6-8o575p3d0skjfibkivjdr5ae7ckf8h1t-00; qrator_ssid=1727453661.386.MOvVYHp8JhF5FLNr-qd9dct2c436f90rro84bn3ds810mgig9; qrator_jsid=1727453661.096.aPcfAQJtHk7wWeQ6-pi2httmc5ac8h61k5o6dvoibvbofvsv6; ab_spa=%7B%22home-presearch-test%22%3A%22main_search_4%22%7D; lang=ru; phonesIdentV2=bfc1f7e1-36c5-428f-97ba-d4b7857d07e2; cartUserCookieIdent_v3=5e2fedce56dc6fae5e456557f0155fc75b17a2ea9c1127941d67658c7975cebca%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22e818f10f-21e5-3da1-a66b-a6a4503dd58e%22%3B%7D; _ga=GA1.1.1915417375.1727453662; tmr_lvid=d5191c5738f0d48c3a3b3bdc87eddbf0; tmr_lvidTS=1727453662375; _ym_uid=1727453662338059554; _ym_d=1727453662; _ym_isad=2; domain_sid=trrg-5LHTioMs6Li8ACHF%3A1727453662539; _ym_visorc=b; city_path=moscow; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; rrpvid=996767739813389; rcuid=66e6075e870b48bf18295dee; _ab_=%7B%22discount-online%22%3A%22discount_online_3%22%7D; PHPSESSID=19b9019cdfaa6458f5ed9e7f6ae14862; _csrf=9501ce5589c7825eba0992c10ecded1625ad50baeab67c92cb4190004d392e50a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22HLHYu_uQ316dcdg-3WudUn4xcbWkX9bj%22%3B%7D; _gcl_au=1.1.257896413.1727453687; tmr_detect=0%7C1727453689652; chatNewMessage=0; _ga_FLS4JETDHW=GS1.1.1727453662.1.1.1727453703.19.0.645838918; rr-testCookie=testvalue',
    'origin': 'https://www.dns-shop.ru',
    'priority': 'u=1, i',
    'referer': 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/no-referrer',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-csrf-token': '0TcgUbz6XDggbNafKkLRhvroNSSUZ19ki5vzoX4evpKZe2gIyaUpaRNd4PtJJraryb9AQMEJaxzo-aTKJifc-A==',
    'x-requested-with': 'XMLHttpRequest',
}

data = 'data={"type":"product-buy","containers":[{"id":"as-aAHkfy","data":{"id":"5073497"}},{"id":"as-3F1kBu","data":{"id":"5051002"}},{"id":"as-mrN8Dl","data":{"id":"5073498"}},{"id":"as-k87soM","data":{"id":"5095628"}},{"id":"as-B66_of","data":{"id":"5067279"}},{"id":"as-y3BDoe","data":{"id":"5067283"}},{"id":"as-BpzUOg","data":{"id":"5421052"}},{"id":"as-3VUAp8","data":{"id":"5051024"}},{"id":"as-ehsTxM","data":{"id":"5051044"}},{"id":"as-2IjJIW","data":{"id":"5074087"}},{"id":"as-bFVUkX","data":{"id":"5033464"}},{"id":"as-selXs3","data":{"id":"5074599"}},{"id":"as-lD3ALr","data":{"id":"5074596"}},{"id":"as-tHbWzB","data":{"id":"5041562"}},{"id":"as-BM_hti","data":{"id":"5074597"}},{"id":"as-0uGe8c","data":{"id":"5033416"}},{"id":"as-_FrxZ1","data":{"id":"5033472"}},{"id":"as-vjL006","data":{"id":"5074097"}}]}'

response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/', cookies=cookies, headers=headers, data=data)

time.sleep(3)
result = response.json()
product =result['data']['states']
for i in product:
    name = i['data']['name']
    price = i['data']['price']
    print(price)