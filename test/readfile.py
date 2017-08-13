
file=open('cookies.txt')
key=[]
value=[]
for line in file:
	a,b=line.split(';')
	key.append(a)
	value.append(b)
cookies=dict(zip(key,value))
print cookies

order=hot&cat=%E6%B5%81%E8%A1%8C&limit=35&offset=35
http://music.163.com/#/discover/playlist/?order=hot&cat=%E6%B5%81%E8%A1%8C&limit=35&offset=1330
User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36
