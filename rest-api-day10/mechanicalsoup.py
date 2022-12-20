import mechanicalsoup

browser=mechanicalsoup.StatefulBrowser()
browser.open("https://steemit.com/")

articlelist=list(browser.get_current_page().find('ul',class_="PostsList__summaries"))[:10]
for child in articlelist:
    user=child.find('span',class_="author").text
    print(user)

    title=child.h2.text
    print(title)



