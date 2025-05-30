from passlib.context import CryptContext


class HashPassword:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def hash_password(self, password: str):
        return self.pwd_context.hash(password)
   

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)
        