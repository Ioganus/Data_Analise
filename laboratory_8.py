# Составить таблицу топ-50 статей с Википедии по запросу "Python".

# В таблицу ввести: 
# название
# URL
# ссылку на URL первой картинки [0] 
# название ссылки на первую статью, расположенную на странице 
# краткое содержание (если есть) - 3 предложения 
# Результат представить можно в виде таблицы Excel или в виде документа Word.

# Примечание:
# На некоторых запросах может возникнуть ошибка DisambiguationError. 
# Данную ошибку можно избежать с помощью модуля try... except. 
# ----------------------------------------------------------------


# РЕШЕНИЕ

import wikipedia
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from time import sleep


# установка языка википедии
wikipedia.set_lang("ru")

# запрос на страницу с темой "Python"
try:
    search_results = wikipedia.search("Python")
    page = wikipedia.page(search_results[0])
except wikipedia.DisambiguationError as e:
    page = wikipedia.page(e.options[0])

# получение списка ссылок на странице
links = page.links

# отбор первых 50 статей
links = links[:50]

# инициализация списка для таблицы результатов
results_table = []

# начальное значение для счетчика запросов
request_counter = 0


# получение информации о каждой статье
for link in links:
    request_counter += 1
    
    try:
        try:
            subpage = wikipedia.page(link)
        except wikipedia.DisambiguationError as e:
            subpage = wikipedia.page(e.options[0])
        except wikipedia.PageError:
            print(f"Page {link} not found. Skipping.")
            continue
        
        # получение ссылки на первую картинку
        images = subpage.images
        image_url = ""
        for image in images:
            if "jpg" in image or "png" in image:
                image_url = image
                break
        # проверка условия: использование sleep каждые три запроса
        if request_counter % 3 == 0:
            sleep(5)

            # получение ссылки на первую картинку
            images = subpage.images
            image_url = ""
            for image in images:
                if "jpg" in image or "png" in image:
                    image_url = image
                    break

        # получение названия первой ссылки на странице
        soup = BeautifulSoup(subpage.html(), "html.parser")
        first_link = soup.find("a")
        first_link_text = first_link.get("title")

        # добавление информации в таблицу результатов
        result_row = [subpage.title, subpage.url, image_url, first_link_text, subpage.summary[:200]]
        results_table.append(result_row)
    except Exception as ex:
        print(f"Error processing {link}: {ex}")
        continue

# создание рабочей книги Excel и листа
wb = Workbook()
ws = wb.active
ws.title = "Python Wikipedia Results"

# добавление заголовков столбцов
headers = ["Название", "URL", "Ссылка на первую картинку", "Название первой статьи", "Краткое содержание"]
ws.append(headers)

# добавление данных в лист
for row in results_table:
    ws.append(row)

# сохранение рабочей книги в файл
wb.save("python_wikipedia_results.xlsx")

