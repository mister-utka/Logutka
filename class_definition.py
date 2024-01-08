import os

class Items:
    host = None
    files_log = {
        # Указываем директорию, где хранятся логи
        'working_directory': None,
        # Файл для просмотра сканирования портов
        'port_scan_logs_file': None,
        # Файл для просмотра неудачных аутентификаций
        'failed_authentication_logs_file': None,
        # Файл для просмотра неудачных аутентификаций по ssh
        'failed_authentication_ssh_logs_file': None
    }

    # Данный метод назначит директорию и файлы для логов по дефолту
    def method(self,
               host,
               working_directory=None,
               port_scan_logs_file=None,
               failed_authentication_logs_file=None,
               failed_authentication_ssh_logs_file=None
               ):
        self.host = host
        self.working_directory = f'/var/log/rsyslog/{host}/logutka/'
        self.port_scan_logs_file = port_scan_logs_file or f'{self.working_directory}port_scan_logs_file'
        self.failed_authentication_logs_file = failed_authentication_logs_file or f'{self.working_directory}failed_authentication_logs_file'
        self.failed_authentication_ssh_logs_file = failed_authentication_ssh_logs_file or f'{self.working_directory}failed_authentication_ssh_logs_file'

        self.checking_the_existence_of_the_file()

    # Данный метод вызывается для определения того, существует ли директория для логов хоста
    # Если ее нет, то она создается
    def checking_the_existence_of_the_file(self):
        # Проверка существования директории
        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)
            print(f"Директория '{self.working_directory}' создана.")

        # Проверка существования файлов
        files = {
            'port_scan_logs_file': self.port_scan_logs_file,
            'failed_authentication_logs_file': self.failed_authentication_logs_file,
            'failed_authentication_ssh_logs_file': self.failed_authentication_ssh_logs_file
        }

        for file_name, file_path in files.items():
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write('')
                #print(f"Файл '{file_name}' создан в директории '{self.working_directory}'.")
            else:
                pass
                #print(f"Файл '{file_name}' уже существует в директории '{self.working_directory}'.")