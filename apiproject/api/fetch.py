
import urllib2
import re

from .models import Article, Category

kewei_url = 'http://www.bjkw.gov.cn/col/col19/index.html'
shijiazhuang_url = 'http://www.sjzkj.gov.cn/eportal/cms/jsp/site001/channel01.jsp?channelidenty=f99ccc8219b2c9120119bc13d9490035&a1b2dd=7xaac'

def read_content(url):
	con = urllib2.urlopen(urllib2.Request(url))
	content = con.read()
	content.replace("(\r\n|\n|\r)", "")
	content.strip()
	return content

def shijiazhuang():
    content = read_content(shijiazhuang_url)
    patt = re.compile('<td.*href=\'(.*\n*.*)\'.*title=\'(.*\n*.*)\'.*')
    result = re.findall(patt, content)
    date_patt = re.compile('<td.*>(.*)<\/span>')
    date_r = re.findall(date_patt, content)
    list = []
    for index in range(len(result)):
        t = {}
        r = result[index]
        t['url'] = r[0]
        t['title'] = r[1]
        t['date'] = date_r[index]
        list.append(t)
    return list

def keiwei():
    content = read_content(kewei_url)
    pat = re.compile('<li><a href=\'(.*\n*.*)\'.*title=\'(.*\n*.*)</a>.*time\'>(.*\n*.*)<\/span')
    result = re.findall(pat, content)
    list = []
    for r in result:
        t = {}
        t['url'] = 'http://www.bjkw.gov.cn' + r[0]
        t['title'] = r[1]
        t['date'] = r[2]
        list.append(t)
    return list

def saveData(data, c_id):
    title = data['title']
    url = data['url']
    date = data['date']
    category = Category.objects.get(pk=c_id)
    article = Article(title=title, url=url, date=date, category=category)
    article.save()

def update_data(c_id):
    Article.objects.all().delete()
    list = []
    if c_id == '1':
        list = keiwei()
    elif c_id == '2':
        list = shijiazhuang()
    for d in list:
        saveData(d, c_id)



