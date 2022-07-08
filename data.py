import requests

parameters = {
    'amount': 10,
    'type': 'boolean',
}

trivia_api = requests.get('https://opentdb.com/api.php', params=parameters)
trivia_api.raise_for_status()

question_data = trivia_api.json()['results']
