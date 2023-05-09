import pandas as pd


def read_csv(csv_path: str):
    df = pd.read_csv(csv_path)

    number_list = []
    number = -1

    for i in df["generate"].tolist():

        if not i:
            number += 1

        number_list.append(number)

    df["question_number"] = number_list

    df.to_csv("youCR.csv", index=False)

    for idx, i in enumerate(df[df["generate"] == False]["input"].tolist()):
        print(f"Question {idx}: {i}")


if __name__ == '__main__':
    read_csv("CR US History-CR US History Func-Testcases (2).xlsx - Test Cases.csv")
