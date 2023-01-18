import random
import string



def user_password():
    all_caracters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password_given = [random.choice(all_caracters) for i in range(16)]
    return " ".join(password_given)

def run():
    user_name = input("Escribe tu nombre: ")
    password_generated = user_password()
    print(f"Hola {user_name} esta es tu contraseña: {password_generated}")
if __name__ == "__main__":
    run()