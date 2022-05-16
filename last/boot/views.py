import os
import csv
import json
import datetime
import urllib.request
from urllib import parse
from urllib.parse import urlencode

from django.http import HttpResponse, HttpResponseRedirect
from boot.httpreqeust import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from config.settings import UPLOAD_DIR
from boot.errorcode import ErrorCode
from model.dao.sqlitedao import SqliteDao
from model.dao.userdao import UserDAO
from model.vo.uservo import UserVO
from model.dao.countrydao import CountryDAO
from model.vo.countryvo import CountryVO
from model.dao.contentdao import ContentDAO
from model.vo.contentvo import ContentVO
from model.dao.commentdao import CommentDAO
from model.vo.commentvo import CommentVO

from static import trans

sqlitedao = SqliteDao('shop')
sqlitedao.makeTable()
userdao = UserDAO('shop')
countrydao = CountryDAO('shop')
contentdao = ContentDAO('shop')
commentdao = CommentDAO('shop')


# def search(request):
#     search = request.GET['search']
#     result = parse.quote(search)  # url 인코딩
#     print(result)
#     print(parse.unquote(result))  # url 디코딩
#     page = '01'
#     url = 'https://search.naver.com/search.naver?where=news&query=' + search + '&start=' + page
#     context = {
#         'url': url,
#         'search': search
#     }
#     return render(request, 'index.html', context)


# Create your views here.
def index(request):
    context = {
        'center': 'main.html'
    }
    data = trans.news_impl()
    for i in range(0, 1):
        context['items'] = data[i]
    list = contentdao.selectall('d')
    if len(list) != 0:
        user = userdao.select(list[0].getUser_id()).getName()
        if user == None:
            list[0].setUser_name('Removed_User')
        else:
            list[0].setUser_name(user)
        context['list'] = list[0]
    try:
        id = request.session['sessionid']
    except KeyError:
        id = None
    session_user = userdao.select(id)
    session_user.setCountry_id(trans.trans_country(session_user.getCountry_id()))
    data = trans.interest_country_impl(session_user.getCountry_id())
    context['user'] = session_user
    context['html'] = data[0]
    context['date'] = data[1]
    return render(request, 'index.html', context)


def charts(request):
    context = {
        'center': 'sample/charts.html'
    }
    return render(request, 'index.html', context)


def password(request):
    context = {
        'center': 'sample/password.html'
    }
    return render(request, 'index.html', context)


def tables(request):
    context = {
        'center': 'sample/tables.html'
    }
    return render(request, 'index.html', context)


class ErrorViews:
    def p401(request):
        context = {
            'center': 'error/401.html'
        }
        return render(request, 'index.html', context)

    def p404(request):
        context = {
            'center': 'error/404.html'
        }
        return render(request, 'index.html', context)

    def p500(request):
        context = {
            'center': 'error/500.html'
        }
        return render(request, 'index.html', context)


