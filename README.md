Для каждого проекта
- Cоздадим виртуальное окружение: ```python3 -m venv venv``` В результате, в директории проекта появится папка ```venv```.


- Активируем окружение: ```source venv/bin/activate``` Если вы решили удалить папку ```venv```, и пересоздать окружение, то сначала деактивируйте его командой: ```deactivate```


- Установить все зависимости (библиотеки) для начала работы: ```pip3 install selenium``` Иногда дополнительно требуется установить библиотеку ```packaging``` ```pip3 install packaging```


- Последнее, что нам понадобится, это библиотека ```webdriver-manager```. Она нужна непосредственно для работы с драйверами Chrome, Firefox и т.д. ```pip3 install webdriver-manager```

### Инициализация Chrome
- Иницализация в одну строчку, через SeleniumManager - он автоматически распознает ваш Chrome и запустит его.
```
from selenium import webdriver

driver = webdriver.Chrome()
```

- Инициализация через WebDriverManager
```
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

- Инициализация через WebDriverManager + версия Chrome
```
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
driver = webdriver.Chrome(service=service)
```
