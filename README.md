# Quizes test work for "Фабрика решений"
This is simple REST API for creating quizzes with questions and give answers. Project include sign up and authentication with JWT.
## How to install
Recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html)
or [conda env](https://conda.io/projects/conda/en/latest/index.html).
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
After requirements was successfully installed use [docker-compose](https://docs.docker.com/):
```
docker-compose up --build
```
Run makemigrations:
```
docker-compose run web python manage.py makemigrations
```
And migrate:
```
docker-compose run web python manage.py migrate
```
For run server:
```
docker-compose up
```
## API
### Signup
POST: /api/v1/signup/
#### Request Example:
```
curl -v -X POST \
-d '{
        "username": "username",
        "email": "example@gmail.com",
        "password": "password"
    }
}' "http://0.0.0.0:8000/api/v1/signup/"
```
#### Response Example:
```
{
    "email": "example@gmail.com",
    "username": "username"
}
```
User was successfully created.
### Login
POST: /api/v1/login/
#### Request Example:
```
curl -v -X POST \
-d '{
        "username": "username",
        "password": "password"
    }
}' "http://0.0.0.0:8000/api/v1/login/"
```
#### Response Example:
```
{
    "username": "username",
    "token": {
        "refresh": "refresh_token",
        "access": "access_token"
    }
}
```
Access token has expired time 60 minutes. To refresh token use:
### Refresh token
POST: /api/v1/token/refresh/
#### Request Example:
```
curl -v -X POST \
-d '{
        "refresh": "refresh_token",
    }
}' "http://0.0.0.0:8000/api/v1/token/refresh/"
```
#### Response Example:
```
{
    "access": "access_token"
}
```
### Create quiz
POST: /api/v1/quiz/create/ \
For admins only
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
-d '{
        "name": "quiz name",
        "end_date": "2022-08-09 20:00",
        "description": "description"
    }
}' "http://0.0.0.0:8000/api/v1/quiz/create/"
```
### Update quiz
PATCH: /api/v1/quiz/update/<quiz_id>/ \
For admins only
#### Request Example:
```
curl -v -X PATCH \
-H "Authorization: Bearer {access_token}" \
-d '{
        "name": "quiz name",
        "end_date": "2022-08-09 20:00",
        "description": "description"
    }
}' "http://0.0.0.0:8000/api/v1/quiz/update/<quiz_id>/"
```
### Delete quiz
DELETE: /api/v1/quiz/delete/<quiz_id>/ \
For admins only
#### Request Example:
```
curl -v -X DELETE \
-H "Authorization: Bearer {access_token}" \
"http://0.0.0.0:8000/api/v1/quiz/delete/<quiz_id>/"
```
#### Response Example:
```
{
    "details": "Successful"
}
```
### Create question
POST: api/v1/quiz/<quiz_id>/question/create/ \
For admins only \
type - required - "typing", "choose_one", "choose_many" \
asnwer_options - optional - dict
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
-d '{
        "text": "question",
        "type": "choose_many",
        "answer_options": {
            "1": "A",
            "2": "B",
            "3": "C"
    }
}'
}' "http://0.0.0.0:8000/api/v1/quiz/<quiz_id>/question/create/"
```
### Update question
PATCH: api/v1/quiz/<quiz_id>/question/update/<question_id>/ \
All fields are optional \
For admins only
#### Request Example:
```
curl -v -X PATCH \
-H "Authorization: Bearer {access_token}" \
-d '{
        "text": "ZZZZ?",
        "type": "choose_one",
        "answer_options": {
            "1": "A",
            "2": "B",
            "3": "C"
        }
}'
}' "http://0.0.0.0:8000/api/v1/quiz/<quiz_id>/question/update/<question_id>/"
```
### Delete question
DELETE: /api/v1/quiz/<quiz_id>/question/delete/<question_id>/ \
For admins only
#### Request Example:
```
curl -v -X DELETE \
-H "Authorization: Bearer {access_token}" \
"http://0.0.0.0:8000/api/v1/users/"
```
#### Response Example:
```
{
    "details": "Successful"
}
```
### Get active quizzes
GET: /api/v1/quiz/actives/ \
For all users
#### Request Example:
```
curl -v -X GET \
-H "Authorization: Bearer {access_token}" \
"http://0.0.0.0:8000/api/v1/quiz/actives/"
```
#### Response Example:
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "quiz name",
            "end_date": "2021-08-09T20:00:00Z",
            "description": "description"
        }
    ]
}
```
### Create answer
POST: /api/v1/quiz/<quiz_id>/question/<question_id>/answer/
#### Request parameters:
For all users
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
-d '{
        "text": "answer",
        "anonymously": true
    }'
"http://0.0.0.0:8000/api/v1/quiz/<quiz_id>/question/<question_id>/answer/
```
OR
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
-d '{
        "text": ["1", "2"],
        "anonymously": true
    }'
"http://0.0.0.0:8000/api/v1/quiz/<quiz_id>/question/<question_id>/answer/
```
#### Response Example:
```
{
    "text": "a",
    "username": null,
    "anonymously": true
}
```
### Get quizzes with answers
POST: /api/v1/quiz/answered/?user_id=<user_id>
#### Request parameters:
Returns only answered quizzes \
For admins and own data users
#### Request Example:
```
curl -v -X POST \
-H "Authorization: Bearer {access_token}" \
"http://0.0.0.0:8000/api/v1/quiz/answered/?user_id=<user_id>
```
#### Response Example
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "quiz name",
            "end_date": "2020-08-09T20:00:00Z",
            "description": "description",
            "questions": [
                {
                    "question_num": 1,
                    "text": "questionq",
                    "type": "choose_many",
                    "answer_options": {
                        "1": "A",
                        "2": "B",
                        "3": "C"
                    },
                    "answer": {
                        "text": "['1', '2']",
                        "username": "admin",
                        "anonymously": false
                    }
                },
                {
                    "question_num": 2,
                    "text": "question2",
                    "type": "choose_one",
                    "answer_options": {
                        "1": "A",
                        "2": "B",
                        "3": "C"
                    },
                    "answer": {
                        "text": "2",
                        "username": null,
                        "anonymously": true
                    }
                },
                {
                    "question_num": 3,
                    "text": "question3",
                    "type": "typing",
                    "answer_options": null,
                    "answer": {
                        "text": "text",
                        "username": null,
                        "anonymously": true
                    }
                }
            ]
        }
    ]
}
```