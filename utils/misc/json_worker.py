import json
import os


async def get_user_phrases(user_id: str) -> list:
    with open(f'data/users/{user_id}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['phrases']


async def add_user_phrase(user_id: str, phrase: str) -> None:
    with open(f'data/users/{user_id}.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data['phrases'].append(phrase)
        file.seek(0)
        json.dump(data, file)
        file.truncate()


async def add_user(user_id: str) -> None:
    with open(f'data/users/{user_id}.json', 'w', encoding='utf-8') as file:
        json.dump({"phrases": []}, file)


async def delete_user(user_id: str) -> bool:
    for userfile in os.listdir('data/users'):
        if userfile.startswith(user_id):
            os.remove(f'data/users/{user_id}.json')
            return True

    return False


async def validate_user(user_id: str) -> bool:
    for userfile in os.listdir('data/users'):
        if userfile.startswith(user_id):
            return True

    return False
