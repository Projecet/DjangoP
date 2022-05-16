import os
import csv
import json
import datetime
import urllib.request
from urllib import parse
from idlelib.pyparse import trans

from django.http import HttpResponse
from boot.httpreqeust import HttpRequest

from model.dao.sqlitedao import SqliteDao
from model.dao.userdao import UserDAO
from model.vo.uservo import UserVO
from model.dao.countrydao import CountryDAO
from model.vo.countryvo import CountryVO
from model.dao.contentdao import ContentDAO
from model.vo.contentvo import ContentVO
from model.dao.commentdao import CommentDAO
from model.vo.commentvo import CommentVO


sqlitedao = SqliteDao('shop')
sqlitedao.makeTable()
userdao = UserDAO('shop')
countrydao = CountryDAO('shop')
contentdao = ContentDAO('shop')
commentdao = CommentDAO('shop')


def trans_sex(sex):
    if sex == 'M':
        return '남성'
    elif sex == 'F':
        return'여성'
    else:
        return sex


def trans_country(country):
    if country == 'Netherlands':
        return '네덜란드'
    elif country == 'Germany':
        return '독일'
    elif country == 'Rusia':
        return '러시아'
    elif country == 'USA':
        return '미국'
    elif country == 'Vietnam':
        return '베트남'
    elif country == 'Singapore':
        return '싱가포르'
    elif country == 'Arab':
        return '아랍에미리트'
    elif country == 'UK':
        return '영국'
    elif country == 'Uzbek':
        return '우즈베키스탄'
    elif country == 'Indonesia':
        return '인도네시아'
    elif country == 'Japen':
        return '일본'
    elif country == 'China':
        return '중국'
    elif country == 'Kazakhstan':
        return '카자흐스탄'
    elif country == 'Quatar':
        return '카타르'
    elif country == 'Canada':
        return '캐나다'
    elif country == 'Turkey':
        return '터키'
    elif country == 'Thailand':
        return '태국'
    elif country == 'Poland':
        return '폴란드'
    elif country == 'Philippines ':
        return '필리핀'
    else:
        return country


def trans_kind(kind):
    if kind == 'not_vac':
        return '미접종'
    elif kind == 'pfizer':
        return '화이자'
    elif kind == 'moderna':
        return '모더나'
    elif kind == 'astra':
        return '아스트라제네카'
    elif kind == 'janssen':
        return '얀센'
    else:
        return kind


def trans_count(count):
    if count == 'n':
        return '미접종'
    else:
        return str(count) + '차'


def trans_corona_travel(user):
    country = trans_country(user.getCountry_id())
    count = trans_count(user.getI_count())
    kind = trans_kind(user.getI_kind())
    injection = user.getInjection()
    return '관심국가 : ' + str(country) + ' / 접종정보 : ' + str(kind) + ', ' + str(count) + ', ' + str(injection) + ' 접종'


def trans_space(str):
    # import unidecode  # 한글을 모조리 로마자로 바꾸는 위험한 물건
    # str = unidecode.unidecode(str)
    str = str.replace(u'\xa0', u'')
    str = str.replace(u'\xa9', u'')
    str = str.replace(u'\u200b', u'')
    str = str.replace(u'\u2008', u'')
    str = str.replace(u'\u2027', u'')
    str = str.replace(u'\u2013', u'')
    str = str.replace(u'\ufeff', u'')
    str = str.replace(u'\u274d', u'')

    return str


def interest_country_impl(country=None):
    if country != None:
        servicekey = '0GFaQKQWFDaV7fSsXoGC6eG/7ib5MKHhKCqmGh7F/ba16RND9esC3i1faBuGOxcEzVjQn02lnyHn7eynJBdc2g=='
        url = 'http://apis.data.go.kr/1262000/CountryOverseasArrivalsService/getCountryOverseasArrivalsList'
        url += '?serviceKey=' + servicekey + \
               '&pageNo=1' + \
               '&numOfRows=1' + \
               '&dataType=JSON' + \
               '&cond[country_nm::EQ]=' + country
        data = HttpRequest().web_request(method_name='GET', url=url, dict_data='')
        if not data.get('data'):
            return '<p>해당국가의 정보가 없습니다.</p>', '0000-00-00'
        else:
            html = data.get('data')[0].get('html_origin_cn')
            date = data.get('data')[0].get('wrt_dt')
            return html, date
    else:
        return '<p>관심 국가가 없습니다.</p>', '0000-00-00'


def news_impl():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/csv'
    my_file = os.path.join(THIS_FOLDER, 'news.csv')
    if os.path.isfile(my_file):
        # csv reader
        f = open(my_file, 'r', encoding='utf-8')
        reader = csv.DictReader(f)
        # for row in reader:
        #     print(row)
        data = list(reader)
        f.close()
        now_time = datetime.datetime.now()
        csv_time = datetime.datetime.strptime(data[0]['update'], '%Y-%m-%d %H:%M:%S')
        if now_time > csv_time:
            out_time = now_time - csv_time
        elif csv_time > now_time:
            out_time = csv_time - now_time
        else:
            out_time = now_time - csv_time
            switch = False

        if out_time.total_seconds() < 120:
            switch = False
        else:
            switch = True
    else:
        switch = True

    if switch is True:
        client_id = "l1kFsjj90OEXAqR61hu9"  # 개발자센터에서 발급받은 Client ID 값
        client_secret = "nSooOA9aWs"  # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote("코로나")
        url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&display=100"
        result = urllib.request.Request(url)
        result.add_header("X-Naver-Client-Id", client_id)
        result.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(result)
        rescode = response.getcode()
        if rescode == 200:
            news = json.loads(response.read().decode('utf-8'))

            # csv writer
            data = []
            fieldnames = ['title', 'originallink', 'link', 'description', 'pubDate', 'update']
            for i in news['items']:
                title = i['title']
                originallink = i['originallink']
                link = i['link']
                description = i['description']
                pubdate = i['pubDate']
                data.append({'title': trans_space(title), 'originallink': trans_space(originallink),
                             'link': trans_space(link), 'description': trans_space(description),
                             'pubDate': trans_space(pubdate), 'update': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            f = open(my_file, 'w', encoding='utf-8')
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            # for row in data:
            #     writer.writerow(row)
            f.close()
            data = news['items']
        else:
            data = [{
                'title': '뉴스읽기 오류',
                'originallink': None,
                'link': None,
                'description': '관리자에게 문의하세요.',
                'pubDate': 'Error'
            }]
    return data
