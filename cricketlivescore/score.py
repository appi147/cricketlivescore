import feedparser
def get():
	scores = feedparser.parse('http://static.espncricinfo.com/rss/livescores.xml')
	return scores.entries
