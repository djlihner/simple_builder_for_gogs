# Простая система автоматизированной сборки Python-проектов для gogs

### Required Software and Tools
Python 3

### Run 

 * Установить модули через pip install -r requirements.txt или python setup.py install 
 * Выполнить python -m builder sys.argv где аргументы:
        
        server_mode - запуск сервера для для обновления сборки по событию
        (Настроить Webhook в gogs с адресом http://127.0.0.1:4567/builder_event)
        адрес репозитория - для автоматической сборки по push 
