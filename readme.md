# PROJET API BIBLIOTHEQUE PYTHON FLASK

## Motivations
Cette API permet de gérer les livres d'une biblotheque dans la base de données.
## Getting Started

### Installing Dependencies

#### Python 3.9.7
#### pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)

Si vous n'avez pas python installé, merci de suivre cet URL pour l'installer [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Vous devez installer le package dotenv en utilisant la commande pip install python-dotenv 

#### PIP Dependencies

Exécuter la commande ci dessous pour installer les dépendences
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the plants_database.sql file provided. From the backend folder in terminal run:
```bash
psql plants_database < plants_database.sql
```

## Running the server

From within the `plants_api` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
To run the server on Windows, execute:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request"
}

The API will return four error types when requests fail:
. 400: Bad request
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL: cet endpoint permet de récupérer la liste des livres 
    
        
    SAMPLE: curl -i http://localhost:5000/livres

        
    "Livres": [
        {
            "Auteur": "RICHARD",
            "Date de publication": "Mon, 09 Oct 2000 00:00:00 GMT",
            "Editeur": "POP",
            "Id de La Categorie": 1,
            "id": 2,
            "isbn": "GAIO",
            "titre": "AMOUR INTERDIT"
        },
        {
            "Auteur": "Lockus",
            "Date de publication": "Sun, 17 Nov 1996 00:00:00 GMT",
            "Editeur": "ROCK",
            "Id de La Categorie": 2,
            "id": 3,
            "isbn": "PAIO",
            "titre": "HOMME"
        },
        {
            "Auteur": "PAPURIS",
            "Date de publication": "Thu, 03 Jun 1999 00:00:00 GMT",
            "Editeur": "RIME",
            "Id de La Categorie": 3,
            "id": 4,
            "isbn": "CAIL",
            "titre": "CHAUVE"
        },
        {
            "Auteur": "JEAN",
            "Date de publication": "Mon, 10 Feb 2020 00:00:00 GMT",
            "Editeur": "JACQUES",
            "Id de La Categorie": 1,
            "id": 7,
            "isbn": "Q25P",
            "titre": "HOLL"
        },
        {
            "Auteur": "ANTOINE",
            "Date de publication": "Tue, 14 Oct 1980 00:00:00 GMT",
            "Editeur": "PAUL",
            "Id de La Categorie": 2,
            "id": 1,
            "isbn": "H52O",
            "titre": "MOINE"
        }
    ],
    "Success": true,
    "total": 5

```

. ## DELETE/livres (id)

    GENERAL: Cet endpoint permet de supprimer un livre
        Les resulats de cette requete se présentent comme suit:
        SAMPLE: curl -X DELETE http://localhost:5000/livres/2

  
 }

    "delete_id": 2,
    "Success": true,
    "Total": 4
}
```

. ##PATCH/livres(id)
  GENERAL:
  This endpoint is used to update a book
  We return a book which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/livres/1 -H "Content-Type:application/json" -d "{
       
            "isbn": "H52O",
            "titre": "MOINE",
            "date_publication": "1980-10-14",
            "auteur": "ANTOINE",
            "editeur": "PAUL",
            "id_categorie": 2
 }"
  ```
  ```
    {    
            "Auteur": "ANTOINE",
            "Date de publication": "Tue, 14 Oct 1980 00:00:00 GMT",
            "Editeur": "PAUL",
            "Id de La Categorie": 2,
            "id": 1,
            "isbn": "H52O",
            "titre": "MOINE"
    }
    
```    
. ## GET/livres (id)

    GENERAL: cet endpoint permet de récupérer un livre dans la bibliotheque
    
        
    SAMPLE: curl -i http://localhost:5000/livres/1


"Selected_Livres": {
        "Auteur": "ANTOINE",
        "Date de publication": "Tue, 14 Oct 1980 00:00:00 GMT",
        "Editeur": "PAUL",
        "Id de La Categorie": 2,
        "id": 1,
        "isbn": "H52O",
        "titre": "MOINE"
    },
    "Sucess": true,
    "selected": 1
} 

```

. ## GET/categories

    GENERAL: cet endpoint permet de récupérer la liste des categories
    
        
    SAMPLE: curl -i http://localhost:5000/categories

{
    "categories": [
        {
            "Libelle de la Categorie": "IPHONE",
            "id": 3
        },
        {
            "Libelle de la Categorie": "Laptop",
            "id": 4
        },
        {
            "Libelle de la Categorie": "Ordinateur",
            "id": 1
        },
        {
            "Libelle de la Categorie": "ANDROID",
            "id": 2
        }
    ],
    "total": 4
}

```     

. ## DELETE/categories (id)

    GENERAL: Cet endpoint permet de supprimer une categorie
        Les resulats de cette requete se présentent comme suit:
        SAMPLE: curl -X DELETE http://localhost:5000/categories/2

## Testing
To run the tests, run

}

    "delete_id": 2,
    "Success": true,
    "Total": 3
}

```

. ##PATCH/categories(id)
  GENERAL:
  This endpoint is used to update a category
  We return a category which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/categories/1 -H "Content-Type:application/json" -d { "libelle_categorie": "ANDROID"}

 ```
  ```
       {
            "Libelle de la Categorie": "ANDROID",
            "id": 1
        }

```

. ## GET/categories (id)

    GENERAL: cet endpoint permet de récupérer une categorie de livre
    
        
    SAMPLE: curl -i http://localhost:5000/catedories/1

{
    "Selected_Categories": {
        "Libelle de la Categorie": "Ordinateur",
        "id": 1
    },
    "Sucess": true,
    "selected": 1
}

 ```
. ## GET/livre (id)

    GENERAL: cet endpoint permet de récupérer les livres d'une categorie
    
        
    SAMPLE: curl -i http://localhost:5000/livre/1

{
    "Selected_Livres": [
        {
            "Auteur": "RICHARD",
            "Date de publication": "Mon, 09 Oct 2000 00:00:00 GMT",
            "Editeur": "POP",
            "Id de La Categorie": 1,
            "id": 2,
            "isbn": "GAIO",
            "titre": "AMOUR INTERDIT"
        },
        {
            "Auteur": "JEAN",
            "Date de publication": "Mon, 10 Feb 2020 00:00:00 GMT",
            "Editeur": "JACQUES",
            "Id de La Categorie": 1,
            "id": 7,
            "isbn": "Q25P",
            "titre": "HOLL"
        }
    ],
    "Sucess": true,
    "selected": 1
}

 ```


