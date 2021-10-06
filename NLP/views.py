# Library
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv('./customer_requests.csv')
print(df.head())

#텍스트 전처리
#한글 형태소 분석기 KONLPy
from konlpy.tag import Okt
oKt = Okt()

text = df["question"][0]

print(f'oKt.pos테스트{oKt.pos(text)}\n')
print(f'oKt.morphs테스트{oKt.pos(text)}\n')

remove_special_characters = df['questions'].str.replace('[^가-힣ㄱ-ㅎㅏ-ㅣA-Za-z]', '')
print(f'특수문자 제거 결과: {remove_special_characters}')

remove_meaningless_korean = remove_special_characters.str.replace('ㅇ','')
print(f' ㅇ 제거 결과: {remove_special_characters}')




