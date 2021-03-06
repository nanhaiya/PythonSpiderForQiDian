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
    body=soup.find_all(attrs={"class":"read-content j_readContent"})[0]
    body=body.find_all("p")
    for j in body:
        string+=j.getText().strip()+"\r\n"

    print(string)
    with open(bookName,"ab+") as file:
        file.write(string.encode("utf-8"))
    pa(nextLine,bookName)

if __name__ == '__main__':
    #起点书籍爬虫
    url=r"https://read.qidian.com/chapter/kpwCq4fKJk01/LGKHGy9k73Q1"        #第一章路径
    bookName="庆余年.txt"              #书名+.txt,或写成绝对路径，如:"d:python/text/庆余年.txt"
    pa(url,bookName)
