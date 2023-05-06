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

    df.to_csv("main.csv", index=False)

    for idx, i in enumerate(df[df["generate"] == False]["input"].tolist()):
        print(f"Question {idx}: {i}")


if __name__ == '__main__':
    read_csv("American Revolution Augmented data - Test Cases.csv")
