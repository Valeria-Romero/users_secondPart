from flask import render_template,request, redirect
from users_app import app 
from users_app.models.User import User
from datetime import date, datetime

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "read.html", users=users )

@app.route("/users/add")
def render_create():
    return render_template("create.html")

@app.route("/users/add", methods=['POST', 'GET'])
def addUser():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    created_at= datetime
    updated_at= datetime

    newUser = User(id,first_name,last_name,email,created_at,updated_at)
    result = User.add_user(newUser)

    return redirect ("/users")

@app.route("/users/update/<id>")
def render_update(id):
    return render_template ("update.html", id=id)

@app.route("/users/update", methods=['POST'])
def update_User():
    user = User.show_user_info(request.form['identifier'])
    id=request.form['identifier']
    first_name = request.form['update_first_name']
    last_name = request.form['update_last_name']
    email = request.form['update_email']
    created_at = user[0]['created_at']
    updated_at = user[0]['updated_at']
    updatedUser = User(id,first_name,last_name,email,created_at,updated_at)
    result= User.updateUser(updatedUser)

    return render_template ("profile.html", user=updatedUser)


@app.route("/users/delete/<id>", methods=['POST', 'GET'])
def remove_user(id):

    User.deleteUser(id)
    return redirect("/users")

@app.route("/users/profile/<id>", methods=['GET'])
def show_user_info(id):
    user = User.show_user_info(id)
    print("User id",user)
    return render_template( "profile.html", user=user[0])
