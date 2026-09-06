from datetime import datetime
import login_and_registration

def log_with_comment(message):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)

            if result == "Function completed":
                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                now = datetime.now().strftime("%Y-%m-%d")

                filename = f"log_{now}.txt"
                username = login_and_registration.USER
                try:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"[{time}] - {username} - {message}\n")
                except FileNotFoundError:
                    print("Log file not found.")
                return result
        return wrapper
    return decorator


def auth_check_decorator(required_auth):
    def decorator(function):
        def wrapper(*args, **kwargs):
            username = login_and_registration.USER
            query = """
                 SELECT auth
                 FROM library_users
                 WHERE username = %s
             """
            result = login_and_registration.database_execute(query, (username,), fetch=True)
            if result[0][0] == required_auth:
                return function(*args, **kwargs)
            else:
                print("No authorization!")
        return wrapper
    return decorator