import requests
import json

class QuizApiClient:
    
    def __init__(self):
        self.api_key =  'HG71NYVt6OdG5QciqJq448lpXhtyhtSa2mXI44gN'
        self.base_url = 'https://quizapi.io/api/v1/questions'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    def get_questions(self, category=None, difficulty=None, limit=None, headers=None):
        params = {'apiKey': self.api_key}
        if category is not None:
            params['category'] = category
        if difficulty is not None:
            params['difficulty'] = difficulty
        if limit is not None:
            params['limit'] = limit

        if headers is None:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    

        headers['X-Api-Key'] = self.api_key

        response = requests.get(self.base_url, params=params, headers=headers)

        return  response.text
    
    



class Question:
    def __init__(self):
        self.id = None
        self.question = None
        self.description = None
        self.answers = {}
        self.multiple_correct_answers = False
        self.correct_answers = {}
        self.explanation = None

    def from_json(self, json_data):
        self.id = json_data.get('id')
        self.question = json_data.get('question')
        self.description = json_data.get('description')
        self.answers = json_data.get('answers', {})
        self.multiple_correct_answers = json_data.get('multiple_correct_answers', False)
        self.correct_answers = json_data.get('correct_answers', {})
        self.explanation = json_data.get('explanation')
        data = json.loads(json_data)
        return [Question(question_data) for question_data in data]




        