import pandas as pd

def make_unique(data):
    data_list = data.iloc[:, 0].values
    data_list_after_preprocessing = list(set(data_list))
    mecab_words = []
    for word in data_list_after_preprocessing:
        word = word.strip()
        word = word + ",,,0,NNP,*,F," + word + ",*,*,*,*"
        mecab_words.append(word)

    with open('./user_after_duplication.csv', 'w', encoding='utf-8') as f:
        for word in mecab_words:
            f.write(word + "\n")

def get_user_dic():
    data_user_origin = pd.read_csv('./user_after_duplication.csv', header=None)
    data_user_add = pd.read_csv('./word_dic.csv', header=None)
    data = pd.concat([data_user_origin, data_user_add], sort=True, axis = 0)
    return data

if __name__ == "__main__":
    data = get_user_dic()
    make_unique(data)
