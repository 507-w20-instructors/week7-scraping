
# scrapehello.py

from bs4 import BeautifulSoup

f = open("hello4.html")
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

print("RESULTS OF find_all()")
print("soup.find_all('li'):", all_list_items)
print("------")
print("soup.find_all('div'):", all_divs)
print('------')
print("soup.find_all('li', class_='french'):", all_french_list_items)
print("------")
print("soup.find_all(id='hello-list'):", all_hello_elements)
print("------")


print("TYPE OF LIST ELEMENTS RETURNED BY find_all()")
print(type(all_list_items[0]))
print('------')

print("EXTRACTING STRINGS FROM LIST ITEMS AND PRINTING THEM UPPERCASE")
for li in all_list_items:
    print(li.string.upper(), type(li.string))
print('------')

print("EXAMINING THE CHILDREN OF THE 'HELLO' LIST")
for child in all_hello_elements[0].contents:
    print(child)
    print(type(child))
    print('------')

print("USING strip() TO GET RID OF WHITESPACE")
print(all_hello_elements[0].contents[0].strip())
print('------')

print("ITERATING THROUGH ITEMS IN A LIST")
hello_list_items = all_hello_elements[0].find_all('li')
for item in hello_list_items:
    print(item.text.strip())
print('------')

print("USING find() INSTEEAD OF find_all()")
hello_div = soup.find(id='hello-list')
print(hello_div)
print('------')

print("ACCESSING TAG ATTRIBUTES")
img_tag = soup.find('img')
print('The img source:')
print(img_tag['src'])
print('------')


