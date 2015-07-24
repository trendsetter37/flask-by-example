
def sanitize(url):
	protocol = 'http://'	# 7
	protocol1 = 'https://'	# 8

	if url[0:7] == protocol or url[0:8] == protocol1:
		return True
	else:
		return False