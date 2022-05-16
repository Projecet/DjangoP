# countrydb table
# data access object
from model.dao.sqlitedao import SqliteDao
from model.sql.sql import Sql
from model.vo.countryvo import CountryVO


class CountryDAO(SqliteDao):

    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, c):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.insert_countrydb, (c.getId(), c.getName(), c.getQurantine(), c.getPopulation(),
                                                          c.getTotal_cases(), c.getInfected(), c.getSafe()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Country Insert Completed : {}'.format(c))

    def delete(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.delete_countrydb, (id,))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Country Delete Complete : {}'.format(id))

    def update(self, c):
        try:
            print(c.getId())
            conn = self.getConn()
            conn['cursor'].execute(Sql.update_countrydb, (c.getName(), c.getQurantine(), c.getPopulation(),
                                                          c.getTotal_cases(), c.getInfected(), c.getSafe(), c.getId()))
            conn['con'].commit()
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Country Update Complete : {}'.format(c))

    def select(self, id):
        try:
            conn = self.getConn()
            conn['cursor'].execute(Sql.select_countrydb, (id,))
            rs = conn['cursor'].fetchone()
            countryvo = CountryVO(rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6])
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Country Select Complete : {}'.format(id))

        return countryvo

    def selectall(self):
        try:
            countrys = []
            conn = self.getConn()
            conn['cursor'].execute(Sql.selectall_countrydb)
            all = conn['cursor'].fetchall()
            for u in all:
                rs = CountryVO(u[0], u[1], u[2], u[3], u[4], u[5], u[6])
                countrys.append(rs)
        except:
            raise Exception
        finally:
            self.close(conn)
        print('Country SelectAll Complete')

        return countrys


if __name__ == '__main__':
    print('start test')

    sqlitedao = SqliteDao('shop')
    sqlitedao.makeTable()
    countrydao = CountryDAO('shop')

    # Insert Test
    # country1 = CountryVO('01', '대한민국', True, '200', '20', '0.2', '안전')
    # countrydao.insert(country1)

    # Update Test
    # country2 = CountryVO('01', '미국', False, '2000', '20', '0.02', '경고')
    # countrydao.update(country2)

    # Select
    # country3 = countrydao.select('01')
    # print(country3)

    # Select All
    # result = countrydao.selectall()
    # for c in result:
    #     print(c)

    print('end test')
