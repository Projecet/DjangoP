# commentdb table
# data access object
from model.dao.sqlitedao import SqliteDao
from model.sql.sql import Sql
from model.vo.commentvo import CommentVO


class CommentDAO(SqliteDao):

    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, m):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.insert_commentdb, (m.getComment_id(), m.getContent_id(), m.getUser_id(),
                                                          m.getComment()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Comment Insert Completed : {}'.format(m))

    def delete(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.delete_commentdb, (id,))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Comment Delete Complete : {}'.format(id))

    def update(self, m):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.update_commentdb, (m.getComment(), m.getComment_id()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Comment Update Complete : {}'.format(m))

    def select(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.select_commentdb, (id,))
            rs = conn['cursor'].fetchone()
            commentvo = CommentVO(rs[0], rs[1], rs[2], None, rs[3], rs[4])
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Comment Select Complete : {}'.format(id))

        return commentvo

    def selectid(self, id):
        try:
            comments = []
            conn = self.getConn()
            conn['cursor'].execute(Sql.selectid_commentdb, (id,))
            all = conn['cursor'].fetchall()
            for u in all:
                rs = CommentVO(u[0], u[1], u[2], None, u[3], u[4])
                comments.append(rs)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Comment SelectAll Complete')

        return comments

    def selectall(self):
        try:
            comments = []
            conn = self.getConn()
            conn['cursor'].execute(Sql.selectall_commentdb)
            all = conn['cursor'].fetchall()
            for u in all:
                rs = CommentVO(u[0], u[1], u[2], None, u[3], u[4])
                comments.append(rs)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Comment SelectAll Complete')

        return comments


if __name__ == '__main__':
    print('start test')

    sqlitedao = SqliteDao('shop')
    sqlitedao.makeTable()
    commentdao = CommentDAO('shop')

    # Insert Test
    # comment1 = CommentVO('01', '01', '안녕하세요', '화이자 2차 22/01/01', None)
    # commentdao.insert(comment1)

    # Update Test
    # comment2 = CommentVO('01', '02', '안녕하세요', '모더나 3차 21/12/01', None)
    # commentdao.update(comment2)

    # Select
    # comment3 = commentdao.select('01')
    # print(comment3)

    # Select All
    result = commentdao.selectall()
    for c in result:
        print(c)

    print('end test')
