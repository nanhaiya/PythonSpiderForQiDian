from bs4 import BeautifulSoup
import requests
import re

def pa(url,bookName):
    string=""
    response=requests.get(url)
    response=response.content
    soup=BeautifulSoup(response)
    nextLine=soup.find_all(attrs={"id":"j_chapterNext"})
    nextLine="http:"+str(nextLine[0].get('href'))
    head=soup.find_all(attrs={"class":"j_chapterName"})
    for m in head:
        print(m.span.string)
        string+=m.span.string+"\r\n"
    index=r"\S+"
    body=soup.find_all(attrs={"class":"read-content j_readContent"})
    # print(body[0].contents[1])
    body=str(body[0].contents[1])
    for j in re.findall(index,body):
        j=str(j).replace("<p>","")
        j=j.replace("</p>","")
        print(j)
        string+=j+"\r\n"

    with open(bookName,"ab+") as file:
        file.write(string.encode("utf-8"))
    pa(nextLine)

if __name__ == '__main__':
    #起点书籍爬虫
    url=r"https://read.qidian.com/chapter/kpwCq4fKJk01/LGKHGy9k73Q1"        #第一章路径
    bookName="庆余年.txt"              #书名+.txt
    pa(url,bookName)
