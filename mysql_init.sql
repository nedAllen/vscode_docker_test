CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypassword';

GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE MY_DB;

CREATE TABLE TB_TZ_MST (
    `ID` INT(11) NOT NULL AUTO_INCREMENT COMMENT '일련번호',
    `MNTH` INT(2) NOT NULL COMMENT '월',
    `HR` INT(2) NOT NULL COMMENT '시간',
    `TZ` VARCHAR(8) NOT NULL COMMENT '전력시간대',
    PRIMARY KEY (ID),
    UNIQUE KEY `UNIQ_TI` (`MNTH`, `HR`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT '전력시간대 마스터 테이블';

INSERT IGNORE INTO `TB_TZ_MST` (`MNTH`, `HR`, `TZ`) VALUES 
    (1, 0, "경부하"),
    (1, 1, "경부하"),
    (1, 2, "경부하"),
    (1, 3, "경부하"),
    (1, 4, "경부하"),
    (1, 5, "경부하"),
    (1, 6, "경부하"),
    (1, 7, "경부하"),
    (1, 8, "경부하"),
    (1, 9, "중간부하"),
    (1, 10, "최대부하"),
    (1, 11, "최대부하"),
    (1, 12, "중간부하"),
    (1, 13, "최대부하"),
    (1, 14, "최대부하"),
    (1, 15, "최대부하"),
    (1, 16, "최대부하"),
    (1, 17, "중간부하"),
    (1, 18, "중간부하"),
    (1, 19, "중간부하"),
    (1, 20, "중간부하"),
    (1, 21, "중간부하"),
    (1, 22, "중간부하"),
    (1, 23, "경부하");

 