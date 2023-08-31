import argparse
import pickle

import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='act')
parser.add_argument('--date', type=str, default='2023-11-11-11-11-11')
parser.add_argument('--dayoff', type=str, default='0')

args = parser.parse_args()

model = args.model
date = args.date
dayoff = args.dayoff

test_data = date.split('-')
test_data.insert(3, dayoff)
test_data = list(map(int, test_data))
test_data = np.array(test_data)
test_data = np.expand_dims(test_data, axis=0)

if __name__ == '__main__':
    act = ['chatting', 'work', 'study']
    if model == 'act':
        with open('act_model.pickle', 'rb') as f:
            model = pickle.load(f)
            print('예측 행동: ', act[int(model.predict(test_data))])
    if model == 'seat':
        with open('seat_model.pickle', 'rb') as f:
            model = pickle.load(f)
            print('예측 좌석 점유율: ', round(model.predict(test_data)[0], 2), '%')
    if model == 'gender':
        with open('gender_model.pickle', 'rb') as f:
            model = pickle.load(f)
            print('예측 성별 비율: ', '{ 남성: ', round(model.predict(test_data)[0], 2), f'여성: {round(100 - model.predict(test_data)[0], 2)}', '}')
    if model == 'menu':
        with open('menu_model.pickle', 'rb') as f:
            model = pickle.load(f)
            print('예측 메뉴 추론: ', round(model.predict(test_data)[0]), '잔')
