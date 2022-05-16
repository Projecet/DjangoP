import folium
import json
import pandas
import pandas as pd
import csv

from folium.plugins import MarkerCluster
from folium.plugins import MiniMap
from folium_jsbutton import JsButton


### 기본 맵 생성
m = folium.Map(
    location = [0,0],
    # width = 1500,
    # height = 800,
    zoom_start = 2,
    max_bounds = False,
    min_zoom = 2,
    max_zoom = 7,
    min_lat = 30,
    max_lat = 0,
    min_lon = 30,
    max_lon = 0,
    tiles = "CartoDB dark_matter"
    # tiles = "CartoDB positron"
    # titles = "OpenStreetMap"
)

### 미니맵 적용
minimap = MiniMap()
m.add_child(minimap)


### geojson 데이터 적용
geo_canada = json.load(open('data/canada.json'))
geo_usa = json.load(open('data/usa.json'))
geo_uk = json.load(open('data/uk.json'))
geo_france = json.load(open('data/france.json'))
geo_poland = json.load(open('data/poland.json'))
geo_germany = json.load(open('data/germany.json'))
geo_netherland = json.load(open('data/netherland.json'))
geo_turkey = json.load(open('data/turkey.json'))
geo_qatar = json.load(open('data/qatar.json'))
geo_uae = json.load(open('data/uae.json'))
geo_kazakhstan = json.load(open('data/kazakhstan.json'))
geo_uzbekistan = json.load(open('data/uzbekistan.json'))
geo_russia = json.load(open('data/russia.json'))
geo_china = json.load(open('data/china.json'))
geo_korea = json.load(open('data/korea.json'))
geo_japan = json.load(open('data/japan.json'))
geo_thailand = json.load(open('data/thailand.json'))
geo_vietnam = json.load(open('data/vietnam.json'))
geo_philippines = json.load(open('data/philippines.json'))
geo_indonesia = json.load(open('data/indonesia.json'))
# geo_singapore = json.load(open('data/singapore.json'))


### 크롤링 csv 데이터 인덱스 추출
worldcorona_data = pd.read_csv('../../static/csv/worldcorona.csv')

usa_t = worldcorona_data.loc[0][1]
usa_p = worldcorona_data.loc[0][2]
france_t = worldcorona_data.loc[3][1]
france_p = worldcorona_data.loc[3][2]
canada_t = worldcorona_data.loc[22][1]
canada_p = worldcorona_data.loc[22][2]
uk_t = worldcorona_data.loc[4][1]
uk_p = worldcorona_data.loc[4][2]
germany_t = worldcorona_data.loc[9][1]
germany_p = worldcorona_data.loc[9][2]
poland_t = worldcorona_data.loc[14][1]
poland_p = worldcorona_data.loc[14][2]
netherland_t = worldcorona_data.loc[16][1]
netherland_p = worldcorona_data.loc[16][2]
qatar_t = worldcorona_data.loc[88][1]
qatar_p = worldcorona_data.loc[88][2]
uae_t = worldcorona_data.loc[57][1]
uae_p = worldcorona_data.loc[57][2]
turkey_t = worldcorona_data.loc[6][1]
turkey_p = worldcorona_data.loc[6][2]
russia_t = worldcorona_data.loc[5][1]
russia_p = worldcorona_data.loc[5][2]
kazakhstan_t = worldcorona_data.loc[43][1]
kazakhstan_p = worldcorona_data.loc[43][2]
uzbekistan_t = worldcorona_data.loc[101][1]
uzbekistan_p = worldcorona_data.loc[101][2]
korea_t = worldcorona_data.loc[56][1]
korea_p= worldcorona_data.loc[56][2]
japan_t = worldcorona_data.loc[26][1]
japan_p = worldcorona_data.loc[26][2]
china_t = worldcorona_data.loc[118][1]
china_p = worldcorona_data.loc[118][2]
indonesia_t = worldcorona_data.loc[15][1]
indonesia_p = worldcorona_data.loc[15][2]
thailand_t = worldcorona_data.loc[29][1]
thailand_p = worldcorona_data.loc[29][2]
vietnam_t = worldcorona_data.loc[30][1]
vietnam_p = worldcorona_data.loc[30][2]
singapore_t = worldcorona_data.loc[86][1]
singapore_p = worldcorona_data.loc[86][2]
philippines_t = worldcorona_data.loc[19][1]
philippines_p = worldcorona_data.loc[19][2]

