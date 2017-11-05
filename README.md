# Windows
Python для Windows можно скачать [тут](https://www.python.org/downloads/windows/). Путь для установки по умолчанию - `C:\Users\georg\AppData\Local\Programs\Python\Python36`

Для запуска программы необходимо указывать полные пути:
> C:\Users\georg\Documents>C:\Users\georg\AppData\Local\Programs\Python\Python36\python.exe C:\Users\georg\Documents\stats.py -u https://github.com/ink-ru/git_hub/ -s

Если вы планируете запускать скрипт другой програмой (планировщиком задач), то для предотвращения появления окна командного процессора, можно использовать интерпретатор python*w*.exe. Если же вы хотите увидеть результат работы программы (включая ошибки) используйте классический интерпретарор `pythonw.exe`

# Linux
В современных дистрибутивах интерпретатор Pytyon установлен изначально. Для запуска программы используйте python версии 3 и выше:

```python3 stats.py -u URL -s```

Для вывода справки используйте ключ -h
> stats.py -h
