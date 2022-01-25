from flask import Flask, request, jsonify
from app.models.posts_models import Post
from datetime import datetime
from app import db


def create_post():
    data = request.get_json()
    id = len(list(db.posts.find()))+1
    title = data.get('title')
    author = data.get('author')
    tags = data.get('tags')
    content = data.get('content')
    if title == None or author == None or tags == None or content == None:
        return {"wrong fields": [{"title": type(title).__name__, "author": type(author).__name__, "tags": type(tags).__name__, "content": type(content).__name__}]}, 400
    new_data = Post(id, title, author, tags, content)
    post_data = new_data.__dict__
    db.posts.insert_one(post_data)
    del post_data["_id"]
    return post_data, 201

def read_posts():
    posts = list(db.posts.find())
    for post in posts:
        del post["_id"]
    return jsonify(posts), 200 

def read_posts_by_id(id):
    posts = list(db.posts.find())
    for post in posts:
        del post["_id"]
        if post["id"] == id:
            return post, 200
    return {"message": "ID não encontrado"}, 404

def delete_post(id):
    try:
        deleted = db.posts.find_one({'id': int(id)})
        del deleted["_id"]
        db.posts.delete_one({"id": int(id)})
        return deleted, 200
    except TypeError:
        return {"message": "post não encontrado"}, 404

def update_post(id):
    try:
        data = request.get_json()
        for key in data.keys():
            print(key == 'author')
            if key != "title" and key != 'author' and key != "tags" and key != "content":
                return {"message": "JSON inválido"}, 400
        db.posts.update_one({"id": int(id)}, {"$set": {**data, "updated_at": datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")}} )
        updated = db.posts.find_one({'id': int(id)})
        del updated['_id']
        return updated, 200
    except TypeError:
        return {"message": "ID não encontrado"}, 404