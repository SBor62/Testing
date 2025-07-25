import requests


def get_random_cat_image():
    """
    Запрашивает случайное изображение кошки с TheCatAPI.
    Возвращает URL изображения при успешном запросе, иначе None.
    """
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and 'url' in data[0]:
            return data[0]['url']
    return None
