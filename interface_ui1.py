from PyQt5 import QtCore, QtGui, QtWidgets
from pickle import *
import re
from datetime import datetime, timedelta
def mrigel(date1, date2):
    jour1, mois1, annee1 = map(int, date1.split('/'))
    jour2, mois2, annee2 = map(int, date2.split('/'))
    
    if annee1 < annee2:
        return True
    elif annee1 > annee2:
        return False
    else:
        if mois1 < mois2:
            return True
        elif mois1 > mois2:
            return False
        else:
            if jour1 < jour2:
                return True
            else:
                return False

def exist_emprunt(code,ref):
     f=open("emprunts.org","rb")
     while True:
            try:
                 e=load(f)
            except Exception:break
            if e["num_inscription"]==code and e["reference"]==ref:
                 f.close()     
                 return True
     f.close()
     return False
     
def retourner1(code,ref):
     f=open("emprunts.org","rb")
     while True:
            try:
                 e=load(f)
            except Exception:break
            if e["num_inscription"]==code and e["reference"]==ref and e["retourne"]==False:
                 f.close()     
                 return True
     f.close()
     return False
            
def increment_max(ref):
        with open('livres.org', 'rb') as f:
                records = []
                while True:
                    try:
                        record = load(f)
                        records.append(record)
                    except EOFError:
                        break
        for record in records:
                if (record['reference'] == ref) and (int(record["nb_ex"])>int(record["max"])):
                     record["max"] =int(record["max"])+1
                     print(record["max"])
                break
        with open('livres.org', 'wb') as f:
                for record in records:
                    dump(record, f)
def verif_emprunt(code,ref):
     f=open("emprunts.org","rb")
     while True:
            try:
                e=load(f)
            except Exception:break
            if e["num_inscription"]==code and e["reference"]==ref :
                 f.close()
                 return True
     f.close()
     return False

def retourner(code,ref):
     with open('emprunts.org', 'rb') as f:
                records = []
                while True:
                    try:
                        record = load(f)
                        records.append(record)
                    except EOFError:
                        break
     for record in records:
                if (record['num_inscription'] == code) and (record['reference'] == ref):
                     date_systeme=datetime.now()
                     record["date_retour"]=date_systeme.strftime("%d/%m/%Y")
                     if record["retourne"]==False:
                        increment_max(ref)
                        record["retourne"]=True

     with open('emprunts.org', 'wb') as f:
                for record in records:
                    dump(record, f)
     
 
def decremente_max(ref):
        with open('livres.org', 'rb') as f:
                records = []
                while True:
                    try:
                        record = load(f)
                        records.append(record)
                    except EOFError:
                        break
        for record in records:
                if record['reference'] == ref:
                     record["max"] =int(record["max"])-1
                break

        with open('livres.org', 'wb') as f:
                for record in records:
                    dump(record, f)       
     

"""def deja_emprunté(code):
     f=open("emprunts.org","rb")
     while True:
            try:
                 e=load(f)
            except EOFError:break
            date_retour=datetime.strptime(e["date_retour"], "%d/%m/%Y")
            date_systeme=datetime.now()
            if e["num_inscription"]==code and  date_retour>date_systeme:
                 f.close()
                 return True
     f.close()
     return False"""
def disponible(ref):
     f=open("livres.org","rb")
     while True:
          try:
               e=load(f)
          except EOFError:break 
          if e["reference"]==ref and int(e["max"])<1:
               f.close()
               return False
     f.close()
     return True

def valid_tel(tel):
     if len(tel)==0:return False
     elif not ((tel.isdigit()) and (len(tel)==8) and (tel[0] in ['2','3','4','5','7','9'])):return False
     else:
            ok=True
            f=open("etudiant.org","rb")
            while True:
                 try:
                      e=load(f)
                      if e["tel"]==tel:
                            ok=False
                 except EOFError:break
            return ok
def valid_mail(mail):
     if len(mail)==0:return False
     regex = r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$'
     if not (re.match(regex, mail)):
            return False
     else:
            ok=True
            f=open("etudiant.org","rb")
            while True:
                 try:
                      e=load(f)
                      if e["mail"]==mail:
                            ok=False
                 except EOFError:break
            return ok
def modify_record2(champ,record_id, new_value):
        with open('livres.org', 'rb') as f:
                records = []
                while True:
                    try:
                        record = load(f)
                        records.append(record)
                    except EOFError:
                        break
        for record in records:
                if record['reference'] == record_id:
                     record[champ] = new_value
                     record["max"]=new_value
                break

        with open('livres.org', 'wb') as f:
                for record in records:
                    dump(record, f)


def modify_record(champ,record_id, new_value):
        with open('etudiant.org', 'rb') as f:
                records = []
                while True:
                    try:
                        record = load(f)
                        records.append(record)
                    except EOFError:
                        break
        for record in records:
                if record['num_inscription'] == record_id:
                     record[champ] = new_value
                break

        with open('etudiant.org', 'wb') as f:
                for record in records:
                    dump(record, f)

def exist_ref(ref):
            f=open("livres.org","rb")
            while True:
                try:
                    e1=load(f)
                except Exception:break
                if e1["reference"]==ref:
                    f.close()
                    return True
                    
            f.close()   
            return False  
def exist(code):
            f=open("etudiant.org","rb")
            while True:
                try:
                    e1=load(f)
                except Exception:break
                if e1["num_inscription"]==code:
                    return True
                    f.close()
            f.close()   
            return False
            f.close()      

