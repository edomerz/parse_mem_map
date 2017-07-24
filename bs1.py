import requests
import bs4
import re

# res = requests.get('file:///D:/SVN/VF2_946/PROJECT_FILES/VFII/debug/VF2.htm#[75]')
# res.raise_for_status()
'''
https://stackoverflow.com/questions/866000/using-beautifulsoup-to-find-a-html-tag-that-contains-certain-text

pattern = re.compile(r'cool')

pprint(soup.find(text=pattern).__dict__)
#>> {'next': u'\n',
#>>  'nextSibling': None,
#>>  'parent': <h2>this is cool #12345678901</h2>,
#>>  'previous': <h2>this is cool #12345678901</h2>,
#>>  'previousSibling': None}

print soup.find('h2')
#>> <h2>this is cool #12345678901</h2>
print soup.find('h2', text=pattern)
#>> this is cool #12345678901
print soup.find('h2', text=pattern).parent
#>> <h2>this is cool #12345678901</h2>

for elem in soup(text=re.compile(r' #\S{11}')):
    print elem.parent
'''


res = open('VF2.htm', 'r')
text = res.read()

# soup = bs4.BeautifulSoup(text)
soup = bs4.BeautifulSoup(text, "lxml")
# print(type(soup))

strongs = soup.select('p strong')
# pattern = re.compile('Init_exec()')
pattern = re.compile('GetSocket()')

# ps = soup.find_all("p")
# print('\nps: ', ps)

strongs = soup.find_all("strong")
# print('\nstrongs: ', strongs)

for i in range(len(strongs)):
    # func = strongs[i].find("a", string="Init_exec()")
    # print(strongs[i])
    func = strongs[i].find(string=pattern)
    if(func):
        print(type(func), func)
        print(func.parent)
        print(func.parent.next_sibling)
        print(func.parent.next_sibling.next_sibling)
        print(func.parent.next_sibling.next_sibling.next_sibling)
        print(func.parent.next_sibling.next_sibling.next_sibling.next_sibling)
        # print(func.parent.next_sibling.next_sibling.next_sibling.next_sibling.child)
        # print('----------------')
        # print(func.next_element)
        # print(func.next_element.next_element)
        # print(func.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
        # print(func.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)
        print('----------------')
        print(func.parent.parent)
        # print(func.parent.parent.next_sibling)
        # print(func.parent.parent.next_sibling.next_sibling)
        # print(func.parent.parent.next_sibling.next_sibling.next_sibling)
        print(func.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling)
        print(func.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling)

        ul = func.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
        for i in ul.find_all("li"):
            # print(i, type(i), i.getText())
            print(i.getText())
        
        print('----------------')
        ul = ul.next_sibling
        calledPattern = re.compile(r'[Called By]')
        while(ul):
            if(ul.string and calledPattern.search(ul.string)):
                print(ul)
                break
            else:
                ul = ul.next_sibling

        print('\nul: ', ul)
        ul = ul.next_sibling
        print('\nul: ', ul)
        for i in ul.find_all("li"):
            # print(i, type(i), i.getText())
            print(i.getText())
        
        # print(ul.next_sibling.next_sibling)
        # print(ul.next_sibling.next_sibling.next_sibling, type(ul.next_sibling.next_sibling.next_sibling))       #[Called By] <class 'bs4.element.NavigableString'>
        

# print(func.parent.parent)
# print(func.parent.parent.parent)

# for i in range(1,10):
#     print(strongs[i])

# funcs = soup.select('a[name]')
# for i in range(1, 10):
#     print(funcs[i].attrs)

# func = soup.select('p[name*="1e6"]')
# print(func)
# print(func.parent.string)

