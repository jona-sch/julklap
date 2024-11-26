from julklap.group import Group
from julklap.person import Person

# Modify to set the sender email address and password
sender_email = "address_sending_out@mails.com"
sender_password = "password"

# Modify to add the different persons in your group
persons = {
    Person("Jan", "jan@mail.com"),
    Person("Luo", "luo@mail.com"),
    Person("Kid", "kid@mail.com"),
}

# Modify to add the different persons in your group
exclusions = [(Person("Jan", "jan@mail.com"), Person("Luo", "luo@mail.com"))]
