__author__ = 'Bryan'

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())

    confirmed_users.append(current_user)

print("\nconfirmed users: ")
for user in confirmed_users:
    print(user.title())