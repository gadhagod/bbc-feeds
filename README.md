# bbc-feeds
[![](https://img.shields.io/pypi/v/bbc-feeds)](https://pypi.org/project/bbc-feeds) \
A python package to get news, weather, and sports from BBC.

## Installation

`pip3 install bbc-feeds`

## Usage
1. Import the library: `import bbc_feeds`
2. Call a class and then a function with `bbc_feeds.news().all()`. In this example news is the class and the function is all. This will return a list of news stories as a dictionary.

### Example
The below example gets the first three stories from the homepage (all) and prints out the story name and summary.
```
import bbc_feeds

stories = bbc_feeds.news().all(limit=3)

for story in stories:
    print(story.title)
    print(story.summary)
```
To get a list of the dictionary keys available use the [`keys()`](https://docs.python.org/3/library/stdtypes.html#dict.keys) function.
## Functions
### News
| Function Name            | Category                | RSS Feed                                                     | Optional Parameters |
|--------------------------|-------------------------|--------------------------------------------------------------|---------------------|
| `news().all()`           | Home                    | http://feeds.bbci.co.uk/news/rss.xml                         | limit               |
| `news().world()`         | World                   | http://feeds.bbci.co.uk/news/world/rss.xml                   | limit               |
| `news().uk()`            | UK                      | http://feeds.bbci.co.uk/news/uk/rss.xml                      | limit               |
| `news().north_america()` | America and Canada      | http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml     | limit               |
| `news().entertainment()` | Entertainment & Arts    | http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml  | limit               |
| `news().business()`      | Business                | http://feeds.bbci.co.uk/news/business/rss.xml                | limit               |
| `news().tech()`          | Technology              | http://feeds.bbci.co.uk/news/technology/rss.xml              | limit               |
| `news().science()`       | Science and Environment | http://feeds.bbci.co.uk/news/science_and_environment/rss.xml | limit               |
| `news().top_stories()`   | Home                    | http://feeds.bbci.co.uk/news/rss.xml?edition=int             | limit <br> edition  |

### Sports
| Function Name          | Category   | RSS Feed                                         | Optional Parameters |
|------------------------|------------|--------------------------------------------------|---------------------|
| `sports().all()`       | Home       | https://feeds.bbci.co.uk/sport/rss.xml           | limit               |
| `sports().cricket()`   | Cricket    | https://feeds.bbci.co.uk/sport/cricket/rss.xml   | limit               |
| `sports().soccer()`    | Soccer     | https://feeds.bbci.co.uk/sport/football/rss.xml  | limit               |
| `sports().football()`  | Football   | https://feeds.bbci.co.uk/sport/football/rss.xml  | limit               |
| `sports().tennis()`    | Tennis     | https://feeds.bbci.co.uk/sport/tennis/rss.xml    | limit               |
| `sports().athletics()` | Athletics  | https://feeds.bbci.co.uk/sport/athletics/rss.xml | limit               |
| `sports().golf()`      | Golf       | https://feeds.bbci.co.uk/sport/golf/rss.xml      | limit               |
| `sports().boxing()`    | Boxing     | https://feeds.bbci.co.uk/sport/boxing/rss.xml    | limit               |
| `sports().swimming()`  | Swimming   | https://feeds.bbci.co.uk/sport/swimming/rss.xml  | limit               |
| `sports().cycling()`   | Cycling    | https://feeds.bbci.co.uk/sport/cycling/rss.xml   | limit               |
| `sports().formula1()`  | Formula1   | https://feeds.bbci.co.uk/sport/formula1/rss.xml  | limit               |         

### Weather
- `weather().forecast(city_id)` (To get your city ID, search for it on the [BBC Weather's Website](https://www.bbc.com/weather)).

All functions have an optional parameter `limit`, where you can limit the number of entries.

## CLI

    Usage: bbc [OPTIONS] COMMAND [ARGS]...

      Get BBC feeds of several categories

    Options:
      --help  Show this message and exit.

    Commands:
      news
      sports
      weather