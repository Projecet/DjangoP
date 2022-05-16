# contentdb table
# id(str), pwd(str), name(str)

class ContentVO:
    def __init__(self, c_id, u_id, u_name, content, corona_travel, regdate):
        self.c_id = c_id
        self.u_id = u_id
        self.u_name = u_name
        self.content = content
        self.corona_travel = corona_travel
        self.regdate = regdate

    def getContent_id(self):
        return self.c_id

    def getUser_id(self):
        return self.u_id

    def getUser_name(self):
        return self.u_name

    def getContent(self):
        return self.content

    def getCorona_travel(self):
        return self.corona_travel

    def getRegdate(self):
        return self.regdate

    def setContent_id(self, c_id):
        self.c_id = c_id

    def setUser_id(self, u_id):
        self.u_id = u_id

    def setUser_name(self, u_name):
        self.u_name = u_name

    def setContent(self, content):
        self.content = content

    def setCorona_travel(self, corona_travel):
        self.corona_travel = corona_travel

    def setRegdate(self, regdate):
        self.regdate = regdate

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.c_id, self.u_id, self.u_name, self.content, self.corona_travel, self.regdate)
