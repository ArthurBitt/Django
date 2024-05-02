import requests


GOOGLE_BOOKS_API_KEY = "AIzaSyA_9AOK8HwBguKX86CwdcVyMbpKtgqjUZE"
GOOGLE_BOOKS_API_BASE_URL = "https://www.googleapis.com/books/v1/volumes"

def search_books(query):
    params = {
        'q': query,
        'key': GOOGLE_BOOKS_API_KEY,
        # 'maxResults': 5  # Número máximo de resultados a serem retornados
    }

    response = requests.get(GOOGLE_BOOKS_API_BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        # Cria uma lista para armazenar as informações dos livros tratados
        lista = []
        if 'items' in data:
            for item in data['items']:
                volume_info = item.get('volumeInfo', {})
                book = {
                    'title': volume_info.get('title', 'Sem título'),
                    'authors': volume_info.get('authors', ['Desconhecido']),
                    'publishedDate': volume_info.get('publishedDate', 'Desconhecido'),
                    'publisher': volume_info.get('publisher', 'Desconhecido'),
                    'description': volume_info.get('description', 'Sem descrição'),
                    'pageCount': volume_info.get('pageCount', 'Desconhecido'),
                    'categories': volume_info.get('categories', ['Sem categoria']),
                    'averageRating': volume_info.get('averageRating', 'Sem avaliação'),
                    'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail', 'Sem imagem')
                }

                lista.append(book)
        return lista
    else:
        raise Exception(f'Erro ao retornar os dados: {response.status_code}')


