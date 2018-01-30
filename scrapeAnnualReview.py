import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import re
import webbrowser
from selenium import webdriver

def similarUrl(url):
	try:
		x = url.find("/pdf/")
		if "/pdf/" in url:
			url = url[:x] + url[x+4:]
	except:
		pass

	try:
		y = url.find("/pdf/")
		if "/abs/" in url:
			url = url[:y] + url[y+4:]
	except:
		pass

	try:
		z = url.find("/full/")
		if "/full/" in url:
			url = url[:z] + url[z+5:]
	except:
		pass
	return url

#x = similarUrl(input("Enter URL"))
#print (x)

browser = webdriver.Chrome()
html = urllib.request.urlopen("http://www.annualreviews.org/action/showPublications")
soup = bs(html, 'lxml')
lst = list()
tags = soup('a')
for tag in tags:
	try:
		if "journal" in tag.get('href', None):
			lst.append(tag.get('href', None))
	except:
		pass
#	lst.append(tag.get('href', None))
#	print(tag.get('href', None))
print(lst)

file = open("AnnualReview.txt","a")
#----------------------#-------------------------#------------------------#---------
for elm in lst:
	url = "http://www.annualreviews.org" + elm
	browser.get(url)
	innerHTML = browser.execute_script("return document.body.innerHTML")
	soup = bs(innerHTML, 'lxml')
	lst2 = list()
	tags = soup('a')
	for tag in tags:
		x= tag.get('href', None)
		try:
			if "toc" in x and x not in lst2:
				lst2.append(x)
		except:
			pass
	print(lst2)
	for elm2 in lst2:
		url = "http://www.annualreviews.org" + elm2
		browser.get(url)
		innerHTML = browser.execute_script("return document.body.innerHTML")
		soup = bs(innerHTML, 'lxml')
		lst3 = list()
		tags = soup('a')
		for tag in tags:
			x= tag.get('href', None)
			try:
				if "doi" in x and "#f" not in x:
					x = similarUrl(x)
					try:
						if lst3[-1]==x or lst3[-2]==x:
							continue
						else:
							lst3.append(x)
					except:
						lst3.append(x)
#						lst3.append(x)
#				for i in ["pdf", "#f", "full"]:
#					if i not in x:
#				lst2.append(x)
				
			except:
				pass
	print(lst3)
	for newElm in lst3:
		file.write("<a href = http://www.annualreviews.org" + newElm + ">" + 'http://www.annualreviews.org' + newElm + "</a>  <br>")

driver.close()
#file.write("http://www.annualreviews.org" + tag.get('href', None))
#file = open("AnnualReview.html","w")


#lstn = list()
#n=0
#for elm in bst:
#	n= n+1
#	if n>1:
#		break
#	html = urllib.request.urlopen("http://www.annualreviews.org" + elm)
#	print(html)
#	for line in html:
#		file.write(line.decode())
#		print(line.decode())
#	print("http://www.annualreviews.org" + elm)
#	soup = bs(html, 'lxml')
#	lst2 = list()
#	tags = soup('a')
#	for tag in tags:
#		try:
#			if "doi" in tag.get('href', None):
#				lst2.append(tag.get('href', None))
#		except:
#			pass
#	print(lst2)
#	lstn[n] = lst2
#	n=n+1
#print(lst2)

#print(sorted(bst))
#print(tags)
#print(html)
#print(soup)