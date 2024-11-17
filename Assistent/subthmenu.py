from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont
import os
from servchar import ANSWER_FILE, QUESTION_FILE, SUBTHEME_FILE, THEME_FILE, SYM_SEP, FORBIDDEN_SYMS, ENCODE
from paths import DATABASE_PATH


class SubthMenu(QWidget):
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
        self.box_thm: QComboBox = QComboBox(self)
        self.lbl_entr: QLabel = QLabel(self)
        self.lin_entr: QLineEdit = QLineEdit(self)
        self.btn_add: QPushButton = QPushButton(self)
        
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'r', encoding=ENCODE) as file:
            themes: str = file.read()
        them_ls: list[str] = themes.split(SYM_SEP)
        self.themes: list[str] = [thm for thm in them_ls if (thm != '')]
        
        self.init_gui()
    
    def update_themes(self) -> None:
        themes: list[str] = self.get_themes_list()
        self.box_thm.clear()
        self.box_thm.addItems(themes)
    
    def get_themes_list(self) -> list[str]:
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'r', encoding=ENCODE) as file:
            themes: str = file.read()
        them_ls: list[str] = themes.split(SYM_SEP)
        themes: list[str] = [thm for thm in them_ls if (thm != '')]
        return themes
    
    def add_subtheme(self) -> None:
        theme: str = self.box_thm.currentText()
        source: str = self.lin_entr.text()
        if source.startswith('_'):
            src: str = source.replace('_', 'I')
            source = src
        subtheme_ls: list[str] = ['' if (sym in FORBIDDEN_SYMS) else sym for sym in source]
        subtheme: str = ''.join(subtheme_ls)
        if subtheme == '':
            return
        subtheme_file: str = f'{DATABASE_PATH}{theme}/{SUBTHEME_FILE}'
        if not os.path.exists(subtheme_file):
            return
        with open(subtheme_file, 'r', encoding=ENCODE) as file:
            subthemes: str = file.read()
        subthemes_ls: list[str] = subthemes.split(SYM_SEP)
        if subtheme in subthemes_ls:
            return
        subthemes_ls.append(subtheme)
        new_subthemes: str = SYM_SEP.join(subthemes_ls)
        with open(subtheme_file, 'w', encoding=ENCODE) as file:
            file.write(new_subthemes)
        subtheme_folder: str = f'{DATABASE_PATH}{theme}/{subtheme}'
        answer_file: str = f'{subtheme_folder}/{ANSWER_FILE}'
        question_file: str = f'{subtheme_folder}/{QUESTION_FILE}'
        os.makedirs(subtheme_folder)
        with open(answer_file, 'w', encoding=ENCODE) as file:
            file.write('')
        with open(question_file, 'w', encoding=ENCODE) as file:
            file.write('')
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_lbl_thm()
        self.init_box_thm()
        self.init_lbl_entr()
        self.init_lin_entr()
        self.init_btn_add()
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])
    
    def init_lbl_thm(self) -> None:
        txt: str = 'Theme'
        self.lbl_thm.setText(txt)
        self.lbl_thm.setFont(self.font)
        self.lbl_thm.setFixedSize(self.widget_w, self.dy)
        self.lbl_thm.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_thm, 0, 0)
    
    def init_box_thm(self) -> None:
        self.box_thm.addItems(self.themes)
        self.box_thm.setFont(self.font)
        self.box_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_thm, 0, 1)
    
    def init_lbl_entr(self) -> None:
        txt: str = 'Enter the subtheme name'
        self.lbl_entr.setText(txt)
        self.lbl_entr.setFont(self.font)
        self.lbl_entr.setFixedSize(self.widget_w, self.dy)
        self.lbl_entr.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_entr, 1, 0)
    
    def init_lin_entr(self) -> None:
        self.lin_entr.setFixedSize(self.widget_w, self.dy)
        self.lin_entr.setFont(self.font)
        self.layout.addWidget(self.lin_entr, 1, 1)
    
    def init_btn_add(self) -> None:
        txt: str = 'Add subtheme'
        self.btn_add.setText(txt)
        self.btn_add.setFont(self.font)
        self.btn_add.setFixedSize(self.widget_w, self.dy)
        self.btn_add.clicked.connect(self.add_subtheme)
        self.layout.addWidget(self.btn_add, 2, 1)
