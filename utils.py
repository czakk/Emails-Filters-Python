import csv


class EmailManager:
    def __init__(self):
        self.emails: list

    def getEmailsFromFile(self, files: list):
        self.emails = []
        for file in files:
            if file.split('.')[1] == 'txt':
                with open(file, 'r') as f:
                    self.emails += list(map(lambda x: x.replace('\n', ''), f.readlines()))
            else:
                with open(file, 'r') as f:
                    f = csv.reader(f, delimiter=';')
                    next(f)
                    for x in f:
                        self.emails.append(x[1])

    def getEmailsFromLogFile(self, file: str):
        self.emails = []
        with open(file, 'r') as f:
            self.emails += list(map(lambda x: x.replace('\n', ''), f.readlines()))
            self.emails = list(map(lambda x: x.rsplit("'")[1], self.emails))

    def getFiltredValidEmails(self, emails: list) -> list:
        return list(set(filter(lambda x: isEmailValid(x), emails)))


def isEmailValid(email: str) -> bool:
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

    if len(domain.split('.')[1]) < 1 or len(domain.split('.')[1]) > 4 or domain.split('.')[1].isalnum() is False:
        return False

    return True

def saveToFile(file_name, header=None):
    def wrap(func):
        def in_wrap(self, *args, **kwargs):
            with open(f'results/{file_name}', 'w') as f:
                result = func(self, *args, **kwargs)
                f.write(f'{header.format(*args, **kwargs)} ({len(result)})\n')
                f.write('\n'.join(result))
            return func(self, *args, **kwargs)
        return in_wrap
    return wrap


