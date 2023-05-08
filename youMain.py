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

#     email_element = driver.find_element(by=By.XPATH, value="//input[@class='class="sc-63e0c30e-0 ePhVwB sc-a4788ff0-0 crcyMV"']")
#     email_element.send_keys(os.getenv("EMAIL"))
#     continue_button = driver.find_element(by=By.XPATH, value="//button[@class='c756c7a38 cd4fe08ec "
#                                                              "c115c32ac c588d3732 _button-login-id']")

#     continue_button.click()
#     email_element = driver.find_element(by=By.XPATH, value="//input[@class='input ca9e64f1c c92fe6a3b']")
#     email_element.send_keys(os.getenv("PASSWORD"))
#     driver.implicitly_wait(10)
#     submit = driver.find_element(by=By.XPATH, value="//button[@class='c756c7a38 "
#                                                     "cd4fe08ec c115c32ac c588d3732 _button-login-password']")

#     submit.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-neutral ml-auto']")
#     next_button.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-neutral ml-auto']")
#     next_button.click()

#     next_button = driver.find_element(by=By.XPATH, value="//button[@class='btn relative btn-primary ml-auto']")
#     next_button.click()

#     time.sleep(3)


# def ask_question(question: str):
#     element = driver.find_element(by=By.XPATH,
#                                   value="//textarea[@class='m-0 w-full resize-none border-0 bg-transparent "
#                                         "p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-"
#                                         "transparent pl-2 md:pl-0']")

#     element.send_keys(question)
#     element.send_keys(Keys.RETURN)
#     time.sleep(10)

#     element = driver.find_element(by=By.XPATH,
#                                   value="//div[@class='group w-full text-gray-800 dark:text-gray-100 border-b "
#                                         "border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]']")

#     text = element.text
#     driver.refresh()

#     time.sleep(1)

#     return text


# def is_acceptable(acc_answer_list: list[str],
#                   answer: str) -> bool:
#     for i in acc_answer_list:
#         if i.lower() in answer.lower():
#             return True

#     return False


def run_all_tests(answer_list: list):
    df = pd.read_csv(filepath_or_buffer="main.csv")

    if "pass" not in df.columns:
        df["pass"] = [None] * len(df)

        df.to_csv("main.csv", index=False)
        df = pd.read_csv(filepath_or_buffer="main.csv")

    for idx, i in enumerate(df["pass"].tolist()):

        if np.isnan(i):
            row = df.iloc[idx]
            inp = row["input"]
            qn = row["question_number"]

            answers = answer_list[qn]

            res = is_acceptable(answers, ask_question(inp))

            df.iloc[idx, df.columns.get_loc('pass')] = res
            df.to_csv("main.csv", index=False)


if __name__ == '__main__':
    initialize()

    # x = [
    #     ("first", "president", "general", "america"),
    #     ("thomas", "revolution"),
    #     ("january", "17", "1706"),
    #     ("lexington", "concord"),
    #     ("john", "adams", "thomas"),
    #     ("British", "stamp", "1765"),
    #     ("1776", "1791"),
    #     ("Yorktown", "virginia"),
    #     ("thomas", "jefferson"),
    #     ("no", "limit", "informal"),
    #     ("july", "4", "1776"),
    #     ("british",),
    #     ("pennsylvania",),
    #     ("william",),
    #     ("20000", "twenty", "thousand"),
    #     ("December", "14", "1799"),
    #     ("yorktown", "virginia"),
    #     ("george",),
    #     ("massachusetts",),
    #     ("1776",),
    #     ("pennsylvania",),
    #     ("treasury",),
    #     ("17",),
    #     ("treasury",),
    #     ("1804",),
    #     ("new",),
    #     ("united",),
    #     ("coming",),
    #     ("tea",),
    #     ("native",),
    #     ("pennsylvania",),
    #     ("common", "sense"),
    # ]

    # run_all_tests(x)
