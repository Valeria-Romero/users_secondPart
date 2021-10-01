from users_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__( self, id, first_name, last_name, email, created_at, updated_at ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at


    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "users_schema" ).query_db( query )

        users = []
        for user in results:
            users.append(User(user['id'],user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))

        return users

    @classmethod
    def add_user(cls, newUser):
        query = "INSERT INTO users(first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, SYSDATE(), SYSDATE());"
        data = {
            "first_name": newUser.first_name,
            "last_name": newUser.last_name,
            "email": newUser.email
                }
        result = connectToMySQL( "users_schema" ).query_db( query, data )
        return result

    @classmethod
    def updateUser(cls, updatedUser):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s"
        
        data ={
        "id":updatedUser.id,
        "first_name": updatedUser.first_name,
        "last_name": updatedUser.last_name,
        "email": updatedUser.email
        }

        result = connectToMySQL( "users_schema" ).query_db( query, data )
        return result

    @classmethod
    def deleteUser(cls, id):
        query = "DELETE users FROM users WHERE id=%(id)s"

        data={
            "id":id
        }

        result = connectToMySQL( "users_schema" ).query_db( query, data )
        return result

    @classmethod
    def show_user_info(cls, id):
        print(2)
        query = "SELECT * FROM users WHERE id=%(id)s"

        data={
            "id":id,
        }

        user_info=[]

        result = connectToMySQL("users_schema").query_db(query, data)

        for user in result:
            user_info.append(User(user['id'],user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))

        print(3)
        return result