import mysql.connector as mariadb

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

