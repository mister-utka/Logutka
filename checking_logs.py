import subprocess
from subprocess import call, check_output, run

def checking_logs(working_directory):
    """Функция сканирует логи на предмет указанных в grep_cmd_ist"""

    def log_entry(output, file):
        """Запись построчно полученных данных в файл логов"""
        with open(file, "w") as f:
            #output_log = []
            if output is None:
                pass
            else:
                f.write(output)
            #for i in output:
                #f.write(i + "\n")
                #output_log.append(i + "\n")
        #return output_log

    grep_cmd_list = [
        # Для просмотра сканирования портов
        '"NEW incoming connection"',
        '"Unable to negotiate with"',
        '"Connection closed by"',
        '"error: kex_exchange_identification"',
        '"banner exchange: Connection from"'
        # Для просмотра неудачных аутентификаций
        '"conversation failed"',
        # Для просмотра неудачных аутентификаций по ssh
        '"Connection closed by authenticating user"'
    ]
    for grep_cmd in grep_cmd_list:
        output = run(f'cat {working_directory}../*.* | grep {grep_cmd}', shell=True, stdout=subprocess.PIPE, text=True).stdout
        #print(output)

        if ("NEW incoming connection" in grep_cmd
        or "Unable to negotiate with" in grep_cmd
        or "Connection closed by" in grep_cmd
        or "banner exchange: Connection from" in grep_cmd):
            file = f"{working_directory}port_scan_logs_file"
            log_entry(output, file)

        elif "onversation failed" in grep_cmd:
            file = f"{working_directory}failed_authentication_logs_file"
            log_entry(output, file)

        elif "Connection closed by authenticating user" in grep_cmd:
            file = f"{working_directory}failed_authentication_ssh_logs_file"
            log_entry(output, file)