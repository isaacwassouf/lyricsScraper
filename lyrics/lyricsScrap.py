import requests
from bs4 import BeautifulSoup,Comment

def get_lyrics(artist,song):
    try:
        artist =artist.lower().replace(' ','')
        song = song.lower().replace(' ','').replace('.','')
        print(artist,song)
        link = 'https://www.azlyrics.com/lyrics/'+artist+'/'+song+'.html'
        print(link)
        response= requests.get(link)
        soup =  BeautifulSoup(response.text,'html.parser')
        if (soup.find(class_='feat') is None):
            lyrics_div = soup.find(class_='ringtone').find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
        else:
            lyrics_div= soup.find(class_='feat').find_next_sibling().find_next_sibling().find_next_sibling()
        
        for element in lyrics_div(text=lambda text: isinstance(text, Comment)):
            element.extract()

        lyrics_div= str(lyrics_div)
        lyrics_div= lyrics_div.replace('<div>','').replace('</div>','').replace('<br/>','').replace('<i>','').replace('</i>','')
        return lyrics_div

    except AttributeError :
        print('no artist or song of which exists')
