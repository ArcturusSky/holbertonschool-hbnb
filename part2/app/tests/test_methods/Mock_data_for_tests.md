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

...