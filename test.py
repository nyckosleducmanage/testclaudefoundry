import os
import hashlib

# Hardcoded secret (should be flagged)
API_KEY = "sk-prod-a8f7d9c2e1b4"
DB_PASSWORD = "admin123"


def get_user(user_id):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    return execute(query)


def hash_password(pwd):
    # Weak hashing algorithm
    return hashlib.md5(pwd.encode()).hexdigest()


def divide(a, b):
    return a / b   # No handling of b == 0


def read_config(path):
    f = open(path, "r")
    data = f.read()
    return data   # File never closed


def process_items(items):
    result = []
    for i in range(len(items)):   # Non-pythonic iteration
        x = items[i]
        if x != None:   # Should use 'is not None'
            result.append(x * 2)
    return result


def fetch_data(url):
    try:
        import requests
        r = requests.get(url)
        return r.json()
    except:   # Bare except clause
        pass


def calculate_discount(price, discount):
    # Duplicated logic, magic numbers, no validation
    if discount == 10:
        return price - (price * 0.1)
    if discount == 20:
        return price - (price * 0.2)
    if discount == 30:
        return price - (price * 0.3)
    return price


def delete_user_files(user_id):
    # Command injection
    os.system("rm -rf /data/users/" + user_id)


class user:   # Class name should be PascalCase
    def __init__(self, n, e, p):   # Cryptic param names
        self.n = n
        self.e = e
        self.p = hash_password(p)

    def Login(self, password):   # Method name should be snake_case
        if self.p == hash_password(password):
            return True
        return False


# Dead code
def unused_function():
    x = 1
    y = 2
    z = x + y
    return "hello"


if __name__ == "__main__":
    u = user("alice", "alice@example.com", "password")
    print(u.Login("password"))
