import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def shorten_link(token, long_url):
    url = "https://api.vk.ru/method/utils.getShortLink"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"v": 5.199, "url": long_url}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["response"]["short_url"]


def count_clicks(token, short_link):
    url = "https://api.vk.ru/method/utils.getLinkStats"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "v": 5.199,
        "interval": "forever",
        "key": short_link,
        "extended": 0
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["response"]["stats"][0]["views"]


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']
    parser = argparse.ArgumentParser(description='Это программа помогает сократить ссылку или уже по сокращенным ссылкам посчитать клики')
    parser.add_argument('--url', type=str, help='Введите ссылку')
    args = parser.parse_args()
    parsed_url = urlparse(args.url)
    try:
        if parsed_url.netloc == "vk.cc":
            print("Количество кликов по ссылке:",
                  count_clicks(token, parsed_url.path[1:]))
        else:
            short_link = shorten_link(token, args.url)
            print('Сокращенная ссылка: ', short_link)
    except requests.exceptions.HTTPError:
        print("Проверьте вашу ссылку:")
    

if __name__ == "__main__":
    main()
