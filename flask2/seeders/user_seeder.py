import bcrypt

class UserSeeder():
    def run(self,db,User):
        print("Start Seeder")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(b"password", salt)
        db.session.add(User('admin','admin@gmail.com',hashed))
        db.session.commit() 
        print("Done Seeder")