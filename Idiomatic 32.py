# Harmful

user_email = {}
for user in users_list:
if user.email:
user_email[user.name] = user.email


# Idiomatic

user_email = {user.name: user.email
for user in users_list if user.email}