class MemberViews:
    def login(request):
        context = {
            'center': 'member/login.html'
        }
        return render(request, 'index.html', context)

    def login_fail(request):
        context = {
            'center': 'member/login_fail.html'
        }
        return render(request, 'index.html', context)

    def login_impl(request):
        try:
            id = request.POST['id']
            password = request.POST['password']
            loginuser = userdao.select(id)
            if password == loginuser.getPassword():
                request.session['sessionid'] = id
            else:
                raise Exception
            return redirect('/')
        except:
            return redirect('login_fail')

    def logout(request):
        if request.session['sessionid'] != None:
            del request.session['sessionid']
        return redirect('/')

    def join(request):
        id = request.POST.getlist('id')
        if len(id) == 0:
            context = {
                'center': 'member/join_check.html'
            }
        else:
            context = {
                'center': 'join.html'
            }
        return render(request, 'index.html', context)

    def join_check(request):
        id = request.POST.getlist('id')
        if len(id) == 0:
            context = {
                'center': 'member/join_check.html'
            }
        else:
            check = userdao.select(id[0])
            if check.getId() == None:  # 아이디가 없으면
                context = {
                    'center': 'member/join.html',
                    'id': id[0]
                }
            else:  # 아이디가 있으면
                context = {
                    'center': 'member/join_check.html',
                    'msg': '중복된 아이디가 있습니다.'
                }
        return render(request, 'index.html', context)

    def join_impl(request):
        id = request.POST['id']
        password = request.POST['pwd']
        name = request.POST['name']
        zipcode = request.POST['zipcode']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        address = zipcode + add1 + add2
        sex = request.POST['sex']
        age = request.POST['age']
        country_id = request.POST['country']
        i_count = request.POST['count']
        i_kind = request.POST['kind']
        injection = request.POST['date']

        user = UserVO(id, password, name, zipcode, add1, add2, sex,
                      age, country_id, i_count, i_kind, str(injection), None)

        userdao.insert(user)
        context = {
            'center': 'main.html'
        }
        return render(request, 'index.html', context)

    def my_page(request):
        id = request.session['sessionid']
        user = userdao.select(id)
        user.setSex(trans.trans_sex(user.getSex()))
        user.setI_kind(trans.trans_kind(user.getI_kind()))
        user.setI_count(trans.trans_count(user.getI_count()))
        user.setCountry_id(trans.trans_country(user.getCountry_id()))
        context = {
            'center': 'member/my_page.html',
            'my': user
        }
        return render(request, 'index.html', context)

    def user_update(request):
        id = request.session['sessionid']
        user = userdao.select(id)

        context = {
            'center': 'member/user_update.html',
            'my': user
        }
        return render(request, 'index.html', context)

    def user_update_impl(request):
        name = request.POST['name']
        id = request.POST['id']
        password = request.POST['password']
        zipcode = request.POST.get('zipcode')
        add1 = request.POST.get('add1')
        add2 = request.POST.get('add2')
        sex = request.POST['sex']
        age = request.POST['age']
        country_id = request.POST.get('country_id')
        i_count = request.POST['i_count']
        i_kind = request.POST['i_kind']
        injection = request.POST['injection']
        user = UserVO(id, password, name, zipcode, add1, add2, sex,
                      age, country_id, i_count, i_kind, injection, None)
        userdao.update(user)

        str = urlencode({'id': id})
        return HttpResponseRedirect('%s?%s' % ('my_page', str))

    def user_delete(request):
        id = request.GET['id']
        userdao.delete(id)
        if request.session['sessionid'] != None:
            del request.session['sessionid']
        return redirect('index')

    def user_country(request):
        context = {
            'center': 'member/user_update.html',
            # 'userupdate': user
        }
        return render(request, 'index.html', context)


