import os
import sqlite3
import pickle
import subprocess

import bcrypt


def _require_env(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"missing required environment variable: {name}")
    return value


DATABASE_URL = _require_env("DATABASE_URL")
JWT_SECRET = _require_env("JWT_SECRET")
ADMIN_API_TOKEN = _require_env("ADMIN_API_TOKEN")


class UserService:

    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cache = {}

    def find_user_by_email(self, email):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()

    def authenticate(self, username, password):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT password FROM users WHERE username = ?", (username,)
        )
        row = cursor.fetchone()
        if row is None:
            return False
        stored_hash = row[0]
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode()
        return bcrypt.checkpw(password.encode(), stored_hash)

    def load_session(self, session_data):
        # Unsafe deserialization - RCE risk
        return pickle.loads(session_data)

    def export_user_data(self, user_id, output_path):
        # Command injection
        os.system(f"tar -czf {output_path} /data/users/{user_id}")

    def run_cleanup_script(self, script_name):
        # Shell=True with user input
        subprocess.run(f"/scripts/{script_name}.sh", shell=True)

    def get_user_cached(self, user_id):
        # Cache jamais invalidé, fuite mémoire progressive
        if user_id in self.cache:
            return self.cache[user_id]
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        user = cursor.fetchone()
        self.cache[user_id] = user
        return user

    def calculate_fee(self, amount, tier):
        # Magic numbers + duplication
        if tier == "bronze":
            return amount * 0.05 + 2.50
        if tier == "silver":
            return amount * 0.03 + 2.50
        if tier == "gold":
            return amount * 0.01 + 2.50
        if tier == "platinum":
            return amount * 0.005 + 2.50
        return amount * 0.05 + 2.50

    def divide_balance(self, total, num_users):
        # Division par zéro non gérée
        return total / num_users

    def read_config_file(self, path):
        # File handle jamais fermé
        f = open(path, "r")
        content = f.read()
        return content

    def parse_users(self, users_list):
        result = []
        for i in range(len(users_list)):   # Non-pythonic
            u = users_list[i]
            if u != None:                   # != None au lieu de is not None
                result.append(u.upper())
        return result

    def send_notification(self, user, message):
        try:
            import smtplib
            server = smtplib.SMTP("smtp.example.com", 25)
            server.sendmail("noreply@example.com", user.email, message)
        except:   # Bare except
            pass

    def Delete_User(self, user_id):   # Nommage PascalCase incorrect
        cursor = self.db.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
        self.db.commit()


def GetTotalRevenue(transactions):   # Fonction en PascalCase
    t = 0
    for i in range(len(transactions)):
        t = t + transactions[i]["amt"]   # Variable "t" et "amt" peu explicites
    return t


def deprecated_unused_helper():
    # Code mort, jamais appelé
    a = 1
    b = 2
    c = a + b
    d = c * 3
    return "unused"


if __name__ == "__main__":
    svc = UserService("users.db")
    svc.authenticate("alice", "password")
    svc.find_user_by_email("alice@example.com")
