#-*- codeing = utf-8 -*-
import sys, os, re, xlwt
import sqlite3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def main():
    print("开始爬取.....")
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    # savepath=u'.\\top250.xls'
    dbpath = 'movie.db'
    saveData2DB(datalist,dbpath)
    # saveData (datalist,savepath)
    # askURL('https://movie.douban.com/top250?start=')

findLink = re.compile(r'<a href="(https?://.*)">')
findImgSrc = re.compile(r'<img .* src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl+str(i*25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            link = re.findall(findLink,item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            title = re.findall(findTitle,item)
            ctitle = title[0]
            data.append(ctitle)
            if (len(title) >= 2):
                otitle = title[1].replace("\xa0/\xa0","")
                data.append(otitle)
            else:
                data.append(' ')

            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judge = re.findall(findJudge,item)[0]
            data.append(judge)
            inq = re.findall(findInq,item)
            if len(inq) != 0 :
                inq = inq[0].replace('。','')
                data.append(inq)
            else:
                data.append(' ')

            bd = re.findall(findBd,item)[0]
            # print(bd)
            bd = re.sub("<br(\s+)?/>(\s+)*","",bd)
            bd = re.sub( "/", "", bd )
            bd = re.sub( "(\xa0){1,4}", " ", bd )
            bd = re.sub( "\n[ ]*", "", bd )
            data.append(bd)
            datalist.append(data)
            # print(title)
            # print(data)
            # break

    print(len(datalist))
    return datalist

# 得到指定一个url的网页内容
def askURL(url):
    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0 Wendell_CY'
    head = {'User-Agent': UA}
    req = urllib.request.Request(url=url, headers=head)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e :
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html


def saveData(datalist,savepath):
    print("save......")
    book = xlwt.Workbook( encoding="utf-8", style_compression=0 )
    sheet = book.add_sheet( '豆瓣电影top250',cell_overwrite_ok=True )
    col = ('电影详情链接',"图片链接","影片中文名","影片外文名","评分","评分数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"% i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)


def saveData2DB(datalist,dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    # cur.execute(sql)

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+ data[index]+'"'
        sql = '''
        insert into movie250(info_link,pic_link,cname,ename,score,rated,instroduciton,info) values(%s)
        '''%",".join(data)
        # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()




def init_db(dbpath):
    sql = '''
    create table movie250 (
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric,
    instroduciton test,
    info text)
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
    # init_db("movie.db")
    print('爬取完成，请查看xls文件')
