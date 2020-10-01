from selenium import webdriver
import time
import load_excell

browser = webdriver.Chrome("C:/selenium/chromedriver")

browser.get("https://shopping.naver.com/")  # 네이버 쇼핑

def search_item(item_name, num_item):
    # 검색 부분에 아이템명 입력
    search_ele = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys(item_name)

    # 서치 아이콘 클릭
    search_ele = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

    #제대로된 로딩과 확인을 위해 타이머 + 스크롤 내리기를 실시한다
    browser.implicitly_wait(1)
    # 휠을 최대로 내린다
    wheel_interval = 1
    prev_webHeight = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scroll(0,document.body.scrollHeight)")

        #페이지 로딩 대기
        time.sleep(wheel_interval)

        cur_webHeight = browser.execute_script("return document.body.scrollHeight")
        if cur_webHeight == prev_webHeight:
            break;
        prev_webHeight = cur_webHeight

    ## 가격 정보 전부 얻어오기
    price_ele = []
    price_ele = browser.find_elements_by_class_name("price_num__2WUXn")

    # 가져온 가격정보를 1개씩 text로 따로 넣기
    price = []
    for value in price_ele:
        value = value.text
        # 가격을 수치화 시키기
        value = value.replace(",", "")
        value = value.replace("원", "")
        price.append(value)

    ## 배송비 정보 전부 얻어오기
    # 배송비에 관한 1차 추출
    price_shipping1 = []
    # 배송비에 관한 2차 추출
    price_shipping2 = []
    # 배송비에 관한 3차 추출
    price_shipping3 = []

    price_shipping_ele = browser.find_elements_by_class_name("basicList_option__3eF2s")
    # 배송비 정보 이외에도 다른 정보가 같이 수집됨(같은 클래스의 이름이 많아서 그럼)
    for value in price_shipping_ele:
        price_shipping1.append(value.text)

    # 배송비 정보만 추출
    for value in price_shipping1:
        if ("배송비" in value):
            price_shipping2.append(value)

    # 배송 가격만 추출
    for value in price_shipping2:
        if ("무료" in value):
            value = value.replace("무료", "0")

        value = value.replace("배송비 ", "")
        value = value.replace("원", "")
        if ("," in value):
            value = value.replace(",", "")

        price_shipping3.append(value)
    # print(price)
    # print(len(price))
    # print(price_shipping3)
    # print(len(price_shipping3))

    ### 위에서 얻은 자료를 토대로 계산
    # 상품 비용과 배송비를 더함
    total_price = []
    i = 0
    while i < len(price):
        total_price.append(int(price[i]) + int(price_shipping3[i]))
        i += 1

    total_price_avg = sum(total_price, 0) / len(total_price)
    total_price_max = max(total_price)
    total_price_min = min(total_price)

    print("평균가: " + str(total_price_avg))
    print("최대가: " + str(total_price_max))
    print("최소가: " + str(total_price_min))
    
    # 지금까지 얻은 값 엑셀에 출력(최저, 최고, 평균순)
    # num_item은 엑셀에 기록할 때 시작 행을 결정
    # 번호는 엑셀 기록할 때 시작 열을 의미
    load_excell.writeTo_excell("Naver", num_item, 3, total_price_min)
    load_excell.writeTo_excell("Naver", num_item, 4, total_price_max)
    load_excell.writeTo_excell("Naver", num_item, 5, total_price_avg)

    return total_price_min, total_price_max, total_price_avg



