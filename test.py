import mysql.connector as mariadb

<<<<<<< HEAD
my_cnx = mariadb.connect(
    host='172.17.0.2',
    port=3306,
    user='myuser',
    password='mypassword',
    database='test',
)

my_cursor = my_cnx.cursor()

my_cursor.execute("""
    CREATE TABLE TB_TZ_MST (
        ID INT(8) NOT NULL AUTO_INCREMENT,
        MONTH INT(2) NOT NULL,
        HOUR INT(2) NOT NULL,
        POWER_TIMEZONE VARCHAR(10) NOT NULL,
        CONSTRAINT TB_TZ_MST_PK PRIMARY KEY(ID)
    )
""")

my_cursor.execute("""
    INSERT IGNORE INTO TB_TEST (ID) VALUES 
    (1),
    (2);
""")
my_cursor.execute("SELECT * FROM TB_TEST;")
my_cursor.fetchall()

=======

class DBManager:
    def __init__(self, db_config):
        self.host = db_config['host']
        self.port = db_config['port']
        self.user = db_config['user']
        self.password = db_config['password']
        self.database = db_config['database']
    
    def __connect(self):
        my_cnx = mariadb.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return my_cnx
    
    def execute(self, query: str, query_type: str):
        my_cnx = self.__connect()
        my_cursor = my_cnx.cursor()
        try:
            results = None
            my_cursor.execute(query)
            if (query_type=="SELECT")|(query_type=="SHOW"):
                results = my_cursor.fetchall()
            my_cnx.commit()
        except Exception as err:
            print(err)
        finally:
            my_cursor.close()
            my_cnx.close()
        return results


def main():
    db_config = {
        "host": "172.24.0.2",
        "port": "3306",
        "user": "myuser",
        "password": "mypassword",
        "database": "MY_DB",
    }

    dbm = DBManager(db_config)
    dbm.execute("SHOW TABLES;", "SHOW")
    dbm.execute("""CREATE TABLE TB_TEST(
        ID INT(11) NOT NULL AUTO_INCREMENT,
        NAME VARCHAR(20) NOT NULL,
        CONSTRAINT TB_TEST_PK PRIMARY KEY(ID)
    );""", "CREATE")
    dbm.execute("""INSERT INTO TB_TEST (NAME) VALUES
        ("유재석"),
        ("박명수");""", "INSERT")
    dbm.execute("SELECT * FROM TB_TEST;", "SELECT")


if __name__ == "__main__":
    main()
>>>>>>> test
