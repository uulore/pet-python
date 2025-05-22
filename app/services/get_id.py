from random import randint

used_id = set()

def get_id():
    id = randint(1000, 9999)
    if id in used_id:
        pass
    else:
        used_id.add(id)
    return id