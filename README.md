## Environment:
- Python version: 3.8
- Django version: 3.0.5
- Django REST framework version: 3.11.0

## Commands

+ run the first time:  
```source ***name_virtual_env/bin/activate```
```pip3 install -r requirements.txt```
```python3 manage.py makemigrations```
```python3 manage.py migrate --run-syncdb```
```python3 manage.py runserver```
        
## Read-Only Files:
- rest_api/tests.py --> tests are not completed
- manage.py

## Data:
Example of a user data JSON object:
```
{
    "id":1,
    "name": "Angelina Jolie",
    "position": "Financial Advisor",
}
```
Example of a trade data JSON object:
```
{
    "id":1,
    "type": "buy",
    "user_id": 23,
    "symbol": "ABX",
    "shares": 30,
    "price": 134,
    "timestamp": 1531522701000
}
```

## About:
It was implemented a model for trade object and the REST service that exposes the `/trades/` and `/users/`endpoint, which allows for managing the collection of trade records in the following way:

**POST** request to `/users/`:

- creates a new user
- expects a JSON trade object without id property as a body payload, but with name and position.
- the response code is 201 and the response body is the created user object

**GET** request to `/users/`:

- return a collection of all users
- the response code is 200 and the response body is an array of all trades objects ordered by their ids in increasing order

**GET** request to `/user/<id>/`:

- returns a user with the given id if the matching user exists, the response code is 200 and the response body is the matching user object if there is no user with the given id in the collection, the response code is 404

**DELETE**, **PUT**, **PATCH** request to `/user/<id>/`:

- the response code is 405-method not allowed because the API does not allow to delete or modify users, for any id value

**POST** request to `/trades/`:

- creates a new trade
- expects a JSON trade object without id property as a body payload. The shares value might be out of accepted [1, 100] range and type might be invalid, i.e not 'buy' or 'sell', and in such case, the API must return 400 error code. You can assume that besides that the given payload is always valid.
- adds the given trade object to the collection of trades and assigns a unique integer id to it. The first created trade must have id 1, the second one 2, and so on.
- the response code is 201 and the response body is the created trade object

**GET** request to `/trades/`:

- return a collection of all trades
- the response code is 200 and the response body is an array of all trades objects ordered by their ids in increasing order

**GET** request to `/trade/<id>/`:

- returns a trade with the given id if the matching trade exists, the response code is 200 and the response body is the matching trade object if there is no trade with the given id in the collection, the response code is 404

**DELETE**, **PUT**, **PATCH** request to `/trade/<id>/`:

- the response code is 405-method not allowed because the API does not allow to delete or modify trades, for any id value






