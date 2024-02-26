from enum import Enum 
# Доступные роуты в приложении
class Routes(Enum):
    # меню начальной настройки перед сканированием
    Begin = 'Begin'
    # просмотр таблицы с сканируемыми файлами
    # в реальном времени
    Watching = 'Watching'