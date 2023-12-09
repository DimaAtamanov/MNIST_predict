import os
from pathlib import Path
import datetime

from keras.models import load_model

def update_back_up() -> None:
    """ 
    
    Обновление back up версии модели. При этом предыдущая версия удаляется.
    
    """
    dirname = Path(os.path.dirname((os.path.abspath(__file__))))
    path_back_up_model = str(next(dirname.glob('back_up_model*'))) #Путь к файлу с back up версией модели
    path_main_model = str(next(dirname.glob('main_model*'))) #Путь к файлу с актуальной версией модели
    cur_date = datetime.date.today().strftime('_%d_%m_%Y') # Дата обновления back up версии модели
    
    os.remove(path_back_up_model)

    model = load_model(path_main_model)
    model.save(path_back_up_model[:-17] + cur_date + '.keras')

    print('Back up версия обновлена')

if __name__ == '__main__':
    update_back_up()