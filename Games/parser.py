import requests, csv, os
from bs4 import BeautifulSoup
from os import system

system('clear')
dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
       'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'E', 'ё':'e', 'Ж':'Zh', 'ж':'zh',
       'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'I', 'й':'i', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
       'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r',
       'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'h', 'х':'h',
       'Ц':'Tc', 'ц':'tc', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Shch', 'щ':'shch', 'Ы':'Y',
       'ы':'y', 'Э':'E', 'э':'e', 'Ю':'Iu', 'ю':'iu', 'Я':'Ia', 'я':'ia'}

alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
            'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
            'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
            'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']


def get_html(url):
    r = requests.get(url)
    return r.text

def total_page(html):
    soup = BeautifulSoup(html, 'lxml')

    page = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')

    total_page = page.split('=')[1].split("&")[0]

    return int(total_page)

def write_csv(data):
    
    data = (data['title'], data['price'], data['place'], data['url'])

    dictionary_all = os.listdir()
    
    for dictionary in dictionary_all:
        if 'avito.csv' in dictionary:
            #print('works')
            pass


    with open('Games/avito.csv', 'a', encoding='utf8') as f:
        
        write = csv.writer(f)

        write.writerow( data )


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    adv = soup.find_all('div', class_='item_table')

    for ad in adv:
        try:
            title = ad.find('a', class_='item-description-title-link').text.strip()
        except:
            title = ''

        try:
            price = ad.find('span', class_='price').text.strip()
        except:
            price = ''

        try:
            place_all = soup.find_all('div', class_='data')
            for place in place_all:
                place = place.find_all('p')
                place = (place[-1])
                place = place.text
        except:
            place = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''
        data = {'title' : title,
                'price': price,
                'place': place,
                'url': url}

        write_csv(data)

def main():
    
    query = str(input("Введите ваш запрос(/cc): "))

    base_url = 'https://www.avito.ru/'
    page_part = 'p='
    query_part = '&q='
    if '/cc' in query:

        city = str(input("Введите город: "))
        
        result = str()

        for i in range(0, len(city)):
            
            if city[i] in alphabet:
                simbol = dic[city[i]]
            else:
                simbol = city[i]
            result = result + simbol
            result = result.lower()
            #city = result
      

        with open('data.txt', 'w', encoding='utf8') as f:
            f.write(result)
        query = str(input("Введите запрос: "))
    
    else:
        with open('data.txt', 'r', encoding='utf8') as f:
            query_1 = f.read()
        result = query_1
        
    
    page_parse = int(input("Сколько страниц отпрарсить: "))
    
    #if len(page_parse) == 0:
    #    page_parse = int(input("Сколько страниц отпрарсить: "))


    #print(city)
    all_= base_url + result + "?"  + page_part + str(page_parse) + query_part + query
    print("Обрабатываемая ссылка: ",all_)
    
    try:

      total_page_value = total_page(get_html(all_))
      print("Работа выполнена успешно!") 
      
    except AttributeError:
        print("Повторите попытку. ")
        exit()
   
    except ValueError:
        print('Ошибка-рыбка')

    if page_parse > (total_page_value):
        print("su much ")
    
    
    else:
        for i in range(1, page_parse):
            url_get = base_url + result + "?" + page_part + str(i) + query_part + query
            html = get_html(url_get)
            get_data(html)

if __name__ == '__main__':
    main()
