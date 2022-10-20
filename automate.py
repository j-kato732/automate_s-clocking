import sys

from s_clocking import SClockingHandler

config_path = './config.ini'
status_list = ['in', 'out']
argument_error = f'ArgumentError: expected at most 1 argument `{status_list[0]}` or `{status_list[1]}`'
config_error = f'ConfigError: config file not found: ./config.ini'


def validate(status):
    return status in status_list


def get_config():
    import os
    import configparser

    if not os.path.exists(config_path):
        print(config_error)
        sys.exit(255)

    config_ini = configparser.ConfigParser()
    config_ini.read(config_path, encoding='utf-8')

    company_code = config_ini['DEFAULT']['CompanyCode']
    employee_code = config_ini['DEFAULT']['EmployeeCode']
    password = config_ini['DEFAULT']['Password']

    return company_code, employee_code, password


def main():
    if len(sys.argv) != 2:
        print(argument_error)
        sys.exit(255)

    status = sys.argv[1]
    if not validate(status):
        print(argument_error)
        sys.exit(255)

    company_code, employee_code, password = get_config()

    s_clocking = SClockingHandler(company_code, employee_code, password)
    s_clocking.login()
    s_clocking.select_engraving()

    if status == status_list[0]:
        s_clocking.clock_in()
    elif status == status_list[1]:
        s_clocking.clock_out()

    s_clocking.quit()


if __name__ == '__main__':
    main()