def existe(tel):
        f=open("etudiant.org","rb")
        while True:
            try:
                e=load(f)
                if e["tel"]==tel:
                        f.close() 
                        return True
            except EOFError:break
        f.close()
        return False


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1107, 809)
        Dialog.setStyleSheet("nameEdit->setStyleSheet(\"color: blue;\"\n"
"                        \"background-color: yellow;\"\n"
"                        \"selection-color: yellow;\"\n"
"                        \"selection-background-color: blue;\");")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1121, 811))
        self.tabWidget.setStyleSheet("color: rgb(92, 121, 134);\n"
"\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1121, 781))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_7)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.tabWidget_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label = QtWidgets.QLabel(self.tab_9)
        self.label.setGeometry(QtCore.QRect(90, 40, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit.setGeometry(QtCore.QRect(280, 70, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 160, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.tab_9)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 250, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.tab_9)
        self.label_3.setGeometry(QtCore.QRect(90, 220, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_9)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 320, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab_9)
        self.label_4.setGeometry(QtCore.QRect(90, 290, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget_18 = QtWidgets.QTabWidget(self.tab_9)
        self.tabWidget_18.setGeometry(QtCore.QRect(0, -40, 1111, 761))
        self.tabWidget_18.setObjectName("tabWidget_18")
        self.tab_62 = QtWidgets.QWidget()
        self.tab_62.setObjectName("tab_62")
        self.line_20 = QtWidgets.QFrame(self.tab_62)
        self.line_20.setGeometry(QtCore.QRect(680, 560, 351, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.label_45 = QtWidgets.QLabel(self.tab_62)
        self.label_45.setGeometry(QtCore.QRect(20, 20, 1061, 681))
        self.label_45.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"border-radius: 30px;")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.label_16 = QtWidgets.QLabel(self.tab_62)
        self.label_16.setGeometry(QtCore.QRect(450, 10, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_16.setFont(font)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setObjectName("label_16")
        self.tel = QtWidgets.QLineEdit(self.tab_62)
        self.tel.setGeometry(QtCore.QRect(320, 480, 211, 31))
        self.tel.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.tel.setObjectName("tel")
        self.ajouter = QtWidgets.QPushButton(self.tab_62)
        self.ajouter.setGeometry(QtCore.QRect(720, 630, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.ajouter.setFont(font)
        self.ajouter.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.ajouter.setObjectName("ajouter")
        self.label_13 = QtWidgets.QLabel(self.tab_62)
        self.label_13.setGeometry(QtCore.QRect(60, 520, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.tab_62)
        self.label_11.setGeometry(QtCore.QRect(60, 450, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(self.tab_62)
        self.label_8.setGeometry(QtCore.QRect(60, 240, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_8.setObjectName("label_8")
        self.nom = QtWidgets.QLineEdit(self.tab_62)
        self.nom.setGeometry(QtCore.QRect(320, 140, 211, 31))
        self.nom.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.nom.setObjectName("nom")
        self.date = QtWidgets.QDateEdit(self.tab_62)
        self.date.setGeometry(QtCore.QRect(320, 270, 211, 31))
        self.date.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.date.setObjectName("date")
        self.label_7 = QtWidgets.QLabel(self.tab_62)
        self.label_7.setGeometry(QtCore.QRect(60, 170, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_7.setObjectName("label_7")
        self.adresse = QtWidgets.QLineEdit(self.tab_62)
        self.adresse.setGeometry(QtCore.QRect(320, 340, 211, 31))
        self.adresse.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.adresse.setObjectName("adresse")
        self.label_14 = QtWidgets.QLabel(self.tab_62)
        self.label_14.setGeometry(QtCore.QRect(60, 590, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_14.setObjectName("label_14")
        self.ni = QtWidgets.QLineEdit(self.tab_62)
        self.ni.setGeometry(QtCore.QRect(320, 80, 211, 31))
        self.ni.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni.setObjectName("ni")
        self.label_10 = QtWidgets.QLabel(self.tab_62)
        self.label_10.setGeometry(QtCore.QRect(60, 310, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.tab_62)
        self.label_6.setGeometry(QtCore.QRect(60, 110, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_6.setObjectName("label_6")
        self.mail = QtWidgets.QLineEdit(self.tab_62)
        self.mail.setGeometry(QtCore.QRect(320, 400, 211, 31))
        self.mail.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.mail.setObjectName("mail")
        self.label_5 = QtWidgets.QLabel(self.tab_62)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(self.tab_62)
        self.label_12.setGeometry(QtCore.QRect(60, 380, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(92, 121, 134);\n"
"")
        self.label_12.setObjectName("label_12")
        self.prenom = QtWidgets.QLineEdit(self.tab_62)
        self.prenom.setGeometry(QtCore.QRect(320, 200, 211, 31))
        self.prenom.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.prenom.setObjectName("prenom")
        self.line = QtWidgets.QFrame(self.tab_62)
        self.line.setGeometry(QtCore.QRect(550, 430, 21, 231))
        self.line.setStyleSheet("color: rgb(67, 87, 97);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab_62)
        self.line_2.setGeometry(QtCore.QRect(550, 70, 21, 241))
        self.line_2.setStyleSheet("color: rgb(67, 87, 97);\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.section = QtWidgets.QComboBox(self.tab_62)
        self.section.setGeometry(QtCore.QRect(320, 551, 211, 31))
        self.section.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.section.setObjectName("section")
        self.section.addItem("")
        self.section.addItem("")
        self.section.addItem("")
        self.section.addItem("")
        self.section.addItem("")
        self.section.addItem("")
        self.premiere = QtWidgets.QRadioButton(self.tab_62)
        self.premiere.setGeometry(QtCore.QRect(330, 620, 81, 20))
        self.premiere.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.premiere.setObjectName("premiere")
        self.deuxieme = QtWidgets.QRadioButton(self.tab_62)
        self.deuxieme.setGeometry(QtCore.QRect(450, 620, 81, 20))
        self.deuxieme.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.deuxieme.setObjectName("deuxieme")
        self.troisieme = QtWidgets.QRadioButton(self.tab_62)
        self.troisieme.setGeometry(QtCore.QRect(390, 650, 81, 20))
        self.troisieme.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.troisieme.setObjectName("troisieme")
        self.erreurni = QtWidgets.QLabel(self.tab_62)
        self.erreurni.setGeometry(QtCore.QRect(320, 110, 251, 16))
        self.erreurni.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni.setText("")
        self.erreurni.setObjectName("erreurni")
        self.erreurnom = QtWidgets.QLabel(self.tab_62)
        self.erreurnom.setGeometry(QtCore.QRect(320, 170, 251, 20))
        self.erreurnom.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurnom.setText("")
        self.erreurnom.setObjectName("erreurnom")
        self.erreurprenom = QtWidgets.QLabel(self.tab_62)
        self.erreurprenom.setGeometry(QtCore.QRect(320, 230, 251, 20))
        self.erreurprenom.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurprenom.setText("")
        self.erreurprenom.setObjectName("erreurprenom")
        self.erreurdate_naiss = QtWidgets.QLabel(self.tab_62)
        self.erreurdate_naiss.setGeometry(QtCore.QRect(320, 300, 251, 20))
        self.erreurdate_naiss.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurdate_naiss.setText("")
        self.erreurdate_naiss.setObjectName("erreurdate_naiss")
        self.erreuradresse = QtWidgets.QLabel(self.tab_62)
        self.erreuradresse.setGeometry(QtCore.QRect(320, 370, 251, 20))
        self.erreuradresse.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreuradresse.setText("")
        self.erreuradresse.setObjectName("erreuradresse")
        self.erreurmail = QtWidgets.QLabel(self.tab_62)
        self.erreurmail.setGeometry(QtCore.QRect(320, 430, 251, 20))
        self.erreurmail.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurmail.setText("")
        self.erreurmail.setObjectName("erreurmail")
        self.erreursection = QtWidgets.QLabel(self.tab_62)
        self.erreursection.setGeometry(QtCore.QRect(320, 580, 251, 20))
        self.erreursection.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreursection.setText("")
        self.erreursection.setObjectName("erreursection")
        self.erreurniveau = QtWidgets.QLabel(self.tab_62)
        self.erreurniveau.setGeometry(QtCore.QRect(330, 670, 251, 20))
        self.erreurniveau.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurniveau.setText("")
        self.erreurniveau.setObjectName("erreurniveau")
        self.erreurtel = QtWidgets.QLabel(self.tab_62)
        self.erreurtel.setGeometry(QtCore.QRect(320, 510, 251, 20))
        self.erreurtel.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurtel.setText("")
        self.erreurtel.setObjectName("erreurtel")
        self.label_29 = QtWidgets.QLabel(self.tab_62)
        self.label_29.setGeometry(QtCore.QRect(670, 580, 351, 41))
        self.label_29.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.tabWidget_18.addTab(self.tab_62, "")
        self.tab_63 = QtWidgets.QWidget()
        self.tab_63.setObjectName("tab_63")
        self.tabWidget_19 = QtWidgets.QTabWidget(self.tab_63)
        self.tabWidget_19.setGeometry(QtCore.QRect(0, 0, 1111, 731))
        self.tabWidget_19.setObjectName("tabWidget_19")
        self.tab_64 = QtWidgets.QWidget()
        self.tab_64.setObjectName("tab_64")
        self.tabWidget_19.addTab(self.tab_64, "")
        self.tab_65 = QtWidgets.QWidget()
        self.tab_65.setObjectName("tab_65")
        self.tabWidget_19.addTab(self.tab_65, "")
        self.tab_66 = QtWidgets.QWidget()
        self.tab_66.setObjectName("tab_66")
        self.tabWidget_19.addTab(self.tab_66, "")
        self.tab_67 = QtWidgets.QWidget()
        self.tab_67.setObjectName("tab_67")
        self.tabWidget_19.addTab(self.tab_67, "")
        self.tabWidget_18.addTab(self.tab_63, "")
        self.tab_68 = QtWidgets.QWidget()
        self.tab_68.setObjectName("tab_68")
        self.tabWidget_20 = QtWidgets.QTabWidget(self.tab_68)
        self.tabWidget_20.setGeometry(QtCore.QRect(0, 0, 781, 731))
        self.tabWidget_20.setObjectName("tabWidget_20")
        self.tab_69 = QtWidgets.QWidget()
        self.tab_69.setObjectName("tab_69")
        self.tabWidget_20.addTab(self.tab_69, "")
        self.tab_70 = QtWidgets.QWidget()
        self.tab_70.setObjectName("tab_70")
        self.tabWidget_20.addTab(self.tab_70, "")
        self.tab_71 = QtWidgets.QWidget()
        self.tab_71.setObjectName("tab_71")
        self.tabWidget_20.addTab(self.tab_71, "")
        self.tabWidget_18.addTab(self.tab_68, "")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_10)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 0, 1111, 731))
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.label_9 = QtWidgets.QLabel(self.tab_16)
        self.label_9.setGeometry(QtCore.QRect(310, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_9.setObjectName("label_9")
        self.ni_supp = QtWidgets.QLineEdit(self.tab_16)
        self.ni_supp.setGeometry(QtCore.QRect(530, 180, 211, 31))
        self.ni_supp.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni_supp.setObjectName("ni_supp")
        self.supprimer = QtWidgets.QPushButton(self.tab_16)
        self.supprimer.setGeometry(QtCore.QRect(450, 260, 151, 51))
        self.supprimer.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer.setObjectName("supprimer")
        self.erreurni_supp = QtWidgets.QLabel(self.tab_16)
        self.erreurni_supp.setGeometry(QtCore.QRect(530, 210, 211, 20))
        self.erreurni_supp.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp.setText("")
        self.erreurni_supp.setObjectName("erreurni_supp")
        self.sucess_sup = QtWidgets.QLabel(self.tab_16)
        self.sucess_sup.setGeometry(QtCore.QRect(390, 300, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup.setFont(font)
        self.sucess_sup.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup.setText("")
        self.sucess_sup.setObjectName("sucess_sup")
        self.tabWidget_6.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.label_15 = QtWidgets.QLabel(self.tab_17)
        self.label_15.setGeometry(QtCore.QRect(380, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_15.setObjectName("label_15")
        self.supprimer2 = QtWidgets.QPushButton(self.tab_17)
        self.supprimer2.setGeometry(QtCore.QRect(450, 260, 151, 51))
        self.supprimer2.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer2.setObjectName("supprimer2")
        self.erreursection_sup = QtWidgets.QLabel(self.tab_17)
        self.erreursection_sup.setGeometry(QtCore.QRect(510, 210, 251, 20))
        self.erreursection_sup.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreursection_sup.setText("")
        self.erreursection_sup.setObjectName("erreursection_sup")
        self.sucess_sup_2 = QtWidgets.QLabel(self.tab_17)
        self.sucess_sup_2.setGeometry(QtCore.QRect(400, 290, 291, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_2.setFont(font)
        self.sucess_sup_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_2.setText("")
        self.sucess_sup_2.setObjectName("sucess_sup_2")
        self.section_supp = QtWidgets.QComboBox(self.tab_17)
        self.section_supp.setGeometry(QtCore.QRect(510, 180, 211, 31))
        self.section_supp.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.section_supp.setObjectName("section_supp")
        self.section_supp.addItem("")
        self.section_supp.addItem("")
        self.section_supp.addItem("")
        self.section_supp.addItem("")
        self.section_supp.addItem("")
        self.section_supp.addItem("")
        self.tabWidget_6.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.label_17 = QtWidgets.QLabel(self.tab_18)
        self.label_17.setGeometry(QtCore.QRect(350, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_17.setObjectName("label_17")
        self.supprimer_2 = QtWidgets.QPushButton(self.tab_18)
        self.supprimer_2.setGeometry(QtCore.QRect(450, 280, 151, 51))
        self.supprimer_2.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer_2.setObjectName("supprimer_2")
        self.erreurni_supp_2 = QtWidgets.QLabel(self.tab_18)
        self.erreurni_supp_2.setGeometry(QtCore.QRect(500, 250, 211, 20))
        self.erreurni_supp_2.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_2.setText("")
        self.erreurni_supp_2.setObjectName("erreurni_supp_2")
        self.sucess_sup_3 = QtWidgets.QLabel(self.tab_18)
        self.sucess_sup_3.setGeometry(QtCore.QRect(390, 310, 291, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_3.setFont(font)
        self.sucess_sup_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_3.setText("")
        self.sucess_sup_3.setObjectName("sucess_sup_3")
        self.deuxieme_2 = QtWidgets.QRadioButton(self.tab_18)
        self.deuxieme_2.setGeometry(QtCore.QRect(620, 180, 81, 20))
        self.deuxieme_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.deuxieme_2.setObjectName("deuxieme_2")
        self.premiere_2 = QtWidgets.QRadioButton(self.tab_18)
        self.premiere_2.setGeometry(QtCore.QRect(500, 180, 81, 20))
        self.premiere_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.premiere_2.setObjectName("premiere_2")
        self.troisieme_2 = QtWidgets.QRadioButton(self.tab_18)
        self.troisieme_2.setGeometry(QtCore.QRect(560, 210, 81, 20))
        self.troisieme_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.troisieme_2.setObjectName("troisieme_2")
        self.tabWidget_6.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.section_supp_2 = QtWidgets.QComboBox(self.tab_19)
        self.section_supp_2.setGeometry(QtCore.QRect(520, 130, 211, 31))
        self.section_supp_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.section_supp_2.setObjectName("section_supp_2")
        self.section_supp_2.addItem("")
        self.section_supp_2.addItem("")
        self.section_supp_2.addItem("")
        self.section_supp_2.addItem("")
        self.section_supp_2.addItem("")
        self.section_supp_2.addItem("")
        self.supprimer2_2 = QtWidgets.QPushButton(self.tab_19)
        self.supprimer2_2.setGeometry(QtCore.QRect(460, 290, 151, 51))
        self.supprimer2_2.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer2_2.setObjectName("supprimer2_2")
        self.label_18 = QtWidgets.QLabel(self.tab_19)
        self.label_18.setGeometry(QtCore.QRect(390, 100, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_18.setObjectName("label_18")
        self.troisieme_3 = QtWidgets.QRadioButton(self.tab_19)
        self.troisieme_3.setGeometry(QtCore.QRect(600, 230, 81, 20))
        self.troisieme_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.troisieme_3.setObjectName("troisieme_3")
        self.label_19 = QtWidgets.QLabel(self.tab_19)
        self.label_19.setGeometry(QtCore.QRect(390, 170, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_19.setObjectName("label_19")
        self.deuxieme_3 = QtWidgets.QRadioButton(self.tab_19)
        self.deuxieme_3.setGeometry(QtCore.QRect(660, 200, 81, 20))
        self.deuxieme_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.deuxieme_3.setObjectName("deuxieme_3")
        self.premiere_3 = QtWidgets.QRadioButton(self.tab_19)
        self.premiere_3.setGeometry(QtCore.QRect(540, 200, 81, 20))
        self.premiere_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.premiere_3.setObjectName("premiere_3")
        self.sucess_sup_4 = QtWidgets.QLabel(self.tab_19)
        self.sucess_sup_4.setGeometry(QtCore.QRect(410, 320, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_4.setFont(font)
        self.sucess_sup_4.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_4.setText("")
        self.sucess_sup_4.setObjectName("sucess_sup_4")
        self.erreurni_supp_3 = QtWidgets.QLabel(self.tab_19)
        self.erreurni_supp_3.setGeometry(QtCore.QRect(540, 260, 211, 20))
        self.erreurni_supp_3.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_3.setText("")
        self.erreurni_supp_3.setObjectName("erreurni_supp_3")
        self.erreursection_sup_2 = QtWidgets.QLabel(self.tab_19)
        self.erreursection_sup_2.setGeometry(QtCore.QRect(520, 160, 261, 20))
        self.erreursection_sup_2.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreursection_sup_2.setText("")
        self.erreursection_sup_2.setObjectName("erreursection_sup_2")
        self.tabWidget_6.addTab(self.tab_19, "")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.modifier1 = QtWidgets.QTabWidget(self.tab_15)
        self.modifier1.setGeometry(QtCore.QRect(0, 0, 1101, 731))
        self.modifier1.setObjectName("modifier1")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.label_20 = QtWidgets.QLabel(self.tab_25)
        self.label_20.setGeometry(QtCore.QRect(310, 90, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_20.setObjectName("label_20")
        self.ni_supp_2 = QtWidgets.QLineEdit(self.tab_25)
        self.ni_supp_2.setGeometry(QtCore.QRect(530, 120, 211, 31))
        self.ni_supp_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni_supp_2.setObjectName("ni_supp_2")
        self.tel_2 = QtWidgets.QLineEdit(self.tab_25)
        self.tel_2.setGeometry(QtCore.QRect(530, 180, 211, 31))
        self.tel_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.tel_2.setObjectName("tel_2")
        self.label_21 = QtWidgets.QLabel(self.tab_25)
        self.label_21.setGeometry(QtCore.QRect(310, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_21.setObjectName("label_21")
        self.supprimer_3 = QtWidgets.QPushButton(self.tab_25)
        self.supprimer_3.setGeometry(QtCore.QRect(430, 250, 151, 51))
        self.supprimer_3.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer_3.setObjectName("supprimer_3")
        self.sucess_sup_5 = QtWidgets.QLabel(self.tab_25)
        self.sucess_sup_5.setGeometry(QtCore.QRect(360, 300, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_5.setFont(font)
        self.sucess_sup_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_5.setText("")
        self.sucess_sup_5.setObjectName("sucess_sup_5")
        self.erreurni_supp_4 = QtWidgets.QLabel(self.tab_25)
        self.erreurni_supp_4.setGeometry(QtCore.QRect(530, 150, 211, 20))
        self.erreurni_supp_4.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_4.setText("")
        self.erreurni_supp_4.setObjectName("erreurni_supp_4")
        self.erreurni_supp_5 = QtWidgets.QLabel(self.tab_25)
        self.erreurni_supp_5.setGeometry(QtCore.QRect(530, 210, 211, 20))
        self.erreurni_supp_5.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_5.setText("")
        self.erreurni_supp_5.setObjectName("erreurni_supp_5")
        self.modifier1.addTab(self.tab_25, "")
        self.tab_27 = QtWidgets.QWidget()
        self.tab_27.setObjectName("tab_27")
        self.supprimer_4 = QtWidgets.QPushButton(self.tab_27)
        self.supprimer_4.setGeometry(QtCore.QRect(430, 250, 151, 51))
        self.supprimer_4.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer_4.setObjectName("supprimer_4")
        self.erreurni_supp_6 = QtWidgets.QLabel(self.tab_27)
        self.erreurni_supp_6.setGeometry(QtCore.QRect(530, 150, 211, 20))
        self.erreurni_supp_6.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_6.setText("")
        self.erreurni_supp_6.setObjectName("erreurni_supp_6")
        self.label_22 = QtWidgets.QLabel(self.tab_27)
        self.label_22.setGeometry(QtCore.QRect(310, 90, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_22.setObjectName("label_22")
        self.erreurni_supp_7 = QtWidgets.QLabel(self.tab_27)
        self.erreurni_supp_7.setGeometry(QtCore.QRect(530, 210, 211, 20))
        self.erreurni_supp_7.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_7.setText("")
        self.erreurni_supp_7.setObjectName("erreurni_supp_7")
        self.label_28 = QtWidgets.QLabel(self.tab_27)
        self.label_28.setGeometry(QtCore.QRect(310, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_28.setObjectName("label_28")
        self.tel_3 = QtWidgets.QLineEdit(self.tab_27)
        self.tel_3.setGeometry(QtCore.QRect(530, 180, 211, 31))
        self.tel_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.tel_3.setObjectName("tel_3")
        self.sucess_sup_6 = QtWidgets.QLabel(self.tab_27)
        self.sucess_sup_6.setGeometry(QtCore.QRect(370, 300, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_6.setFont(font)
        self.sucess_sup_6.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_6.setText("")
        self.sucess_sup_6.setObjectName("sucess_sup_6")
        self.ni_supp_3 = QtWidgets.QLineEdit(self.tab_27)
        self.ni_supp_3.setGeometry(QtCore.QRect(530, 120, 211, 31))
        self.ni_supp_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni_supp_3.setObjectName("ni_supp_3")
        self.modifier1.addTab(self.tab_27, "")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.sucess_sup_11 = QtWidgets.QLabel(self.tab_26)
        self.sucess_sup_11.setGeometry(QtCore.QRect(370, 310, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_11.setFont(font)
        self.sucess_sup_11.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_11.setText("")
        self.sucess_sup_11.setObjectName("sucess_sup_11")
        self.supprimer_9 = QtWidgets.QPushButton(self.tab_26)
        self.supprimer_9.setGeometry(QtCore.QRect(430, 250, 151, 51))
        self.supprimer_9.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.supprimer_9.setObjectName("supprimer_9")
        self.erreurni_supp_16 = QtWidgets.QLabel(self.tab_26)
        self.erreurni_supp_16.setGeometry(QtCore.QRect(530, 150, 211, 20))
        self.erreurni_supp_16.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_16.setText("")
        self.erreurni_supp_16.setObjectName("erreurni_supp_16")
        self.erreurni_supp_17 = QtWidgets.QLabel(self.tab_26)
        self.erreurni_supp_17.setGeometry(QtCore.QRect(530, 210, 211, 20))
        self.erreurni_supp_17.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_supp_17.setText("")
        self.erreurni_supp_17.setObjectName("erreurni_supp_17")
        self.label_39 = QtWidgets.QLabel(self.tab_26)
        self.label_39.setGeometry(QtCore.QRect(310, 90, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_39.setObjectName("label_39")
        self.ni_supp_8 = QtWidgets.QLineEdit(self.tab_26)
        self.ni_supp_8.setGeometry(QtCore.QRect(530, 120, 211, 31))
        self.ni_supp_8.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni_supp_8.setObjectName("ni_supp_8")
        self.label_40 = QtWidgets.QLabel(self.tab_26)
        self.label_40.setGeometry(QtCore.QRect(310, 150, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_40.setObjectName("label_40")
        self.tel_8 = QtWidgets.QLineEdit(self.tab_26)
        self.tel_8.setGeometry(QtCore.QRect(530, 180, 211, 31))
        self.tel_8.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.tel_8.setObjectName("tel_8")
        self.modifier1.addTab(self.tab_26, "")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_8)
        self.tabWidget_4.setGeometry(QtCore.QRect(-40, -30, 1141, 781))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.tab_11)
        self.tabWidget_7.setGeometry(QtCore.QRect(40, 0, 1131, 751))
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.label_31 = QtWidgets.QLabel(self.tab_20)
        self.label_31.setGeometry(QtCore.QRect(420, 0, 581, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color :rgb(92, 121, 134);")
        self.label_31.setObjectName("label_31")
        self.afficher1 = QtWidgets.QPushButton(self.tab_20)
        self.afficher1.setGeometry(QtCore.QRect(480, 100, 121, 41))
        self.afficher1.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1.setObjectName("afficher1")
        self.label_46 = QtWidgets.QLabel(self.tab_20)
        self.label_46.setGeometry(QtCore.QRect(20, 150, 1061, 531))
        self.label_46.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.tabWidget_7.addTab(self.tab_20, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.ni_affiche = QtWidgets.QLineEdit(self.tab_22)
        self.ni_affiche.setGeometry(QtCore.QRect(540, 110, 211, 31))
        self.ni_affiche.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni_affiche.setObjectName("ni_affiche")
        self.label_23 = QtWidgets.QLabel(self.tab_22)
        self.label_23.setGeometry(QtCore.QRect(330, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_23.setObjectName("label_23")
        self.label_47 = QtWidgets.QLabel(self.tab_22)
        self.label_47.setGeometry(QtCore.QRect(30, 260, 1051, 171))
        self.label_47.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.afficher2 = QtWidgets.QPushButton(self.tab_22)
        self.afficher2.setGeometry(QtCore.QRect(470, 190, 131, 51))
        self.afficher2.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher2.setObjectName("afficher2")
        self.erreurni_affiche = QtWidgets.QLabel(self.tab_22)
        self.erreurni_affiche.setGeometry(QtCore.QRect(540, 140, 221, 16))
        self.erreurni_affiche.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_affiche.setText("")
        self.erreurni_affiche.setObjectName("erreurni_affiche")
        self.tabWidget_7.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.label_24 = QtWidgets.QLabel(self.tab_23)
        self.label_24.setGeometry(QtCore.QRect(400, 50, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_24.setObjectName("label_24")
        self.label_48 = QtWidgets.QLabel(self.tab_23)
        self.label_48.setGeometry(QtCore.QRect(30, 230, 1051, 441))
        self.label_48.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.afficher3 = QtWidgets.QPushButton(self.tab_23)
        self.afficher3.setGeometry(QtCore.QRect(470, 140, 131, 51))
        self.afficher3.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher3.setObjectName("afficher3")
        self.erreursection_affiche = QtWidgets.QLabel(self.tab_23)
        self.erreursection_affiche.setGeometry(QtCore.QRect(520, 110, 241, 16))
        self.erreursection_affiche.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreursection_affiche.setText("")
        self.erreursection_affiche.setObjectName("erreursection_affiche")
        self.section_2 = QtWidgets.QComboBox(self.tab_23)
        self.section_2.setGeometry(QtCore.QRect(520, 80, 211, 31))
        self.section_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.section_2.setObjectName("section_2")
        self.section_2.addItem("")
        self.section_2.addItem("")
        self.section_2.addItem("")
        self.section_2.addItem("")
        self.section_2.addItem("")
        self.section_2.addItem("")
        self.tabWidget_7.addTab(self.tab_23, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.label_27 = QtWidgets.QLabel(self.tab_21)
        self.label_27.setGeometry(QtCore.QRect(410, 20, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_27.setObjectName("label_27")
        self.afficher4 = QtWidgets.QPushButton(self.tab_21)
        self.afficher4.setGeometry(QtCore.QRect(470, 140, 131, 51))
        self.afficher4.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher4.setObjectName("afficher4")
        self.label_49 = QtWidgets.QLabel(self.tab_21)
        self.label_49.setGeometry(QtCore.QRect(30, 230, 1051, 441))
        self.label_49.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.erreurniveau_affiche = QtWidgets.QLabel(self.tab_21)
        self.erreurniveau_affiche.setGeometry(QtCore.QRect(510, 120, 221, 16))
        self.erreurniveau_affiche.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurniveau_affiche.setText("")
        self.erreurniveau_affiche.setObjectName("erreurniveau_affiche")
        self.deuxieme_4 = QtWidgets.QRadioButton(self.tab_21)
        self.deuxieme_4.setGeometry(QtCore.QRect(630, 50, 81, 20))
        self.deuxieme_4.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.deuxieme_4.setObjectName("deuxieme_4")
        self.premiere_4 = QtWidgets.QRadioButton(self.tab_21)
        self.premiere_4.setGeometry(QtCore.QRect(510, 50, 81, 20))
        self.premiere_4.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.premiere_4.setObjectName("premiere_4")
        self.troisieme_4 = QtWidgets.QRadioButton(self.tab_21)
        self.troisieme_4.setGeometry(QtCore.QRect(570, 80, 81, 20))
        self.troisieme_4.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.troisieme_4.setObjectName("troisieme_4")
        self.tabWidget_7.addTab(self.tab_21, "")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.label_25 = QtWidgets.QLabel(self.tab_24)
        self.label_25.setGeometry(QtCore.QRect(390, 20, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_24)
        self.label_26.setGeometry(QtCore.QRect(390, 90, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_26.setObjectName("label_26")
        self.afficher5 = QtWidgets.QPushButton(self.tab_24)
        self.afficher5.setGeometry(QtCore.QRect(470, 200, 131, 51))
        self.afficher5.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher5.setObjectName("afficher5")
        self.label_50 = QtWidgets.QLabel(self.tab_24)
        self.label_50.setGeometry(QtCore.QRect(20, 270, 1051, 391))
        self.label_50.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.erreurni_12 = QtWidgets.QLabel(self.tab_24)
        self.erreurni_12.setGeometry(QtCore.QRect(510, 80, 271, 16))
        self.erreurni_12.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_12.setText("")
        self.erreurni_12.setObjectName("erreurni_12")
        self.erreurni_13 = QtWidgets.QLabel(self.tab_24)
        self.erreurni_13.setGeometry(QtCore.QRect(510, 170, 251, 16))
        self.erreurni_13.setAutoFillBackground(False)
        self.erreurni_13.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_13.setText("")
        self.erreurni_13.setObjectName("erreurni_13")
        self.section_3 = QtWidgets.QComboBox(self.tab_24)
        self.section_3.setGeometry(QtCore.QRect(510, 50, 211, 31))
        self.section_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.section_3.setObjectName("section_3")
        self.section_3.addItem("")
        self.section_3.addItem("")
        self.section_3.addItem("")
        self.section_3.addItem("")
        self.section_3.addItem("")
        self.section_3.addItem("")
        self.deuxieme_5 = QtWidgets.QRadioButton(self.tab_24)
        self.deuxieme_5.setGeometry(QtCore.QRect(640, 120, 81, 20))
        self.deuxieme_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.deuxieme_5.setObjectName("deuxieme_5")
        self.troisieme_5 = QtWidgets.QRadioButton(self.tab_24)
        self.troisieme_5.setGeometry(QtCore.QRect(580, 150, 81, 20))
        self.troisieme_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.troisieme_5.setObjectName("troisieme_5")
        self.premiere_5 = QtWidgets.QRadioButton(self.tab_24)
        self.premiere_5.setGeometry(QtCore.QRect(520, 120, 81, 20))
        self.premiere_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.premiere_5.setObjectName("premiere_5")
        self.tabWidget_7.addTab(self.tab_24, "")
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_12)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 341, 131))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_5.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tabWidget_5.addTab(self.tab_14, "")
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_10 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_10.setGeometry(QtCore.QRect(0, 0, 1111, 781))
        self.tabWidget_10.setObjectName("tabWidget_10")
        self.tab_30 = QtWidgets.QWidget()
        self.tab_30.setObjectName("tab_30")
        self.tabWidget_11 = QtWidgets.QTabWidget(self.tab_30)
        self.tabWidget_11.setGeometry(QtCore.QRect(0, 0, 1101, 751))
        self.tabWidget_11.setStyleSheet("")
        self.tabWidget_11.setObjectName("tabWidget_11")
        self.tab_32 = QtWidgets.QWidget()
        self.tab_32.setObjectName("tab_32")
        self.label_51 = QtWidgets.QLabel(self.tab_32)
        self.label_51.setGeometry(QtCore.QRect(20, 10, 1061, 671))
        self.label_51.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"border-radius: 30px;")
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.ajouter_2 = QtWidgets.QPushButton(self.tab_32)
        self.ajouter_2.setGeometry(QtCore.QRect(420, 600, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.ajouter_2.setFont(font)
        self.ajouter_2.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.ajouter_2.setObjectName("ajouter_2")
        self.label_58 = QtWidgets.QLabel(self.tab_32)
        self.label_58.setGeometry(QtCore.QRect(260, 170, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_58.setObjectName("label_58")
        self.line_3 = QtWidgets.QFrame(self.tab_32)
        self.line_3.setGeometry(QtCore.QRect(240, 510, 591, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.erreurni_5 = QtWidgets.QLabel(self.tab_32)
        self.erreurni_5.setGeometry(QtCore.QRect(550, 430, 251, 16))
        self.erreurni_5.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_5.setText("")
        self.erreurni_5.setObjectName("erreurni_5")
        self.label_57 = QtWidgets.QLabel(self.tab_32)
        self.label_57.setGeometry(QtCore.QRect(260, 290, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_57.setObjectName("label_57")
        self.erreurni_2 = QtWidgets.QLabel(self.tab_32)
        self.erreurni_2.setGeometry(QtCore.QRect(550, 230, 251, 16))
        self.erreurni_2.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_2.setText("")
        self.erreurni_2.setObjectName("erreurni_2")
        self.erreurni_3 = QtWidgets.QLabel(self.tab_32)
        self.erreurni_3.setGeometry(QtCore.QRect(550, 290, 251, 16))
        self.erreurni_3.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_3.setText("")
        self.erreurni_3.setObjectName("erreurni_3")
        self.mail_2 = QtWidgets.QLineEdit(self.tab_32)
        self.mail_2.setGeometry(QtCore.QRect(550, 400, 211, 31))
        self.mail_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.mail_2.setObjectName("mail_2")
        self.tel_9 = QtWidgets.QLineEdit(self.tab_32)
        self.tel_9.setGeometry(QtCore.QRect(550, 470, 211, 31))
        self.tel_9.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.tel_9.setObjectName("tel_9")
        self.nom_2 = QtWidgets.QLineEdit(self.tab_32)
        self.nom_2.setGeometry(QtCore.QRect(550, 200, 211, 31))
        self.nom_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.nom_2.setObjectName("nom_2")
        self.label_62 = QtWidgets.QLabel(self.tab_32)
        self.label_62.setGeometry(QtCore.QRect(440, 40, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_62.setObjectName("label_62")
        self.prenom_2 = QtWidgets.QLineEdit(self.tab_32)
        self.prenom_2.setGeometry(QtCore.QRect(550, 260, 211, 31))
        self.prenom_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.prenom_2.setObjectName("prenom_2")
        self.label_61 = QtWidgets.QLabel(self.tab_32)
        self.label_61.setGeometry(QtCore.QRect(260, 230, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_61.setObjectName("label_61")
        self.adresse_2 = QtWidgets.QLineEdit(self.tab_32)
        self.adresse_2.setGeometry(QtCore.QRect(550, 330, 211, 31))
        self.adresse_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.adresse_2.setObjectName("adresse_2")
        self.label_60 = QtWidgets.QLabel(self.tab_32)
        self.label_60.setGeometry(QtCore.QRect(260, 440, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_60.setObjectName("label_60")
        self.erreurni_4 = QtWidgets.QLabel(self.tab_32)
        self.erreurni_4.setGeometry(QtCore.QRect(550, 360, 251, 16))
        self.erreurni_4.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_4.setText("")
        self.erreurni_4.setObjectName("erreurni_4")
        self.label_59 = QtWidgets.QLabel(self.tab_32)
        self.label_59.setGeometry(QtCore.QRect(260, 370, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_59.setObjectName("label_59")
        self.erreurni_6 = QtWidgets.QLabel(self.tab_32)
        self.erreurni_6.setGeometry(QtCore.QRect(550, 500, 251, 16))
        self.erreurni_6.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_6.setText("")
        self.erreurni_6.setObjectName("erreurni_6")
        self.label_30 = QtWidgets.QLabel(self.tab_32)
        self.label_30.setGeometry(QtCore.QRect(370, 550, 351, 41))
        self.label_30.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.tabWidget_11.addTab(self.tab_32, "")
        self.tab_34 = QtWidgets.QWidget()
        self.tab_34.setObjectName("tab_34")
        self.tabWidget_12 = QtWidgets.QTabWidget(self.tab_34)
        self.tabWidget_12.setGeometry(QtCore.QRect(0, 0, 1111, 721))
        self.tabWidget_12.setStyleSheet("color: rgb(92, 121, 134);")
        self.tabWidget_12.setObjectName("tabWidget_12")
        self.tab_35 = QtWidgets.QWidget()
        self.tab_35.setObjectName("tab_35")
        self.nom_3 = QtWidgets.QLineEdit(self.tab_35)
        self.nom_3.setGeometry(QtCore.QRect(520, 160, 211, 31))
        self.nom_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.nom_3.setObjectName("nom_3")
        self.label_98 = QtWidgets.QLabel(self.tab_35)
        self.label_98.setGeometry(QtCore.QRect(370, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_98.setFont(font)
        self.label_98.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_98.setObjectName("label_98")
        self.erreurni_7 = QtWidgets.QLabel(self.tab_35)
        self.erreurni_7.setGeometry(QtCore.QRect(520, 190, 251, 16))
        self.erreurni_7.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_7.setText("")
        self.erreurni_7.setObjectName("erreurni_7")
        self.ajouter_3 = QtWidgets.QPushButton(self.tab_35)
        self.ajouter_3.setGeometry(QtCore.QRect(430, 240, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.ajouter_3.setFont(font)
        self.ajouter_3.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.ajouter_3.setObjectName("ajouter_3")
        self.sucess_sup_7 = QtWidgets.QLabel(self.tab_35)
        self.sucess_sup_7.setGeometry(QtCore.QRect(390, 270, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_7.setFont(font)
        self.sucess_sup_7.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_7.setText("")
        self.sucess_sup_7.setObjectName("sucess_sup_7")
        self.tabWidget_12.addTab(self.tab_35, "")
        self.tab_37 = QtWidgets.QWidget()
        self.tab_37.setObjectName("tab_37")
        self.label_64 = QtWidgets.QLabel(self.tab_37)
        self.label_64.setGeometry(QtCore.QRect(400, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.nom_4 = QtWidgets.QLineEdit(self.tab_37)
        self.nom_4.setGeometry(QtCore.QRect(520, 160, 211, 31))
        self.nom_4.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.nom_4.setObjectName("nom_4")
        self.ajouter_4 = QtWidgets.QPushButton(self.tab_37)
        self.ajouter_4.setGeometry(QtCore.QRect(430, 240, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.ajouter_4.setFont(font)
        self.ajouter_4.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.ajouter_4.setObjectName("ajouter_4")
        self.erreurni_8 = QtWidgets.QLabel(self.tab_37)
        self.erreurni_8.setGeometry(QtCore.QRect(520, 190, 251, 16))
        self.erreurni_8.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_8.setText("")
        self.erreurni_8.setObjectName("erreurni_8")
        self.sucess_sup_8 = QtWidgets.QLabel(self.tab_37)
        self.sucess_sup_8.setGeometry(QtCore.QRect(390, 260, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_8.setFont(font)
        self.sucess_sup_8.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_8.setText("")
        self.sucess_sup_8.setObjectName("sucess_sup_8")
        self.tabWidget_12.addTab(self.tab_37, "")
        self.tab_36 = QtWidgets.QWidget()
        self.tab_36.setObjectName("tab_36")
        self.label_65 = QtWidgets.QLabel(self.tab_36)
        self.label_65.setGeometry(QtCore.QRect(400, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.ajouter_5 = QtWidgets.QPushButton(self.tab_36)
        self.ajouter_5.setGeometry(QtCore.QRect(430, 240, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.ajouter_5.setFont(font)
        self.ajouter_5.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.ajouter_5.setObjectName("ajouter_5")
        self.nom_5 = QtWidgets.QLineEdit(self.tab_36)
        self.nom_5.setGeometry(QtCore.QRect(520, 160, 211, 31))
        self.nom_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.nom_5.setObjectName("nom_5")
        self.erreurni_9 = QtWidgets.QLabel(self.tab_36)
        self.erreurni_9.setGeometry(QtCore.QRect(520, 190, 251, 16))
        self.erreurni_9.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_9.setText("")
        self.erreurni_9.setObjectName("erreurni_9")
        self.sucess_sup_9 = QtWidgets.QLabel(self.tab_36)
        self.sucess_sup_9.setGeometry(QtCore.QRect(390, 260, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_9.setFont(font)
        self.sucess_sup_9.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_9.setText("")
        self.sucess_sup_9.setObjectName("sucess_sup_9")
        self.tabWidget_12.addTab(self.tab_36, "")
        self.tabWidget_11.addTab(self.tab_34, "")
        self.tab_33 = QtWidgets.QWidget()
        self.tab_33.setObjectName("tab_33")
        self.line_4 = QtWidgets.QFrame(self.tab_33)
        self.line_4.setGeometry(QtCore.QRect(320, 260, 491, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_33)
        self.pushButton_28.setGeometry(QtCore.QRect(470, 300, 151, 51))
        self.pushButton_28.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_60.setGeometry(QtCore.QRect(600, 190, 211, 31))
        self.lineEdit_60.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.tab_33)
        self.lineEdit_61.setGeometry(QtCore.QRect(600, 130, 211, 31))
        self.lineEdit_61.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.label_66 = QtWidgets.QLabel(self.tab_33)
        self.label_66.setGeometry(QtCore.QRect(320, 160, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.tab_33)
        self.label_67.setGeometry(QtCore.QRect(320, 100, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(92, 121, 134);")
        self.label_67.setObjectName("label_67")
        self.erreurni_10 = QtWidgets.QLabel(self.tab_33)
        self.erreurni_10.setGeometry(QtCore.QRect(600, 160, 251, 16))
        self.erreurni_10.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_10.setText("")
        self.erreurni_10.setObjectName("erreurni_10")
        self.erreurni_11 = QtWidgets.QLabel(self.tab_33)
        self.erreurni_11.setGeometry(QtCore.QRect(600, 220, 251, 16))
        self.erreurni_11.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_11.setText("")
        self.erreurni_11.setObjectName("erreurni_11")
        self.sucess_sup_10 = QtWidgets.QLabel(self.tab_33)
        self.sucess_sup_10.setGeometry(QtCore.QRect(390, 340, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.sucess_sup_10.setFont(font)
        self.sucess_sup_10.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 20pt \"Segoe UI Black\";\n"
"")
        self.sucess_sup_10.setText("")
        self.sucess_sup_10.setObjectName("sucess_sup_10")
        self.tabWidget_11.addTab(self.tab_33, "")
        self.tabWidget_10.addTab(self.tab_30, "")
        self.tab_31 = QtWidgets.QWidget()
        self.tab_31.setObjectName("tab_31")
        self.tabWidget_13 = QtWidgets.QTabWidget(self.tab_31)
        self.tabWidget_13.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.tabWidget_13.setObjectName("tabWidget_13")
        self.tab_38 = QtWidgets.QWidget()
        self.tab_38.setObjectName("tab_38")
        self.label_52 = QtWidgets.QLabel(self.tab_38)
        self.label_52.setGeometry(QtCore.QRect(20, 150, 1061, 531))
        self.label_52.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_52.setText("")
        self.label_52.setObjectName("label_52")
        self.label_41 = QtWidgets.QLabel(self.tab_38)
        self.label_41.setGeometry(QtCore.QRect(430, 0, 581, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color :rgb(92, 121, 134);")
        self.label_41.setObjectName("label_41")
        self.afficher1_2 = QtWidgets.QPushButton(self.tab_38)
        self.afficher1_2.setGeometry(QtCore.QRect(470, 100, 121, 41))
        self.afficher1_2.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1_2.setObjectName("afficher1_2")
        self.tabWidget_13.addTab(self.tab_38, "")
        self.tab_40 = QtWidgets.QWidget()
        self.tab_40.setObjectName("tab_40")
        self.label_68 = QtWidgets.QLabel(self.tab_40)
        self.label_68.setGeometry(QtCore.QRect(360, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.tab_40)
        self.lineEdit_62.setGeometry(QtCore.QRect(530, 110, 211, 31))
        self.lineEdit_62.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.line_5 = QtWidgets.QFrame(self.tab_40)
        self.line_5.setGeometry(QtCore.QRect(360, 160, 371, 31))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_53 = QtWidgets.QLabel(self.tab_40)
        self.label_53.setGeometry(QtCore.QRect(30, 280, 1051, 171))
        self.label_53.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.afficher1_3 = QtWidgets.QPushButton(self.tab_40)
        self.afficher1_3.setGeometry(QtCore.QRect(470, 200, 121, 41))
        self.afficher1_3.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1_3.setObjectName("afficher1_3")
        self.erreurni_14 = QtWidgets.QLabel(self.tab_40)
        self.erreurni_14.setGeometry(QtCore.QRect(530, 140, 251, 16))
        self.erreurni_14.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_14.setText("")
        self.erreurni_14.setObjectName("erreurni_14")
        self.tabWidget_13.addTab(self.tab_40, "")
        self.tab_41 = QtWidgets.QWidget()
        self.tab_41.setObjectName("tab_41")
        self.line_6 = QtWidgets.QFrame(self.tab_41)
        self.line_6.setGeometry(QtCore.QRect(360, 160, 371, 31))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.tab_41)
        self.lineEdit_63.setGeometry(QtCore.QRect(530, 110, 211, 31))
        self.lineEdit_63.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.label_54 = QtWidgets.QLabel(self.tab_41)
        self.label_54.setGeometry(QtCore.QRect(30, 280, 1051, 401))
        self.label_54.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")
        self.erreurni_15 = QtWidgets.QLabel(self.tab_41)
        self.erreurni_15.setGeometry(QtCore.QRect(530, 140, 251, 16))
        self.erreurni_15.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_15.setText("")
        self.erreurni_15.setObjectName("erreurni_15")
        self.afficher1_4 = QtWidgets.QPushButton(self.tab_41)
        self.afficher1_4.setGeometry(QtCore.QRect(470, 200, 121, 41))
        self.afficher1_4.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1_4.setObjectName("afficher1_4")
        self.label_69 = QtWidgets.QLabel(self.tab_41)
        self.label_69.setGeometry(QtCore.QRect(390, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.tabWidget_13.addTab(self.tab_41, "")
        self.tab_42 = QtWidgets.QWidget()
        self.tab_42.setObjectName("tab_42")
        self.line_7 = QtWidgets.QFrame(self.tab_42)
        self.line_7.setGeometry(QtCore.QRect(360, 160, 371, 31))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.tab_42)
        self.lineEdit_64.setGeometry(QtCore.QRect(530, 110, 211, 31))
        self.lineEdit_64.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.label_55 = QtWidgets.QLabel(self.tab_42)
        self.label_55.setGeometry(QtCore.QRect(30, 280, 1051, 401))
        self.label_55.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_55.setText("")
        self.label_55.setObjectName("label_55")
        self.erreurni_16 = QtWidgets.QLabel(self.tab_42)
        self.erreurni_16.setGeometry(QtCore.QRect(530, 140, 251, 16))
        self.erreurni_16.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_16.setText("")
        self.erreurni_16.setObjectName("erreurni_16")
        self.afficher1_5 = QtWidgets.QPushButton(self.tab_42)
        self.afficher1_5.setGeometry(QtCore.QRect(470, 200, 121, 41))
        self.afficher1_5.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1_5.setObjectName("afficher1_5")
        self.label_70 = QtWidgets.QLabel(self.tab_42)
        self.label_70.setGeometry(QtCore.QRect(360, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.tabWidget_13.addTab(self.tab_42, "")
        self.tab_43 = QtWidgets.QWidget()
        self.tab_43.setObjectName("tab_43")
        self.line_8 = QtWidgets.QFrame(self.tab_43)
        self.line_8.setGeometry(QtCore.QRect(360, 160, 371, 31))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.tab_43)
        self.lineEdit_65.setGeometry(QtCore.QRect(530, 110, 211, 31))
        self.lineEdit_65.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.label_56 = QtWidgets.QLabel(self.tab_43)
        self.label_56.setGeometry(QtCore.QRect(30, 280, 1051, 401))
        self.label_56.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.erreurni_17 = QtWidgets.QLabel(self.tab_43)
        self.erreurni_17.setGeometry(QtCore.QRect(530, 140, 251, 16))
        self.erreurni_17.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_17.setText("")
        self.erreurni_17.setObjectName("erreurni_17")
        self.afficher1_6 = QtWidgets.QPushButton(self.tab_43)
        self.afficher1_6.setGeometry(QtCore.QRect(470, 200, 121, 41))
        self.afficher1_6.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1_6.setObjectName("afficher1_6")
        self.label_71 = QtWidgets.QLabel(self.tab_43)
        self.label_71.setGeometry(QtCore.QRect(360, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.tabWidget_13.addTab(self.tab_43, "")
        self.tab_39 = QtWidgets.QWidget()
        self.tab_39.setObjectName("tab_39")
        self.label_63 = QtWidgets.QLabel(self.tab_39)
        self.label_63.setGeometry(QtCore.QRect(20, 150, 1061, 531))
        self.label_63.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.label_42 = QtWidgets.QLabel(self.tab_39)
        self.label_42.setGeometry(QtCore.QRect(350, 0, 581, 111))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color :rgb(92, 121, 134);")
        self.label_42.setObjectName("label_42")
        self.afficher1_7 = QtWidgets.QPushButton(self.tab_39)
        self.afficher1_7.setGeometry(QtCore.QRect(480, 90, 121, 41))
        self.afficher1_7.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"border-radius: 4px;\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(92, 121, 134);")
        self.afficher1_7.setObjectName("afficher1_7")
        self.tabWidget_13.addTab(self.tab_39, "")
        self.tabWidget_10.addTab(self.tab_31, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_9 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_9.setGeometry(QtCore.QRect(0, 0, 1111, 781))
        self.tabWidget_9.setObjectName("tabWidget_9")
        self.tab_28 = QtWidgets.QWidget()
        self.tab_28.setObjectName("tab_28")
        self.tabWidget_14 = QtWidgets.QTabWidget(self.tab_28)
        self.tabWidget_14.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.tabWidget_14.setObjectName("tabWidget_14")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_99 = QtWidgets.QLabel(self.tab_6)
        self.label_99.setGeometry(QtCore.QRect(20, 10, 1061, 681))
        self.label_99.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"border-radius: 30px;")
        self.label_99.setText("")
        self.label_99.setObjectName("label_99")
        self.label_77 = QtWidgets.QLabel(self.tab_6)
        self.label_77.setGeometry(QtCore.QRect(410, 90, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_77.setFont(font)
        self.label_77.setStyleSheet("\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_77.setObjectName("label_77")
        self.label_76 = QtWidgets.QLabel(self.tab_6)
        self.label_76.setGeometry(QtCore.QRect(320, 180, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.label_74 = QtWidgets.QLabel(self.tab_6)
        self.label_74.setGeometry(QtCore.QRect(320, 240, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.erreurni_18 = QtWidgets.QLabel(self.tab_6)
        self.erreurni_18.setGeometry(QtCore.QRect(540, 240, 291, 16))
        self.erreurni_18.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_18.setText("")
        self.erreurni_18.setObjectName("erreurni_18")
        self.erreurni_21 = QtWidgets.QLabel(self.tab_6)
        self.erreurni_21.setGeometry(QtCore.QRect(510, 360, 251, 16))
        self.erreurni_21.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.erreurni_21.setText("")
        self.erreurni_21.setObjectName("erreurni_21")
        self.line_9 = QtWidgets.QFrame(self.tab_6)
        self.line_9.setGeometry(QtCore.QRect(250, 380, 591, 31))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.erreurni_19 = QtWidgets.QLabel(self.tab_6)
        self.erreurni_19.setGeometry(QtCore.QRect(540, 300, 291, 16))
        self.erreurni_19.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_19.setText("")
        self.erreurni_19.setObjectName("erreurni_19")
        self.ni_2 = QtWidgets.QLineEdit(self.tab_6)
        self.ni_2.setGeometry(QtCore.QRect(540, 210, 211, 31))
        self.ni_2.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.ni_2.setObjectName("ni_2")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_34.setGeometry(QtCore.QRect(450, 480, 181, 71))
        self.pushButton_34.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_34.setObjectName("pushButton_34")
        self.nom_6 = QtWidgets.QLineEdit(self.tab_6)
        self.nom_6.setGeometry(QtCore.QRect(540, 270, 211, 31))
        self.nom_6.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.nom_6.setObjectName("nom_6")
        self.label_32 = QtWidgets.QLabel(self.tab_6)
        self.label_32.setGeometry(QtCore.QRect(370, 420, 381, 41))
        self.label_32.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_6)
        self.label_33.setGeometry(QtCore.QRect(370, 430, 931, 41))
        self.label_33.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.tabWidget_14.addTab(self.tab_6, "")
        self.tab_45 = QtWidgets.QWidget()
        self.tab_45.setObjectName("tab_45")
        self.lineEdit_68 = QtWidgets.QLineEdit(self.tab_45)
        self.lineEdit_68.setGeometry(QtCore.QRect(590, 100, 211, 31))
        self.lineEdit_68.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.lineEdit_70 = QtWidgets.QLineEdit(self.tab_45)
        self.lineEdit_70.setGeometry(QtCore.QRect(590, 160, 211, 31))
        self.lineEdit_70.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.label_78 = QtWidgets.QLabel(self.tab_45)
        self.label_78.setGeometry(QtCore.QRect(330, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.tab_45)
        self.label_79.setGeometry(QtCore.QRect(330, 70, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.line_10 = QtWidgets.QFrame(self.tab_45)
        self.line_10.setGeometry(QtCore.QRect(280, 230, 591, 31))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.pushButton_36 = QtWidgets.QPushButton(self.tab_45)
        self.pushButton_36.setGeometry(QtCore.QRect(480, 340, 181, 71))
        self.pushButton_36.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_36.setObjectName("pushButton_36")
        self.erreurni_22 = QtWidgets.QLabel(self.tab_45)
        self.erreurni_22.setGeometry(QtCore.QRect(590, 130, 281, 16))
        self.erreurni_22.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_22.setText("")
        self.erreurni_22.setObjectName("erreurni_22")
        self.erreurni_23 = QtWidgets.QLabel(self.tab_45)
        self.erreurni_23.setGeometry(QtCore.QRect(590, 190, 301, 16))
        self.erreurni_23.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_23.setText("")
        self.erreurni_23.setObjectName("erreurni_23")
        self.erreurni_24 = QtWidgets.QLabel(self.tab_45)
        self.erreurni_24.setGeometry(QtCore.QRect(570, 260, 251, 16))
        self.erreurni_24.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.erreurni_24.setText("")
        self.erreurni_24.setObjectName("erreurni_24")
        self.label_34 = QtWidgets.QLabel(self.tab_45)
        self.label_34.setGeometry(QtCore.QRect(450, 290, 931, 41))
        self.label_34.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.tabWidget_14.addTab(self.tab_45, "")
        self.tab_46 = QtWidgets.QWidget()
        self.tab_46.setObjectName("tab_46")
        self.label_80 = QtWidgets.QLabel(self.tab_46)
        self.label_80.setGeometry(QtCore.QRect(340, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.lineEdit_71 = QtWidgets.QLineEdit(self.tab_46)
        self.lineEdit_71.setGeometry(QtCore.QRect(600, 100, 211, 31))
        self.lineEdit_71.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.lineEdit_72 = QtWidgets.QLineEdit(self.tab_46)
        self.lineEdit_72.setGeometry(QtCore.QRect(600, 160, 211, 31))
        self.lineEdit_72.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.label_81 = QtWidgets.QLabel(self.tab_46)
        self.label_81.setGeometry(QtCore.QRect(340, 70, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.line_11 = QtWidgets.QFrame(self.tab_46)
        self.line_11.setGeometry(QtCore.QRect(300, 290, 591, 31))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_46)
        self.pushButton_37.setGeometry(QtCore.QRect(470, 400, 181, 71))
        self.pushButton_37.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_37.setObjectName("pushButton_37")
        self.erreurni_25 = QtWidgets.QLabel(self.tab_46)
        self.erreurni_25.setGeometry(QtCore.QRect(600, 130, 251, 16))
        self.erreurni_25.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_25.setText("")
        self.erreurni_25.setObjectName("erreurni_25")
        self.erreurni_26 = QtWidgets.QLabel(self.tab_46)
        self.erreurni_26.setGeometry(QtCore.QRect(600, 190, 251, 16))
        self.erreurni_26.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_26.setText("")
        self.erreurni_26.setObjectName("erreurni_26")
        self.label_35 = QtWidgets.QLabel(self.tab_46)
        self.label_35.setGeometry(QtCore.QRect(460, 340, 931, 41))
        self.label_35.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.label_103 = QtWidgets.QLabel(self.tab_46)
        self.label_103.setGeometry(QtCore.QRect(340, 190, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_103.setFont(font)
        self.label_103.setObjectName("label_103")
        self.date_3 = QtWidgets.QDateEdit(self.tab_46)
        self.date_3.setGeometry(QtCore.QRect(600, 220, 211, 31))
        self.date_3.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;")
        self.date_3.setObjectName("date_3")
        self.tabWidget_14.addTab(self.tab_46, "")
        self.tab_44 = QtWidgets.QWidget()
        self.tab_44.setObjectName("tab_44")
        self.tabWidget_15 = QtWidgets.QTabWidget(self.tab_44)
        self.tabWidget_15.setGeometry(QtCore.QRect(0, 0, 1101, 731))
        self.tabWidget_15.setObjectName("tabWidget_15")
        self.tab_47 = QtWidgets.QWidget()
        self.tab_47.setObjectName("tab_47")
        self.lineEdit_73 = QtWidgets.QLineEdit(self.tab_47)
        self.lineEdit_73.setGeometry(QtCore.QRect(580, 100, 211, 31))
        self.lineEdit_73.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.lineEdit_74 = QtWidgets.QLineEdit(self.tab_47)
        self.lineEdit_74.setGeometry(QtCore.QRect(580, 160, 211, 31))
        self.lineEdit_74.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.label_82 = QtWidgets.QLabel(self.tab_47)
        self.label_82.setGeometry(QtCore.QRect(320, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.tab_47)
        self.label_83.setGeometry(QtCore.QRect(320, 70, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab_47)
        self.dateEdit_5.setGeometry(QtCore.QRect(580, 270, 211, 31))
        self.dateEdit_5.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.label_84 = QtWidgets.QLabel(self.tab_47)
        self.label_84.setGeometry(QtCore.QRect(320, 240, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.line_12 = QtWidgets.QFrame(self.tab_47)
        self.line_12.setGeometry(QtCore.QRect(260, 310, 591, 31))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.pushButton_38 = QtWidgets.QPushButton(self.tab_47)
        self.pushButton_38.setGeometry(QtCore.QRect(470, 410, 181, 71))
        self.pushButton_38.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_38.setObjectName("pushButton_38")
        self.erreurni_30 = QtWidgets.QLabel(self.tab_47)
        self.erreurni_30.setGeometry(QtCore.QRect(550, 60, 251, 16))
        self.erreurni_30.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.erreurni_30.setText("")
        self.erreurni_30.setObjectName("erreurni_30")
        self.erreurni_31 = QtWidgets.QLabel(self.tab_47)
        self.erreurni_31.setGeometry(QtCore.QRect(580, 130, 251, 16))
        self.erreurni_31.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_31.setText("")
        self.erreurni_31.setObjectName("erreurni_31")
        self.erreurni_32 = QtWidgets.QLabel(self.tab_47)
        self.erreurni_32.setGeometry(QtCore.QRect(580, 190, 251, 16))
        self.erreurni_32.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_32.setText("")
        self.erreurni_32.setObjectName("erreurni_32")
        self.erreurni_33 = QtWidgets.QLabel(self.tab_47)
        self.erreurni_33.setGeometry(QtCore.QRect(580, 260, 251, 16))
        self.erreurni_33.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_33.setText("")
        self.erreurni_33.setObjectName("erreurni_33")
        self.label_37 = QtWidgets.QLabel(self.tab_47)
        self.label_37.setGeometry(QtCore.QRect(440, 360, 931, 41))
        self.label_37.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.label_108 = QtWidgets.QLabel(self.tab_47)
        self.label_108.setGeometry(QtCore.QRect(320, 190, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_108.setFont(font)
        self.label_108.setObjectName("label_108")
        self.dateEdit_13 = QtWidgets.QDateEdit(self.tab_47)
        self.dateEdit_13.setGeometry(QtCore.QRect(580, 210, 211, 31))
        self.dateEdit_13.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_13.setObjectName("dateEdit_13")
        self.label_38 = QtWidgets.QLabel(self.tab_47)
        self.label_38.setGeometry(QtCore.QRect(260, 10, 931, 41))
        self.label_38.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_38.setObjectName("label_38")
        self.tabWidget_15.addTab(self.tab_47, "")
        self.tab_48 = QtWidgets.QWidget()
        self.tab_48.setObjectName("tab_48")
        self.lineEdit_75 = QtWidgets.QLineEdit(self.tab_48)
        self.lineEdit_75.setGeometry(QtCore.QRect(580, 160, 211, 31))
        self.lineEdit_75.setAutoFillBackground(False)
        self.lineEdit_75.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.lineEdit_76 = QtWidgets.QLineEdit(self.tab_48)
        self.lineEdit_76.setGeometry(QtCore.QRect(580, 100, 211, 31))
        self.lineEdit_76.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.pushButton_39 = QtWidgets.QPushButton(self.tab_48)
        self.pushButton_39.setGeometry(QtCore.QRect(470, 410, 181, 71))
        self.pushButton_39.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_39.setObjectName("pushButton_39")
        self.line_13 = QtWidgets.QFrame(self.tab_48)
        self.line_13.setGeometry(QtCore.QRect(260, 310, 591, 31))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.label_85 = QtWidgets.QLabel(self.tab_48)
        self.label_85.setGeometry(QtCore.QRect(320, 70, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.tab_48)
        self.label_86.setGeometry(QtCore.QRect(320, 240, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.tab_48)
        self.label_87.setGeometry(QtCore.QRect(320, 130, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.tab_48)
        self.dateEdit_6.setGeometry(QtCore.QRect(580, 270, 211, 31))
        self.dateEdit_6.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.erreurni_27 = QtWidgets.QLabel(self.tab_48)
        self.erreurni_27.setGeometry(QtCore.QRect(580, 130, 251, 16))
        self.erreurni_27.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_27.setText("")
        self.erreurni_27.setObjectName("erreurni_27")
        self.erreurni_28 = QtWidgets.QLabel(self.tab_48)
        self.erreurni_28.setGeometry(QtCore.QRect(580, 190, 251, 16))
        self.erreurni_28.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_28.setText("")
        self.erreurni_28.setObjectName("erreurni_28")
        self.erreurni_29 = QtWidgets.QLabel(self.tab_48)
        self.erreurni_29.setGeometry(QtCore.QRect(560, 270, 251, 16))
        self.erreurni_29.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.erreurni_29.setText("")
        self.erreurni_29.setObjectName("erreurni_29")
        self.erreurni_43 = QtWidgets.QLabel(self.tab_48)
        self.erreurni_43.setGeometry(QtCore.QRect(580, 260, 251, 16))
        self.erreurni_43.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_43.setText("")
        self.erreurni_43.setObjectName("erreurni_43")
        self.label_36 = QtWidgets.QLabel(self.tab_48)
        self.label_36.setGeometry(QtCore.QRect(440, 360, 931, 41))
        self.label_36.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.label_109 = QtWidgets.QLabel(self.tab_48)
        self.label_109.setGeometry(QtCore.QRect(320, 180, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_109.setFont(font)
        self.label_109.setObjectName("label_109")
        self.dateEdit_14 = QtWidgets.QDateEdit(self.tab_48)
        self.dateEdit_14.setGeometry(QtCore.QRect(580, 210, 211, 31))
        self.dateEdit_14.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_14.setObjectName("dateEdit_14")
        self.label_43 = QtWidgets.QLabel(self.tab_48)
        self.label_43.setGeometry(QtCore.QRect(270, 30, 931, 41))
        self.label_43.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 87 15pt \"Segoe UI Black\";\n"
"")
        self.label_43.setObjectName("label_43")
        self.tabWidget_15.addTab(self.tab_48, "")
        self.tabWidget_14.addTab(self.tab_44, "")
        self.tabWidget_9.addTab(self.tab_28, "")
        self.tab_29 = QtWidgets.QWidget()
        self.tab_29.setObjectName("tab_29")
        self.tabWidget_16 = QtWidgets.QTabWidget(self.tab_29)
        self.tabWidget_16.setGeometry(QtCore.QRect(0, 0, 1111, 761))
        self.tabWidget_16.setStyleSheet("")
        self.tabWidget_16.setObjectName("tabWidget_16")
        self.tab_49 = QtWidgets.QWidget()
        self.tab_49.setObjectName("tab_49")
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_49)
        self.pushButton_47.setGeometry(QtCore.QRect(450, 40, 161, 61))
        self.pushButton_47.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_47.setObjectName("pushButton_47")
        self.label_100 = QtWidgets.QLabel(self.tab_49)
        self.label_100.setGeometry(QtCore.QRect(10, 120, 1071, 561))
        self.label_100.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_100.setText("")
        self.label_100.setObjectName("label_100")
        self.tabWidget_16.addTab(self.tab_49, "")
        self.tab_51 = QtWidgets.QWidget()
        self.tab_51.setObjectName("tab_51")
        self.pushButton_45 = QtWidgets.QPushButton(self.tab_51)
        self.pushButton_45.setGeometry(QtCore.QRect(480, 180, 181, 71))
        self.pushButton_45.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_45.setObjectName("pushButton_45")
        self.line_19 = QtWidgets.QFrame(self.tab_51)
        self.line_19.setGeometry(QtCore.QRect(270, 150, 591, 31))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.label_97 = QtWidgets.QLabel(self.tab_51)
        self.label_97.setGeometry(QtCore.QRect(350, 60, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_97.setFont(font)
        self.label_97.setObjectName("label_97")
        self.lineEdit_78 = QtWidgets.QLineEdit(self.tab_51)
        self.lineEdit_78.setGeometry(QtCore.QRect(570, 90, 211, 31))
        self.lineEdit_78.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.label_101 = QtWidgets.QLabel(self.tab_51)
        self.label_101.setGeometry(QtCore.QRect(20, 270, 1061, 411))
        self.label_101.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_101.setText("")
        self.label_101.setObjectName("label_101")
        self.erreurni_41 = QtWidgets.QLabel(self.tab_51)
        self.erreurni_41.setGeometry(QtCore.QRect(570, 120, 251, 16))
        self.erreurni_41.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_41.setText("")
        self.erreurni_41.setObjectName("erreurni_41")
        self.tabWidget_16.addTab(self.tab_51, "")
        self.tab_52 = QtWidgets.QWidget()
        self.tab_52.setObjectName("tab_52")
        self.lineEdit_77 = QtWidgets.QLineEdit(self.tab_52)
        self.lineEdit_77.setGeometry(QtCore.QRect(570, 90, 211, 31))
        self.lineEdit_77.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.pushButton_44 = QtWidgets.QPushButton(self.tab_52)
        self.pushButton_44.setGeometry(QtCore.QRect(480, 180, 181, 71))
        self.pushButton_44.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_44.setObjectName("pushButton_44")
        self.line_18 = QtWidgets.QFrame(self.tab_52)
        self.line_18.setGeometry(QtCore.QRect(280, 150, 591, 31))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.label_96 = QtWidgets.QLabel(self.tab_52)
        self.label_96.setGeometry(QtCore.QRect(330, 60, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_96.setFont(font)
        self.label_96.setObjectName("label_96")
        self.label_102 = QtWidgets.QLabel(self.tab_52)
        self.label_102.setGeometry(QtCore.QRect(20, 270, 1061, 411))
        self.label_102.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_102.setText("")
        self.label_102.setObjectName("label_102")
        self.erreurni_40 = QtWidgets.QLabel(self.tab_52)
        self.erreurni_40.setGeometry(QtCore.QRect(570, 120, 251, 16))
        self.erreurni_40.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_40.setText("")
        self.erreurni_40.setObjectName("erreurni_40")
        self.tabWidget_16.addTab(self.tab_52, "")
        self.tab_53 = QtWidgets.QWidget()
        self.tab_53.setObjectName("tab_53")
        self.label_88 = QtWidgets.QLabel(self.tab_53)
        self.label_88.setGeometry(QtCore.QRect(330, 60, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.dateEdit_7 = QtWidgets.QDateEdit(self.tab_53)
        self.dateEdit_7.setGeometry(QtCore.QRect(580, 90, 201, 31))
        self.dateEdit_7.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_7.setObjectName("dateEdit_7")
        self.erreurni_39 = QtWidgets.QLabel(self.tab_53)
        self.erreurni_39.setGeometry(QtCore.QRect(580, 120, 251, 16))
        self.erreurni_39.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_39.setText("")
        self.erreurni_39.setObjectName("erreurni_39")
        self.label_104 = QtWidgets.QLabel(self.tab_53)
        self.label_104.setGeometry(QtCore.QRect(20, 270, 1061, 411))
        self.label_104.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_104.setText("")
        self.label_104.setObjectName("label_104")
        self.pushButton_46 = QtWidgets.QPushButton(self.tab_53)
        self.pushButton_46.setGeometry(QtCore.QRect(470, 180, 181, 71))
        self.pushButton_46.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_46.setObjectName("pushButton_46")
        self.erreurni_42 = QtWidgets.QLabel(self.tab_53)
        self.erreurni_42.setGeometry(QtCore.QRect(580, 150, 251, 16))
        self.erreurni_42.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.erreurni_42.setText("")
        self.erreurni_42.setObjectName("erreurni_42")
        self.line_21 = QtWidgets.QFrame(self.tab_53)
        self.line_21.setGeometry(QtCore.QRect(280, 150, 591, 31))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.tabWidget_16.addTab(self.tab_53, "")
        self.tab_54 = QtWidgets.QWidget()
        self.tab_54.setObjectName("tab_54")
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_54)
        self.pushButton_41.setGeometry(QtCore.QRect(480, 190, 181, 71))
        self.pushButton_41.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_41.setObjectName("pushButton_41")
        self.line_15 = QtWidgets.QFrame(self.tab_54)
        self.line_15.setGeometry(QtCore.QRect(270, 160, 591, 31))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.label_89 = QtWidgets.QLabel(self.tab_54)
        self.label_89.setGeometry(QtCore.QRect(330, 70, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.dateEdit_8 = QtWidgets.QDateEdit(self.tab_54)
        self.dateEdit_8.setGeometry(QtCore.QRect(600, 100, 201, 31))
        self.dateEdit_8.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_8.setObjectName("dateEdit_8")
        self.erreurni_38 = QtWidgets.QLabel(self.tab_54)
        self.erreurni_38.setGeometry(QtCore.QRect(600, 130, 251, 16))
        self.erreurni_38.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_38.setText("")
        self.erreurni_38.setObjectName("erreurni_38")
        self.label_105 = QtWidgets.QLabel(self.tab_54)
        self.label_105.setGeometry(QtCore.QRect(20, 280, 1061, 411))
        self.label_105.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_105.setText("")
        self.label_105.setObjectName("label_105")
        self.tabWidget_16.addTab(self.tab_54, "")
        self.tab_50 = QtWidgets.QWidget()
        self.tab_50.setObjectName("tab_50")
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_50)
        self.pushButton_42.setGeometry(QtCore.QRect(480, 230, 181, 71))
        self.pushButton_42.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_42.setObjectName("pushButton_42")
        self.line_16 = QtWidgets.QFrame(self.tab_50)
        self.line_16.setGeometry(QtCore.QRect(290, 200, 591, 31))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.label_90 = QtWidgets.QLabel(self.tab_50)
        self.label_90.setGeometry(QtCore.QRect(350, 40, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.dateEdit_9 = QtWidgets.QDateEdit(self.tab_50)
        self.dateEdit_9.setGeometry(QtCore.QRect(620, 70, 201, 31))
        self.dateEdit_9.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_9.setObjectName("dateEdit_9")
        self.label_91 = QtWidgets.QLabel(self.tab_50)
        self.label_91.setGeometry(QtCore.QRect(350, 110, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.dateEdit_10 = QtWidgets.QDateEdit(self.tab_50)
        self.dateEdit_10.setGeometry(QtCore.QRect(620, 140, 201, 31))
        self.dateEdit_10.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_10.setObjectName("dateEdit_10")
        self.label_92 = QtWidgets.QLabel(self.tab_50)
        self.label_92.setGeometry(QtCore.QRect(360, 30, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        self.erreurni_36 = QtWidgets.QLabel(self.tab_50)
        self.erreurni_36.setGeometry(QtCore.QRect(430, 190, 491, 20))
        self.erreurni_36.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_36.setText("")
        self.erreurni_36.setObjectName("erreurni_36")
        self.erreurni_37 = QtWidgets.QLabel(self.tab_50)
        self.erreurni_37.setGeometry(QtCore.QRect(620, 170, 251, 16))
        self.erreurni_37.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_37.setText("")
        self.erreurni_37.setObjectName("erreurni_37")
        self.label_106 = QtWidgets.QLabel(self.tab_50)
        self.label_106.setGeometry(QtCore.QRect(20, 330, 1061, 361))
        self.label_106.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_106.setText("")
        self.label_106.setObjectName("label_106")
        self.tabWidget_16.addTab(self.tab_50, "")
        self.tab_55 = QtWidgets.QWidget()
        self.tab_55.setObjectName("tab_55")
        self.label_93 = QtWidgets.QLabel(self.tab_55)
        self.label_93.setGeometry(QtCore.QRect(350, 70, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.line_17 = QtWidgets.QFrame(self.tab_55)
        self.line_17.setGeometry(QtCore.QRect(280, 220, 591, 31))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.dateEdit_11 = QtWidgets.QDateEdit(self.tab_55)
        self.dateEdit_11.setGeometry(QtCore.QRect(580, 170, 201, 31))
        self.dateEdit_11.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_11.setObjectName("dateEdit_11")
        self.dateEdit_12 = QtWidgets.QDateEdit(self.tab_55)
        self.dateEdit_12.setGeometry(QtCore.QRect(580, 100, 201, 31))
        self.dateEdit_12.setStyleSheet("color: rgb(92, 121, 134);\n"
"font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"border: 2px solid rgb(255, 145, 150);\n"
"border-radius: 4px;\n"
"")
        self.dateEdit_12.setObjectName("dateEdit_12")
        self.pushButton_43 = QtWidgets.QPushButton(self.tab_55)
        self.pushButton_43.setGeometry(QtCore.QRect(470, 250, 181, 71))
        self.pushButton_43.setStyleSheet("color: rgb(67, 87, 97);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-color: rgb(85, 170, 255);\n"
"selection-color: rgb(255, 114, 94);\n"
"selection-background-color: rgb(158, 109, 96);\n"
"selection-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-color: rgb(157, 109, 96);\n"
"alternate-background-color: rgb(156, 107, 94);\n"
"color: rgb(255, 156, 142);\n"
"background-color: rgb(255, 156, 142);\n"
"background-color: rgb(92, 121, 134);")
        self.pushButton_43.setObjectName("pushButton_43")
        self.label_94 = QtWidgets.QLabel(self.tab_55)
        self.label_94.setGeometry(QtCore.QRect(370, 30, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        self.label_95 = QtWidgets.QLabel(self.tab_55)
        self.label_95.setGeometry(QtCore.QRect(350, 140, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_95.setFont(font)
        self.label_95.setObjectName("label_95")
        self.erreurni_34 = QtWidgets.QLabel(self.tab_55)
        self.erreurni_34.setGeometry(QtCore.QRect(440, 210, 461, 20))
        self.erreurni_34.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_34.setText("")
        self.erreurni_34.setObjectName("erreurni_34")
        self.erreurni_35 = QtWidgets.QLabel(self.tab_55)
        self.erreurni_35.setGeometry(QtCore.QRect(580, 200, 251, 16))
        self.erreurni_35.setStyleSheet("color: rgb(255, 156, 142);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"")
        self.erreurni_35.setText("")
        self.erreurni_35.setObjectName("erreurni_35")
        self.label_107 = QtWidgets.QLabel(self.tab_55)
        self.label_107.setGeometry(QtCore.QRect(20, 330, 1061, 361))
        self.label_107.setStyleSheet("background-color:rgba(0,0, 0, 20);\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"color: rgb(92, 121, 134);\n"
"border-radius: 30px;\n"
"border: 2px solid rgb(255, 145, 150);")
        self.label_107.setText("")
        self.label_107.setObjectName("label_107")
        self.tabWidget_16.addTab(self.tab_55, "")
        self.tabWidget_9.addTab(self.tab_29, "")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_18.setCurrentIndex(0)
        self.tabWidget_19.setCurrentIndex(3)
        self.tabWidget_20.setCurrentIndex(2)
        self.tabWidget_6.setCurrentIndex(3)
        self.modifier1.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(4)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(0)
        self.tabWidget_12.setCurrentIndex(2)
        self.tabWidget_13.setCurrentIndex(1)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_14.setCurrentIndex(0)
        self.tabWidget_15.setCurrentIndex(1)
        self.tabWidget_16.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.ajouter.clicked.connect(self.action)
        self.afficher1.clicked.connect(self.affiche_etud)
        self.supprimer.clicked.connect(self.supprimer1)
        self.supprimer2.clicked.connect(self.supprimer21)
        self.supprimer_2.clicked.connect(self.supprimer31)
        self.supprimer2_2.clicked.connect(self.supprimer_niveau_section)
        self.supprimer_3.clicked.connect(self.modifier_tel)
        self.supprimer_4.clicked.connect(self.modifier_adresse)
        self.supprimer_9.clicked.connect(self.modifier_mail)
        self.afficher2.clicked.connect(self.afficher_2)
        self.afficher3.clicked.connect(self.afficher_3)
        self.afficher4.clicked.connect(self.afficher_4)
        self.afficher5.clicked.connect(self.afficher_5)
        self.ajouter_2.clicked.connect(self.action2)
        self.afficher1_2.clicked.connect(self.affiche_livres1)
        self.afficher1_3.clicked.connect(self.affiche_livres2)
        self.afficher1_4.clicked.connect(self.affiche_livres3)
        self.afficher1_5.clicked.connect(self.affiche_livres4)
        self.afficher1_6.clicked.connect(self.affiche_livres5)
        self.afficher1_7.clicked.connect(self.affiche_livres6)
        self.pushButton_28.clicked.connect(self.modifier_nb_ex)
        self.ajouter_3.clicked.connect(self.supprimer_livres1)
        self.ajouter_4.clicked.connect(self.supprimer_livres2)
        self.ajouter_5.clicked.connect(self.supprimer_livres3)
        self.pushButton_34.clicked.connect(self.action3)
        self.pushButton_47.clicked.connect(self.afficher_emprunt1)
        self.pushButton_36.clicked.connect(self.retour_emprunt)
        self.pushButton_37.clicked.connect(self.supprimer_emprunt)
        self.pushButton_38.clicked.connect(self.modifier_emprunt1)
        self.pushButton_39.clicked.connect(self.modifier_emprunt2)
        self.pushButton_45.clicked.connect(self.afficher_emprunt2)
        self.pushButton_44.clicked.connect(self.afficher_emprunt3)
        self.pushButton_46.clicked.connect(self.afficher_emprunt4)
        self.pushButton_41.clicked.connect(self.afficher_emprunt5)
        self.pushButton_42.clicked.connect(self.afficher_emprunt6)
        self.pushButton_43.clicked.connect(self.afficher_emprunt7)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "ACCUEL"))
        self.label.setText(_translate("Dialog", "Num inscription"))
        self.label_2.setText(_translate("Dialog", "Num inscription"))
        self.label_3.setText(_translate("Dialog", "Num inscription"))
        self.label_4.setText(_translate("Dialog", "Num inscription"))
        self.label_16.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "AJOUTER ETUDIANTS"))
        self.ajouter.setText(_translate("Dialog", "A J O U T E R"))
        self.label_13.setText(_translate("Dialog", "Section"))
        self.label_11.setText(_translate("Dialog", "Tel"))
        self.label_8.setText(_translate("Dialog", "Date néssance"))
        self.label_7.setText(_translate("Dialog", "Prenom"))
        self.label_14.setText(_translate("Dialog", "Niveau étude"))
        self.label_10.setText(_translate("Dialog", "Adresse"))
        self.label_6.setText(_translate("Dialog", "Nom"))
        self.label_5.setText(_translate("Dialog", "Num inscription"))
        self.label_12.setText(_translate("Dialog", "Mail"))
        self.section.setItemText(0, _translate("Dialog", "selectionner une section"))
        self.section.setItemText(1, _translate("Dialog", "CPI"))
        self.section.setItemText(2, _translate("Dialog", "LI"))
        self.section.setItemText(3, _translate("Dialog", "TIC"))
        self.section.setItemText(4, _translate("Dialog", "EEA"))
        self.section.setItemText(5, _translate("Dialog", "MA"))
        self.premiere.setText(_translate("Dialog", "1ère"))
        self.deuxieme.setText(_translate("Dialog", "2ème"))
        self.troisieme.setText(_translate("Dialog", "3ème"))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_62), _translate("Dialog", "Ajouter un nouvel etudiant"))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_64), _translate("Dialog", "Supression etudiant donné"))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_65), _translate("Dialog", "Supression des etudiants d\'une section donnée"))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_66), _translate("Dialog", "Supression des étudiants d\'un niveau donné"))
        self.tabWidget_19.setTabText(self.tabWidget_19.indexOf(self.tab_67), _translate("Dialog", "Supression des étudiants d\'une section et un niveau"))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_63), _translate("Dialog", "Supprimer un etudiant"))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_69), _translate("Dialog", "Téléphone"))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_70), _translate("Dialog", "Mail"))
        self.tabWidget_20.setTabText(self.tabWidget_20.indexOf(self.tab_71), _translate("Dialog", "Adresse"))
        self.tabWidget_18.setTabText(self.tabWidget_18.indexOf(self.tab_68), _translate("Dialog", "Modifier etudiant"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("Dialog", "Ajouter un nouvel etudiant"))
        self.label_9.setText(_translate("Dialog", "Num inscription"))
        self.supprimer.setText(_translate("Dialog", "SUPPRIMER"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_16), _translate("Dialog", "Supression etudiant donné"))
        self.label_15.setText(_translate("Dialog", "Section"))
        self.supprimer2.setText(_translate("Dialog", "SUPPRIMER"))
        self.section_supp.setItemText(0, _translate("Dialog", "selectionner une section"))
        self.section_supp.setItemText(1, _translate("Dialog", "CPI"))
        self.section_supp.setItemText(2, _translate("Dialog", "LI"))
        self.section_supp.setItemText(3, _translate("Dialog", "TIC"))
        self.section_supp.setItemText(4, _translate("Dialog", "EEA"))
        self.section_supp.setItemText(5, _translate("Dialog", "MA"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_17), _translate("Dialog", "Supression des etudiants d\'une section donnée"))
        self.label_17.setText(_translate("Dialog", "Niveau"))
        self.supprimer_2.setText(_translate("Dialog", "SUPPRIMER"))
        self.deuxieme_2.setText(_translate("Dialog", "2ème"))
        self.premiere_2.setText(_translate("Dialog", "1ère"))
        self.troisieme_2.setText(_translate("Dialog", "3ème"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_18), _translate("Dialog", "Supression des étudiants d\'un niveau donné"))
        self.section_supp_2.setItemText(0, _translate("Dialog", "selectionner une section"))
        self.section_supp_2.setItemText(1, _translate("Dialog", "CPI"))
        self.section_supp_2.setItemText(2, _translate("Dialog", "LI"))
        self.section_supp_2.setItemText(3, _translate("Dialog", "TIC"))
        self.section_supp_2.setItemText(4, _translate("Dialog", "EEA"))
        self.section_supp_2.setItemText(5, _translate("Dialog", "MA"))
        self.supprimer2_2.setText(_translate("Dialog", "SUPPRIMER"))
        self.label_18.setText(_translate("Dialog", "Section"))
        self.troisieme_3.setText(_translate("Dialog", "3ème"))
        self.label_19.setText(_translate("Dialog", "Niveau"))
        self.deuxieme_3.setText(_translate("Dialog", "2ème"))
        self.premiere_3.setText(_translate("Dialog", "1ère"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_19), _translate("Dialog", "Supression des étudiants d\'une section et un niveau"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("Dialog", "Supprimer un etudiant"))
        self.label_20.setText(_translate("Dialog", "Num inscription"))
        self.label_21.setText(_translate("Dialog", "Tel"))
        self.supprimer_3.setText(_translate("Dialog", "MODIFIER"))
        self.modifier1.setTabText(self.modifier1.indexOf(self.tab_25), _translate("Dialog", "Téléphone"))
        self.supprimer_4.setText(_translate("Dialog", "MODIFIER"))
        self.label_22.setText(_translate("Dialog", "Num inscription"))
        self.label_28.setText(_translate("Dialog", "Adresse"))
        self.modifier1.setTabText(self.modifier1.indexOf(self.tab_27), _translate("Dialog", "Adresse"))
        self.supprimer_9.setText(_translate("Dialog", "MODIFIER"))
        self.label_39.setText(_translate("Dialog", "Num inscription"))
        self.label_40.setText(_translate("Dialog", "Mail"))
        self.modifier1.setTabText(self.modifier1.indexOf(self.tab_26), _translate("Dialog", "Mail"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("Dialog", "Modifier etudiant"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Dialog", "mise a jour des etudiants"))
        self.label_31.setText(_translate("Dialog", "AFFICHAGE DES ETUDIANTS"))
        self.afficher1.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_20), _translate("Dialog", "Contenu du dictionnaire étudiants"))
        self.label_23.setText(_translate("Dialog", "Num inscription"))
        self.afficher2.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_22), _translate("Dialog", "Recherche par numero inscription"))
        self.label_24.setText(_translate("Dialog", "Section"))
        self.afficher3.setText(_translate("Dialog", "AFFICHER"))
        self.section_2.setItemText(0, _translate("Dialog", "selectionner une section"))
        self.section_2.setItemText(1, _translate("Dialog", "CPI"))
        self.section_2.setItemText(2, _translate("Dialog", "LI"))
        self.section_2.setItemText(3, _translate("Dialog", "TIC"))
        self.section_2.setItemText(4, _translate("Dialog", "EEA"))
        self.section_2.setItemText(5, _translate("Dialog", "MA"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_23), _translate("Dialog", "Recherche par section"))
        self.label_27.setText(_translate("Dialog", "Niveau"))
        self.afficher4.setText(_translate("Dialog", "AFFICHER"))
        self.deuxieme_4.setText(_translate("Dialog", "2ème"))
        self.premiere_4.setText(_translate("Dialog", "1ère"))
        self.troisieme_4.setText(_translate("Dialog", "3ème"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_21), _translate("Dialog", "Recherche par niveau"))
        self.label_25.setText(_translate("Dialog", "SECTION"))
        self.label_26.setText(_translate("Dialog", "NIVEAU"))
        self.afficher5.setText(_translate("Dialog", "AFFICHER"))
        self.section_3.setItemText(0, _translate("Dialog", "selectionner une section"))
        self.section_3.setItemText(1, _translate("Dialog", "CPI"))
        self.section_3.setItemText(2, _translate("Dialog", "LI"))
        self.section_3.setItemText(3, _translate("Dialog", "TIC"))
        self.section_3.setItemText(4, _translate("Dialog", "EEA"))
        self.section_3.setItemText(5, _translate("Dialog", "MA"))
        self.deuxieme_5.setText(_translate("Dialog", "2ème"))
        self.troisieme_5.setText(_translate("Dialog", "3ème"))
        self.premiere_5.setText(_translate("Dialog", "1ère"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_24), _translate("Dialog", "Recherche par section et niveau"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("Dialog", "Recherche affichage et tri"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), _translate("Dialog", "Ajouter un nouvel etudiant"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), _translate("Dialog", "Supprimer un etudiant"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("Dialog", "mise a jour des etudiants"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Dialog", "Recherche affichage "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Gestion des etudiantss"))
        self.ajouter_2.setText(_translate("Dialog", "A J O U T E R"))
        self.label_58.setText(_translate("Dialog", "Référence"))
        self.label_57.setText(_translate("Dialog", "Nom et prénom auteur"))
        self.label_62.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_62.setText(_translate("Dialog", "AJOUTER UN LIVRE"))
        self.label_61.setText(_translate("Dialog", "Titre"))
        self.label_60.setText(_translate("Dialog", "Nombres d\'exemplaires"))
        self.label_59.setText(_translate("Dialog", "Année édition"))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_32), _translate("Dialog", "Ajouter un nouvel livre"))
        self.label_98.setText(_translate("Dialog", "Référence"))
        self.ajouter_3.setText(_translate("Dialog", "SUPPRIMER"))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_35), _translate("Dialog", "Supprimer livre donné"))
        self.label_64.setText(_translate("Dialog", "Auteur"))
        self.ajouter_4.setText(_translate("Dialog", "SUPPRIMER"))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_37), _translate("Dialog", "Suppression livres d\'un auteur donné"))
        self.label_65.setText(_translate("Dialog", "Année"))
        self.ajouter_5.setText(_translate("Dialog", "SUPPRIMER"))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_36), _translate("Dialog", "Suppression livre d\'une année donnée"))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_34), _translate("Dialog", "Supprimer"))
        self.pushButton_28.setText(_translate("Dialog", "MODIFIER"))
        self.label_66.setText(_translate("Dialog", "Nombres d\'exemplaires"))
        self.label_67.setText(_translate("Dialog", "Référence"))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_33), _translate("Dialog", "Modifier nombre d\'exemplaire d\'un livre"))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_30), _translate("Dialog", "mise a jour"))
        self.label_41.setText(_translate("Dialog", "AFFICHAGE DES LIVRES"))
        self.afficher1_2.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_38), _translate("Dialog", "Contenu du dictionnaire LIVRE"))
        self.label_68.setText(_translate("Dialog", "Référence"))
        self.afficher1_3.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_40), _translate("Dialog", "Recherche par référence"))
        self.afficher1_4.setText(_translate("Dialog", "AFFICHER"))
        self.label_69.setText(_translate("Dialog", "Titre"))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_41), _translate("Dialog", "echerche par titre"))
        self.afficher1_5.setText(_translate("Dialog", "AFFICHER"))
        self.label_70.setText(_translate("Dialog", "Année edition"))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_42), _translate("Dialog", "Recherche livres par année édition donnée"))
        self.afficher1_6.setText(_translate("Dialog", "AFFICHER"))
        self.label_71.setText(_translate("Dialog", "Auteur"))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_43), _translate("Dialog", "echerche livre d\'un auteur donnée"))
        self.label_42.setText(_translate("Dialog", "AFFICHAGE DES LIVRES PAR ORDRE ALPHABETIQUE"))
        self.afficher1_7.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_13.setTabText(self.tabWidget_13.indexOf(self.tab_39), _translate("Dialog", "Recherche et affichage des livres par ordre alphabétique"))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_31), _translate("Dialog", "Recherche et affichage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Gestion des livres"))
        self.label_77.setText(_translate("Dialog", "AJOUTER UN EMPRUNT"))
        self.label_76.setText(_translate("Dialog", "Num Inscription"))
        self.label_74.setText(_translate("Dialog", "Référence du livre"))
        self.pushButton_34.setText(_translate("Dialog", "AJOUTER"))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_6), _translate("Dialog", "Ajouter un nouvel emprunt"))
        self.label_78.setText(_translate("Dialog", "Référence du livre"))
        self.label_79.setText(_translate("Dialog", "Num Inscription"))
        self.pushButton_36.setText(_translate("Dialog", "VALIDER"))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_45), _translate("Dialog", "Retour d\'un emprunt"))
        self.label_80.setText(_translate("Dialog", "Référence du livre"))
        self.label_81.setText(_translate("Dialog", "Num Inscription"))
        self.pushButton_37.setText(_translate("Dialog", "SUPPRIMER"))
        self.label_103.setText(_translate("Dialog", "Date d\'emprunt"))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_46), _translate("Dialog", "Supprimer d\'un emprunt"))
        self.label_82.setText(_translate("Dialog", "Référence du livre"))
        self.label_83.setText(_translate("Dialog", "Num Inscription"))
        self.label_84.setText(_translate("Dialog", "Date emprunt 2"))
        self.pushButton_38.setText(_translate("Dialog", "MODIFIER"))
        self.label_108.setText(_translate("Dialog", "Date emprunt 2"))
        self.label_38.setText(_translate("Dialog", "modifier la date emprunt 1 avec la date emprunt 2"))
        self.tabWidget_15.setTabText(self.tabWidget_15.indexOf(self.tab_47), _translate("Dialog", "Date emprunt"))
        self.pushButton_39.setText(_translate("Dialog", "MODIFIER"))
        self.label_85.setText(_translate("Dialog", "Num Inscription"))
        self.label_86.setText(_translate("Dialog", "Date retour2"))
        self.label_87.setText(_translate("Dialog", "Référence du livre"))
        self.label_109.setText(_translate("Dialog", "Date retour1"))
        self.label_43.setText(_translate("Dialog", "modifier la date retour 1 avec la date retour 2"))
        self.tabWidget_15.setTabText(self.tabWidget_15.indexOf(self.tab_48), _translate("Dialog", "Date retour"))
        self.tabWidget_14.setTabText(self.tabWidget_14.indexOf(self.tab_44), _translate("Dialog", "Modifier emprunt"))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_28), _translate("Dialog", "mise a jour"))
        self.pushButton_47.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_49), _translate("Dialog", "Contenu du dictionnaire emprunt"))
        self.pushButton_45.setText(_translate("Dialog", "AFFICHER"))
        self.label_97.setText(_translate("Dialog", "Référence"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_51), _translate("Dialog", "Recherche emprunts par livre"))
        self.pushButton_44.setText(_translate("Dialog", "AFFICHER"))
        self.label_96.setText(_translate("Dialog", "Num Inscription"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_52), _translate("Dialog", "Recherche emprunts par étudiant"))
        self.label_88.setText(_translate("Dialog", "Date emprunt"))
        self.pushButton_46.setText(_translate("Dialog", "AFFICHER"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_53), _translate("Dialog", "Recherche livres empruntés a une date donnée"))
        self.pushButton_41.setText(_translate("Dialog", "AFFICHER"))
        self.label_89.setText(_translate("Dialog", "Date retour"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_54), _translate("Dialog", "Recherche livres retournés a une date donnée"))
        self.pushButton_42.setText(_translate("Dialog", "AFFICHER"))
        self.label_90.setText(_translate("Dialog", "Date 1"))
        self.label_91.setText(_translate("Dialog", "Date 2"))
        self.label_92.setText(_translate("Dialog", "recherche livre empruntés entre date 1 et date 2"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_50), _translate("Dialog", "Recherche livre empruntés entre 2 dates donnée"))
        self.label_93.setText(_translate("Dialog", "Date 1"))
        self.pushButton_43.setText(_translate("Dialog", "AFFICHER"))
        self.label_94.setText(_translate("Dialog", "recherche livre retournés entre date 1 et date 2"))
        self.label_95.setText(_translate("Dialog", "Date 2"))
        self.tabWidget_16.setTabText(self.tabWidget_16.indexOf(self.tab_55), _translate("Dialog", "Recherche livres retournés entre 2 dates données"))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_29), _translate("Dialog", "Recherche et affichage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Gestion des emprunts"))
    def afficher_3(self):
         if self.section_2.currentIndex()==0:
              self.erreursection_affiche.setText("aucune section selectionné!")
         else:
                code=self.section_2.currentText()
                f = open("etudiant.org", "rb")
                data = []
                while True:
                                try:
                                        e = load(f)
                                        if e["section"]==code:
                                                data.append("num_inscription = {}   nom = {}   prenom = {}\n"
                                        "date de naissance = {}   adresse = {}   mail = {}\n"
                                        "tel = {}   section = {}   niveau = {}\n\n\n".format(
                                        e["num_inscription"], e["nom"], e["prenom"],
                                        e["date"], e["adresse"], e["mail"],
                                        e["tel"],e["section"], e["niveau"]))
                                except EOFError:break
                f.close()
                self.label_48.setText(''.join(data))
                self.erreursection_affiche.setText("")
    def afficher_4(self):
         ok=True
         if self.premiere_4.isChecked():
                code1 = "premiere"
         elif self.deuxieme_4.isChecked():
                code1 = "deuxieme"
         elif self.troisieme_4.isChecked():
                code1 = "troisieme"
         else:
                ok=False
                self.erreurniveau_affiche.setText("aucune boutton selectionnée ! ")
         if ok:
              f = open("etudiant.org", "rb")
              data = []
              while True:
                                try:
                                        e = load(f)
                                        if e["niveau"]==code1:
                                                data.append("num_inscription = {}   nom = {}   prenom = {}\n"
                                        "date de naissance = {}   adresse = {}   mail = {}\n"
                                        "tel = {}   section = {}   niveau = {}\n\n\n".format(
                                        e["num_inscription"], e["nom"], e["prenom"],
                                        e["date"], e["adresse"], e["mail"],
                                        e["tel"],e["section"], e["niveau"]))
                                except EOFError:break
              f.close()
              self.label_49.setText(''.join(data))
              self.erreurniveau_affiche.setText("")
              
    def afficher_5(self):
         ok=True
         if self.premiere_5.isChecked():
                code1 = "premiere"
         elif self.deuxieme_5.isChecked():
                code1 = "deuxieme"
         elif self.troisieme_5.isChecked():
                code1 = "troisieme"
         else:
                ok=False
                self.erreurni_13.setText("aucune boutton selectionnée ! ")
         if self.section_3.currentIndex()==0:
               ok=False
               self.erreurni_12.setText("aucune section selectionné! ")
         else:
               code2=self.section_3.currentText()
         if ok:
               f = open("etudiant.org", "rb")
               data = []
               while True:
                                try:
                                        e = load(f)
                                        if e["niveau"]==code1 and e["section"]==code2:
                                                data.append("num_inscription = {}   nom = {}   prenom = {}\n"
                                        "date de naissance = {}   adresse = {}   mail = {}\n"
                                        "tel = {}   section = {}   niveau = {}\n\n\n".format(
                                        e["num_inscription"], e["nom"], e["prenom"],
                                        e["date"], e["adresse"], e["mail"],
                                        e["tel"],e["section"], e["niveau"]))
                                except EOFError:break
               f.close()
               self.label_50.setText(''.join(data))
               self.erreurni_12.setText("")
               self.erreurni_13.setText("")
               


    def afficher_2(self):
         code=self.ni_affiche.text()
         if exist(code):
                f = open("etudiant.org", "rb")
                data = []
                while True:
                        try:
                                e = load(f)
                                if e["num_inscription"]==code:
                                        data.append("num_inscription = {}   nom = {}   prenom = {}\n"
                                        "date de naissance = {}   adresse = {}   mail = {}\n"
                                        "tel = {}   section = {}   niveau = {}\n\n\n".format(
                                        e["num_inscription"], e["nom"], e["prenom"],
                                        e["date"], e["adresse"], e["mail"],
                                        e["tel"],e["section"], e["niveau"]))
                        except EOFError:break
                f.close()
                self.label_47.setText(''.join(data))
                self.erreurni_affiche.setText("")
         else:
              self.erreurni_affiche.setText("le numero n'existe pas")
    def modifier_adresse(self):
         code=self.ni_supp_3.text()
         tel=self.tel_3.text()
         if exist(code):
             if len(self.tel_3.text())==0:
                  self.erreurni_supp_7.setText("adresse vide !")
             else:
                    
                  modify_record("adresse",code,tel)
                  self.sucess_sup_6.setText("modification done")
                  self.erreurni_supp_6.setText("")
                  self.erreurni_supp_7.setText("")

         else:
              self.erreurni_supp_6.setText("le numero n'existe pas")
    def modifier_mail(self):
         code=self.ni_supp_8.text()
         tel=self.tel_8.text()
         if exist(code):
              if valid_mail(tel):
                  modify_record("mail",code,tel)
                  self.sucess_sup_11.setText("modification done")
                  self.erreurni_supp_16.setText("")
                  self.erreurni_supp_17.setText("")
              else:
                    self.erreurni_supp_17.setText("le mail invalid")
         else:
              self.erreurni_supp_16.setText("le numero n'existe pas")
    def modifier_tel(self):
         code=self.ni_supp_2.text()
         tel=self.tel_2.text()
         if exist(code):
              if valid_tel(tel):
                  modify_record("tel",code,tel)
                  self.sucess_sup_5.setText("modification done")
                  self.erreurni_supp_4.setText("")
                  self.erreurni_supp_5.setText("")
              else:
                    self.erreurni_supp_5.setText("le numero invalid")
         else:
              self.erreurni_supp_4.setText("le numero n'existe pas")
                    
    def supprimer1(self):
        code=self.ni_supp.text()
        if exist(code):
            f = open("etudiant.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                if e["num_inscription"] != code:
                    records.append(e)

            f.close()

            f = open("etudiant.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.sucess_sup.setText("supression done ")
            self.erreurni_supp.setText("")
            
        else:
            self.erreurni_supp.setText("le numero n'existe pas")
    def supprimer_niveau_section(self):
        ok=True
        if self.premiere_3.isChecked():
                code1 = "premiere"
        elif self.deuxieme_3.isChecked():
                code1 = "deuxieme"
        elif self.troisieme_3.isChecked():
                code1 = "troisieme"
        else:
                ok=False
                self.erreurni_supp_3.setText("aucune boutton selectionnée ! ")
                return
        if self.section_supp_2.currentIndex()==0:
             ok=False
             self.erreursection_sup_2.setText("aucune section selectionnée ! ")
        else:
                code2 = self.section_supp_2.currentText()
        if ok:

                f = open("etudiant.org", "rb")
                records = []
                while True:
                    try:
                        e = load(f)
                    except EOFError:
                        break
                if e["niveau"] != code1 or e["section"] != code2:
                        records.append(e)
                f.close()

                f = open("etudiant.org", "wb")
                for e in records:
                        dump(e, f)
                f.close()
                self.sucess_sup_4.setText("supression done ")
                self.erreursection_sup_2.setText("")
                self.erreurni_supp_3.setText("")
   
    def supprimer21(self):
        if (self.section_supp.currentIndex()==0):
              self.erreursection_sup.setText("aucune section selectionnée !")
        else:
                code=self.section_supp.currentText()
                f = open("etudiant.org", "rb")
                records=[]
                while True:
                    try:
                        e = load(f)
                    except EOFError:
                        break
                if e["section"] != code:
                    records.append(e)
                f.close()

                f = open("etudiant.org", "wb")
                for e in records:
                        dump(e, f)
                f.close()
                self.sucess_sup_2.setText("supression done ")
                self.erreursection_sup.setText("")
                


    def supprimer31(self):
        ok=True
        if self.premiere_2.isChecked():
            code="premiere"
        elif self.deuxieme_2.isChecked():
             code="deuxieme"
        elif self.troisieme_2.isChecked():
             code="troisieme"
        else:
            ok=False
            self.erreurni_supp_2.setText("aucune boutton selectionnée ! ")
        if ok:
                f = open("etudiant.org", "rb")
                records=[]
                while True:
                    try:
                        e = load(f)
                    except EOFError:
                        break
                    if e["niveau"] != code:
                        records.append(e)
                f.close()

                f = open("etudiant.org", "wb")
                for e in records:
                        dump(e, f)
                f.close()
                self.sucess_sup_3.setText("supression done ")    
                self.erreurni_supp_2.setText("")     
    def action(self):
        e={}
        ok=True
        code=self.ni.text()
        if code.isdigit() and len(code) == 8:
            f=open("etudiant.org","rb")
            result=True
            f=open("etudiant.org","rb")
            while True:
                try:
                    e1=load(f)
                except Exception:break
                if e1["num_inscription"]==code:
                    result=False
                    break  
            f.close()          
            if result:
                e["num_inscription"]=code
                self.erreurni.setText('Le code d\'inscription valide ✓')
                self.erreurni.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            else:
                ok=False
                self.erreurni.setText('Le code d\'inscription existe déjà ')
        else:
            ok=False
            self.erreurni.setText("num inscription invalid !")
        


        nom=self.nom.text()
        pattern = r'^[a-zA-Z]+(([\'\,\.\-][a-zA-Z])?[a-zA-Z]*)*$'
        match = re.match(pattern, nom)
        if match:
            self.erreurnom.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            self.erreurnom.setText("nom valide ✓")
            e["nom"]=nom
        else:
            ok=False
            self.erreurnom.setText("nom invalid !")

        
        prenom=self.prenom.text()
        pattern = r'^[a-zA-Z]+(([\'\,\.\-][a-zA-Z])?[a-zA-Z]*)*$'
        match = re.match(pattern, prenom)
        if match:
            self.erreurprenom.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            self.erreurprenom.setText("prenom valide ✓")
            e["prenom"]=prenom
        else:
            ok=False
            self.erreurprenom.setText("prenom invalid !")
        e["date"]=self.date.text()
        adresse=self.adresse.text()
        if len(adresse)>0:
            e["adresse"]=adresse
            self.erreuradresse.setText("adresse valid ✓")
            self.erreuradresse.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")

        else:
            ok=False
            self.erreuradresse.setText("adresse invalid !")

        mail=self.mail.text()
        pattern = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
        match = re.match(pattern, mail)
        if match:
            result=True
            f=open("etudiant.org","rb")
            while True:
                try:
                    e1=load(f)
                except Exception:break
                if e1["mail"]==mail:
                    result=False
                    break 
            f.close() 
            if result:
                e["mail"]=mail
                self.erreurmail.setText("mail valid ✓")
                self.erreurmail.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            else:
                ok=False
                self.erreurmail.setText("mail existe deja")
        else:
            ok=False
            self.erreurmail.setText("mail invalid !")
        tel=self.tel.text()
        if len(tel)>0:
            match=(len(tel)==8) and (tel[0] in ['2','3','4','5','7','9'])
            if match:
                if existe(tel):
                    ok=False
                    self.erreurtel.setText("tel existe deja !")
                else:
                    e["tel"]=tel
                    self.erreurtel.setText("tel valid ✓")
                    self.erreurtel.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            else:
                ok=False
                self.erreurtel.setText("tel invalid !")
        else:
            ok=False
            self.erreurtel.setText("tel vide !")

        if self.section.currentIndex()==0:
            ok=False
            self.erreursection.setText("selectionner svp !")
        else:
            e["section"]=self.section.currentText()
            self.erreursection.setText("section selectionner ✓")
            self.erreursection.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")

        if self.premiere.isChecked():
            e["niveau"]="premiere"
            self.erreurniveau.setText("niveau selectionner ✓")
            self.erreurniveau.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
        elif self.deuxieme.isChecked():
            e["niveau"]="deuxieme"
            self.erreurniveau.setText("niveau selectionner ✓")
            self.erreurniveau.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
        elif self.troisieme.isChecked():
            e["niveau"]="troisieme"
            self.erreurniveau.setText("niveau selectionner ✓")
            self.erreurniveau.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
        else:
            ok=False
            self.erreurniveau.setText("aucune boutton selectionnée ! ")
        
        if ok:
            f=open("etudiant.org","ab")
            dump(e,f)
            f.close()
            self.label_29.setText("eleve ajoutée avec sucée✓")
        
    def affiche_etud(self):
        f = open("etudiant.org", "rb")
        data = []
        while True:
                try:
                        e = load(f)
                        data.append("num_inscription = {}   nom = {}   prenom = {}\n"
                                        "date de naissance = {}   adresse = {}   mail = {}\n"
                                        "tel = {}   section = {}   niveau = {}\n\n\n".format(
                                        e["num_inscription"], e["nom"], e["prenom"],
                                        e["date"], e["adresse"], e["mail"],
                                        e["tel"],e["section"], e["niveau"]))
                except EOFError:break
        f.close()
        self.label_46.setText(''.join(data))           

#------------------------------------------------------------------------------------
    def action2(self):
        e={}
        ok=True
        code=self.nom_2.text()
        if code.isdigit() and len(code) == 8:
            f=open("livres.org","rb")
            result=True
            f=open("livres.org","rb")
            while True:
                try:
                    e1=load(f)
                except Exception:break
                if e1["reference"]==code:
                    result=False
                    break  
            f.close()          
            if result:
                e["reference"]=code
                self.erreurni_2.setText('Le code reference valide ✓')
                self.erreurni_2.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            else:
                ok=False
                self.erreurni_2.setText('Le code reference existe déjà ')
        else:
            ok=False
            self.erreurni_2.setText("code reference invalid !")
        


        titre=self.prenom_2.text()
        if all(c.isalnum() or c.isspace() for c in titre) and (len(titre)>0):
            self.erreurni_3.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            self.erreurni_3.setText("titre valide ✓")
            e["titre"]=titre
        else:
            ok=False
            self.erreurni_3.setText("titre invalid !")

        
        name=self.adresse_2.text()
        pattern = r'^[A-Za-z]+([\s][A-Za-z]+)*$'
        match = re.match(pattern, name) is not None
        if match:
            self.erreurni_4.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            self.erreurni_4.setText("nom et prenom valide ✓")
            e["name"]=name
        else:
            ok=False
            self.erreurni_4.setText("nom et prenom invalid !")
        annee=self.mail_2.text()
        if len(annee) == 4 and annee.isdigit():
                e["annee"]=annee
                self.erreurni_5.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
                self.erreurni_5.setText("année valid ✓")
        else:
             ok=False
             self.erreurni_5.setText("année invalid !")
             
        nb_ex=self.tel_9.text()
        if len(nb_ex)>0 and nb_ex.isnumeric():
            e["nb_ex"]=nb_ex
            e["max"]=nb_ex
            self.erreurni_6.setText("nombres d'exemplaires valid ✓")
            self.erreurni_6.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")

        else:
            ok=False
            self.erreurni_6.setText("nombres d'exemplaires invalid !")
        if ok:
            f=open("livres.org","ab")
            dump(e,f)
            f.close()
            self.label_30.setText("livre ajoutée avec sucée✓")
        
    def affiche_livres1(self):
        f = open("livres.org", "rb")
        data = []
        while True:
            try:
                e = load(f)
                if "reference" in e and "titre" in e and "name" in e and "annee" in e and "nb_ex" in e:
                    data.append("reference = {}   titre = {}   nom et prenom auteur = {}\n"
                                    "année édition = {}   nombres d'exemplaires = {} \n\n"
                                    .format(e["reference"], e["titre"], e["name"],e["annee"], e["nb_ex"]))
            except EOFError:
                break
        f.close()
        self.label_52.setText(''.join(data)) 

    def affiche_livres2(self):
        f = open("livres.org", "rb")
        data = []
        reference = self.lineEdit_62.text()
        if reference.isdigit() and len(reference) == 8 :
                while True:
                    try:
                        e = load(f)
                        if reference == e["reference"]:
                                data.append("reference = {}   titre = {}   nom et prenom auteur = {}\n"
                                                "année édition = {}   nombres d'exemplaires = {} \n\n"
                                                .format(e["reference"], e["titre"], e["name"],e["annee"], e["nb_ex"]))
                    except EOFError:
                        break
                f.close()
                self.label_53.setText(''.join(data)) 
                self.erreurni_14.setText("")
        else:
             self.erreurni_14.setText("reference n'existe pas")

    def affiche_livres3(self):
        f = open("livres.org", "rb")
        data = []
        titre = self.lineEdit_63.text()
        if all(c.isalnum() or c.isspace() for c in titre) and (len(titre)>0):
                while True:
                    try:
                        e = load(f)
                        if titre == e["titre"]:
                                data.append("reference = {}   titre = {}   nom et prenom auteur = {}\n"
                                                "année édition = {}   nombres d'exemplaires = {} \n\n"
                                                .format(e["reference"], e["titre"], e["name"],e["annee"], e["nb_ex"]))
                    except EOFError:
                        break
                f.close()
                self.label_54.setText(''.join(data)) 
                self.erreurni_15.setText("")
        else:
             self.erreurni_15.setText("titre invalid !")
    def affiche_livres4(self):
        f = open("livres.org", "rb")
        data = []
        annee = self.lineEdit_64.text()
        if len(annee) == 4 and annee.isdigit():
                while True:
                    try:
                        e = load(f)
                        if annee == e["annee"]:
                                data.append("reference = {}   titre = {}   nom et prenom auteur = {}\n"
                                                "année édition = {}   nombres d'exemplaires = {} \n\n"
                                                .format(e["reference"], e["titre"], e["name"],e["annee"], e["nb_ex"]))
                    except EOFError:
                        break
                f.close()
                self.label_55.setText(''.join(data)) 
                self.erreurni_16.setText("")
        else:
             self.erreurni_16.setText("année invalid !")


    def affiche_livres5(self):
        f = open("livres.org", "rb")
        data = []
        name = self.lineEdit_65.text()
        pattern = r'^[A-Za-z]+([\s][A-Za-z]+)*$'
        match = re.match(pattern, name) is not None
        if match :
                while True:
                    try:
                        e = load(f)
                        if name == e["name"]:
                                data.append("reference = {}   titre = {}   nom et prenom auteur = {}\n"
                                                "année édition = {}   nombres d'exemplaires = {} \n\n"
                                                .format(e["reference"], e["titre"], e["name"],e["annee"], e["nb_ex"]))
                    except EOFError:
                        break
                f.close()
                self.label_56.setText(''.join(data)) 
                self.erreurni_17.setText("")
        else:
             self.erreurni_17.setText("année invalid !")
        
    def affiche_livres6(self):
        with open("livres.org", "rb") as f:
                books = []
                while True:
                    try:
                        book = load(f)
                        books.append(book)
                    except EOFError:
                        break
                sorted_books = sorted(books, key=lambda x: x["titre"]) 
                data = []
                for book in sorted_books:
                    data.append("reference = {}   titre = {}   nom et prenom auteur = {}\n"
                                "année édition = {}   nombres d'exemplaires = {} \n\n"
                                .format(book["reference"], book["titre"], book["name"], book["annee"], book["nb_ex"]))
                self.label_63.setText(''.join(data))

    def modifier_nb_ex(self):
         reference=self.lineEdit_61.text()
         nb_ex=self.lineEdit_60.text()
         if exist_ref(reference):
              if len(nb_ex)>0 and nb_ex.isnumeric():
                  modify_record2("nb_ex",reference,nb_ex)
                  self.sucess_sup_10.setText("modification done")
                  self.erreurni_10.setText("")
                  self.erreurni_11.setText("")
              else:
                    self.erreurni_11.setText("nombres d'exemplaires invalid")
         else:
              self.erreurni_10.setText("le reference n'existe pas")           

    def supprimer_livres1(self):
        code=self.nom_3.text()
        if exist_ref(code):
            f = open("livres.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                if e["reference"] != code:
                    records.append(e)

            f.close()

            f = open("livres.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.sucess_sup_7.setText("supression done ")
            self.erreurni_7.setText("")
            
        else:
            self.erreurni_7.setText("le référence n'existe pas")

    def supprimer_livres2(self):
        code=self.nom_4.text()
        pattern = r'^[A-Za-z]+([\s][A-Za-z]+)*$'
        match = re.match(pattern, code) is not None
        if match:
            f = open("livres.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                if e["name"] != code:
                    records.append(e)

            f.close()

            f = open("livres.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.sucess_sup_8.setText("supression done ")
            self.erreurni_8.setText("")
            
        else:
            self.erreurni_8.setText("le nom invalid !")

    def supprimer_livres3(self):
        code=self.nom_5.text()
        if len(code) == 4 and code.isnumeric():
            f = open("livres.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                if e["annee"] != code:
                    records.append(e)

            f.close()

            f = open("livres.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.sucess_sup_9.setText("supression done ")
            self.erreurni_9.setText("")
            
        else:
            self.erreurni_9.setText("l'année invalid !") 
#↓----------------------------------------------------------------------------------
    def action3(self):
        e={}
        ok=True
        code=self.ni_2.text()
        ref=self.nom_6.text()
        if not(exist(code)):
             ok=False
             self.erreurni_18.setText("cette numero n'existe pas")
        #elif deja_emprunté(code):
             #ok=False
             #self.erreurni_18.setText("cette eleve est déja emprunté un livre dans cette moment")
        else:
            e["num_inscription"]=code
            self.erreurni_18.setText("num inscription valide")
            self.erreurni_18.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
            
                  

        
        if not(exist_ref(ref)):
             ok=False
             self.erreurni_19.setText("cette livre n'existe pas")
        elif not(disponible(ref)):
             ok=False
             self.erreurni_19.setText("cette livre n'est pas disponible")
        else: 
            e["reference"]=ref
            self.erreurni_19.setText("cette livre est disponible")
            self.erreurni_19.setStyleSheet("color: rgb(92, 121, 134);\nfont: 87 9pt 'Segoe UI Black';\n")
        date=datetime.now().strftime('%d/%m/%Y')
        e["date_emprunt"]=date
        date1 = datetime.strptime(date, "%d/%m/%Y") 
        new_date = date1 + timedelta(days=15)  
        date_retour = new_date.strftime("%d/%m/%Y")
        e["date_retour"]=date_retour
        if ok:
             e["retourne"]=False
             f=open("emprunts.org","ab")
             dump(e,f)
             decremente_max(ref)
             f.close()
             #self.label_32.setText("emprunt ajouté avec sucées")
    def afficher_emprunt1(self):
        f = open("emprunts.org", "rb")
        data = []
        while True:
            try:
                e = load(f)
                data.append("num_inscription = {}   reference = {}  \n"
                                    "date d'emprunt = {}   date de retour = {} \n\n"
                                    .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
            except EOFError:
                break
        f.close()
        self.label_100.setText(''.join(data)) 

    def retour_emprunt(self):
                code=self.lineEdit_68.text()   
                ref=self.lineEdit_70.text()
                ok=True        
                if not(exist(code)):
                        ok=False
                        self.erreurni_22.setText("numero d'inscription n'existe pas")
                else:
                        self.erreurni_22.setText("")
                if not(exist_ref(ref)):
                        ok=False
                        self.erreurni_23.setText("reference n'existe pas")
                else:
                        self.erreurni_23.setText("")
                if not(verif_emprunt(code,ref)):
                        ok=False
                        self.label_34.setText("cette eleve n'a pas emprunté cette livre")
                if not(retourner1(code,ref)):
                        ok=False
                        self.label_34.setText("cette eleve est déja retourné cette livre")
                if ok:
                        self.label_34.setText("emprunt retourné")
                        retourner(code,ref)

    def supprimer_emprunt(self):
        code=self.lineEdit_71.text()
        ref = self.lineEdit_72.text()
        date=self.date_3.text()
        ok=True
        if not(exist_emprunt(code,ref)):
             ok=False
             self.label_35.setText("numero ou reference n'existe pas")
        if ok:
            f = open("emprunts.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                if (e["num_inscription"] != code) or (e["reference"]!=ref) or (e["date_emprunt"]!=date):
                    records.append(e)
                else:
                     increment_max(ref)
            f.close()

            f = open("emprunts.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.label_35.setText("supression done ")
    def modifier_emprunt1(self):
        code=self.lineEdit_73.text()
        ref = self.lineEdit_74.text()
        date1=self.dateEdit_13.text()
        date2=self.dateEdit_5.text()
        ok=True
        if not(exist_emprunt(code,ref)):
             ok=False
             self.label_37.setText("numero ou reference n'existe pas")
        if ok:
            f = open("emprunts.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                records.append(e)
            f.close()
            for e in records:
                 if e["num_inscription"]==code and e["reference"]==ref and e["date_emprunt"]==date1:
                      e["date_emprunt"]==date2
                      

            f = open("emprunts.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.label_37.setText("modification done ")
    def modifier_emprunt2(self):
        code=self.lineEdit_76.text()
        ref = self.lineEdit_75.text()
        date1=self.dateEdit_14.text()
        date2=self.dateEdit_6.text()
        ok=True
        if not(exist_emprunt(code,ref)):
             ok=False
             self.label_37.setText("numero ou reference n'existe pas")
        if ok:
            f = open("emprunts.org", "rb")
            records=[]
            while True:
                try:
                    e = load(f)
                except EOFError:
                    break
                records.append(e)
            f.close()
            for e in records:
                 if e["num_inscription"]==code and e["reference"]==ref and e["date_retour"]==date1:
                      e["date_retour"]==date2
                      

            f = open("emprunts.org", "wb")
            for e in records:
                dump(e, f)
            f.close()
            self.label_36.setText("modification done ")
    def afficher_emprunt2(self):
        ref=self.lineEdit_78.text()
        ok=True
        if not(exist_ref(ref)):
             self.erreurni_41.setText("cette livre n'existe pas !")
             ok = False
        if ok:
                f = open("emprunts.org", "rb")
                data = []
                while True:
                    try:
                        e = load(f)
                        if e["reference"]==ref:
                                data.append("num_inscription = {}   reference = {}  \n"
                                                "date d'emprunt = {}   date de retour = {} \n\n"
                                                .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
                    except EOFError:
                        break  
                f.close()
                self.label_101.setText(''.join(data)) 


    def afficher_emprunt3(self):
        code=self.lineEdit_77.text()
        ok=True
        if not(exist(code)):
             self.erreurni_41.setText("cette eleve n'existe pas !")
             ok = False
        if ok:
                f = open("emprunts.org", "rb")
                data = []
                while True:
                    try:
                        e = load(f)
                        if e["num_inscription"]==code:
                                data.append("num_inscription = {}   reference = {}  \n"
                                                "date d'emprunt = {}   date de retour = {} \n\n"
                                                .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
                    except EOFError:
                        break  
                f.close()
                self.label_102.setText(''.join(data))


    def afficher_emprunt4(self):
        date=self.dateEdit_7.text()
        ok=True
        if ok:
                f = open("emprunts.org", "rb")
                data = []
                while True:
                    try:
                        e = load(f)
                        if e["date_emprunt"]==date:
                                data.append("num_inscription = {}   reference = {}  \n"
                                                "date d'emprunt = {}   date de retour = {} \n\n"
                                                .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
                    except EOFError:
                        break  
                f.close()
                self.label_104.setText(''.join(data))


    def afficher_emprunt5(self):
        date=self.dateEdit_8.text()
        ok=True
        if ok:
                f = open("emprunts.org", "rb")
                data = []
                while True:
                    try:
                        e = load(f)
                        if e["date_retour"]==date:
                                data.append("num_inscription = {}   reference = {}  \n"
                                                "date d'emprunt = {}   date de retour = {} \n\n"
                                                .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
                    except EOFError:
                        break  
                f.close()
                self.label_105.setText(''.join(data))
    def afficher_emprunt6(self):
        date1=self.dateEdit_9.text()
        date2=self.dateEdit_10.text()
        if not(mrigel(date1,date2)):
             ok=False
             self.erreurni_36.setText("la date 1 doit etre inferieur a la date 2")
        ok=True

        if ok:
                f = open("emprunts.org", "rb")
                data = []
                while True:
                    try:
                        e = load(f)
                        if mrigel(date1,e["date_emprunt"]) and mrigel(e["date_emprunt"],date2) :
                                data.append("num_inscription = {}   reference = {}  \n"
                                                "date d'emprunt = {}   date de retour = {} \n\n"
                                                .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
                    except EOFError:
                        break  
                f.close()
                self.label_106.setText(''.join(data))


    def afficher_emprunt7(self):
        date1=self.dateEdit_12.text()
        date2=self.dateEdit_11.text()
        if not(mrigel(date1,date2)):
             ok=False
             self.erreurni_34.setText("la date 1 doit etre inferieur a la date 2")
        ok=True
        if ok:
                f = open("emprunts.org", "rb")
                data = []
                while True:
                    try:
                        e = load(f)
                        if mrigel(date1,e["date_retour"]) and mrigel(e["date_retour"],date2) :
                                data.append("num_inscription = {}   reference = {}  \n"
                                                "date d'emprunt = {}   date de retour = {} \n\n"
                                                .format(e["num_inscription"], e["reference"], e["date_emprunt"],e["date_retour"]))
                    except EOFError:
                        break  
                f.close()
                self.label_107.setText(''.join(data))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
