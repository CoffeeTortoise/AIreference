from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QTextEdit, QComboBox, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
import os
from servchar import ANSWER_FILE, QUESTION_FILE, THEME_FILE, SUBTHEME_FILE, SYM_SEP, ENCODE
from paths import DATABASE_PATH


class QuestMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 dy: int,
                 style_border: str,
                 size: tuple[int, int],
                 pos: tuple[int, int]) -> None:
        super().__init__(master)
        self.dy: int = dy
        self.widget_w: int = int(size[0] * .5)
        self.border: str = style_border
        self.size: tuple[int, int] = size
        self.pos: tuple[int, int] = pos
        self.font: QFont = font
        self.layout: QGridLayout = QGridLayout(self)
        
        self.lbl_quest: QLabel = QLabel(self)
        self.txt_quest: QTextEdit = QTextEdit(self)
        
        self.lbl_answ: QLabel = QLabel(self)
        self.txt_answ: QTextEdit = QTextEdit(self)
        
        self.lbl_thm: QLabel = QLabel(self)
        self.box_thm: QComboBox = QComboBox(self)
        
        self.lbl_subthm: QLabel = QLabel(self)
        self.box_subthm: QComboBox = QComboBox(self)
        self.btn_subthm: QPushButton = QPushButton(self)
        
        self.btn_add: QPushButton = QPushButton(self)
        
        self.init_gui()
    
    def add_question(self) -> None:
        theme: str = self.box_thm.currentText()
        subtheme: str = self.box_subthm.currentText()
        subthemes: list[str] = self.get_subthemes_list(theme)
        if subtheme not in subthemes:
            return
        answer_file: str = f'{DATABASE_PATH}{theme}/{subtheme}/{ANSWER_FILE}'
        question_file: str = f'{DATABASE_PATH}{theme}/{subtheme}/{QUESTION_FILE}'
        if not os.path.exists(answer_file):
            return
        if not os.path.exists(question_file):
            return
        with open(answer_file, 'r', encoding=ENCODE) as file:
            answrs: str = file.read()
        with open(question_file, 'r', encoding=ENCODE) as file:
            qsts: str = file.read()
        ans_ls: list[str] = answrs.split(SYM_SEP)
        qst_ls: list[str] = qsts.split(SYM_SEP)
        answer: str = self.txt_answ.toPlainText()
        question: str = self.txt_quest.toPlainText()
        if question in qst_ls:
            return
        ans_ls.append(answer)
        qst_ls.append(question)
        answers: str = SYM_SEP.join(ans_ls)
        questions: str = SYM_SEP.join(qst_ls)
        with open(answer_file, 'w', encoding=ENCODE) as file:
            file.write(answers)
        with open(question_file, 'w', encoding=ENCODE) as file:
            file.write(questions)
    
    def update_db(self) -> None:
        self.update_themes()
        self.update_subthemes()

    def update_themes(self) -> None:
        themes: list[str] = self.get_themes_list()
        self.box_thm.clear()
        self.box_thm.addItems(themes)
    
    def update_subthemes(self) -> None:
        theme: str = self.box_thm.currentText()
        subthemes: list[str] = self.get_subthemes_list(theme)
        self.box_subthm.clear()
        self.box_subthm.addItems(subthemes)
    
    def get_themes_list(self) -> list[str]:
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        if not os.path.exists(theme_file):
            return ['']
        with open(theme_file, 'r', encoding=ENCODE) as file:
            themes: str = file.read()
        thm_ls: list[str] = themes.split(SYM_SEP)
        thms: list[str] = [theme for theme in thm_ls if (theme != '')]
        return thms

    def get_subthemes_list(self, theme: str) -> list[str]:
        subthm_file: str = f'{DATABASE_PATH}{theme}/{SUBTHEME_FILE}'
        if not os.path.exists(subthm_file):
            return ['']
        with open(subthm_file, 'r', encoding=ENCODE) as file:
            subthms: str = file.read()
        subthm_ls: list[str] = subthms.split(SYM_SEP)
        subthemes: list[str] = [subtheme for subtheme in subthm_ls if (subtheme != '')]
        return subthemes
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_lbl_quest()
        self.init_txt_quest()
        self.init_lbl_answ()
        self.init_txt_answ()
        self.init_lbl_thm()
        self.init_box_thm()
        self.init_lbl_subthm()
        self.init_box_subthm()
        self.init_btn_subthm()
        self.init_btn_add()
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])
    
    def init_lbl_quest(self) -> None:
        txt: str = 'Question'
        self.lbl_quest.setText(txt)
        self.lbl_quest.setFont(self.font)
        self.lbl_quest.setFixedSize(self.widget_w, self.dy)
        self.lbl_quest.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_quest, 2, 0)
    
    def init_txt_quest(self) -> None:
        size: tuple[int, int] = self.widget_w, self.dy * 5
        self.txt_quest.setFixedSize(size[0], size[1])
        self.txt_quest.setFont(self.font)
        self.layout.addWidget(self.txt_quest, 3, 0)
    
    def init_lbl_answ(self) -> None:
        txt: str = 'Answer'
        self.lbl_answ.setText(txt)
        self.lbl_answ.setFont(self.font)
        self.lbl_answ.setFixedSize(self.widget_w, self.dy)
        self.lbl_answ.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_answ, 2, 1)
    
    def init_txt_answ(self) -> None:
        size: tuple[int, int] = self.widget_w, self.dy * 5
        self.txt_answ.setFixedSize(size[0], size[1])
        self.txt_answ.setFont(self.font)
        self.layout.addWidget(self.txt_answ, 3, 1)
    
    def init_lbl_thm(self) -> None:
        txt: str = 'Theme'
        self.lbl_thm.setText(txt)
        self.lbl_thm.setFont(self.font)
        self.lbl_thm.setFixedSize(self.widget_w, self.dy)
        self.lbl_thm.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_thm, 0, 0)
    
    def init_box_thm(self) -> None:
        themes: list[str] = self.get_themes_list()
        self.box_thm.addItems(themes)
        self.box_thm.setFont(self.font)
        self.box_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_thm, 1, 0)
    
    def init_lbl_subthm(self) -> None:
        txt: str = 'Subthemes'
        self.lbl_subthm.setText(txt)
        self.lbl_subthm.setFont(self.font)
        self.lbl_subthm.setFixedSize(self.widget_w, self.dy)
        self.lbl_subthm.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_subthm, 0, 1)
    
    def init_box_subthm(self) -> None:
        self.box_subthm.setFont(self.font)
        self.box_subthm.setFixedSize(self.widget_w, self.dy)
        self.update_subthemes()
        self.layout.addWidget(self.box_subthm, 1, 1)
    
    def init_btn_subthm(self) -> None:
        txt: str = 'Update subthemes'
        self.btn_subthm.setText(txt)
        self.btn_subthm.setFont(self.font)
        self.btn_subthm.setFixedSize(self.widget_w, self.dy)
        self.btn_subthm.clicked.connect(self.update_subthemes)
        self.layout.addWidget(self.btn_subthm, 4, 0)
    
    def init_btn_add(self) -> None:
        txt: str = 'Add question'
        self.btn_add.setText(txt)
        self.btn_add.setFont(self.font)
        self.btn_add.setFixedSize(self.widget_w, self.dy)
        self.btn_add.clicked.connect(self.add_question)
        self.layout.addWidget(self.btn_add, 4, 1)
