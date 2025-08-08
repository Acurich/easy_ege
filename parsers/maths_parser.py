from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests
import json


driver = webdriver.Chrome()
for i in range(548424, 548425):
    try:
        driver.get(f'https://ege.sdamgia.ru/problem?id={i}')
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        res = driver.find_element(By.TAG_NAME, "body").text
        if not 'Такого задания не существует' in res:
            task_type = int(driver.find_element(By.CLASS_NAME, 'prob_nums').text.split()[1])

            task_div = driver.find_element(By.CLASS_NAME, 'pbody')
            tasks = []
            images = []
            for j in task_div.find_elements(By.CLASS_NAME, 'left_margin'):
                tasks.append(j.text.replace('\u202f\u202f', ' '))
                try:
                    images.append(j.find_element(By.TAG_NAME, 'img').get_attribute('src'))
                except:
                    pass

            print(tasks, images)

            answers_div = driver.find_element(By.CLASS_NAME, 'solution').find_elements(By.TAG_NAME, 'p')[-1]
            answers = driver.execute_script('return arguments[0].textContent;', answers_div)
            answers_img = [j.get_attribute('src') for j in answers_div.find_elements(By.TAG_NAME, 'img')]
            print(answers, answers_img)
            print(type(i), type(task_type), type(tasks), type(images), type(answers), type(answers_img))

            r = requests.post('http://ege-scrapper-bot.na4u.ru/api/maths', data=json.dumps({
                "task_id": i,
                "task_type": task_type,
                "task": tasks,
                "task_img": images,
                "answer": [answers],
                "answer_img": answers_img
            }), headers={'content-type': 'application/json'})
            print('req', r.text)

    except Exception as e:
        print(e)
