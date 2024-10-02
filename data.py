import json

def get_films(file_path:str='data.json', film_id:int|None=None):
    with open(file_path, 'r') as f:
        films = json.load(f)
        if film_id != None and film_id < len(films):
            return films[film_id]
        return films

def add_film(film:dict, file_path:str='data.json'):
    film = get_films(file_path=file_path, film_id=None)
    if film:
        films.append(film)
        with open(file_path, 'w') as fp:
            json.dump(films, fp, indent=4, ensure_ascii=False)
