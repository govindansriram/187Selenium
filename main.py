import os
import time

import numpy as np
import pandas as pd
import undetected_chromedriver as uc
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

driver = uc.Chrome()


def initialize():
    driver.get("https://andisearch.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # element = driver.find_element(by=By.XPATH, value="//input[@class= 'rcw-new-message']")
    # element.click()
    #element.send_keys("blablah")
    #driver.implicitly_wait(5)

    #email_element = driver.find_element(by=By.XPATH, value="//input[@class='input ca9e64f1c c27c338e9']")
    #email_element.send_keys(os.getenv("EMAIL"))
    #continue_button = driver.find_element(by=By.XPATH, value="//button[@class='c756c7a38 cd4fe08ec ""c115c32ac c588d3732 _button-login-id']")

    #continue_button.click()
    #email_element = driver.find_element(by=By.XPATH, value="//input[@class='input ca9e64f1c c92fe6a3b']")
    #email_element.send_keys(os.getenv("PASSWORD"))
    #driver.implicitly_wait(10)
    #submit = driver.find_element(by=By.XPATH, value="//button[@class='rcw-send']")

    #submit.click()

    #next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-neutral ml-auto']")
    #next_button.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-neutral ml-auto']")
#     next_button.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-primary ml-auto']")
#     next_button.click()

    time.sleep(2)


def ask_question(question: str):
    # element = driver.find_element(by=By.XPATH,
    #                               value="//input[@class= 'rcw-new-message']")
    
    element = driver.find_element(by=By.XPATH,
                                  value="//input[@class= 'rcw-new-message']")
    
    print("question:", question)
    element.send_keys(question)
    element.send_keys(Keys.RETURN)
    time.sleep(8)
    element = driver.find_element(by=By.XPATH, value="//div[@class= 'rcw-message'][3]")

    text = element.text
    print("text: ", text)
    driver.refresh()

    time.sleep(1)

    return text


def is_acceptable(acc_answer_list: list[str],
                  answer: str) -> bool:
    for i in acc_answer_list:
        if i.lower() in answer.lower():
            return True

    return False


def run_all_tests(answer_list: list):
    df = pd.read_csv(filepath_or_buffer="main.csv")

    if "pass" not in df.columns:
        df["pass"] = [None] * len(df)

        df.to_csv("main.csv", index=False)
        df = pd.read_csv(filepath_or_buffer="main.csv")

    for idx, i in enumerate(df["pass"].tolist()):

        if np.isnan(i):
            print("idx is", idx)
            row = df.iloc[idx]
            inp = row["input"]
            qn = row["question_number"]

            answers = answer_list[qn]

            res = is_acceptable(answers, ask_question(inp))

            df.iloc[idx, df.columns.get_loc('pass')] = res
            df.to_csv("main.csv", index=False)


if __name__ == '__main__':
    initialize()

    x = [
        ("industrial", "revolution", "america"),
        ("James", "Watt", "Richard", "Thomas"),
        ("telegraph", "telephone"),
        ("resources", "fuel", "natural"),
        ("air", "pollution", "illness"),
        ("April", "18", "19", "1775"),
        ("weaving", "mechanized"),
        ("communicate", "wire"),
        ("Anthony", "Wallace", "Eli"),
        ("inventor", "engineer", "cotton","gin"),
        ("settlement", "farm", "cattle"),
        ("edison", "London"),
        ("stressful", "illness"),
        ("Britain",),
        ("Britain",),
        ("George", "Washington", "Anthony", "Wallace", "Eli"),
    ]

    run_all_tests(x)
