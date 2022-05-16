# userdb table
# data access object
from model.dao.sqlitedao import SqliteDao
from model.sql.sql import Sql
from model.vo.uservo import UserVO


class UserDAO(SqliteDao):

    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, u):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.insert_userdb, (u.getId(), u.getPassword(), u.getName(), u.getZipcode(),
                                                       u.getAdd1(), u.getAdd2(), u.getSex(), u.getAge(),
                                                       u.getCountry_id(), u.getI_count(), u.getI_kind(),
                                                       u.getInjection()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('User Insert Completed : {}'.format(u))

    def delete(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.delete_userdb, (id,))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('User Delete Complete : {}'.format(id))

    def update(self, u):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.update_userdb, (u.getPassword(), u.getName(), u.getZipcode(),
                                                       u.getAdd1(), u.getAdd2(), u.getSex(), u.getAge(),
                                                       u.getCountry_id(),  u.getI_count(), u.getI_kind(),
                                                       u.getInjection(), u.getId()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('User Update Complete : {}'.format(u))

    def select(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.select_userdb, (id,))
            rs = conn['cursor'].fetchone()
            user = UserVO(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6],
                          rs[7], rs[8],  rs[9],  rs[10], rs[11], rs[12])
        except TypeError:
            user = UserVO(None, None, None, None, None, None, None,
                          None, None, None, None, None, None)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('User Select Complete : {}'.format(id))
        return user

    def selectall(self):
        try:
            users = []
            conn = self.getConn()
            conn['cursor'].execute(Sql.selectall_userdb)
            all = conn['cursor'].fetchall()
            for u in all:
                rs = UserVO(u[0], u[1], u[2], u[3], u[4], u[5], u[6],
                            u[7], u[8],  u[9],  u[10], u[11], u[12])
                users.append(rs)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('User SelectAll Complete')
        return users


if __name__ == '__main__':
    print('start test')

    sqlitedao = SqliteDao('shop')
    sqlitedao.makeTable()
    userdao = UserDAO('shop')

    # Insert Test
    # user1 = UserVO('id01', 'password01', 'james01', '서울시', '남자', 20, '코로나', '2021-12-30', None)
    # userdao.insert(user1)

    # Update Test
    # user2 = UserVO('id01', 'password01', 'james02', '부산시', '여자', 20, '코로나', '2021-12-30', None)
    # userdao.update(user2)

    # Select
    # user3 = userdao.select('id01')
    # print(user3)

    # Select All
    # result = userdao.selectall()
    # for u in result:
    #     print(u)

    print('end test')
