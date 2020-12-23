from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# bs4
from bs4 import BeautifulSoup
import requests
from .serializers import YourSerializer


@api_view(["GET"])
def featureded(request):
    featured = []
    url = "https://www.podbean.com/all"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    featuredpodcasts = soup.find("div", id='featured-podcasts')
    podcasts = featuredpodcasts.findAll("div")
    for podcast in podcasts:
        featuredpodcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        'types' : podcast.find('i').getText(),
        }
        featured.append(featuredpodcast)
        results = YourSerializer(featured, many=True).data
    return Response(results)

@api_view(["GET"])
def comedy(request):
    top = []
    url = "https://www.podbean.com/comedy-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topcomedypodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    
    for podcast in topcomedypodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)
       
    return Response(top)



@api_view(["GET"])
def education(request):
    top = []
    url = "https://www.podbean.com/education-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topeducationpodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in topeducationpodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)


@api_view(["GET"])
def fiction(request):
    top = []
    url = "https://www.podbean.com/fiction-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topfictionpodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in topfictionpodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)


@api_view(["GET"])
def business(request):
    top = []
    url = "https://www.podbean.com/business-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topbusinesspodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in topbusinesspodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)


@api_view(["GET"])
def music(request):
    top = []
    url = "https://www.podbean.com/music-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topmusicpodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in topmusicpodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)


@api_view(["GET"])
def science(request):
    top = []
    url = "https://www.podbean.com/science-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topsciencepodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in topsciencepodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)


@api_view(["GET"])
def sports(request):
    top = []
    url = "https://www.podbean.com/sports-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    topsportspodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in topsportspodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)


@api_view(["GET"])
def technology(request):
    top = []
    url = "https://www.podbean.com/technology-podcasts"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    toptechnologypodcasts = soup.find("ul", class_='ul-list clearfix').findAll('li')
    for podcast in toptechnologypodcasts:
        podcast = {
        'img' : podcast.find('img').get('data-src'),
        'link' : podcast.find('a').get('href'),
        'title' : podcast.find('strong').getText(),
        }
        top.append(podcast)

    return Response(top)
@api_view(["GET"])
def home(request):
    
    return Response('pls work')




# this is going to be the podcast detail 




@api_view(["GET"])
def info(request, link):
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    if  soup.find("div", class_='container') :

        container = soup.find("div", class_='container')

        headerBlock = container.find("div", class_='usersite-header')

        episodes =[]

        
        playlist = soup.find('div', class_='main-panel').find('div' , class_='playlist-panel').findAll('div', class_='entry')
        for episode in playlist:
            durl = episode.find('a' , class_='post_toolbar_download').get('href')
            dpage = requests.get(durl)
            dsoup = BeautifulSoup(dpage.content, 'html.parser')
            dlink = dsoup.find('a', class_='btn btn-ios download-btn').get('href')
            data = {
                'eTitle' : episode.find('h2').getText(),
                'date' : episode.find('span', class_='day').getText(),
                'download' : dlink,
            }
            episodes.append(data)

        datas = {
        'img' : soup.find('table', class_='profileinfo').find('img').get('data-src'),
        'title' : headerBlock.find('h1' , class_='tit').getText(),
        'next' : soup.find('a', class_='next-page').get('href'),
        'episode' : episodes,
        }

    return Response(datas)




















