import re

def is_encrypted(username):

    if re.match(r'^[A-Za-z0-9@#$%^&+=!?*()_~-]+$',username):
        common_words = ["admin", "user", "name", "test", "guest"]
    if not any(word in username.lower() for word in common_words):
        return True
    return False

    # Example usage
usernames = ["jD3@!9xL", "admin123", "Qx!4z_P", "username123"]
for user in usernames:
    print(f"{user}: {'Encrypted' if is_encrypted(user) else 'Not Encrypted'}")