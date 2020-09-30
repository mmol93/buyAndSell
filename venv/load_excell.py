from openpyxl import load_workbook

# 불러올 엑셀 파일 설정
# data_only=True : 수식없이 값만 가져오게 설정
# 내가 저장한 AI_List 들고오기
load_wb = load_workbook("C:/Users/ijiu/Desktop/work/Git/buyAndsSell/venv/buyAndSell.xlsx", data_only=True)

# 메루카리 시트 먼저 불러오기
def load_excell_merukari():

    # 불러올 시트 설정
    load_sheet = load_wb['Merukari']

    # 메루카리 아이템 리스트
    merukari_itemList = []

    # 모든 기록한 아이템 리스트 가져오기
    for i in range(6, 100):
        item_name = load_sheet.cell(i, 2).value
        if item_name == None:
            break
        merukari_itemList.append(item_name)

    return merukari_itemList

def load_excell_naver():
    # 불러올 시트 설정
    load_sheet = load_wb['Naver']

    # 네이버 아이템 리스트
    naver_itemList = []

    # 모든 기록한 아이템 리스트 가져오기
    for i in range(6, 100):
        item_name = load_sheet.cell(i, 2).value
        if item_name == None:
            break
        naver_itemList.append(item_name)

    return naver_itemList

# def write_excell():