import os.path
from pathlib import Path

from keras.models import load_model

def set_back_up() -> None:
    """
    
    Откатывает актуальную версию модели до back_up версии
    
    """
    dirname = Path(os.path.dirname((os.path.abspath(__file__))))
    path_back_up_model = str(next(dirname.glob('back_up_model*'))) #Путь к файлу с back up версией модели
    path_main_model = str(next(dirname.glob('main_model*'))) #Путь к файлу с актуальной версией модели

    model = load_model(path_back_up_model)
    model.save(path_main_model)

    print('Откат модели выполнен')
    
if __name__ == '__main__':
    set_back_up()
