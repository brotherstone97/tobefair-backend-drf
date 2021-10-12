import pandas as pd
import numpy as np
from konlpy.tag import Okt

menu_df = pd.read_csv("/content/drive/MyDrive/ITStartup/fastfood_menu.csv")
count_df = pd.read_csv("/content/drive/MyDrive/ITStartup/count.csv")
conj_df = pd.read_csv("/content/drive/MyDrive/ITStartup/conj.csv")

okt = Okt()


def extract(sentence):
    # 프론트로 보낼 dictionary
    response = {}

    # 메뉴와 수량을 담을 list
    menu_list = np.array([])
    count_list = []

    # 슬라이싱을 시작할 인덱스 설정
    start_index = 0

    # 매개변수로 받은 문장을 쪼개서 list로 만듦
    splitedSentence = okt.morphs(sentence)

    # 개수의 단위가 자연수로 들어올 것을 대비, morph를 비교할 ndarray를 모두 str형으로 cast.(for ln:23)
    casted_count_df_ndarray = count_df.to_numpy().astype(str)

    # 반복문을 돌면서 index와 각 형태소(morph)를 전달
    for (i, morph) in enumerate(splitedSentence):

        # 문장안에 개수를 뜻하는 단어와 count_df를 매칭(개수 다음 접속사 매칭)
        if morph in casted_count_df_ndarray:
            print('splitedSentence[start_index : i] : ', splitedSentence[start_index:i], '\n')
            print('splitedSentence[start_index+1 : i] : ', splitedSentence[start_index + 1: i], '\n')

            # splitedSentence를 슬라이싱 한 후 join한 결과물이 menu_df의 values와 일치하는지 확인
            # 어, 음 같은 추임새 넣을 경우도 대비해 경우의 수 추가하였음
            containing_menu_df = menu_df[(menu_df['menu'] == ''.join(splitedSentence[start_index:i])) | (
                    menu_df['menu'] == ''.join(splitedSentence[start_index + 1:i]))]

            # 일치하는 키워드를 menu_list에 저장. 일치하는 키워드 없을 경우 경고메시지 저장
            if containing_menu_df['menu'].to_numpy():
                menu_list = np.append(menu_list, containing_menu_df['menu'].to_numpy())
                # loc을 이용한 문장 속 자연수(natural_num 찾기)
                # count_df[natural_num]의 값이 정수이므로 문자열로 변환함
                count_list.append(count_df.loc[(count_df['natural_num'].astype(str) == morph) |
                                               (count_df['count'] == morph) | (count_df['sub_count'] == morph) |
                                               (count_df['chinese_char'] == morph) | (count_df['exception'] == morph),
                                               'natural_num'].tolist())
            else:
                print("메뉴없음")
                menu_list = np.append(menu_list, "주문하신 메뉴가 존재하지 않습니다.")
                # 수량도 0으로 리턴
                count_list.append([0])
            print('menu_list:', menu_list, '\n')

            start_index = i + 1

        elif morph in conj_df.to_numpy():
            start_index = i + 1

    print('final menu_list : ', menu_list, '\n')
    print('count_list:', count_list, '\n')
    response['menu'] = menu_list
    response['count'] = count_list
    return response