class ContentViews:
    def content(request):
        c_id = request.GET['c_id']
        content = contentdao.select(c_id)
        user = userdao.select(content.getUser_id()).getName()
        if user == None:
            content.setUser_name('Removed_User')
        else:
            content.setUser_name(user)
        list = commentdao.selectid(c_id)
        for l in list:
            name = userdao.select(l.getUser_id()).getName()
            if name == None:
                l.setUser_name('Removed_User')
            else:
                l.setUser_name(name)

        context = {
            'center': 'content/content.html',
            'content': content,
            'list': list
        }
        return render(request, 'index.html', context)

    def contents(request):
        get_page = request.GET.getlist('page')
        if len(get_page) != 0:
            now_page = int(get_page[0])
        else:
            now_page = 1

        count = contentdao.count()
        page = int((count-1)/5)+1

        list = contentdao.selectlimit(count, now_page, 'd')
        for l in list:
            name = userdao.select(l.getUser_id()).getName()
            if name == None:
                l.setUser_name('Removed_Name')
            else:
                l.setUser_name(name)

        context = {
            'center': 'content/contents.html',
            'list': list,
            'count': count,
            'range_page': range(1, page+1),
            'now_page': now_page,
            'page': page
        }
        return render(request, 'index.html', context)

    def contents_impl(request):
        check = request.POST.getlist('check')
        content = request.POST['content']
        user = userdao.select(request.session['sessionid'])
        id = user.getId()
        corona_travel = trans.trans_corona_travel(user)
        if len(check) != 0:  # check 길이가 0이 아닐때
            contents = ContentVO(None, id, None, content, corona_travel, None)
        else:
            contents = ContentVO(None, id, None, content, None, None)
        contentdao.insert(contents)
        return redirect('contents')

    def content_update(request):
        check = request.POST.getlist('check')
        content = request.POST['content']
        c_id = request.POST['id']
        if len(check) != 0:  # check 길이가 0이 아닐때
            user = userdao.select(request.session['sessionid'])
            corona_travel = trans.trans_corona_travel(user)
            contents = ContentVO(c_id, None, None, content, corona_travel, None)
        else:
            contents = ContentVO(c_id, None, None, content, None, None)
        contentdao.update(contents)
        context = {
            'center': 'content/content_move.html',
            'c_id': c_id
        }
        return render(request, 'index.html', context)

    def content_delete(request):
        c_id = request.POST['id']
        contentdao.delete(c_id)
        return redirect('contents')

    def comment(request):
        c_id = request.GET['c_id']
        new_comment = request.POST.getlist('comment')
        user = userdao.select(request.session['sessionid'])
        id = user.getId()
        if len(new_comment) != 0:
            comment = CommentVO(None, str(c_id), id, None, new_comment[0], None)
            commentdao.insert(comment)
        context = {
            'center': 'content/content_move.html',
            'c_id': c_id
        }
        return render(request, 'index.html', context)

    def comment_update(request):
        m_id = request.POST['id']
        comment = commentdao.select(m_id)
        c_id = comment.getContent_id()
        new_comment = request.POST.getlist('comment')
        if len(new_comment) != 0:
            comment = CommentVO(m_id, None, None, None, new_comment[0], None)
            commentdao.update(comment)
        context = {
            'center': 'content/content_move.html',
            'c_id': c_id
        }
        return render(request, 'index.html', context)

    def comment_delete(request):
        m_id = request.POST['id']
        comment = commentdao.select(m_id)
        c_id = comment.getContent_id()
        commentdao.delete(m_id)
        context = {
            'center': 'content/content_move.html',
            'c_id': c_id
        }
        return render(request, 'index.html', context)


class MapViews:
    def world(request):
        context = {
            'center': 'map/world.html'
        }
        # country = ['Canada',
        #            'China',
        #            'France',
        #            'Germany',
        #            'Indonesia',
        #            'Japan',
        #            'Kazakhstan',
        #            'Korea',
        #            'Netherlands',
        #            'Philippines',
        #            'Poland',
        #            'Qatar',
        #            'Russia',
        #            'Singapore',
        #            'Thailand',
        #            'Turkey',
        #            'UAE',
        #            'UK',
        #            'USA',
        #            'Uzbekistan',
        #            'Vietnam']
        # if os.path.isfile('static/csv/worldcorona.csv'):
        #     # csv reader
        #     f = open("static/csv/worldcorona.csv", "r")
        #     reader = csv.DictReader(f)
        #     # for row in reader:
        #     #     print(row)
        #     data = list(reader)
        #     f.close()
        #     for d in data:
        #         for c in country:
        #             if d['country_name'].upper() == c.upper():
        #                 context[c] = d
        return render(request, 'map/map.html', context)


