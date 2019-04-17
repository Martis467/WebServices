###To run the app run the following command
docker-compose up --build -d 


#Web service API documentation

## Usage

Response form:

```json
{
  "data": "Holds the contents of a response",
  "message": "Description of what happened"
}
```

Further end-point documentation will only detail the data field

### Show All users

**Definition**

`GET /users`

**Response**

- `200 Ok` on success

```json
[
  {
    "id" : 1,
    "firstName": "Tomas",
    "lastName": "Anavicius",
    "email": "tomas.anavicius@gmail.com"
  },
  
  {
    "id": 2,
    "firstName": "Paulius",
    "lastName": "Staisiunas",
    "email": "paulius.paulius@gmail.com"
  }
]
```

### Show All users with notes

**Definition**

`GET /users/notes`

**Response**

- `200 Ok` on success

```json
[
  {
    "id" : 1,
    "firstName": "Tomas",
    "lastName": "Anavicius",
    "email": "tomas.anavicius@gmail.com",
    "notes": [
      {
        "title": "Filmai",
        "author": "Tomaas Anavcius",
        "comment": "Avengers End Game"
      },
      {
        "title": "Laborai",
        "author": "Tomaas Anavcius",
        "comment": "Operaciniu sistemu pirmas ir antras"
      }
    ]
  },
  {
  "id" : 2,
    "firstName": "Paulius",
    "lastName": "Staisiunas",
    "email": "paulius.paulius@gmail.com",
    "notes": [
      {
        "title": "Maisto produktai",
        "author": "Paulius Staisiunas",
        "comment": "Milky way, snickers"
      },
      {
        "title": "Kursinis",
        "author": "Paulius Staisiunas",
        "comment": "Pasirasyt izanga"
      }
    ]
  }
]
```

### Add new user

**Definition**

`POST /users`

**Arguments**

- `"firstName": string`
- `"lastName": string`
- `"email": string`

**Response**

- `201 Created` on success
- `3000 Email Already Exists` if email is already taken 

```json
{
    "id": 1,
    "firstName": "Paulius",
    "lastName": "Staisiunas",
    "email": "paulius.paulius@gmail.com"
}
```

### Add new user note

**Definition**

`POST /users/1/notes`

**Arguments**

- `"title": string`
- `"comment": string`

**Response**

- `201 Created` on success

```json
{
    "title": "Darbai",
    "comment": "Isplaut grindis, pasert suni"
}
```

### Show user with notes

**Definition**

`GET /users/{id}`

**Response**

- `200 Ok` on success
- `404 Not Found` if user doesnt exist

```json
{
    "id": 1,
    "firstName": "Paulius",
    "lastName": "Staisiunas",
    "email": "paulius.paulius@gmail.com",
    "notes": [
      {
        "title": "Maisto produktai",
        "author": "Paulius Staisiunas",
        "comment": "Milky way, snickers"
      },
      {
        "title": "Kursinis",
        "author": "Paulius Staisiunas",
        "comment": "Pasirasyt izanga"
      }
    ]
}
```

### Update a user

**Definition**

`PUT /users/{id}`

**Arguments**

- `"firstName": string`
- `"lastName": string`
- `"email": string`

**Response**

- `202 Accepted` on success
- `404 Not Found` if user doesnt exist
- `3000 Email Already Exists` if email is already taken 

### Update a user note

**Definition**

`PUT /users/notes/{title}`

**Arguments**

- `"title": string`
- `"comment": string`

**Response**

- `202 Accepted` on success
- `404 Not Found` if note doesnt exist

### Patch a user

**Definition**

`PATCH /user/{id}`

**Arguments**

- `"firstName": string`
- `"lastName": string`
- `"email": string`

**Response**

- `202 Accepted` on success
- `404 Not Found` if user doesnt exist
- `3000 Email Already Exists` if email is already taken 

### Delete a user

**Definition**

`DELTE /users/{id}`

**Response**

- `204 No Content` on success
- `404 Not found` if user doesnt exist

### Delete a user note

**Definition**

`DELTE /users/notes/{title}`

**Response**

- `204 No Content` on success
- `404 Not found` if note doesnt exist