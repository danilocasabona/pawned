import hashlib, requests

def get_user_input():
    user_input = input("Enter your password: ")
    user_password = user_input
    return prep_input_with_hashlib(user_password)

def prep_input_with_hashlib(user_password):
    hashed_password = hashlib.sha1(f"{user_password}".encode()).hexdigest().upper()
    first_five = hashed_password[:5]
    remaining = hashed_password[5:]
    return call_api(user_password, first_five, remaining)

def call_api(user_password, first_five, remaining):
    url_address = f"https://api.pwnedpasswords.com/range/{first_five}"
    api_response = requests.get(url=url_address)
    line_split = api_response.text.splitlines()
    return check_response(user_password, line_split, remaining)

def check_response(user_password, line_split, remaining):
    for line in line_split:
        if remaining in line:
            count = line.split(":")[1]
            print(f"Your password {user_password} has been pwned {count} times. Please choose a different password.")
            return
    print(f"Your password {user_password} has not been pwned. It is safe to use.")
        
get_user_input()