from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = ''
    with open('dongche.html', encoding='UTF-8') as f:
        html = f.read()
    bs = BeautifulSoup(html, 'html.parser')
    all_car = bs.find('ol', class_='tw-mt-12').find_all('li', class_='list_item__3gOKl')
    cars=[]
    for car in all_car:
        price = car.find('p', class_='tw-leading-22').string
        name = car.find('div', class_='tw-leading-28 tw-h-28 tw-truncate').find('a').string
        print()
