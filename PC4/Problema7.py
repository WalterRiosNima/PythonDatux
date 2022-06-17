import re

regex = r""

lista_emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

for email in lista_emails:
    if re.match(regex, email) and re.search("@", email)  and re.search(".com", email):
        print("The email {} is a valid email".format(email))
    else:
        print("The email {} is invalid".format(email))