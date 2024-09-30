import json

def get_films(file_path:str='data.json', film_id:int|None=None):
    with open(file_path, 'r') as f:
        films = json.load(f)
        if film_id != None and film_id < len(films):
            return films[film_id]
        return films

    