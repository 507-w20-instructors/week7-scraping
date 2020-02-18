
# scrapehello.py

from bs4 import BeautifulSoup

f = open("hello3.html")
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')
# print(soup.prettify())

# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye')

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')

print('list items:', all_list_items)
print('------')
print('divs:', all_divs)
print('------')
print('goodbye elements:', all_goodbye_elements)
print('------')
print('french stuff:', all_french_list_items)
print('------')
print('hello id elements:', all_hello_elements)
print('------')

print(type(all_list_items[0]))
print('------')

for li in all_list_items:
    print(li.string, type(li.string))
    print(li.string.upper())

print('------')

for child in all_hello_elements[0].contents:
    print(child)
    print(type(child))
    print('------')

print('------')
print(all_hello_elements[0].contents[0].strip())
print('------')

print('------')
hello_div = soup.find(id='hello-list')
print('------')

for child in hello_div.contents:
    print(child)
    print(type(child))
    print('------')

print('------')
print(hello_div.contents[0].strip())
print('------')

img_tag = soup.find('img')
print('The img source:')
print(img_tag['src'])
print('------')


