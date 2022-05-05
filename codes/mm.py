person_array = []


class invalid_name_exception(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class invalid_age_exception(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class invalid(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class invalid_mobNo_exception(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class custom_exception:
    def __init__(self, name, age, mobNo, email):
        self.name = name
        self.age = age
        self.mobNo = mobNo
        self.email = email

    def validations(self):
        if len(self.name) < 3:
            raise invalid_name_exception('Enter the valid name ')
        else:
            person_array.append(self.name)

        if self.age < 0:
            raise invalid_age_exception('Entered age is not correct ')
        else:
            person_array.append(self.age)

        if len(self.mobNo) != 10:
            raise invalid_mobNo_exception('Enter the valid Mobile Number')
        else:
            person_array.append(self.mobNo)

        if '.' not in self.email and '@' not in self.email:
            raise invalid('Enter the valid Email Id')
        else:
            person_array.append(self.email)


obj = custom_exception("mayur", 21, "7798762936", "mayurtadge@gmail.com")
obj.validations()
if len(person_array) == 4:
    print(person_array)
else:
    person_array.clear()