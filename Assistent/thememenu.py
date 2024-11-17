from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
import os
from paths import DATABASE_PATH
from servchar import THEME_FILE, SUBTHEME_FILE, FORBIDDEN_SYMS, SYM_SEP, ENCODE


class ThemeMenu(QWidget):
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
        self.lbl_theme: QLabel = QLabel(self)
        self.lin_theme: QLineEdit = QLineEdit(self)
        self.btn_add: QPushButton = QPushButton(self)
        self.init_gui()
    
    def add_theme(self) -> None:
        source: str = self.lin_theme.text()
        if source.startswith('_'):
            r_source: str = source.replace('_', 'I')
            source = r_source
        syms: list[str] = ['' if (sym in FORBIDDEN_SYMS) else sym for sym in source]
        theme: str = ''.join(syms)
        if theme == '':
            return
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'r', encoding=ENCODE) as file:
            lines: str = file.read()
        theme_found: list[str] = lines.split(SYM_SEP)
        if theme in theme_found:
            return
        theme_found.append(theme)
        themes: str = SYM_SEP.join(theme_found)
        with open(theme_file, 'w', encoding=ENCODE) as file:
            file.write(themes)
        theme_folder: str = f'{DATABASE_PATH}{theme}'
        subtheme_file: str = f'{theme_folder}/{SUBTHEME_FILE}'
        os.makedirs(theme_folder)
        with open(subtheme_file, 'w', encoding=ENCODE) as file:
            file.write('')
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_lbl_theme()
        self.init_lin_theme()
        self.init_btn_add()
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])
    
    def init_lbl_theme(self) -> None:
        txt: str = 'Enter theme name'
        size: tuple[int, int] = self.widget_w, self.dy
        self.lbl_theme.setFixedSize(size[0], size[1])
        self.lbl_theme.setText(txt)
        self.lbl_theme.setFont(self.font)
        self.lbl_theme.setStyleSheet(self.border)
        self.layout.addWidget(self.lbl_theme, 0, 0)
    
    def init_lin_theme(self) -> None:
        txt: str = 'Example'
        size: tuple[int, int] = self.widget_w, self.dy
        self.lin_theme.setFixedSize(size[0], size[1])
        self.lin_theme.setText(txt)
        self.lin_theme.setFont(self.font)
        self.layout.addWidget(self.lin_theme, 0, 1)
    
    def init_btn_add(self) -> None:
        txt: str = 'Add theme'
        size: tuple[int, int] = self.widget_w, self.dy
        self.btn_add.setFixedSize(size[0], size[1])
        self.btn_add.setText(txt)
        self.btn_add.setFont(self.font)
        self.btn_add.clicked.connect(self.add_theme)
        self.layout.addWidget(self.btn_add, 1, 1)
        