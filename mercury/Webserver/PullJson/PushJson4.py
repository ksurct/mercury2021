import urllib



post_data = [('name','Gladys'),]     # a sequence of two element tuples
result = urlopen('http://example.com', urllib.urlencode(post_data))
content = result.read()