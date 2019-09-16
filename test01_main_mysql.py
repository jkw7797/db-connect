from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
import sys, pandas as pd, pymysql
from test01 import Ui_MainWindow as mainW
from test02 import Ui_MainWindow as printW

class test(QMainWindow,mainW):
    global test2

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sqlConnect()
        self.createData()
        self.show()

    def sqlConnect(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='test',
                password='123456',
                db='test',
                port=3306,
                charset='utf8'
            )

        except:
             print('서버 접속 에러')
             exit()
        print('연결성공')
        self.cur = self.conn.cursor()


    def createData(self):
        try:
            query = 'Create table STUDENT(ID int, sname varchar(20), DeptNo int)'
            self.cur.execute(query)

            query = 'CREATE UNIQUE INDEX IDX_STUDENT ON STUDENT(ID)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (1,"이상봉",10)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (2,"이승준",10)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (3,"김준호",20)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (4,"박재은",20)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (5,"정혜원",30)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (6,"송주혜",30)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (7,"최현화",30)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (8,"정민재",60)'
            self.cur.execute(query)

            query = 'INSERT INTO STUDENT VALUES (9,"강유석",70)'
            self.cur.execute(query)

            query = 'Create table DEPARTMENT (DEPTNO INT, DEPTNAME VARCHAR(40))'
            self.cur.execute(query)

            query = 'CREATE UNIQUE INDEX IDX_DEPARTMENT ON DEPARTMENT(DEPTNO,DEPTNAME)'
            self.cur.execute(query)

            query = 'INSERT INTO DEPARTMENT VALUES (10,"컴퓨터공학과")'
            self.cur.execute(query)

            query = 'INSERT INTO DEPARTMENT VALUES (20,"통계과")'
            self.cur.execute(query)

            query = 'INSERT INTO DEPARTMENT VALUES (30,"심리학과")'
            self.cur.execute(query)

            query = 'INSERT INTO DEPARTMENT VALUES (40,"경제학과")'
            self.cur.execute(query)

            query = 'Create table RESULT_DEPT (DEPTNO INT, DEPTNAME VARCHAR(40),ID INT, SNAME VARCHAR(20))'
            self.cur.execute(query)

            query = 'CREATE UNIQUE INDEX IDX_DEPT ON RESULT_DEPT (DEPTNO,ID)'
            self.cur.execute(query)
            self.conn.commit()

        except:
            print('테이블 생성에러')
            exit(1)


    def join(self):
        try:
            query = 'SELECT DEPTNO FROM department WHERE DEPTNAME = "{}"'.format(self.txt_d.text())
            self.cur.execute(query)
            self.conn.commit()
            dno = int(self.cur.fetchall()[0][0])

            query = 'SELECT ID FROM student WHERE sname = "{}"'.format(self.txt_s.text())
            self.cur.execute(query)
            self.conn.commit()
            sid = int(self.cur.fetchall()[0][0])

            query = "INSERT INTO RESULT_DEPT VALUES ({},'{}',{},'{}')".format(dno, self.txt_d.text(), sid, self.txt_s.text())
            self.cur.execute(query)
            self.conn.commit()

            QMessageBox.information(self, "조인성공", "'{}'와'{}' 조인하였습니다.".format(self.txt_s.text(), self.txt_d.text()), QMessageBox.Yes, QMessageBox.Yes)

        except:
            QMessageBox.information(self, "삽입오류", "이름이나 학과가 올바르지 않습니다. 다시입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
            print('조인 에러')
            exit(1)


    def printExcel(self):
        test2.show()


class excel(QMainWindow,printW):
    global test

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def print_ok(self):
        try:
            query = 'SELECT * FROM result_dept'
            test.cur.execute(query)
            test.conn.commit()
            data = list(test.cur.fetchall())
            df = pd.DataFrame(data)

            if(self.txt_fName.text() != ""):
                if(self.txt_save.text() != ""):
                    addr = self.txt_save.text()
                    e_name = self.txt_fName.text()

                else:
                    addr = 'C:\ '
                    e_name = self.txt_fName.text()

            else:
                QMessageBox.information(self, "입력오류", "파일명을 입력하세요.", QMessageBox.Yes, QMessageBox.Yes)
                return

            df.to_excel(addr + e_name + '.xlsx')
            test2.close()
        except:
            QMessageBox.information(self, "입력오류", "주소 또는 파일명을 확인하세요", QMessageBox.Yes, QMessageBox.Yes)


app = QApplication([])
test = test()
test2 = excel()
sys.exit(app.exec_())