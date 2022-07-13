from sys import argv
from commands import IncorrectEmails, SearchedEmails, GroupByDomain, EmailsNotInLogs


EMAIL_FILES = [
    'emails/email-pack-1.txt',
    'emails/emails-pack-2.txt',
    'emails/last-email-pack.csv',
    'emails/other-emails4.txt',
    'emails/emails3.txt',
]


if len(argv) > 1:
    match argv[1]:
        case '--incorrect-emails' | '-ic':
            command = IncorrectEmails()
            command.getEmailsFromFile(EMAIL_FILES)
            command.getIncorrectEmails()
        case '--search' | '-s':
            try:
                search = argv[2]
                command = SearchedEmails()
                command.getEmailsFromFile(EMAIL_FILES)
                command.getSearchedEmails(search)
            except IndexError:
                print('No search given\nUsage --search <search>')
        case '--group-by-domain' | '-gbd':
            command = GroupByDomain()
            command.getEmailsFromFile(EMAIL_FILES)
            command.getGroupedEmails()
        case '--find-emails-not-in-logs' | '-feil':
            try:
                logFile = argv[2]
                command = EmailsNotInLogs()
                command.getEmailsNotInLogFile(logFile, EMAIL_FILES)
            except IndexError:
                print('No log file given\nUsage --find-emails-not-in-logs path_to_logs_file <log_file_path>')
            except FileNotFoundError:
                print('File not found\nUsage --find-emails-not-in-logs path_to_logs_file <log_file_path>')
        case _:
            print('Command not found')
