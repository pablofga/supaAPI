from flask import Flask, jsonify
from supabase import create_client, Client
from dotenv import dotenv_values

app = Flask(__name__)

# Cargar fichero .env
config = dotenv_values(".env")

url=config['SUPABASE_URL']
key=config['SUPABASE_KEY']

# Crear cliente supabase con los valores leidos de .env
supabase: Client = create_client(url, key)

@app.route('/')
def main_page():
    return "<html><head></head><body>@PRUEBA pfga A RESTful API in Flask using SQLAlchemy. For more info on usage, go to <a href>https://github.com/mgreenw/flask-restapi-example</a>.</body></html>"

# Mostrar Doctor
@app.route('/api/v1/posts/<id2>', methods=['GET'])
def show_post(id2):
    try:
        post = supabase.table("posts").select("*").eq("id",id2).execute()
        return jsonify(post.data),200
    except:
        return not_found("Post does not exis1")

# Custom Error Helper Functions
def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response
