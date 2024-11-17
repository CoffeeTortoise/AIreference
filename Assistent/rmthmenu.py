from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
import shutil
import os
from servchar import THEME_FILE, SYM_SEP, ENCODE
from paths import DATABASE_PATH


class RmThmMenu(QWidget):
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
        
        self.btn_update: QPushButton = QPushButton(self)
        self.btn_remove: QPushButton = QPushButton(self)
        
        self.init_gui()
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_lbl_thm()
        self.init_box_thm()
        self.init_btn_update()
        self.init_btn_remove()
    
    def rm_theme(self) -> None:
        theme: str = self.box_thm.currentText()
        if (theme == '') or (theme == ' '):
            return
        theme_dir: str = f'{DATABASE_PATH}{theme}'
        if not os.path.exists(theme_dir):
            return
        shutil.rmtree(theme_dir)
        themes: list[str] = self.get_themes_list()
        themes.remove(theme)
        thms: str = SYM_SEP.join(themes)
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'w', encoding=ENCODE) as file:
            file.write(thms)
    
    def update_themes(self) -> None:
        themes: list[str] = self.get_themes_list()
        self.box_thm.clear()
        self.box_thm.addItems(themes)
    
    def get_themes_list(self) -> list[str]:
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        if not os.path.exists(theme_file):
            return ['']
        with open(theme_file, 'r', encoding=ENCODE) as file:
            themes: str = file.read()
        thm_ls: list[str] = themes.split(SYM_SEP)
        thms: list[str] = [theme for theme in thm_ls if (theme != '')]
        return thms
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])
    
    def init_lbl_thm(self) -> None:
        txt: str = 'Themes'
        self.lbl_thm.setText(txt)
        self.lbl_thm.setFont(self.font)
        self.lbl_thm.setStyleSheet(self.border)
        self.lbl_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.lbl_thm, 0, 0)
    
    def init_box_thm(self) -> None:
        self.update_themes()
        self.box_thm.setFont(self.font)
        self.box_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_thm, 0, 1)
    
    def init_btn_update(self) -> None:
        txt: str = 'Update themes'
        self.btn_update.setText(txt)
        self.btn_update.setFont(self.font)
        self.btn_update.setFixedSize(self.widget_w, self.dy)
        self.btn_update.clicked.connect(self.update_themes)
        self.layout.addWidget(self.btn_update, 1, 0)
    
    def init_btn_remove(self) -> None:
        txt: str = 'Remove theme'
        self.btn_remove.setText(txt)
        self.btn_remove.setFont(self.font)
        self.btn_remove.setFixedSize(self.widget_w, self.dy)
        self.btn_remove.clicked.connect(self.rm_theme)
        self.layout.addWidget(self.btn_remove, 1, 1)
