from supabase import create_client, Client
from dotenv import dotenv_values

# Cargar fichero .env
config = dotenv_values(".env")

url=config['SUPABASE_URL']
key=config['SUPABASE_KEY']

# Crear cliente supabase con los valores leidos de .env
supabase: Client = create_client(url, key)

# Function to Fetch All Posts
def find_all_posts():
    data = supabase.table("posts").select("*").execute()
    return data

posts = find_all_posts()
print(posts)