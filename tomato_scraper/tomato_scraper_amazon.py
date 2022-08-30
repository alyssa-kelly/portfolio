import pandas as pd
import requests
from bs4 import BeautifulSoup

print('working')

# set up
site = 'https://www.rottentomatoes.com'
df = pd.DataFrame(columns = ['service', 'type', 'title', 'year', 'genre', 'critic_score', 'audience_score'])
super_list = [['https://www.rottentomatoes.com/browse/tv_series_browse/affiliates:amazon_prime~audience:upright~critics:fresh~sort:popular?page=5', 'Amazon Prime', 'TV Show'],
['https://www.rottentomatoes.com/browse/movies_at_home/affiliates:amazon_prime~audience:upright~critics:fresh~sort:critic_popular?page=5', 'Amazon Prime', 'Movie']]


# loops through all search pages in super list
for item in super_list:
    URL = item[0]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', attrs={'class' : 'discovery-grids-container'})
    a_class = results.find_all('a')
    link_list = []
    
    # creates list of urls for all search results on page
    for each in a_class:
        entry_link = site + each['href']
        link_list.append(entry_link)
    
    # scrapes content if using TV show pages
    if item[2] == 'TV Show':
        for link in link_list:
            URL = link
            page = requests.get(URL)
            entry = BeautifulSoup(page.content, 'html.parser')
            title = ((entry.find('title')).text).removesuffix(' - Rotten Tomatoes')
            if title is None:
                title = 'name error'
            
            # prints to track status
            print('service : {0}, type : {1}, title: {2}'.format(item[1], item[2], title)) 
            
            release_date = entry.find(attrs={'data-qa' : 'series-details-premiere-date'})
            if release_date is None:
                release_date = 'unknown'
                year = 'unknown'
            else:
                release_date = release_date.text
                year = release_date[7:]
            genre = entry.find(attrs={'data-qa' : 'series-details-genre'})
            if genre is None:
                genre = 'unknown'
            else:
                genre = genre.text
            critic_score = entry.find(attrs={'data-qa' : 'tomatometer'})
            if critic_score is None:
                critic_score = 'unknown'
            else:
                critic_score = critic_score.text
            audience_score = entry.find(attrs={'class' : 'mop-ratings-wrap__percentage', 'data-qa' : 'audience-score'})
            if audience_score is None:
                audience_score = 'no audience ratings'
            else: 
                audience_score = audience_score.text
            
            # creating new row for dataframe
            new_row = {'service' : item[1], 'type' : item[2], 'title' : title, 'year' : year, 'genre' : genre, 'critic_score' : critic_score.strip(), 'audience_score' : audience_score.strip()}
            df = df.append(new_row, ignore_index = True)
                
    # scrapes content if using movie pages:
    else:
        for link in link_list:
            URL = link
            page = requests.get(URL)
            entry = BeautifulSoup(page.content, 'html.parser')
            title = entry.find(attrs={'data-qa' : 'score-panel-movie-title'})
            if title is None:
                title = 'name error'
            else:
                title = title.text
            
            # prints to track status
            print('service : {0}, type : {1}, title: {2}'.format(item[1], item[2], title)) 
            
            details = entry.find('p', attrs={'slot' : 'info', 'class' : 'scoreboard__info'})
            if details is None:
                details = 'unknown'
                year = 'unknown'
                genre = 'unknown'
            else:
                details = (details.text).split(', ')
                year = details[0]
                genre = details[1]
            critic_score = entry.find('score-board')['tomatometerscore']
            if critic_score is None:
                critic_score = 'no critic ratings'
            audience_score = entry.find('score-board')['audiencescore']
            if audience_score is None:
                audience_score = 'no audience ratings'

            # creating new row for dataframe
            new_row = {'service' : item[1], 'type' : item[2], 'title' : title, 'year' : year, 'genre' : genre, 'critic_score' : critic_score.strip(), 'audience_score' : audience_score.strip()}             
            df = df.append(new_row, ignore_index = True)

print('dataframe created')
df.to_csv('/Users/alyssa/Desktop/data_analysis/project/rotten_tomatoes_amazon.csv', sep=',', index=False) 
print('dataframe written to csv. done!')