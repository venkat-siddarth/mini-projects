import pyshorteners
url=input("enter the url:")
shortner=pyshorteners.Shortener()
a=shortner.tinyurl.short(url)
print(a)