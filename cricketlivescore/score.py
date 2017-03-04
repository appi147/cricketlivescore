import feedparser
def get():
	scores = feedparser.parse('http://static.espncricinfo.com/rss/livescores.xml')
	for i in range(len(scores.entries)):
		print scores.entries[i].title