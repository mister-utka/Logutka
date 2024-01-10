import subprocess
from subprocess import call, check_output, run

def checking_logs(working_directory):
    """Функция сканирует логи на предмет указанных в grep_cmd_ist"""

    def log_reading(file):
        """Считывание существующего лога и создание из него списка для сравнения"""
        with open(file, "r") as f:
            reading_log = [line.strip() for line in f]
            # if reading_log == []:
            #     reading_log.append("")
        return reading_log

    def log_entry_a(output, file):
        """Запись построчно полученных данных в файл логов"""
        with open(file, "a") as f:
            #output_log = []
            if output is None:
                pass
            else:
                f.write(output)

    def compare_lists(list1, list2):
        """Сравнивает два списка и выводит различия"""
        diff = set(list1) - set(list2)
        return list(diff)

    def checking_logs(grep_cmd_list):
        output_list = []

        # Перебор элементов в списке
        for grep_cmd in grep_cmd_list:

            output = run(f'cat {working_directory}../*.* | grep {grep_cmd}', shell=True, stdout=subprocess.PIPE,
                         text=True).stdout
            # print(output)
            output = output.strip().split("\n")
            if output != ['']:
                output_list = output_list + output

        reading_log = log_reading(file)

        differences = compare_lists(output_list, reading_log)
        # print("Различия между списками:", differences)
        if differences == []:
            pass
            # print("1 Сходится!")
        else:
            # print("1 Не сходится!")
            for diff in differences:
                log_entry_a(diff + "\n", file)

    grep_cmd_dict = {
        # Для просмотра сканирования портов
        'port_scan_logs': ['"NEW incoming connection"',
                           '"Unable to negotiate with"',
                           '"Connection closed by"',
                           '"error: kex_exchange_identification"',
                           '"banner exchange: Connection from"'],
        # Для просмотра неудачных аутентификаций
        'failed_authentication_logs': ['"conversation failed"'],
        # Для просмотра неудачных аутентификаций по ssh
        'failed_authentication_ssh_logs': ['"Connection closed by authenticating user"']
    }

    for key, grep_cmd_list in grep_cmd_dict.items():

        if key == 'port_scan_logs':

            file = f"{working_directory}port_scan_logs_file"
            checking_logs(grep_cmd_list)


        if key == 'failed_authentication_logs':

            file = f"{working_directory}failed_authentication_logs_file"
            checking_logs(grep_cmd_list)


        if key == 'failed_authentication_ssh_logs':

            file = f"{working_directory}failed_authentication_ssh_logs_file"
            checking_logs(grep_cmd_list)
