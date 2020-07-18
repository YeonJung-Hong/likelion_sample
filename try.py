import requests
import openpyxl
import urllib.request

client_id = 'plS7u_hgu46IJHO58Edi'
client_secret = '3aUj54CRHq'

start = 1
num = 0

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['F'].width = 100
excel_sheet.append(['NO','제목','최저가','최고가','쇼핑몰','링크'])

for index in range(10):
    start_num = start + (index * 100)
    encText = urllib.parse.quote('아이리스 "PCF-SC15T" -옥션 -11번가 -인터파크')
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=' + encText + '&display=100&start='+str(start_num)
    header_parms = {"X-Naver-Client-Id":client_id, "X-naver-Client-Secret":client_secret}
    res=requests.get(naver_open_api,headers=header_parms)

    if res.status_code == 200:
        data=res.json()
        for item in data['items']:
            num += 1
            excel_sheet.append([num, item['title'],item['lprice'],item['hprice'],item['mallName'],item['link']])
    else:
        print("Error : ", res.status_code)

excel_file.save('naverapi_shopping.xlsx')

excel_file.close()