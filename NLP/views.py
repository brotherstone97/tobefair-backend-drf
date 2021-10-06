# Library
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv('./customer_requests.csv')
print(df.head())

# 텍스트 전처리
# 한글 형태소 분석기 KONLPy
from konlpy.tag import Okt

oKt = Okt()

text = df["questions"][0]

print(f'oKt.pos테스트{oKt.pos(text)}\n')
print(f'oKt.morphs테스트{oKt.pos(text)}\n')

# 특수 문자 제거
remove_special_characters = df['questions'].str.replace('[^가-힣ㄱ-ㅎㅏ-ㅣA-Za-z]', '')
print(f'특수문자 제거 결과: {remove_special_characters}\n')

remove_meaningless_korean = remove_special_characters.str.replace('ㅇ', '')

df['questions_cleaned'] = remove_meaningless_korean
print(df.head(20))

# 실습

stop_words = ['게', '의', '은', '도', '들', '는', '에', '하', '이', '가', '던', '지', '를', '고', '다', '을', '저', '기', '든']


def tokenizer(sentence):
    cleaned_token = []
    uncleand_tokens = oKt.morphs(sentence)

    for word in uncleand_tokens:
        if not word in stop_words:
            cleaned_token.append(word)

    return cleaned_token


df['questions_cleaned'] = remove_meaningless_korean.apply(lambda setence: tokenizer(setence))
