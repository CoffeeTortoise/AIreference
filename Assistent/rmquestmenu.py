from PyQt5.QtWidgets import QWidget, QMainWindow, QComboBox, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QFont
import os
from servchar import ANSWER_FILE, QUESTION_FILE, SUBTHEME_FILE, THEME_FILE, SYM_SEP, ENCODE
from paths import DATABASE_PATH


class RmQuestMenu(QWidget):
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
        
        self.lbl_thm: QLabel = QLabel(self)
        self.lbl_subthm: QLabel = QLabel(self)
        self.lbl_qst: QLabel = QLabel(self)
        
        self.box_thm: QComboBox = QComboBox(self)
        self.box_subthm: QComboBox = QComboBox(self)
        self.box_qst: QComboBox = QComboBox(self)
        
        self.btn_update: QPushButton = QPushButton(self)
        self.btn_remove: QPushButton = QPushButton(self)
        
        self.init_gui()
    
    def rm_question(self) -> None:
        theme: str = self.box_thm.currentText()
        subtheme: str = self.box_subthm.currentText()
        question_file: str = f'{DATABASE_PATH}{theme}/{subtheme}/{QUESTION_FILE}'
        if not os.path.exists(question_file):
            return
        answer_file: str = f'{DATABASE_PATH}{theme}/{subtheme}/{ANSWER_FILE}'
        question: str = self.box_qst.currentText()
        questions: list[str] = RmQuestMenu.get_quests_list(theme, subtheme)
        answers: list[str] = RmQuestMenu.get_answers_list(theme, subtheme)
        qst_ind: int = questions.index(question)
        answer: str = answers[qst_ind]
        questions.remove(question)
        answers.remove(answer)
        answrs: str = SYM_SEP.join(answers)
        qsts: str = SYM_SEP.join(questions)
        with open(question_file, 'w', encoding=ENCODE) as file:
            file.write(qsts)
        with open(answer_file, 'w', encoding=ENCODE) as file:
            file.write(answrs)
        self.update_questions()
    
    def update_db(self) -> None:
        self.update_themes()
        self.update_subthemes()
        self.update_questions()

    def update_themes(self) -> None:
        themes: list[str] = RmQuestMenu.get_themes_list()
        self.box_thm.clear()
        self.box_thm.addItems(themes)
    
    def update_data(self) -> None:
        self.update_subthemes()
        self.update_questions()
    
    def update_questions(self) -> None:
        theme: str = self.box_thm.currentText()
        subtheme: str = self.box_subthm.currentText()
        questions: list[str] = RmQuestMenu.get_quests_list(theme, subtheme)
        quests: list[str] = [quest for quest in questions if (quest != '')]
        self.box_qst.clear()
        self.box_qst.addItems(quests)
    
    def update_subthemes(self) -> None:
        theme: str = self.box_thm.currentText()
        subthemes: list[str] = self.get_subthemes_list(theme)
        self.box_subthm.clear()
        self.box_subthm.addItems(subthemes)
    
    @staticmethod
    def get_quests_list(theme: str,
                        subtheme: str) -> list[str]:
        question_file: str = f'{DATABASE_PATH}{theme}/{subtheme}/{QUESTION_FILE}'
        if not os.path.exists(question_file):
            return ['']
        with open(question_file, 'r', encoding=ENCODE) as file:
            qsts: str = file.read()
        questions: list[str] = qsts.split(SYM_SEP)
        return questions
    
    @staticmethod
    def get_answers_list(theme: str,
                         subtheme: str) -> list[str]:
        answer_file: str = f'{DATABASE_PATH}{theme}/{subtheme}/{ANSWER_FILE}'
        if not os.path.exists(answer_file):
            return ['']
        with open(answer_file, 'r', encoding=ENCODE) as file:
            answrs: str = file.read()
        answers: list[str] = answrs.split(SYM_SEP)
        return answers
    
    @staticmethod
    def get_themes_list() -> list[str]:
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'r', encoding=ENCODE) as file:
            themes: str = file.read()
        thm_ls: list[str] = themes.split(SYM_SEP)
        thms: list[str] = [theme for theme in thm_ls if (theme != '')]
        return thms

    @staticmethod
    def get_subthemes_list(theme: str) -> list[str]:
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
        self.init_lbl_thm()
        self.init_lbl_subthm()
        self.init_box_thm()
        self.init_box_subthm()
        self.init_lbl_qst()
        self.init_box_qst()
        self.init_btn_update()
        self.init_btn_remove()
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])
    
    def init_lbl_thm(self) -> None:
        txt: str = 'Theme'
        self.lbl_thm.setText(txt)
        self.lbl_thm.setFont(self.font)
        self.lbl_thm.setStyleSheet(self.border)
        self.lbl_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.lbl_thm, 0, 0)
    
    def init_lbl_subthm(self) -> None:
        txt: str = 'Subtheme'
        self.lbl_subthm.setText(txt)
        self.lbl_subthm.setFont(self.font)
        self.lbl_subthm.setStyleSheet(self.border)
        self.lbl_subthm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.lbl_subthm, 0, 1)
    
    def init_box_thm(self) -> None:
        themes: list[str] = RmQuestMenu.get_themes_list()
        self.box_thm.addItems(themes)
        self.box_thm.setFont(self.font)
        self.box_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_thm, 1, 0)
    
    def init_box_subthm(self) -> None:
        self.update_subthemes()
        self.box_subthm.setFont(self.font)
        self.box_subthm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_subthm, 1, 1)
    
    def init_lbl_qst(self) -> None:
        size: tuple[int, int] = self.widget_w, self.dy * 9
        txt: str = 'Question'
        self.lbl_qst.setText(txt)
        self.lbl_qst.setFont(self.font)
        self.lbl_qst.setStyleSheet(self.border)
        self.lbl_qst.setFixedSize(size[0], size[1])
        self.layout.addWidget(self.lbl_qst, 2, 0)
    
    def init_box_qst(self) -> None:
        self.update_questions()
        self.box_qst.setFont(self.font)
        size: tuple[int, int] = self.widget_w, self.dy * 9
        self.box_qst.setFixedSize(size[0], size[1])
        self.layout.addWidget(self.box_qst, 2, 1)
    
    def init_btn_update(self) -> None:
        txt: str = 'Update'
        self.btn_update.setText(txt)
        self.btn_update.setFont(self.font)
        self.btn_update.setFixedSize(self.widget_w, self.dy)
        self.btn_update.clicked.connect(self.update_data)
        self.layout.addWidget(self.btn_update, 3, 0)
    
    def init_btn_remove(self) -> None:
        txt: str = 'Remove question'
        self.btn_remove.setText(txt)
        self.btn_remove.setFont(self.font)
        self.btn_remove.setFixedSize(self.widget_w, self.dy)
        self.btn_remove.clicked.connect(self.rm_question)
        self.layout.addWidget(self.btn_remove, 3, 1)
