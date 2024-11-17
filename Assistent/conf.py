from paths import CONF
from servchar import ENCODE


class Config:
    ROWS: int = 0
    COLS: int = 0
    SIZE: int = 0
    FNT_SIZE: int = 0
    BORDER_W: int = 0
    WND_WIDTH: int = 0
    WND_HEIGHT: int = 0
    WND_SIZE: tuple[int, int] = 0, 0
    TITLE: str = ''
    SEP: str = '='
    NAMES: tuple[str, ...] = 'ROWS', 'COLS', 'SIZE', 'TITLE'
    """ROWS, COLS, SIZE, TITLE"""
    
    @staticmethod
    def read_conf() -> None:
        with open(CONF, 'r', encoding=ENCODE) as file:
            lines: list[str] = file.readlines()
        source: list[str] = [line.replace('\n', '').replace(' ', '') for line in lines]
        for line in source:
            if line.startswith(Config.NAMES[0]):
                Config.ROWS = int(line.split(Config.SEP)[1])
            elif line.startswith(Config.NAMES[1]):
                Config.COLS = int(line.split(Config.SEP)[1])
            elif line.startswith(Config.NAMES[2]):
                Config.SIZE = int(line.split(Config.SEP)[1])
            elif line.startswith(Config.NAMES[3]):
                Config.TITLE = line.split(Config.SEP)[1]
            else:
                continue
        Config.FNT_SIZE = int(Config.SIZE * .5)
        Config.BORDER_W = int(Config.SIZE * .1)
        Config.WND_WIDTH = Config.SIZE * Config.COLS
        Config.WND_HEIGHT = Config.SIZE * Config.ROWS
        Config.WND_SIZE = Config.WND_WIDTH, Config.WND_HEIGHT
    
    @staticmethod
    def write_conf(arg_name: str, arg_value: str) -> None:
        if arg_name not in Config.NAMES:
            return
        if type(arg_value) is not str:
            return
        with open(CONF, 'r', encoding=ENCODE) as file:
            lines: list[str] = file.readlines()
        res: str = ''
        for line in lines:
            if not line.startswith(arg_name):
                continue
            source: str = line.replace('\n', '').replace(' ', '').split(Config.SEP)[1]
            new_line: str = line.replace(source, arg_value)
            txt: str = ''.join(lines)
            res: str = txt.replace(line, new_line)
        with open(CONF, 'w', encoding=ENCODE) as file:
            file.write(res)
