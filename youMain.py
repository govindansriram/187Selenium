import email
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
    driver.get("https://you.com/search?q=who+are+you&tbm=youchat&cfr=chat")
    driver.maximize_window()
    driver.implicitly_wait(10)

    signIn_element = driver.find_element(by=By.XPATH, value="//button[text()='Sign in']")
    signIn_element.click()
    time.sleep(5)
    driver.implicitly_wait(10)

    email_element = driver.find_element(By.ID,'1-email')
    email_element.send_keys(os.getenv("EMAIL"))
    # continue_button = driver.find_element(by=By.XPATH, value="//button[@class='c756c7a38 cd4fe08ec "
    #                                                          "c115c32ac c588d3732 _button-login-id']")

    # continue_button.click()
    email_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="your password"]')
    email_element.send_keys(os.getenv("PASSWORD"))
    driver.implicitly_wait(10)
    submit = driver.find_element(By.CSS_SELECTOR, '[aria-label="Log In"]')

    submit.click()
    
    time.sleep(5)
    
    # questionInput = driver.find_element(By.XPATH, "//textarea[@class='sc-f107b18f-1 eEofTy']")
    # questionInput.send_keys('Who is MLK?')
    # questionInput.send_keys(Keys.RETURN)
    # time.sleep(20)

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-neutral ml-auto']")
#     next_button.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-neutral ml-auto']")
#     next_button.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-primary ml-auto']")
#     next_button.click()

#     time.sleep(3)


def ask_question(question: str):
    element = driver.find_element(By.XPATH, "//textarea[@class='sc-f107b18f-1 eEofTy']")
    print("in ask_question")
    element.send_keys(question)
    time.sleep(2)
    element.send_keys(Keys.RETURN)
    time.sleep(10)

    # element = driver.find_element(by=By.XPATH,
    #                               value="//div[@class='group w-full text-gray-800 dark:text-gray-100 border-b "
    #                                     "border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]']")

    text = element.text
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
    df = pd.read_csv(filepath_or_buffer="youCR.csv")

    if "pass" not in df.columns:
        df["pass"] = [None] * len(df)

        df.to_csv("youCR.csv", index=False)
        df = pd.read_csv(filepath_or_buffer="youCR.csv")

    for idx, i in enumerate(df["pass"].tolist()):

        if np.isnan(i):
            row = df.iloc[idx]
            inp = row["input"]
            qn = row["question_number"]

            answers = answer_list[qn]

            res = is_acceptable(answers, ask_question(inp))

            df.iloc[idx, df.columns.get_loc('pass')] = res
            df.to_csv("youCR.csv", index=False)


if __name__ == '__main__':
    initialize()

    x = [
        ("Martin Luther King", "Rosa Parks", "Ruby Bridges"), 
        ("dream", "discrimination", "segregation", "civil rights"),
        ("1970", "1960s", "1967"),
        ("Lincoln", "memorial"),
        ("lydon", "johnson", "kennedy"),
        ("segregation", "African Americans", "mlk"),
        ("november", "1960"),
        ("south"),
        ("lydon", "johnson"),
        ("end", "segregation", "african americans"),
        ("1960", "1970", "1950"),
        ("protests","non violent", "law","segregation"),
        ("south","southern"),
        ("gandhi","non-violent"),
        ("Civil Rights", "Act", "1964"),
        ("1960", "1970", "1950"),
        ("south", "alabama"),
        ("1960", "1970", "1950"),
        ("massachusetts",),
        ("south",),
        ("segregation","discrimination",),
        ("1974",),
        ("Lincoln","Memorial",),
        ("bus","activist","protest"),
        
    ]

    run_all_tests(x)
