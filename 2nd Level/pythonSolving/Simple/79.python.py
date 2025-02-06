# Remove first and last char of a string


def remove_first_last(s):
    return s[1:-1] if len(s) > 1 else ""

s = "HI BOSS"

new_s = remove_first_last(s)

print(new_s)