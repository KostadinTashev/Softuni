username = input()
password = input()
new_password = input()
# Докато новата парола не е същата като правилната/първоначалната
while new_password != password:
    new_password = input()
print(f"Welcome {username}!")