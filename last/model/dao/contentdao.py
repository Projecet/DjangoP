# contentdb table
# data access object
from model.dao.sqlitedao import SqliteDao
from model.sql.sql import Sql
from model.vo.contentvo import ContentVO


class ContentDAO(SqliteDao):

    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, c):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.insert_contentdb, (c.getContent_id(), c.getUser_id(), c.getContent(),
                                                          c.getCorona_travel()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content Insert Completed : {}'.format(c))

    def delete(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.delete_contentdb, (id,))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content Delete Complete : {}'.format(id))

    def update(self, c):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.update_contentdb, (c.getContent(), c.getCorona_travel(), c.getContent_id()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content Update Complete : {}'.format(c))

    def count(self):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.count_contentdb)
            count = conn['cursor'].fetchone()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content Select Complete : {}'.format(id))

        return count[0]

    def select(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.select_contentdb, (id,))
            rs = conn['cursor'].fetchone()
            contentvo = ContentVO(rs[0], rs[1], None, rs[2], rs[3], rs[4])
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content Select Complete : {}'.format(id))

        return contentvo

    def selectlimit(self, count, page, d='a'):
        try:
            if page*5 > count:
                if count % 5 == 0:
                    count = 5
                else:
                    count = count % 5
            else:
                count = 5
            page = (page - 1) * 5
            print(page, '부터', count, '개')
            contents = []
            conn = self.getConn()
            if d == 'd':
                conn['cursor'].execute(Sql.selectlimit_d_contentdb, (page, count))
            elif d != 'a':
                conn['cursor'].execute(Sql.selectlimit_contentdb, (page, count))
            all = conn['cursor'].fetchall()
            for u in all:
                rs = ContentVO(u[0], u[1], None, u[2], u[3], u[4])
                contents.append(rs)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content SelectLimit Complete')

        return contents

    def selectall(self, d='a'):
        try:
            contents = []
            conn = self.getConn()
            if d == 'd':
                conn['cursor'].execute(Sql.selectall_d_contentdb)
            elif d != 'a':
                conn['cursor'].execute(Sql.selectall_contentdb)
            all = conn['cursor'].fetchall()
            for u in all:
                rs = ContentVO(u[0], u[1], None, u[2], u[3], u[4])
                contents.append(rs)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Content SelectAll Complete')

        return contents


if __name__ == '__main__':
    print('start test')

    sqlitedao = SqliteDao('shop')
    sqlitedao.makeTable()
    contentdao = ContentDAO('shop')

    # Insert Test
    # content1 = ContentVO('01', '01', '안녕하세요', '화이자 2차 22/01/01', None)
    # contentdao.insert(content1)

    # Update Test
    # content2 = ContentVO('01', '02', '안녕하세요', '모더나 3차 21/12/01', None)
    # contentdao.update(content2)

    # Select
    # content3 = contentdao.select('01')
    # print(content3)

    # Select All
    result = contentdao.selectall()
    for c in result:
        print(c)

    print('end test')
