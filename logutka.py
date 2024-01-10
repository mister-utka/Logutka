from class_definition import Items
import checking_logs
import time

# Указываем папки, которые появились после настройки rsyslog
# Они находятся по пути /var/log/rsyslog
host_list = ['host1', 'host2']

def creating_an_instance(host):
    # Создаем экземпляр класса Items
    host_instance = Items()
    # Вызываем метод method() от экземпляра класса
    host_instance.method(host=f'{host}')
    # Получение логов
    checking_logs.checking_logs(host_instance.working_directory)

while True:
    for host in host_list:
        print(host)
        creating_an_instance(host)
        time.sleep(1)
    time.sleep(10)
