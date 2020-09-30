import csv
import requests # requests pip install 필요
from bs4 import BeautifulSoup   # BeautifulSoup pip install 필요
import lxml # lxml pip install 필요
import search_NaverShop
import search_Merukari
import load_excell

# **** 엑셀에서 데이터 가져오기 -ok
merukari_itemList = []
naver_itemList = []

merukari_itemList = load_excell.load_excell_merukari()
naver_itemList = load_excell.load_excell_naver()

print(merukari_itemList)
print(naver_itemList)

# **** 네이버 쇼핑에서 정보 가져오기 - ing
# 아이템 이름으로 검색 실시
search_NaverShop.search_item(naver_itemList[0])

