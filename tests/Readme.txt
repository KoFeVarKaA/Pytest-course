Правила нейминга : 
    tests выносим или держим на одном уровне с тестируемым объектом
    Называть нужно следующим образом "test_название" (конфигурируется в файле)
    С функциями анагично "def test_имя():" (не обязательно)

Чтобы прогнать тест: 
                pytest -v tests/test_mainl4.py::test_divide[1-2-0.5]
                -v - многословные
                файлик::название_ф-ии[параметры] - запустить конкретный тест 
                (названия отображаются при обычном запуске)

"(Pytest-course) PS D:\Programming\Pytest-course> pytest
============ test session starts =========
platform win32 -- Python 3.12.8, pytest-8.3.5, pluggy-1.5.0 - платформа, на которой мы работаем
rootdir: D:\Programming\Pytest-course                       - рабочая папка
configfile: pyproject.toml                                  - файл конфигурации
collected 1 item                                            - кол-во найденных тестов

tests\test_main.py .                [100%]                  - логи (статус)

============ 1 passed in 0.07s =========="

Настройка VS:
    Колба - confige python tests - pytest - . 