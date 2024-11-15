# Methods tests

This document is meant to sum up the test and especially to help me to just have to copy and past my test instead of rewriting each time.

## User methods

### POST

*Payload to put into Swagger documentation:*

```bash
{
  "first_name": "Carmilla",
  "last_name": "Carmine",
  "username": "BladeOverlord",
  "password": "AngelicSteel12",
  "email": "Carmine.C@example.com",
  "localisation": "Hell",
  "phone_number": "0102030405",
  "is_admin": false
}

{
  "first_name": "Odette",
  "last_name": "Carmine",
  "username": "LabDevil",
  "password": "LittleMamaGirl01",
  "email": "Carmine.O@example.com",
  "localisation": "Hell",
  "phone_number": "0203040506",
  "is_admin": false
}

{
  "first_name": "Clara",
  "last_name": "Carmine",
  "username": "ClaraC",
  "password": "LittleMamaGirl02",
  "email": "Carmine.Cl@example.com",
  "localisation": "Hell",
  "phone_number": "0304050607",
  "is_admin": false
}
```

![Swagger_result](../../images/user_Swagger_POST_test.png)

*CURL version:*
```bash
curl -X POST http://localhost:5000/api/v1/users/ \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "username": "Jojo1",
  "password": "Test0102030405",
  "email": "Johen.doe@example.com",
  "localisation": "Paris",
  "phone_number": "0102030405",
  "is_admin": false
}'
```

### GET (by ID)

*put the id returned by POST method into the SWAGGER "user_id" request*

![Swagger_result](../../images/user_Swagger_GET_test.png)

*CURL version:*

```bash
curl -X GET http://localhost:5000/api/v1/users/given_id \
-H "Content-Type: application/json"
```

### GET (all users)

After putting the 3 Carmines profiles, trying getting all users:



### PUT

## Places Methods

```bash
{
  "placename": "The Tower",
  "description": "The Tower of Carmilla Carmines, OverLord",
  "price": 15000,
  "latitude": -90,
  "longitude": -180,
  "owner_id": "f8c0259d-58cb-4f86-8abf-e473dc9616e5",
  "amenities": [
    "wifi", "angelic weapons"
  ]
}
```
## Review methods

### POST

```bash
{
  "title": "I love this place!",
  "text": "This is the best place ever!!",
  "rating": 5,
  "user_id": "959a0421-8088-42d7-aa4d-098c68e36339",
  "place_id": "4df3a108-97c0-4f1c-9c4d-71060dfe7213"
}
```