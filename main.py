import os
from scrapper import Scrapper
from urllib.request import Request, urlopen

link = "https://www.google.com/search?q=shetland+dog&tbm=isch&ved=2ahUKEwjz4ZHM-6H8AhWrtIsKHR8fDp4Q2-cCegQIABAA&oq=" \
             "shetland+dog&gs_lcp=CgNpbWcQAzIFCAAQgAQyBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBAgAEB4yBggAEAUQHjIGCAAQBRA" \
             "eMgYIABAFEB46BAgjECc6BAgAEEM6BwgAELEDEEM6CAgAELEDEIMBOggIABCABBCxA1C1CVi5FmC6GGgAcAB4AIABc4gB8gmSAQM5LjSYAQCg" \
             "AQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=Ei2vY_OQMqvprgSfvrjwCQ&bih=754&biw=1536&rlz=1C1GCEB_enPL898PL898"


scrapper = Scrapper("chromedriver.exe", link)
scrapper.start_scrapping()
div_elements = scrapper.get_div_with_img()

img_catalog_path = "images\\"
try:
    os.mkdir(img_catalog_path)
except FileExistsError:
    pass

imgs = []

for i in range(len(div_elements)):
    img = div_elements[i].contents[1].contents[0].contents[0]
    imgs.append(img)

img_links = []
for i in range(len(imgs)):
    attrs = imgs[i].attrs
    if 'src' in attrs.keys():
        img_link = attrs['src']
    else:
        img_link = attrs['data-src']
    img_links.append(img_link)

for i in range(len(img_links)):
    if img_links[i] != "" and img_links[i] is not None:
        req = Request(img_links[i], headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        with open(img_catalog_path + str(i) + '.jpg', 'wb') as image_writer:
            image_writer.write(webpage)


