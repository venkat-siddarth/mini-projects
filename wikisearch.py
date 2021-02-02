import wikipedia
x=input("What do you want to know?")
data=wikipedia.page(x)
print(data.summary)