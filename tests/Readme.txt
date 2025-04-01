Правила нейминга : tests выносим или держим на одном уровне с тестируемым объектом
    Называть нужно следующим образом "test_название" (конфигурируется в файле)

Чтобы прогнать тест: 
                pytest -v
                -v - многословные

"(Pytest-course) PS D:\Programming\Pytest-course> pytest
============ test session starts =========
platform win32 -- Python 3.12.8, pytest-8.3.5, pluggy-1.5.0 - платформа, на которой мы работаем
rootdir: D:\Programming\Pytest-course                       - рабочая папка
configfile: pyproject.toml                                  - файл конфигурации
collected 1 item                                            - кол-во найденных тестов

tests\test_main.py .                [100%]                  - логи (статус)

============ 1 passed in 0.07s =========="