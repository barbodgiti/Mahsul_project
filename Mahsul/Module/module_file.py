import os
import pickle

file_name = "../data/mahsul.dat"


def save_data(mahsul):
    file = open(file_name, "wb")
    pickle.dump(mahsul, file)
    file.close()


def load_data():
    if os.path.exists(file_name):
        file = open(file_name, "rb")
        mahsul = pickle.load(file)
        file.close()
    else:
        mahsul = []
    return mahsul
