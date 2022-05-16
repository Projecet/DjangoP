# userdb table
# id(str), pwd(str), name(str)

class UserVO:
    def __init__(self, id, password, name, zipcode, add1, add2, sex, age, country_id, i_count, i_kind, injection, regdate):
        self.id = id
        self.password = password
        self.name = name
        self.zipcode = zipcode
        self.add1 = add1
        self.add2 = add2
        self.sex = sex
        self.age = age
        self.country_id = country_id
        self.i_count = i_count
        self.i_kind = i_kind
        self.injection = injection
        self.regdate = regdate

    def getId(self):
        return self.id

    def getPassword(self):
        return self.password

    def getName(self):
        return self.name

    def getZipcode(self):
        return self.zipcode

    def getAdd1(self):
        return self.add1

    def getAdd2(self):
        return self.add2

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getCountry_id(self):
        return self.country_id

    def getI_count(self):
        return self.i_count

    def getI_kind(self):
        return self.i_kind

    def getInjection(self):
        return self.injection

    def getRegdate(self):
        return self.regdate

    def setId(self, id):
        self.id = id

    def setPassword(self, password):
        self.password = password

    def setName(self, name):
        self.name = name

    def setZipcode(self, zipcode):
        self.zipcode = zipcode

    def setAdd1(self, add1):
        self.add1 = add1

    def setAdd2(self, add2):
        self.add2 = add2

    def setSex(self, sex):
        self.sex = sex

    def setAge(self, age):
        self.age = age

    def setCountry_id(self, country_id):
        self.country_id = country_id

    def setI_count(self, i_count):
        self.i_count = i_count

    def setI_kind(self, i_kind):
        self.i_kind = i_kind

    def setInjection(self, injection):
        self.injection = injection

    def setRegdate(self, regdate):
        self.regdate = regdate

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.id, self.password, self.name, self.zipcode,
                                                           self.add1, self.add2, self.sex, self.age, self.country_id,
                                                           self.i_count, self.i_kind, self.injection, self.regdate)
