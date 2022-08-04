import feedparser

def parse(url, limit):
    entries = feedparser.parse(url)['entries']
    if limit:
        return(entries[:limit])
    else:
        return(entries)

class news():
    def __init__(self):
        self.url = 'https://feeds.bbci.co.uk/news'

    def all(self, limit=False):
        return(parse(self.url + '/rss.xml', limit=limit))

    def world(self, limit=False):
        return(parse(self.url + '/world/rss.xml', limit=limit))

    def north_america(self, limit=False):
        return(parse(self.url + '/world/us_and_canada/rss.xml', limit=limit))

    def uk(self, limit=False):
        return(parse(self.url + '/uk/rss.xml', limit=limit))

    def entertainment(self, limit=False):
        return(parse(self.url + '/entertainment_and_arts/rss.xml', limit=limit))

    def business(self, limit=False):
        return(parse(self.url + '/business/rss.xml', limit=limit))

    def tech(self, limit=False):
        return(parse(self.url + '/technology/rss.xml', limit=limit))

    def science(self, limit=False):
        return(parse(self.url + '/science_and_environment/rss.xml', limit=limit))
    
    def top_stories(self, edition='int', limit=False):
        return(parse(self.url + f'/rss.xml?edition={edition}', limit=limit))

class sports():
    def __init__(self):
        self.url = 'https://feeds.bbci.co.uk/sport'

    def all(self, limit=False):
        return(parse(self.url + '/rss.xml', limit=limit))

    def cricket(self, limit=False):
        return(parse(self.url + '/cricket/rss.xml', limit=limit))

    def soccer(self, limit=False):
        return(parse(self.url + '/football/rss.xml', limit=limit))

    def tennis(self, limit=False):
        return(parse(self.url + '/tennis/rss.xml', limit=limit))

    def athletics(self, limit=False):
        return(parse(self.url + '/athletics/rss.xml', limit=limit))

    def golf(self, limit=False):
        return(parse(self.url + '/golf/rss.xml', limit=limit))

    def boxing(self, limit=False):
        return(parse(self.url + '/boxing/rss.xml', limit=limit))

    def swimming(self, limit=False):
        return(parse(self.url + '/swimming/rss.xml', limit=limit))

    def cycling(self, limit=False):
        return(parse(self.url + '/cycling/rss.xml', limit=limit))

    def formula1(self, limit=False):
        return(parse(self.url + '/formula1/rss.xml', limit=limit))
    
class weather():
    def forecast(self, city_id, limit=False):
        return(parse('https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/' + str(city_id), limit=limit))