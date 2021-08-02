# Harmful

users_first_names = set()
for user in users:
users_first_names.add(user.first_name)


# Idiomatic

users_first_names = {user.first_name for user in users}
