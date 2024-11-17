from PyQt5.QtWidgets import QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont
from conf import Config


class ConfMenu(QWidget):
    def __init__(self,
                 master: QMainWindow,
                 font: QFont,
                 dy: int,
                 style_border: str,
                 size: tuple[int, int],
                 pos: tuple[int, int]) -> None:
        super().__init__(master)
        self.font: QFont = font
        self.dy: int = dy
        self.border: str = style_border
        self.size: tuple[int, int] = size
        self.pos: tuple[int, int] = pos
        self.layout: QGridLayout = QGridLayout(self)
        self.labels: list[QLabel] = []
        self.lines: list[QLineEdit] = []
        self.btn_confirm: QPushButton = QPushButton(self)
        self.init_gui()
    
    def init_gui(self) -> None:
        self.init_wnd()
        self.init_edit()
        self.init_btn_confirm()
    
    def change_config(self) -> None:
        values: list[str] = [line.text() for line in self.lines]
        names_int: tuple[str, ...] = Config.NAMES[:3]
        nums: str = '0123456789.'
        for i, arg in enumerate(Config.NAMES):
            if arg in names_int:
                val: list[str] = []
                number: str = values[i].replace(' ', '').replace('\n', '')
                for sym in number:
                    if sym not in nums:
                        val.append('')
                    else:
                        val.append(sym)
                num: str = ''.join(val)
                if (num.startswith('0') or num.startswith('.')) or (num == ''):
                    values[i] = getattr(Config, arg)
                else:
                    values[i] = num
            Config.write_conf(arg, values[i])
    
    def init_btn_confirm(self) -> None:
        txt: str = 'Confirm'
        size: tuple[int, int] = int(self.size[0] * .5), self.dy
        row: int = len(self.lines)
        self.btn_confirm.setText(txt)
        self.btn_confirm.setFixedSize(size[0], size[1])
        self.btn_confirm.setFont(self.font)
        self.btn_confirm.clicked.connect(self.change_config)
        self.layout.addWidget(self.btn_confirm, row, 1)
    
    def init_edit(self) -> None:
        width: int = int(self.size[0] * .5)
        for i, param in enumerate(Config.NAMES):
            self.init_lbl(i, width, param)
            arg: int | str = getattr(Config, param)
            if type(arg) is not str:
                str_arg: str = str(arg)
                arg: str = str_arg
            self.init_line(i, width, arg)
    
    def init_line(self,
                  row: int,
                  width: int,
                  text: str) -> None:
        line: QLineEdit = QLineEdit(self)
        line.setFixedSize(width, self.dy)
        line.setText(text)
        line.setFont(self.font)
        self.layout.addWidget(line, row, 1)
        self.lines.append(line)
    
    def init_lbl(self,
                 row: int,
                 width: int,
                 text: str) -> None:
        label: QLabel = QLabel(self)
        label.setFixedSize(width, self.dy)
        label.setText(text)
        label.setFont(self.font)
        label.setStyleSheet(self.border)
        self.layout.addWidget(label, row, 0)
        self.labels.append(label)
    
    def init_wnd(self) -> None:
        self.setFixedSize(self.size[0], self.size[1])
        self.move(self.pos[0], self.pos[1])