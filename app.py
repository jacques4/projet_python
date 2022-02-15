
from json import load
from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false, true
import os
from dotenv import load_dotenv
load_dotenv()

motdepasse=os.getenv("password")
hote=os.getenv("host")
utilisateur=os.getenv("user")
dialecte=os.getenv("dialect")

########################################################
# CONNEXION A LA BASE DE DONNES
########################################################

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '{0}://{1}:{2}@{3}/bibliotheque'.format(dialecte,utilisateur,motdepasse,hote)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


########################################################
# CREATION DE LA CLASSE CATEGORIES ET DES METHODES
########################################################

class Categorie(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer,primary_key=true)
    libelle_categorie=db.Column(db.String(500),nullable=false)
    livres=db.relationship('Livre',backref='categories',lazy=True)


    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie
        

    def insert(self):
         db.session.add(self)
         db.session.commit()
   

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     

    def update(self):
         db.session.commit()

    def format(self):
         return{
        'id': self.id,
        'Libelle de la Categorie': self.libelle_categorie,
        
      }


########################################################
# CREATION DE LA CLASSE LIVRES ET DES METHODES
########################################################

class Livre(db.Model):
    __tablename__='livres'
    id=db.Column(db.Integer,primary_key=true)
    isbn=db.Column(db.String(300),nullable=false)
    titre=db.Column(db.String(300),nullable=true)
    date_publication=db.Column(db.DateTime,nullable=true)
    auteur=db.Column(db.String(300),nullable=false)
    editeur=db.Column(db.String(200),nullable=true)
    id_categorie=db.Column(db.Integer, db.ForeignKey('categories.id'),nullable=False)

    def __init__(self, isbn,titre,date_publication,auteur,editeur,id_categorie):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.id_categorie=id_categorie

    def insert(self):
         db.session.add(self)
         db.session.commit()
   

    def delete(self):
        db.session.delete(self)
        db.session.commit()
     

    def update(self):
         db.session.commit()

    def format(self):
         return{
        'id': self.id,
        'isbn': self.isbn,
        'titre': self.titre,
        'Date de publication': self.date_publication,
        'Auteur': self.auteur,
        'Editeur': self.editeur,
        'Id de La Categorie': self.id_categorie,
      }

db.create_all()

########################################################
# AFFICHAGE DES LIVRES
########################################################

@app.route('/livres',methods=['GET'])
def livres():
    livres=Livre.query.all()
    formated_students=[et.format() for et in livres]
    if livres is None:
        abort (404)
    else:
       return jsonify({
        'Success' : True,
        'Livres': formated_students,
        'total': len(Livre.query.all())
    })

########################################################
# AFFICHAGE DES CATEGORIES
########################################################

@app.route('/categories',methods=['GET'])
def categorie():
    categorie=Categorie.query.all()
    formated_categorie=[et.format() for et in categorie]
    if livres is None:
        abort (404)
    else:
      return jsonify({
        'Success' : True,
        'categories': formated_categorie,
        'total': len(Categorie.query.all())
    })

########################################################
# AFFICHAGE D'UN LIVRE 
########################################################

@app.route('/livres/<int:id>', methods=['GET'])
def un_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return jsonify({

                "Sucess": True,
                "selected": id,
                "Selected_Livres": livre.format()

            })

########################################################
# AFFICHAGE D'UNE CATEGORIE 
########################################################

@app.route('/categories/<int:id>', methods=['GET'])
def une_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return jsonify({

                "Sucess": True,
                "selected": id,
                "Selected_Categories": categorie.format()

            })


########################################################
# AFFICHAGE D'UN LIVRE D'UNE CATEGORIE
########################################################

@app.route('/livre/<int:id>', methods=['GET'])
def unlivre(id):
    livre = Livre.query.filter_by(id_categorie=id).all()
    formated_livre=[et.format() for et in livre]
    if livre is None:
        abort(404)
    else:
        return jsonify({

                "Sucess": True,
                "selected": id,
                "Selected_Livres": formated_livre

            })

########################################################
# SUPPRESSION D'UN LIVRE 
########################################################

@app.route('/livres/<int:id>', methods=['DELETE'])
def sup_livre(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify(
            {
                "delete_id": id,
                "Sucess": True,
                "Total": Livre.query.count(),
            
            })


########################################################
# SUPPRESSION D'UNE CATEGORIE 
########################################################
            
@app.route('/categories/<int:id>', methods=['DELETE'])
def sup_categorie(id):
    categorie=Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        categorie.delete()
        return jsonify(
            {
                "delete_id": id,
                "Sucess": True,
                "Total": Categorie.query.count(),
            
            })


########################################################
# MODIFICATION D'UN LIVRE
######################################################## 

@app.route('/livres/<int:id>', methods=['PATCH'])
def mod_livre(id):
    livre=Livre.query.get(id)

    body=request.get_json()
    livre.isbn=body.get('isbn',None)
    livre.titre=body.get('titre',None)
    livre.date_publication=body.get('date_publication',None)
    livre.auteur=body.get('auteur',None)
    livre.editeur=body.get('editeur',None)
    livre.id_categorie=body.get('id_categorie',None)

    if  livre.isbn is None or livre.titre is None or livre.date_publication is None or livre.auteur is None or livre.editeur is None or livre.id_categorie is None:
        abort(400)
    else:    
       livre.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_Livre": id,
                "New_Book": livre.format()
            })


########################################################
# MODIFICATION D'UNE CATEGORIE
########################################################

@app.route('/categories/<int:id>', methods=['PATCH'])
def mod_categorie(id):
    categorie=Categorie.query.get(id)

    body=request.get_json()
    categorie.libelle_categorie=body.get('libelle_categorie',None)
    
    if  categorie.libelle_categorie is None :
        abort(400)
    else:    
       categorie.update()
       return jsonify(
            {
                "Sucess": True,
                "Update_id_Categorie": id,
                "New_Categorie": categorie.format()
            })


        
@app.errorhandler(404)
def client_erreur(error):
    return jsonify(
            {
                "Sucess": False,
                "erreur": 404,
                "Message": "Not found"
            })

@app.errorhandler(400)
def server_erreur(error):
    return jsonify(
            {
                "Sucess": False,
                "erreur": 400,
                "Message": "Bad request "
            })