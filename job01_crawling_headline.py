from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']     # 페이지 순으로 정렬
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

df_titles = pd.DataFrame()      # 빈 데이터 프레임
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
# 나 request 아니고 브라우저야 속이기
# resp = requests.get(url, headers=headers)        # requests :  웹서버 주소에 요쳥. url 주소로부터 응답을 받아옴. 웹크롤링 하도 하니까 웹브라우저의 요청만
# # print(list(resp))                              #            받아오게 막아놈. requests 안됨. but 속이고 가능.
# print(type(resp))
# soup = BeautifulSoup(resp.text, 'html.parser')
# # print(soup)
# title_tags = soup.select('.sh_text_headline')   # 요소들 가지고 올때는 .을 찍는다.
# print(title_tags)
# print(len(title_tags))
# print(type(title_tags[0]))
# titles = []     # 뉴스 제목들을 담을 빈 리스트 생성
# for title_tag in title_tags:
#     titles.append(re.compile('[^가-힣|a-z|A-Z]').sub(' ', title_tag.text))        # re. -> 내가 원하는 내용들만 뽑아올때. 모든 한글조합.
# print(titles)
# print(len(titles))
        # 모든 페이지의 헤드라인 뉴스들만 가져오기

df_titles = pd.DataFrame()
re_title = re.compile('[^가-힣]|a-z|A-Z')

for i in range(6):
    resp = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i),).