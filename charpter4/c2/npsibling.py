html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
print("siblings:")
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))
print("parent:")
print(list(enumerate(soup.a.parents)))
print(list(enumerate(soup.a.parent)))