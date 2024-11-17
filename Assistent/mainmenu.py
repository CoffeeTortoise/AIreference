from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont


class MainMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 dy: int,
                 style_border: str,
                 size: tuple[int, int],
                 pos: tuple[int, int]) -> None:
        super().__init__(master)
        self.dy: int = dy
        self.border: str = style_border
        self.pos: tuple[int, int] = pos
        self.size: tuple[int, int] = size
        self.font: QFont = font
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.button_conf: QPushButton = QPushButton(self)
        self.button_theme: QPushButton = QPushButton(self)
        self.button_subthm: QPushButton = QPushButton(self)
        self.btn_add_quest: QPushButton = QPushButton(self)
        self.btn_ask_quest: QPushButton = QPushButton(self)
        self.btn_rm_quest: QPushButton = QPushButton(self)
        self.btn_rm_subthm: QPushButton = QPushButton(self)
        self.btn_rm_thm: QPushButton = QPushButton(self)
        self.btn_rm_all: QPushButton = QPushButton(self)
        self.btn_update: QPushButton = QPushButton(self)
        self.btn_quit: QPushButton = QPushButton(self)
        self.init_gui()
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_btn_conf()
        self.init_btn_theme()
        self.init_btn_subthm()
        self.init_btn_add_quest()
        self.init_btn_ask_quest()
        self.init_btn_rm_quest()
        self.init_btn_rm_subthm()
        self.init_btn_rm_thm()
        self.init_btn_rm_all()
        self.init_btn_update()
        self.init_btn_quit()
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])
    
    def init_btn_conf(self) -> None:
        size: tuple[int, int] = self.size[0], self.dy
        txt: str = 'Configure'
        self.button_conf.setFixedSize(size[0], size[1])
        self.button_conf.setText(txt)
        self.button_conf.setFont(self.font)
        self.layout.addWidget(self.button_conf)
    
    def init_btn_theme(self) -> None:
        size: tuple[int, int] = self.size[0], self.dy
        txt: str = 'Add theme'
        self.button_theme.setFixedSize(size[0], size[1])
        self.button_theme.setText(txt)
        self.button_theme.setFont(self.font)
        self.layout.addWidget(self.button_theme)
    
    def init_btn_subthm(self) -> None:
        size: tuple[int, int] = self.size[0], self.dy
        txt: str = 'Add subtheme'
        self.button_subthm.setFixedSize(size[0], size[1])
        self.button_subthm.setText(txt)
        self.button_subthm.setFont(self.font)
        self.layout.addWidget(self.button_subthm)
    
    def init_btn_add_quest(self) -> None:
        txt: str = 'Add question'
        self.btn_add_quest.setText(txt)
        self.btn_add_quest.setFont(self.font)
        self.btn_add_quest.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_add_quest)
    
    def init_btn_ask_quest(self) -> None:
        txt: str = 'Ask question'
        self.btn_ask_quest.setText(txt)
        self.btn_ask_quest.setFont(self.font)
        self.btn_ask_quest.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_ask_quest)
    
    def init_btn_rm_quest(self) -> None:
        txt: str = 'Remove question'
        self.btn_rm_quest.setText(txt)
        self.btn_rm_quest.setFont(self.font)
        self.btn_rm_quest.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_rm_quest)
    
    def init_btn_rm_subthm(self) -> None:
        txt: str = 'Remove subtheme'
        self.btn_rm_subthm.setText(txt)
        self.btn_rm_subthm.setFont(self.font)
        self.btn_rm_subthm.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_rm_subthm)
    
    def init_btn_rm_thm(self) -> None:
        txt: str = 'Remove theme'
        self.btn_rm_thm.setText(txt)
        self.btn_rm_thm.setFont(self.font)
        self.btn_rm_thm.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_rm_thm)
    
    def init_btn_rm_all(self) -> None:
        txt: str = 'Remove all'
        self.btn_rm_all.setText(txt)
        self.btn_rm_all.setFont(self.font)
        self.btn_rm_all.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_rm_all)
    
    def init_btn_update(self) -> None:
        txt: str = 'Update all'
        self.btn_update.setText(txt)
        self.btn_update.setFont(self.font)
        self.btn_update.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_update)
    
    def init_btn_quit(self) -> None:
        txt: str = 'Quit'
        self.btn_quit.setText(txt)
        self.btn_quit.setFont(self.font)
        self.btn_quit.setFixedSize(self.size[0], self.dy)
        self.layout.addWidget(self.btn_quit)
