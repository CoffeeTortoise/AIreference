from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QTextEdit, QComboBox, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
import os
from servchar import ANSWER_FILE, QUESTION_FILE, THEME_FILE, SUBTHEME_FILE, SYM_SEP, ENCODE, MAX_SCORE
from paths import DATABASE_PATH


class AskMenu(QWidget):
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
        self.lbl_ans: QLabel = QLabel(self)
        self.lbl_answer: QLabel = QLabel(self)
        
        self.box_thm: QComboBox = QComboBox(self)
        self.box_subthm: QComboBox = QComboBox(self)
        
        self.txt_qst: QTextEdit = QTextEdit(self)
        
        self.btn_subthm: QPushButton = QPushButton(self)
        self.btn_answer: QPushButton = QPushButton(self)
        
        self.init_gui()
    
    def get_answer(self) -> None:
        theme: str = self.box_thm.currentText()
        subtheme: str = self.box_subthm.currentText()
        subthemes: list[str] = self.get_subthemes_list(theme)
        if subtheme not in subthemes:
            self.lbl_answer.setText('')
            return
        question: str = self.txt_qst.toPlainText()
        questions: list[str] = AskMenu.get_quests_list(theme, subtheme)
        answers: list[str] = AskMenu.get_answers_list(theme, subtheme)
        points: list[float] = [AskMenu.get_compare_point(question, quest) for quest in questions]
        fit_index: int = points.index(max(points))
        self.lbl_answer.setText(answers[fit_index])
    
    @staticmethod
    def get_compare_point(user_quest: str,
                          question: str) -> float:
        if len(user_quest) > len(question):
            big: str = user_quest
            small: str = question
        else:
            big: str = question
            small: str = user_quest
        comm_chrs: int = len(list(set(big) & set(small)))
        dif: int = len(big) + len(small) - comm_chrs
        if dif == 0:
            return MAX_SCORE
        k: float = comm_chrs / dif
        words_small: list[str] = small.split(' ')
        words_big: list[str] = big.split(' ')
        points: float = 0
        for word in words_small:
            for wrd in words_big:
                word_f: str = word.lower()
                wrd_f: str = wrd.lower()
                compare: list[bool] = list(map(lambda i, j: i == j, word_f, wrd_f))
                point: float = len([res for res in compare if res])
                points += point
        points *= k
        return points
    
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
        self.init_lbl_thm()
        self.init_lbl_subthm()
        self.init_box_thm()
        self.init_box_subthm()
        self.init_txt_qst()
        self.init_lbl_qst()
        self.init_lbl_ans()
        self.init_lbl_answer()
        self.init_btn_subthm()
        self.init_btn_answer()
    
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
        themes: list[str] = self.get_themes_list()
        self.box_thm.setFont(self.font)
        self.box_thm.setFixedSize(self.widget_w, self.dy)
        self.box_thm.addItems(themes)
        self.layout.addWidget(self.box_thm, 1, 0)
    
    def init_box_subthm(self) -> None:
        self.box_subthm.setFont(self.font)
        self.box_subthm.setFixedSize(self.widget_w, self.dy)
        self.update_subthemes()
        self.layout.addWidget(self.box_subthm, 1, 1)
    
    def init_lbl_qst(self) -> None:
        txt: str = 'Question'
        self.lbl_qst.setText(txt)
        self.lbl_qst.setFont(self.font)
        self.lbl_qst.setStyleSheet(self.border)
        self.lbl_qst.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.lbl_qst, 2, 0)
    
    def init_txt_qst(self) -> None:
        size: tuple[int, int] = self.widget_w, self.dy * 9
        self.txt_qst.setFont(self.font)
        self.txt_qst.setFixedSize(size[0], size[1])
        self.layout.addWidget(self.txt_qst, 3, 0)
    
    def init_lbl_ans(self) -> None:
        txt: str = 'Answer'
        self.lbl_ans.setText(txt)
        self.lbl_ans.setFont(self.font)
        self.lbl_ans.setStyleSheet(self.border)
        self.lbl_ans.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.lbl_ans, 2, 1)
    
    def init_lbl_answer(self) -> None:
        txt: str = ''
        size: tuple[int, int] = int(self.widget_w * .95), self.dy * 9
        self.lbl_answer.setText(txt)
        self.lbl_answer.setFont(self.font)
        self.lbl_answer.setStyleSheet(self.border)
        self.lbl_answer.setFixedSize(size[0], size[1])
        self.layout.addWidget(self.lbl_answer, 3, 1)
    
    def init_btn_subthm(self) -> None:
        txt: str = 'Update subthemes'
        self.btn_subthm.setText(txt)
        self.btn_subthm.setFont(self.font)
        self.btn_subthm.setFixedSize(self.widget_w, self.dy)
        self.btn_subthm.clicked.connect(self.update_subthemes)
        self.layout.addWidget(self.btn_subthm, 4, 0)
    
    def init_btn_answer(self) -> None:
        txt: str = 'Get answer'
        self.btn_answer.setText(txt)
        self.btn_answer.setFont(self.font)
        self.btn_answer.setFixedSize(self.widget_w, self.dy)
        self.btn_answer.clicked.connect(self.get_answer)
        self.layout.addWidget(self.btn_answer, 4, 1)


if __name__ == '__main__':
    ls1: list[str] = ['Turtle', 'Lizard', 'Snake']
    ls2: list[str] = ['coffee', 'Good choice', 'Snake', 'cake', 'pie']
    ls3: list[bool] = list(map(lambda i, j: i == j, ls2, ls1))
    print(ls3)
