class Sql:
    #
    # USER_DB
    make_userdb = ''' CREATE TABLE IF NOT EXISTS USER_DB (
        USER_ID TEXT NOT NULL PRIMARY KEY,
        PASSWORD TEXT,
        NAME TEXT,
        ZIPCODE TEXT,
        ADD1 TEXT,
        ADD2 TEXT,
        SEX TEXT,
        AGE NUMBER,
        COUNTRY_ID TEXT,
        I_COUNT TEXT,
        I_KIND TEXT,
        INJECTION TEXT,
        REGDATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) '''
    insert_userdb = ''' INSERT INTO USER_DB (USER_ID, PASSWORD, NAME, ZIPCODE, ADD1, ADD2,
                                             SEX, AGE, COUNTRY_ID, I_COUNT, 
                                             I_KIND, INJECTION) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
    update_userdb = ''' UPDATE USER_DB SET
                        PASSWORD=?, NAME=?, ZIPCODE=?, ADD1=?, ADD2=?, SEX=?, 
                        AGE=?, COUNTRY_ID=?, I_COUNT=?, 
                        I_KIND=?, INJECTION=? WHERE USER_ID=? '''
    delete_userdb = ''' DELETE FROM USER_DB WHERE USER_ID=? '''
    select_userdb = ''' SELECT * FROM USER_DB WHERE USER_ID=? '''
    selectall_userdb = ''' SELECT * FROM USER_DB '''

    #
    # COUNTRY_DB
    make_countrydb = ''' CREATE TABLE IF NOT EXISTS COUNTRY_DB (
        COUNTRY_ID TEXT NOT NULL PRIMARY KEY,
        COUNTRY_NAME TEXT,
        QURANTINE BOOL,
        POPULATION TEXT,
        TOTAL_CASES TEXT,
        INFECTED TEXT,
        SAFE TEXT
    ) '''
    insert_countrydb = ''' INSERT INTO COUNTRY_DB (COUNTRY_ID, COUNTRY_NAME, QURANTINE, POPULATION,
                                                   TOTAL_CASES, INFECTED, SAFE) VALUES (?, ?, ?, ?, ?, ?, ?) '''
    update_countrydb = ''' UPDATE COUNTRY_DB SET
                        COUNTRY_NAME=?, QURANTINE=?, POPULATION=?,
                        TOTAL_CASES=?, INFECTED=?, SAFE=? WHERE COUNTRY_ID=? '''
    delete_countrydb = ''' DELETE FROM COUNTRY_DB WHERE COUNTRY_ID=? '''
    select_countrydb = ''' SELECT * FROM COUNTRY_DB WHERE COUNTRY_ID=? '''
    selectall_countrydb = ''' SELECT * FROM COUNTRY_DB '''

    #
    # CONTENT_DB
    make_contentdb = ''' CREATE TABLE IF NOT EXISTS CONTENT_DB (
        CONTENT_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        USER_ID TEXT,
        CONTENT TEXT,
        CORONA_TRAVEL TEXT,
        REGDATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) '''
    insert_contentdb = ''' INSERT INTO CONTENT_DB (CONTENT_ID, USER_ID, CONTENT, CORONA_TRAVEL) 
                           VALUES (?, ?, ?, ?) '''
    update_contentdb = ''' UPDATE CONTENT_DB SET CONTENT=?, CORONA_TRAVEL=? WHERE CONTENT_ID=? '''
    delete_contentdb = ''' DELETE FROM CONTENT_DB WHERE CONTENT_ID=? '''
    select_contentdb = ''' SELECT * FROM CONTENT_DB WHERE CONTENT_ID=? '''
    count_contentdb = ''' SELECT count(*) FROM CONTENT_DB '''
    selectlimit_contentdb = ''' SELECT * FROM CONTENT_DB LIMIT ?, ? '''
    selectlimit_d_contentdb = ''' SELECT * FROM CONTENT_DB ORDER BY CONTENT_ID DESC LIMIT ?, ? '''
    selectall_contentdb = ''' SELECT * FROM CONTENT_DB '''
    selectall_d_contentdb = ''' SELECT * FROM CONTENT_DB ORDER BY CONTENT_ID DESC '''

    #
    # COMMENT_DB
    make_commentdb = ''' CREATE TABLE IF NOT EXISTS COMMENT_DB (
        COMMENT_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        CONTENT_ID TEXT,
        USER_ID TEXT,
        COMMENT TEXT,
        REGDATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) '''
    insert_commentdb = ''' INSERT INTO COMMENT_DB (COMMENT_ID, CONTENT_ID, USER_ID, COMMENT) 
                           VALUES (?, ?, ?, ?) '''
    update_commentdb = ''' UPDATE COMMENT_DB SET
                        COMMENT=? WHERE COMMENT_ID=? '''
    delete_commentdb = ''' DELETE FROM COMMENT_DB WHERE COMMENT_ID=? '''
    select_commentdb = ''' SELECT * FROM COMMENT_DB WHERE COMMENT_ID=? '''
    selectid_commentdb = ''' SELECT * FROM COMMENT_DB WHERE CONTENT_ID=? '''
    selectall_commentdb = ''' SELECT * FROM COMMENT_DB '''
