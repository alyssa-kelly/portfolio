## The Problem
While working on a data analysis project about streaming services, I encountered subsets of [IMDb data](https://www.imdb.com/interfaces/). I found that many values did not match the current information on IMDb's website, and sought another way to collect data on the ratings of popular movies and TV shows.

## My Solution
I first explored the Rotten Tomatoes site and found that using their search tool with certain parameters gave me the list of titles I was looking for (top 150 movies and top 150 TV shows for various platforms). I could easily parse the title, audience, and critic scores for each search listing. However, I also wanted genre and release year and had to go a step farther. I used nested for loops to iterate over each search page: opening the individual page for each movie/show and then parsing genre and release year from that page's code.

I used **BeautifulSoup** for the web scraping aspects of these scripts and **Pandas** to append the parsed information to a dataframe. I wrote an additional script to combined my separate dataframes into one, and then write them to a csv. Finally, I analyzed the data in SQL and used Tableau to create relevant data visualizations.

note: Ideally, I would use a single script to scrape all info from the 6 urls. However, I found that separating my scripts by streaming platform allowed me to more easily identify and troubleshoot bugs.
  
## The Results
* [Click here](https://docs.google.com/presentation/d/12uD64NjnHPpyrmea9Ch7E4vKM-MxSHM9V_UYIIaLUak/edit?usp=sharing) to see my group's analysis!
* In the folder above, I've included the csv of my scraped data and the sql queries I used to transform the data.
