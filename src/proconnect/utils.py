import bcrypt
def MAKE_PASSWORD(password):
    password = password.encode()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash.decode()


# match password to hashed one
def CHECK_PASSWORD(password, hash):
    return bcrypt.checkpw(password.encode(), hash.encode())