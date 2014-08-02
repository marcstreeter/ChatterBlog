import models
from app import db


class Member(object):
    __email = ""
    __phone = ""
    __reputation = ""
    __password = ""
    __name = ""

    def __init__(self, name, password, email, phone):
        self.__email = email
        self.__phone = phone
        self.__password = password
        self.__name = name


    @classmethod
    def get_member(cls, id):
        session =  db.session()
        # set variables from id
        name = ""
        password = ""
        email = ""
        phone = ""
        reputation = ""
        try:
            existing_member =  cls(name=name, password=password, email=email, phone=phone)
        except:
            return None

        existing_member.__reputation = reputation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value.title()

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def reputation(self):
        return self.__reputation

    # important inherited values

    def __str__(self):
        return "{name}".format(name=self.name)

    def __repr__(self):
        return "<User {name} e:{email} p:{phone}".format(name=self.name, email=self.email, phone=self.phone)