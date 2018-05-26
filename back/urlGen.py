def url_gen(str):
    return "https://www.google.com/search?q=" + str.replace(" ", "+") + "&tbm=nws"

print(url_gen("game"))
print(url_gen("political news"))