### Geojson 스타일 적용 '#3F94E9'
style1 = {'fillColor': '#00ff0000', 'color': '#FFFFFF', 'weight' : 1,'fill_opacity':'0.2', 'line_opacity':'1'}
style2 = {'fillColor': '#00ff0000', 'color': '#FFFFFF', 'weight' : 1,'fill_opacity':'0.2', 'line_opacity':'1'}
style3 = {'fillColor': '#00ff0000', 'color': '#FFFFFF', 'weight' : 1,'fill_opacity':'0.2', 'line_opacity':'1'}
style_china = {'fillColor': '#AB5234', 'color': '#FFFFFF', 'weight' : 1,'fill_opacity': '0.2', 'line_opacity':'1'}

### 크롤링 데이터 맵 적용
d_korea = '<img src="img/korea.png"><br><b>Korea</strong></b><br>',\
          '확진자 :',korea_t,\
          '<br>','총인구 : ',\
          korea_p,
d_japan = '<img src="img/japan.png"><br><b>Japan</b><br>','확진자 :',\
          japan_t,'<br>',\
          '총인구 : ',\
          japan_p
d_china = '<img src="img/China.png"><br><b>China</b><br>',\
          '확진자 :',\
          china_t,\
          '<br>',\
          '총인구 : ',\
          china_p
d_thailand = '<img src="img/Thailand.png"><br><b>Thailand</b><br>',\
             '확진자 :',\
             thailand_t,\
             '<br>',\
             '총인구 : ',\
             thailand_p
d_philippines = '<img src="img/Philippines.png"><br><b>Philippines</b><br>',\
                '확진자 :',\
                philippines_t,\
                '<br>',\
                '총인구 : ',\
                philippines_p
d_vietnam = '<img src="img/Vietnam.png"><br><b>Vietnam</b><br>',\
            '확진자 :',\
            vietnam_t,\
            '<br>',\
            '총인구 : ',\
            vietnam_p
d_indonesia = '<img src="img/indonesia.png"><br><b>Indonesia</b><br>',\
              '확진자 :',\
              indonesia_t,\
              '<br>',\
              '총인구 : ',\
              indonesia_p
d_singapore = '<img src="img/Singapore.png"><br><b>Singapore</b><br>',\
              '확진자 :',\
              singapore_t,\
              '<br>',\
              '총인구 : ',\
              singapore_p
d_uae = '<img src="img/UAE.png"><br><b>UAE</b><br>',\
        '확진자 :',\
        uae_t,\
        '<br>',\
        '총인구 : ',\
        uae_p
d_qatar = '<img src="img/Qatar.png"><br><b>Qatar</b><br>',\
          '확진자 :',\
          qatar_t,\
          '<br>',\
          '총인구 : ',\
          qatar_p
d_turkey = '<img src="img/Turkey.png"><br><b>Turkey</b><br>',\
           '확진자 :',\
           turkey_t,\
           '<br>',\
           '총인구 : ',\
           turkey_p
d_russia = '<img src="img/Russia.png"><br><b>Russia</b><br>',\
           '확진자 :',\
           russia_t,\
           '<br>',\
           '총인구 : ',\
           russia_p
d_Kazakhstan = '<img src="img/Kazakhstan.png"><br><b>Kazakhstan</b><br>',\
               '확진자 :',\
               kazakhstan_t,\
               '<br>',\
               '총인구 : ',\
               kazakhstan_p
d_Uzbekistan = '<img src="img/Uzbekistan.png"><br><b>Uzbekistan</b><br>',\
               '확진자 :',\
               uzbekistan_t,\
               '<br>',\
               '총인구 : ',\
               uzbekistan_p
d_usa = '<img src="img/usa.png"><br><b>USA</b><br>',\
        '확진자 :',\
        usa_t,\
        '<br>',\
        '총인구 : ',\
        usa_p,
d_canada = '<img src="img/canada.png"><br><b>Canada</b><br>',\
           '확진자 :',\
           canada_t,\
           '<br>',\
           '총인구 : ',\
           canada_p
d_poland = '<img src="img/Poland.png"><br><b>Poland</b><br>',\
           '확진자 :',\
           poland_t,\
           '<br>',\
           '총인구 : ',\
           poland_p
d_uk = '<img src="img/UK.png"><br><b>UK</b><br>',\
       '확진자 :',\
       uk_t,\
       '<br>',\
       '총인구 : ',\
       usa_p
d_netherland = '<img src="img/Netherlands.png"><br><b>Netherland</b><br>',\
               '확진자 :',\
               netherland_t,\
               '<br>',\
               '총인구 : ',\
               netherland_p
d_france = '<img src="img/France.png"><br><b>France</b><br>',\
           '확진자 :',\
           france_t,\
           '<br>',\
           '총인구 : ',\
           france_p
d_germany = '<img src="img/germany.png"><br><b>Germany</b><br>',\
            '확진자 :',\
            germany_t,\
            '<br>',\
            '총인구 : ',\
            germany_p

