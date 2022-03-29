import requests
url = 'https://tradeit.gg/api/v2/inventory/data?gameId=730&offset=0&limit=250&sortType=Popularity&searchValue=&minPrice=0&maxPrice=100000&minFloat=0&maxFloat=1&fresh=true'
data = requests.get(url)