import pandas as pd

def make_unique(data):
    data_list = data.iloc[:, 0].values
    data_list_after_preprocessing = list(set(data_list))
    with open('./unique_word.csv', 'w', encoding='utf-8') as f:
        for word in data_list_after_preprocessing:
            f.write(word + "\n")

def get_user_dic():
    data= pd.read_csv('./user_after_duplication.csv', header=None)
    return data

if __name__ == "__main__":
    data = get_user_dic()
    make_unique(data)
