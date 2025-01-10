'''Python Functions - xxargs and dictionary'''


def save_user(**user):
    '''Save user function'''
    print(user)

save_user(id=1, name="Jelani", age=37)
