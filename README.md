# Windows
Python для Windows можно скачать [тут](https://www.python.org/downloads/windows/). Путь для установки по умолчанию - `C:\Users\georg\AppData\Local\Programs\Python\Python36`

Если вы планируете запускать скрипт другой програмой (планировщиком задач), то для предотвращения появления окна командного процессора, можно использовать интерпретатор python*w*.exe. Если же вы хотите увидеть результат работы программы (включая ошибки) используйте классический интерпретарор `pythonw.exe`

Для запуска программы необходимо указывать полные пути:
> C:\Users\georg\Documents>C:\Users\georg\AppData\Local\Programs\Python\Python36\python.exe C:\Users\georg\Documents\stats.py -u https://github.com/ink-ru/git_hub/ -s

Для того чтобы не указывать пути каждый раз можно прописать переменные окружения. Для этого перейдите в "Парметры" => "Дополнительные параметры системы" и на вкладке "Доплнительно" нажмите кнопку "Переменные среды". Далее необходимо в переменную PATH добавить путь к интерпретатору python, например:
> %USERPROFILE%\AppData\Local\Programs\Python\Python36

Теперь, если перейти в директорию со скриптом, можно dsgjkyznm команду без указания полных путей:
> cd Documents
> python .\stats.py -u https://github.com/ink-ru/git_hub/ -s

# Linux
В современных дистрибутивах интерпретатор Pytyon установлен изначально. Для запуска программы используйте python версии 3 и выше:

```python3 stats.py -u URL -s```

Для вывода справки используйте ключ -h
> stats.py -h
