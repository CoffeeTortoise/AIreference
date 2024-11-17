from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
import shutil
import os
from servchar import SUBTHEME_FILE, THEME_FILE, SYM_SEP, ENCODE
from paths import DATABASE_PATH


class RmSubthmMenu(QWidget):
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
        
        self.box_thm: QComboBox = QComboBox(self)
        self.box_subthm: QComboBox = QComboBox(self)
        
        self.btn_update: QPushButton = QPushButton(self)
        self.btn_remove: QPushButton = QPushButton(self)
        
        self.init_gui()
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_lbl_thm()
        self.init_lbl_subthm()
        self.init_box_thm()
        self.init_box_subthm()
        self.init_btn_update()
        self.init_btn_remove()
    
    def rm_subthm(self) -> None:
        theme: str = self.box_thm.currentText()
        subtheme: str = self.box_subthm.currentText()
        subtheme_file: str = f'{DATABASE_PATH}{theme}/{SUBTHEME_FILE}'
        subtheme_dir: str = f'{DATABASE_PATH}{theme}/{subtheme}'
        if not os.path.exists(subtheme_dir):
            return
        if not os.path.exists(subtheme_file):
            return
        shutil.rmtree(subtheme_dir)
        subthemes: list[str] = self.get_subthemes_list(theme)
        subthemes.remove(subtheme)
        sbthms: str = SYM_SEP.join(subthemes)
        with open(subtheme_file, 'w', encoding=ENCODE) as file:
            file.write(sbthms)
    
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
    
    def init_lbl_subthm(self) -> None:
        txt: str = 'Subthemes'
        self.lbl_subthm.setText(txt)
        self.lbl_subthm.setFont(self.font)
        self.lbl_subthm.setStyleSheet(self.border)
        self.lbl_subthm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.lbl_subthm, 0, 1)
    
    def init_box_thm(self) -> None:
        themes: list[str] = self.get_themes_list()
        self.box_thm.addItems(themes)
        self.box_thm.setFont(self.font)
        self.box_thm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_thm, 1, 0)
    
    def init_box_subthm(self) -> None:
        self.update_subthemes()
        self.box_subthm.setFont(self.font)
        self.box_subthm.setFixedSize(self.widget_w, self.dy)
        self.layout.addWidget(self.box_subthm, 1, 1)
    
    def init_btn_update(self) -> None:
        txt: str = 'Update subthemes'
        self.btn_update.setText(txt)
        self.btn_update.setFont(self.font)
        self.btn_update.setFixedSize(self.widget_w, self.dy)
        self.btn_update.clicked.connect(self.update_subthemes)
        self.layout.addWidget(self.btn_update, 2, 0)
    
    def init_btn_remove(self) -> None:
        txt: str = 'Remove subtheme'
        self.btn_remove.setText(txt)
        self.btn_remove.setFont(self.font)
        self.btn_remove.setFixedSize(self.widget_w, self.dy)
        self.btn_remove.clicked.connect(self.rm_subthm)
        self.layout.addWidget(self.btn_remove, 2, 1)
    