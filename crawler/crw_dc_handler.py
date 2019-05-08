import requests, os, datetime, csv, mysql_conn
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl, time, contextlib

class CrMain:
    def __init__(self, board_url, board_name, start_page = 1):
        self.board_url = board_url
        self.board_name = board_name
        self.start_page = start_page

    def save_db(self, title, content, date):
        print("saving.......")
        conn = mysql_conn.MysqlConn().conn()
        sql = "insert into crw_dc_data(title, date, content, board) values (%s, %s, %s, %s)"
        for cnt, value in enumerate(title):
            if cnt % 200 == 0 : print("db : ", cnt, ", ", value)
            try:
                with conn.cursor() as curs:
                    curs.execute(sql, (title[cnt],  date[cnt], content[cnt], board))
                    conn.commit()
            except Exception as e:
                print(cnt, ", ", value, ", ", e)
                continue

    def save_csv(self, title, content, date):
        print("saving.......")
        with open('../datas/'+self.board_name+".csv", 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for cnt, value in enumerate(title):
                title_ = title[cnt]
                content_ = content[cnt]
                date_ = date[cnt]
                writer.writerow((title_, date_, content_))

    def get_content(self, board_list):
        print("get title, content, date .......")
        titles, contents, dates = [], [], []
        for cnt, board_url in enumerate(board_list):
            if cnt % 50 == 0 : print("get content : ", cnt, ", ", board_url)
            try:
                context = ssl._create_unverified_context()
                url_open = urlopen(board_url, context=context)
                time.sleep(1)
                soup = BeautifulSoup(url_open, 'lxml', from_encoding='utf-8')
                title = soup.find("div", {'class' : 'gallview_head'}).find('h3').findAll('span')[1].text.strip()
                date = str(soup.find("div", {'class' : 'gallview_head'}).find('span', {'class' : 'gall_date'})['title']).split(" ")[0]
                content = soup.find("div", {'class' : 'gallview_contents'}).find("div", {'class' : 'inner'}).text.strip()
            except Exception as e :
                print("error in detail! :  ", e)
                print(board_url)
                continue

        print(len(titles), len(contents), len(dates))
        #self.save_csv(titles, contents, dates)
        self.save_db(titles, contents, dates)

    def start(self):
        board_list = []
        page_num = int(self.start_page)
        today = datetime.datetime.now()
        while True:
            print("get url.....", page_num)
            try:
                url = self.board_url + str(page_num)
                soup = BeautifulSoup(url_open, 'lxml', from_encoding='utf-8')
                board_row = soup.find('table', {'class' : 'gall_list'}).find('tbody').findAll('tr')
                print("1. len  row : ", len(board_row))
                if len(board_row) < 2:
                    print("page num : ", page_num)
                    self.get_content(board_list)
                    board_list = []
                    break
                for cnt, row in enumerate(board_row):
                    board_list.append("https://gall.dcinside.com"+row.findAll('td')[1].findAll('a')[0].attrs['href'])
                    #break
                url_open.close()
                page_num += 1
                #break
            except Exception as e:
                print("error! :  ", e)
                continue
