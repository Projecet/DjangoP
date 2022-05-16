"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from boot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('charts', views.charts, name='charts'),
    path('password', views.password, name='password'),
    path('tables', views.tables, name='tables'),

    # error part
    path('p401', views.ErrorViews.p401, name='p401'),
    path('p404', views.ErrorViews.p404, name='p404'),
    path('p500', views.ErrorViews.p500, name='p500'),

    # member part
    path('login', views.MemberViews.login, name='login'),
    path('login_impl', views.MemberViews.login_impl, name='login_impl'),
    path('login_fail', views.MemberViews.login_fail, name='login_fail'),
    path('logout', views.MemberViews.logout, name='logout'),
    path('join', views.MemberViews.join, name='join'),
    path('join_check', views.MemberViews.join_check, name='join_check'),
    path('join_impl', views.MemberViews.join_impl, name='join_impl'),
    path('my_page', views.MemberViews.my_page, name='my_page'),
    path('user_update', views.MemberViews.user_update, name='user_update'),
    path('user_update_impl', views.MemberViews.user_update_impl, name='user_update_impl'),
    path('user_delete', views.MemberViews.user_delete, name='user_delete'),
    path('user_country', views.MemberViews.user_country, name='user_country'),

    # content part
    path('content', views.ContentViews.content, name='content'),
    path('content', views.ContentViews.content, name='content'),
    path('content_update', views.ContentViews.content_update, name='content_update'),
    path('content_delete', views.ContentViews.content_delete, name='content_delete'),
    path('comment', views.ContentViews.comment, name='comment'),
    path('comment_update', views.ContentViews.comment_update, name='comment_update'),
    path('comment_delete', views.ContentViews.comment_delete, name='comment_delete'),
    path('contents', views.ContentViews.contents, name='contents'),
    path('contents_impl', views.ContentViews.contents_impl, name='contents_impl'),

    # map part
    path('world', views.MapViews.world, name='world'),

    # contryinfo
    path('contryinfo', views.ContryinfoViews.contryinfo, name='contryinfo'),
    path('russia', views.ContryinfoViews.russia, name='russia'),
    path('china', views.ContryinfoViews.china, name='china'),
    path('indonesia', views.ContryinfoViews.indonesia, name='indonesia'),
    path('japan', views.ContryinfoViews.japan, name='japan'),
    path('kazakhstan', views.ContryinfoViews.kazakhstan, name='kazakhstan'),
    path('malaysia', views.ContryinfoViews.malaysia, name='malaysia'),
    path('philippines', views.ContryinfoViews.philippines, name='philippines'),
    path('qatar', views.ContryinfoViews.qatar, name='qatar'),
    path('singapore', views.ContryinfoViews.singapore, name='singapore'),
    path('thailand', views.ContryinfoViews.thailand, name='thailand'),
    path('turkey', views.ContryinfoViews.turkey, name='turkey'),
    path('uae', views.ContryinfoViews.uae, name='uae'),
    path('uzbekistan', views.ContryinfoViews.uzbekistan, name='uzbekistan'),
    path('vietnam', views.ContryinfoViews.vietnam, name='vietnam'),
    path('uk', views.ContryinfoViews.uk, name='uk'),
    path('netherlands', views.ContryinfoViews.netherlands, name='netherlands'),
    path('germany', views.ContryinfoViews.germany, name='germany'),
    path('poland', views.ContryinfoViews.poland, name='poland'),
    path('canada', views.ContryinfoViews.canada, name='canada'),
    path('usa', views.ContryinfoViews.usa, name='usa'),

    # interest_country part
    path('interest_country', views.InterestViews.interest_country, name='interest_country'),

    # news part
    path('news', views.NewsViews.news, name='news'),

    # tweets part
    path('tweets', views.TweetsViews.tweets, name='tweets'),
    path('france', views.TweetsViews.france, name='france'),
    path('india', views.TweetsViews.india, name='india'),
    path('japan', views.TweetsViews.japan, name='japan'),
    path('korea', views.TweetsViews.korea, name='korea'),
    path('usa', views.TweetsViews.usa, name='usa'),
]
