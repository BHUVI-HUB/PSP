# Harmful

def get_both_popular_and_active_users():
# Assume the following two functions each return a
# list of user names
most_popular_users = get_list_of_most_popular_users()
most_active_users = get_list_of_most_active_users()
popular_and_active_users = []
for user in most_active_users:
if user in most_popular_users:
popular_and_active_users.append(user)
return popular_and_active_users

# Idiomatic

def get_both_popular_and_active_users():
# Assume the following two functions each return a
# list of user names
return(set(
get_list_of_most_active_users()) & set(
get_list_of_most_popular_users()))

