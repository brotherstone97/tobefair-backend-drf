# Library
# import pandas as pd
import numpy as np

# Load Dataset
# df = pd.read_csv('./customer_requests.csv')
# print(df.head())

# 텍스트 전처리
# 한글 형태소 분석기 KONLPy
from konlpy.tag import Okt

oKt = Okt()
#메뉴의 핵심 키워드를 일일이 사전정의해서 해당 텍스트를 골라내는 방법
#또 다른 알고리즘으로 메뉴이름 캐치, 수량은 '개' 등의 텍스트를 통해 필터링

##idea: ex)xxx 두개 주세요 처럼 일반적으로 메뉴를 먼저말하고 개수를 그 다음에 말하는 특징을 활용해서 슬라이싱 하자


meaningfulWords = ['개','줘','주세요',]
def tokenizer(sentence):
    #한 문장을 쪼개서 배열로 만듦
    splitedSentence = oKt.morphs(sentence)
# text = df["questions"][0]

# 특수 문자 제거
# df['questions_cleaned'] = df['questions'].str.replace('[^가-힣ㄱ-ㅎㅏ-ㅣA-Za-z]', '')
# print(df.head(20))


# 실습
# 필요없는 단어 제거
stop_words = ['게', '의', '은', '도', '들', '는', '에', '하', '이', '가', '던', '지', '를', '고', '다', '을', '저', '기', '든']


def _tokenizer(sentence):
    cleaned_token = []
    uncleaned_tokens = oKt.morphs(sentence)

    for word in uncleaned_tokens:
        if not word in stop_words:
            cleaned_token.append(word)

    return cleaned_token


# 특수문자 제거한 열에 stop_words를 제거하는 tokenizer함수를 입힌 결과를 덮어 씌움
# df['questions_cleaned'] = df['questions_cleaned'].apply(lambda sentence: tokenizer(sentence))
