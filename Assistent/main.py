from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QFont
import shutil
from paths import ICON, FONT, DATABASE_PATH
import sys
from servchar import THEME_FILE, ENCODE, SYM_SEP
from conf import Config
from mainmenu import MainMenu
from confmenu import ConfMenu
from thememenu import ThemeMenu
from subthmenu import SubthMenu
from questmenu import QuestMenu
from askmenu import AskMenu
from rmquestmenu import RmQuestMenu
from rmsubthmenu import RmSubthmMenu
from rmthmenu import RmThmMenu


class Assistent(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_main_wnd()
        font: QFont = QFont(FONT, Config.FNT_SIZE)
        dy: int = Config.SIZE * 2
        border: str = f'border: {Config.BORDER_W}px solid black'
        
        menu_pos: tuple[int, int] = 0, 0
        menu_size: tuple[int, int] = Config.SIZE * 10, Config.WND_HEIGHT
        self.menu_wnd: MainMenu = MainMenu(self, font, dy, border, menu_size, menu_pos)
        
        conf_pos: tuple[int, int] = menu_size[0], 0
        conf_size: tuple[int, int] = Config.WND_WIDTH - menu_size[0], menu_size[1]
        self.menu_conf: ConfMenu = ConfMenu(self, font, dy, border, conf_size, conf_pos)
        
        theme_pos: tuple[int, int] = conf_pos
        theme_size: tuple[int, int] = conf_size
        self.menu_theme: ThemeMenu = ThemeMenu(self, font, dy, border, theme_size, theme_pos)
        
        subthm_pos: tuple[int, int] = conf_pos
        subthm_size: tuple[int, int] = conf_size
        self.menu_subthm: SubthMenu = SubthMenu(self, font, dy, border, subthm_size, subthm_pos)
        
        qstm_pos: tuple[int, int] = conf_pos
        qstm_size: tuple[int, int] = conf_size
        self.menu_quest: QuestMenu = QuestMenu(self, font, dy, border, qstm_size, qstm_pos)
        
        askm_pos: tuple[int, int] = conf_pos
        askm_size: tuple[int, int] = conf_size[0], Config.WND_HEIGHT
        self.menu_ask: AskMenu = AskMenu(self, font, dy, border, askm_size, askm_pos)
        
        rmqst_pos: tuple[int, int] = conf_pos
        rmqst_size: tuple[int, int] = conf_size[0], Config.WND_HEIGHT
        self.menu_rmquest: RmQuestMenu = RmQuestMenu(self, font, dy, border, rmqst_size, rmqst_pos)
        
        rmsubth_pos: tuple[int, int] = conf_pos
        rmsubth_size: tuple[int, int] = conf_size[0], Config.SIZE * 10
        self.menu_rmsubth: RmSubthmMenu = RmSubthmMenu(self, font, dy, border, rmsubth_size, rmsubth_pos)
        
        rmthm_pos: tuple[int, int] = conf_pos
        rmthm_size: tuple[int, int] = conf_size[0], Config.SIZE * 10
        self.menu_rmthm: RmThmMenu = RmThmMenu(self, font, dy, border, rmthm_size, rmthm_pos)
        
        self.hide_widgets()
        self.set_menu_buttons()
    
    def update_db(self) -> None:
        self.menu_ask.update_db()
        self.menu_quest.update_db()
        self.menu_rmquest.update_db()
        self.menu_rmsubth.update_db()
        self.menu_rmthm.update_themes()
        self.menu_subthm.update_themes()
    
    def rm_all(self) -> None:
        themes: list[str] = self.get_themes_list()
        thm_dirs: list[str] = [f'{DATABASE_PATH}{theme}' for theme in themes if (theme != '')]
        [shutil.rmtree(tree) for tree in thm_dirs]
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'w', encoding=ENCODE) as file:
            file.write('')
    
    def get_themes_list(self) -> list[str]:
        theme_file: str = f'{DATABASE_PATH}{THEME_FILE}'
        with open(theme_file, 'r', encoding=ENCODE) as file:
            themes: str = file.read()
        thm_ls: list[str] = themes.split(SYM_SEP)
        thms: list[str] = [theme for theme in thm_ls if (theme != '')]
        return thms
    
    def open_menu_conf(self) -> None:
        self.hide_widgets()
        self.menu_conf.show()
    
    def open_menu_theme(self) -> None:
        self.hide_widgets()
        self.menu_theme.show()
    
    def open_menu_subthm(self) -> None:
        self.hide_widgets()
        self.menu_subthm.show()
    
    def open_menu_quest(self) -> None:
        self.hide_widgets()
        self.menu_quest.show()
    
    def open_menu_ask(self) -> None:
        self.hide_widgets()
        self.menu_ask.show()
    
    def open_menu_rmquest(self) -> None:
        self.hide_widgets()
        self.menu_rmquest.show()
    
    def open_menu_rmsubth(self) -> None:
        self.hide_widgets()
        self.menu_rmsubth.show()
    
    def open_menu_rmthm(self) -> None:
        self.hide_widgets()
        self.menu_rmthm.show()
    
    def hide_widgets(self) -> None:
        self.menu_conf.hide()
        self.menu_theme.hide()
        self.menu_subthm.hide()
        self.menu_quest.hide()
        self.menu_ask.hide()
        self.menu_rmquest.hide()
        self.menu_rmsubth.hide()
        self.menu_rmthm.hide()
    
    def set_menu_buttons(self) -> None:
        self.menu_wnd.button_conf.clicked.connect(self.open_menu_conf)
        self.menu_wnd.button_theme.clicked.connect(self.open_menu_theme)
        self.menu_wnd.button_subthm.clicked.connect(self.open_menu_subthm)
        self.menu_wnd.btn_add_quest.clicked.connect(self.open_menu_quest)
        self.menu_wnd.btn_ask_quest.clicked.connect(self.open_menu_ask)
        self.menu_wnd.btn_rm_quest.clicked.connect(self.open_menu_rmquest)
        self.menu_wnd.btn_rm_subthm.clicked.connect(self.open_menu_rmsubth)
        self.menu_wnd.btn_rm_thm.clicked.connect(self.open_menu_rmthm)
        self.menu_wnd.btn_rm_all.clicked.connect(self.rm_all)
        self.menu_wnd.btn_update.clicked.connect(self.update_db)
        self.menu_wnd.btn_quit.clicked.connect(QApplication.quit)
    
    def init_main_wnd(self) -> None:
        icon: QIcon = QIcon(ICON)
        self.setFixedSize(Config.WND_WIDTH, Config.WND_HEIGHT)
        self.setWindowTitle(Config.TITLE)
        self.setWindowIcon(icon)


if __name__ == '__main__':
    Config.read_conf()
    app: QApplication = QApplication(sys.argv)
    assist: Assistent = Assistent()
    assist.show()
    sys.exit(app.exec_())