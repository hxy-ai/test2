from bs4 import BeautifulSoup

import requests

import csv

import bs4

#检查url地址

def check_link(url):

    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'
        }
        r = requests.get(url, headers=header)

        r.raise_for_status()

        r.encoding = r.apparent_encoding
        print(r.text)

        return r.text

    except:

        print('无法链接服务器！！！')

#爬取资源

def get_contents(ulist,rurl):

    soup = BeautifulSoup(rurl,'lxml')

    trs = soup.find_all('tr')
    print(trs)

    for tr in trs:

        ui = []

        for td in tr:

            ui.append(td.string)

        ulist.append(ui)

#保存资源

def save_contents(urlist):

    with open("企业债券兑付 付息 服务费提示（2023年2月）.csv", 'w', newline='') as f:

        writer = csv.writer(f)
        for i in range(len(urlist)):
            if len(urlist[i])>8 and urlist[i][1].isdigit():
                writer.writerow([urlist[i][1],urlist[i][2],urlist[i][3],urlist[i][4],urlist[i][5],urlist[i][6]])

def main():

    urli = []

    url = "https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml"

    rs = check_link(url)

    get_contents(urli,rs)
    print(urli)

    save_contents(urli)

main()