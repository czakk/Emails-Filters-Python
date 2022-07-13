from utils import EmailManager, isEmailValid, saveToFile


class IncorrectEmails(EmailManager):

    @saveToFile(file_name='incorrect_emails.txt', header='Incorrect Emails')
    def getIncorrectEmails(self):
        return list(filter(lambda x:isEmailValid(x) is False, self.emails))

class SearchedEmails(EmailManager):

    @saveToFile(file_name='searched_emails.txt', header='Found emails with "{}" in email')
    def getSearchedEmails(self, search):
        return list(filter(lambda x: search in x, self.getFiltredValidEmails(self.emails)))

class GroupByDomain(EmailManager):

    @saveToFile(file_name='grouped_emails.txt', header='Emails grouped by domain')
    def getGroupedEmails(self):
        validEmails = self.getFiltredValidEmails(self.emails)
        domains = sorted(set(map(lambda x: x.rsplit('@')[1], validEmails)))
        # groupedEmails =  {domain: [email for email in validEmails if email.rsplit('@')[1] == domain] for domain in domains}
        groupedEmails =  {domain: list(filter(lambda x: x.rsplit('@')[1] == domain, validEmails)) for domain in domains}

        return [f'Domain {domain[0]} ({len(domain[1])})\n\t' + '\n\t'.join(domain[1]) for domain in groupedEmails.items()]

class EmailsNotInLogs(EmailManager):

    @saveToFile(file_name='emails_not_in_logs.txt', header='Emails not sent')
    def getEmailsNotInLogFile(self, log_files, text_files):
        self.getEmailsFromFile(text_files)
        txtEmails = self.getFiltredValidEmails(self.emails)
        self.getEmailsFromLogFile(log_files)
        logEmails = self.getFiltredValidEmails(self.emails)

        return sorted(list(filter(lambda x: x not in logEmails, txtEmails)))
