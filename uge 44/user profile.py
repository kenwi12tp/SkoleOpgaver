profile = {}
def build_profile(profile):
    name = input("What is your name? ")
    lastname = input("What is your last name? ")
    location = input("Where do you live? ")
    moms_name = input("What is your moms name? ")
    favorite_hobbi = input("What is your favorite hobbi? ")
    profile.update({"name": name, "lastname": lastname, "location": location, "moms_name": moms_name, favorite_hobbi: favorite_hobbi})
    return profile
profile = build_profile(profile)
print(profile)