from users import UserFactory


uf = UserFactory(max_users=2)

# for u in uf:
#     print(u)

new_user = next(uf)
print(new_user)

new_user = next(uf)
print(new_user)

new_user = next(uf)
print(new_user)

new_user = next(uf)
print(new_user)
