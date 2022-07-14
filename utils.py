import csv


class EmailManager:
    def __init__(self):
        self.emails: list

    def get_emails_from_file(self, files: list):
        self.emails = []
        for file_name in files:
            if file_name.split('.')[1] == 'txt':
                with open(file_name, 'r', encoding='UTF-8') as file:
                    self.emails += list(map(lambda x: x.replace('\n', ''), file.readlines()))
            else:
                with open(file_name, 'r', encoding='UTF-8') as file:
                    file = csv.reader(file, delimiter=';')
                    next(file)
                    for row in file:
                        self.emails.append(row[1])

    def get_emails_from_log_file(self, file_name: str):
        self.emails = []
        with open(file_name, 'r', encoding='UTF-8') as file:
            self.emails += list(map(lambda x: x.replace('\n', ''), file.readlines()))
            self.emails = list(map(lambda x: x.rsplit("'")[1], self.emails))

    def get_filtered_valid_emails(self, emails: list) -> list:
        return list(set(filter(is_email_valid, emails)))


def is_email_valid(email: str) -> bool:
    email = email.rsplit('@')

    if len(email) > 1:
        name = email[0]
        domain = email[1]
    else:
        return False

    if name.count('@') + domain.count('@') > 0:
        return False

    if len(name) < 1 or len(domain) < 1:
        return False

    if len(domain.split('.')[0]) < 1:
        return False

    if len(domain.split('.')[1]) < 1\
            or len(domain.split('.')[1]) > 4\
            or domain.split('.')[1].isalnum() is False:
        return False

    return True

def save_to_file(file_name, header=None):
    def wrap(func):
        def in_wrap(self, *args, **kwargs):
            with open(f'results/{file_name}', 'w', encoding='UTF-8') as file:
                result = func(self, *args, **kwargs)
                file.write(f'{header.format(*args} ({len(result)})\n')
                file.write('\n'.join(result))
            return func(self, *args, **kwargs)
        return in_wrap
    return wrap
