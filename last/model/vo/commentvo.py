# commentdb table
# id(str), pwd(str), name(str)

class CommentVO:
    def __init__(self, m_id, c_id, u_id, u_name, comment, regdate):
        self.m_id = m_id
        self.c_id = c_id
        self.u_id = u_id
        self.u_name = u_name
        self.comment = comment
        self.regdate = regdate

    def getComment_id(self):
        return self.m_id

    def getContent_id(self):
        return self.c_id

    def getUser_id(self):
        return self.u_id

    def getUser_name(self):
        return self.u_name

    def getComment(self):
        return self.comment

    def getRegdate(self):
        return self.regdate

    def setComment_id(self, m_id):
        self.m_id = m_id

    def setContent_id(self, c_id):
        self.c_id = c_id

    def setUser_id(self, u_id):
        self.u_id = u_id

    def setUser_name(self, u_name):
        self.u_name = u_name

    def setComment(self, comment):
        self.comment = comment

    def setRegdate(self, regdate):
        self.regdate = regdate

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.m_id, self.c_id, self.u_id, self.u_name, self.comment, self.regdate)