class ContryinfoViews:
    def contryinfo(request):
        context = {
            'center': 'contryinfo/contents.html'
        }
        return render(request, 'index.html', context)

    def russia(request):
        context = {
            'center': 'contryinfo/russia.html'
        }
        return render(request, 'index.html', context)

    def china(request):
        context = {
            'center': 'contryinfo/china.html'
        }
        return render(request, 'index.html', context)

    def indonesia(request):
        context = {
            'center': 'contryinfo/indonesia.html'
        }
        return render(request, 'index.html', context)

    def japan(request):
        context = {
            'center': 'contryinfo/japan.html'
        }
        return render(request, 'index.html', context)

    def kazakhstan(request):
        context = {
            'center': 'contryinfo/kazakhstan.html'
        }
        return render(request, 'index.html', context)

    def malaysia(request):
        context = {
            'center': 'contryinfo/malaysia.html'
        }
        return render(request, 'index.html', context)

    def philippines(request):
        context = {
            'center': 'contryinfo/philippines.html'
        }
        return render(request, 'index.html', context)

    def qatar(request):
        context = {
            'center': 'contryinfo/qatar.html'
        }
        return render(request, 'index.html', context)

    def singapore(request):
        context = {
            'center': 'contryinfo/singapore.html'
        }
        return render(request, 'index.html', context)

    def thailand(request):
        context = {
            'center': 'contryinfo/thailand.html'
        }
        return render(request, 'index.html', context)

    def turkey(request):
        context = {
            'center': 'contryinfo/turkey.html'
        }
        return render(request, 'index.html', context)

    def uae(request):
        context = {
            'center': 'contryinfo/uae.html'
        }
        return render(request, 'index.html', context)

    def uzbekistan(request):
        context = {
            'center': 'contryinfo/uzbekistan.html'
        }
        return render(request, 'index.html', context)

    def vietnam(request):
        context = {
            'center': 'contryinfo/vietnam.html'
        }
        return render(request, 'index.html', context)

    def uk(request):
        context = {
            'center': 'contryinfo/uk.html'
        }
        return render(request, 'index.html', context)

    def netherlands(request):
        context = {
            'center': 'contryinfo/netherlands.html'
        }
        return render(request, 'index.html', context)

    def germany(request):
        context = {
            'center': 'contryinfo/germany.html'
        }
        return render(request, 'index.html', context)

    def poland(request):
        context = {
            'center': 'contryinfo/poland.html'
        }
        return render(request, 'index.html', context)

    def canada(request):
        context = {
            'center': 'contryinfo/poland.html'
        }
        return render(request, 'index.html', context)

    def usa(request):
        context = {
            'center': 'contryinfo/poland.html'
        }
        return render(request, 'index.html', context)


class InterestViews:
    def interest_country(request):
        try:
            id = request.session['sessionid']
            user = userdao.select(id)
            country = request.GET.getlist('country')
            if len(country) != 0:
                country = country[0]
                data = trans.interest_country_impl(country)
            else:
                user.setCountry_id(trans.trans_country(user.getCountry_id()))
                data = trans.interest_country_impl(user.getCountry_id())
            context = {
                'center': 'interest_country/interest_country.html',
                'user': user,
                'country': country,
                'html': data[0],
                'date': data[1]
            }
            return render(request, 'index.html', context)
        except KeyError:
            context = {
                'center': 'interest_country/interest_country.html'
            }
            return render(request, 'index.html', context)


class NewsViews:
    def news(request):
        context = {
            'center': 'news/news.html',
        }
        data = trans.news_impl()

        get_page = request.GET.getlist('page')
        if len(get_page) != 0:
            now_page = int(get_page[0])
        else:
            now_page = 1
        count = len(data)
        page = int((count-1)/10)+1
        context['items'] = []
        for i in range((now_page*10)-10, now_page*10):
            context['items'].append(data[i])
        context['count'] = count
        context['range_page'] = range(1, page+1)
        context['now_page'] = now_page
        context['page'] = page
        return render(request, 'index.html', context)


class TweetsViews:
    def tweets(request):
        context = {
            'center': 'tweets/tweets.html',
            'france': 'tweets/france.html',
            'india': 'tweets/india.html',
            'japan': 'tweets/japan.html',
            'korea': 'tweets/korea.html',
            'usa': 'tweets/USA.html',
        }
        return render(request, 'index.html', context)

    def france(request):
        context = {
            'center': 'tweets/france.html'
        }
        return render(request, 'index.html', context)

    def india(request):
        context = {
            'center': 'tweets/india.html'
        }
        return render(request, 'index.html', context)

    def japan(request):
        context = {
            'center': 'tweets/japan.html'
        }
        return render(request, 'index.html', context)

    def korea(request):
        context = {
            'center': 'tweets/korea.html'
        }
        return render(request, 'index.html', context)

    def usa(request):
        context = {
            'center': 'tweets/USA.html'
        }
        return render(request, 'index.html', context)