### 국가별 확진자 시각화
kkk = folium.Choropleth(
    geo_data='data/hot_country.json',
    data=worldcorona_data,
    columns=['country_name','active_cases','population'],
    key_on="feature.properties.name",
    fill_color="Dark2",
    fill_opacity=0.5,
    line_opacity=0.1,
    legend_name="World Corona",
    highlight=True,
    reset=False,
).add_to(m)


## geojson 적용
folium.GeoJson(geo_canada,
               style_function=lambda x:style1,
               tooltip = d_canada,
               # tooltip=folium.features.GeoJsonTooltip(fields=['name'])
               ).add_to(m)
folium.GeoJson(geo_usa,
               name='usa',
               style_function=lambda x:style2,
               tooltip=d_usa,
               ).add_to(m)
folium.GeoJson(geo_uk,
               name='uk',
               style_function=lambda x:style2,
               tooltip=d_uk,
               ).add_to(m)
folium.GeoJson(geo_france,
               name='france',
               style_function=lambda x:style2,
               tooltip=d_france,
               ).add_to(m)
folium.GeoJson(geo_poland,
               name='poland',
               style_function=lambda x:style2,
               tooltip=d_poland,
               ).add_to(m)
folium.GeoJson(geo_germany,
               name='germany',
               style_function=lambda x:style2,
               tooltip=d_germany,
               ).add_to(m)
folium.GeoJson(geo_netherland,
               name='netherland',
               style_function=lambda x:style2,
               tooltip=d_netherland,
               ).add_to(m)
folium.GeoJson(geo_turkey,
               name='turkey',
               style_function=lambda x:style2,
               tooltip=d_turkey,
               ).add_to(m)
folium.GeoJson(geo_qatar,
               name='qatar',
               style_function=lambda x:style2,
               tooltip=d_qatar,
               ).add_to(m)
folium.GeoJson(geo_uae,
               name='uae',
               style_function=lambda x:style2,
               tooltip=d_uae,
               ).add_to(m)
folium.GeoJson(geo_kazakhstan,
               name='kazakhstan',
               style_function=lambda x:style2,
               tooltip=d_Kazakhstan,
               ).add_to(m)
folium.GeoJson(geo_uzbekistan,
               name='uzbekistan',
               style_function=lambda x:style2,
               tooltip=d_Uzbekistan,
               ).add_to(m)
folium.GeoJson(geo_russia,
               name='russia',
               style_function=lambda x:style2,
               tooltip=d_russia,
               ).add_to(m)
folium.GeoJson(geo_china,
               name='china',
               style_function=lambda x:style_china,
               tooltip=d_china,
               ).add_to(m)
folium.GeoJson(geo_korea,
               name='korea',
               style_function=lambda x:style2,
               tooltip=d_korea,
               ).add_to(m)
folium.GeoJson(geo_japan,
               name='japan',
               style_function=lambda x:style2,
               tooltip=d_japan,
               ).add_to(m)
folium.GeoJson(geo_thailand,
               name='thailand',
               style_function=lambda x:style2,
               tooltip=d_thailand,
               ).add_to(m)
folium.GeoJson(geo_vietnam,
               name='vietnam',
               style_function=lambda x:style2,
               tooltip=d_vietnam,
               ).add_to(m)
folium.GeoJson(geo_philippines,
               name='philippines',
               style_function=lambda x:style2,
               tooltip=d_philippines,
               ).add_to(m)
folium.GeoJson(geo_indonesia,
               name='indonesia',
               style_function=lambda x:style2,
               tooltip=d_indonesia,
               ).add_to(m)
# folium.GeoJson(geo_singapore,
#                name='singapore',
#                style_function=lambda x:style2,
#                ).add_to(m)

### landmark 마커생성
###  마커 군집화
mc = MarkerCluster().add_to(m)

# usa
land_usa1 = '<img src="landmark/나이아가라.png">'
land_usa2 = '<img src="landmark/그랜드캐니언.jpg">'
land_usa3 = '<img src="landmark/자유의여신상.jpg">'
land_usa4 = '<img src="landmark/러시모어.jpg">'

folium.Marker(location = [43.08303558635485, -79.07361573121621],
              icon = folium.Icon(color='orange', icon='heart', draggable=False),
              tooltip= land_usa1).add_to(mc)
folium.Marker(location = [36.16711590000854, -112.1068011771472],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_usa2).add_to(mc)
folium.Marker(location = [40.68938767778527, -74.0438781292954],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_usa3).add_to(mc)
folium.Marker(location = [43.87937314706051, -103.45845515804322],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_usa4).add_to(mc)
# canada
land_canada1 = '<img src="landmark/벤프국립공원.jpg">'

