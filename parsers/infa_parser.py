from selenium import webdriver
from selenium.webdriver.common.by import By


from bs4 import BeautifulSoup
import requests
import json


driver = webdriver.Chrome()
driver.get(f'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=1&cat12=on&cat13=on')
soup = BeautifulSoup(driver.page_source, features="html.parser")
problems = driver.find_element(By.CLASS_NAME, 'vartopic')
pb = problems.find_elements(By.TAG_NAME, 'tr')
for i in range(0, len(pb), 2):
    task_type = pb[i].find_element(By.CLASS_NAME, 'egeno').text
    task = pb[i].find_element(By.CLASS_NAME, 'topicview')
    task_id = pb[i].find_element(By.CLASS_NAME, 'topicview').text.split(')')[0].lstrip('(№ ')
    try:
        img = task.find_element(By.TAG_NAME, 'img')
        img = [img.get_attribute('src')]
    except:
        try:
            img = task.find_element(By.TAG_NAME, 'a')
            img = [img.get_attribute('href')]
        except:
            img = []
    tasks = ')'.join(task.text.split(')')[1:]).lstrip('.').lstrip(' ')

    button = pb[i + 1].find_element(By.CLASS_NAME, 'answer').find_element(By.TAG_NAME, 'a')
    button.click()
    answers = pb[i + 1].find_element(By.CLASS_NAME, 'hidedata').text.split()
    answers_img = []
    print({
        "task_id": int(task_id),
        "task_type": int(task_type),
        "task": [tasks],
        "task_img": img,
        "answer": answers,
        "answer_img": answers_img
    })
    r = requests.post('http://ege-scrapper-bot.na4u.ru/api/inf', data=json.dumps({
        "task_id": int(task_id),
        "task_type": int(task_type),
        "task": [tasks],
        "task_img": img,
        "answer": answers,
        "answer_img": answers_img
    }), headers={'content-type': 'application/json'})
    print('req', r.text)



