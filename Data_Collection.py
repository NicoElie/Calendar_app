"""
This part of the code is responsible for importing the class schedules from the University of Illinois website

"""
# importing request
import requests
# importing the BeautifulSoup library#
from bs4 import BeautifulSoup

# We get the main url for uploading the class schedules
page = requests.get('https://courses.illinois.edu/schedule/DEFAULT/DEFAULT')
# --------------------------check for successful request--------------------------------------------------------------#
if page:
    soup = BeautifulSoup(page.text, 'html.parser')
    print("Request successful")
else:
    print("Request Failed")
# ----------------------------------get department links------------------------------------------------------------#
dep_links = []  # all the links for each department will be stored in this list
dep_name = soup.find(class_='table-responsive')  # where the data to collect are stored in the website
name_links = dep_name.find_all('a')  # tag to signify that it is a link
for name in name_links:
    dep_links.append('https://courses.illinois.edu' + name.get('href'))
print(len(dep_links))  # there is 187 links in our list
# -------------------------------Based on Departments links, get courses links---------------------------------------#
# -----------------------------------------links from 0 to 10--------------------------------------------------------#
class_links = []  # all the links for each class will be stored here
i = 0
while i < 10:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ----------------------------------------------links from 10 t0 20 --------------------------------------------------#
i = 10
while i < 20:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ----------------------------------------------links from 20 t0 30 --------------------------------------------------#
i = 20
while i < 30:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -------------------------------------------from 30 t0 40-------------------------------------------------------#
i = 30
while i < 40:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# --------------------------------------------from 40 t0 50-------------------------------------------------------#
i = 40
while i < 50:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ------------------------------------------------from 50 t0 60----------------------------------------------------#
i = 50
while i < 60:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ------------------------------------------from 60 t0 70--------------------------------------------------------#
i = 60
while i < 70:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -----------------------------------------------from 70 t0 80----------------------------------------------------#
i = 70
while i < 80:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')   # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ---------------------------------------------------from 80 t0 90---------------------------------------------------#
i = 80
while i < 90:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -------------------------------------------------from 90 t0 100---------------------------------------------------#
i = 90
while i < 100:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ------------------------------------------------from 100 t0 110--------------------------------------------------#
i = 100
while i < 110:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -----------------------------------------from 110 t0 120---------------------------------------------------------#
i = 110
while i < 120:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -------------------------------------------from 120 t0 130-----------------------------------------------------#
i = 120
while i < 130:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ---------------------------------------------from 130 t0 140----------------------------------------------------#
i = 130
while i < 140:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -------------------------------------------from 140 t0 150-------------------------------------------------------#
i = 140
while i < 150:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -------------------------------------------from 150 t0 160--------------------------------------------------------#
i = 150
while i < 160:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -----------------------------------------from 160 t0 170-------------------------------------------------------#
i = 160
while i < 170:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# ---------------------------------------from 170 t0 180----------------------------------------------------------#
i = 170
while i < 180:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))
# -----------------------------------from 180 t0 187-------------------------------------------------------------#
i = 180
while i < 187:
    page_1 = requests.get(dep_links[i])
    soup_1 = BeautifulSoup(page_1.text, 'html.parser')
    class_name = soup_1.find(id='default-dt')  # where the data are
    l = class_name.find_all('a')  # tag for links
    i += 1
    for name in l:
        class_links.append('https://courses.illinois.edu' + name.get('href'))