folium.Marker(location = [51.50674044666477, -115.86886813643909],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_canada1).add_to(mc)

# china
land_china1 = '<img src="landmark/만리장성.jpg">'
land_china2 = '<img src="landmark/자금성.png">'
ddd = folium.Html('<h>만리장성</h>')
folium.Marker(location = [41, 116],
              icon = folium.Icon(color='orange',opacity=0.5, icon='heart'),
              tooltip= land_china1).add_to(mc)
folium.Marker(location = [39.91715309794264, 116.39116015163518],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_china2).add_to(mc)

# russia
land_russia1 = '<img src="landmark/붉은광장.jpg">'
folium.Marker(location = [55.7540902775089, 37.62118123641891],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_russia1).add_to(mc)

# japan
land_japan1= '<img src="landmark/오사카성.jpg">'
land_japan2= '<img src="landmark/교토.jpg">'

folium.Marker(location = [34.68708808816008, 135.52620554780017],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_japan1).add_to(mc)
folium.Marker(location = [35.02912746518446, 135.76625947182552],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_japan2).add_to(mc)

# turkey
land_turkey1= '<img src="landmark/파묵칼레.jpg">'

folium.Marker(location = [37.92416635341453, 29.126017878505987],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_turkey1).add_to(mc)

# france
land_france1= '<img src="landmark/에펠탑.jpg">'
land_france2= '<img src="landmark/몽상미셀.jpg">'

folium.Marker(location = [48.858567723716206, 2.2948675365478857],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_france1).add_to(mc)
folium.Marker(location = [48.63607233087017, -1.5112825611030036],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_france2).add_to(mc)

# poland
land_poland1= '<img src="landmark/소금광산.jpg">'
land_poland2= '<img src="landmark/자코파네.jpg">'

folium.Marker(location = [49.9836073757427, 20.05418263809784],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_poland1).add_to(mc)
folium.Marker(location = [49.27273417653909, 19.995503473462414],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_poland2).add_to(mc)

# germany
land_germany1= '<img src="landmark/브란덴부르크.jpg">'
land_germany2= '<img src="landmark/노이슈반스타인.jpg">'
land_germany3= '<img src="landmark/쾰른.jpg">'

folium.Marker(location = [52.516437801596645, 13.377940132959507],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_germany1).add_to(mc)
folium.Marker(location = [47.55775498747499, 10.750261738360392],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_germany2).add_to(mc)
folium.Marker(location = [50.94420918652306, 6.9577033523929135],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_germany3).add_to(mc)
# uk
land_uk1 = '<img src="landmark/런던.jpg">'
folium.Marker(location = [51.51787751599378, -0.12975699730052495],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_uk1).add_to(mc)
# kazakhstan
land_kazakhstan = '<img src="landmark/이멜공원.jpg">'
folium.Marker(location = [44.0040107826841, 78.83787816190217],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_kazakhstan).add_to(mc)
# uzbekistan
land_uzbekistan = '<img src="landmark/부하라.jpg">'
folium.Marker(location = [39.778208343895905, 64.4137167434066],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_uzbekistan).add_to(mc)

# thailand
land_thailand = '<img src="landmark/왓아룬.jpg">'
folium.Marker(location = [13.74470047625937, 100.49143704753398],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_thailand).add_to(mc)

# philippines
land_philippines = '<img src="landmark/세부.jpg">'
folium.Marker(location = [10.32185587275577, 123.88320189634042],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_philippines).add_to(mc)

# vietnam
land_vietnam = '<img src="landmark/할롱만.jpg">'
folium.Marker(location = [20.917229393531578, 107.19116776304557],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_vietnam).add_to(mc)

# indonesia
land_indonesia = '<img src="landmark/발리.jpg">'
folium.Marker(location = [-8.348670435338866, 115.09347680413913],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_indonesia).add_to(mc)

# singapore
land_singapore = '<img src="landmark/싱가폴.jpg">'
folium.Marker(location = [1.3654804612546823, 103.86758597372247],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_singapore).add_to(mc)

# uae
land_uae = '<img src="landmark/두바이.jpg">'
folium.Marker(location = [25.201324368489423, 55.27645817142001],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_uae).add_to(mc)

# qatar
land_qatar = '<img src="landmark/도하.jpg">'
folium.Marker(location = [25.292678951628965, 51.563002513887355],
              icon = folium.Icon(color='orange', icon='heart'),
              tooltip= land_qatar).add_to(mc)





### 버튼 만들기 
JsButton(
    title='<i class="button"></i>',function="""
 
    function(btn, map) {
        alert('ddd');
        btn.state('zoom-to-forest');
    }
    """).add_to(m)

### 맵 생성 및 저장
m.save('map.html')

