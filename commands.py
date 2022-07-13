from utils import EmailManager, is_email_valid, save_to_file


class IncorrectEmails(EmailManager):
    @save_to_file(file_name='incorrect_emails.txt', header='Incorrect Emails')
    def get_incorrect_emails(self):
        return list(filter(lambda x: is_email_valid(x) is False, self.emails))

class SearchedEmails(EmailManager):

    @save_to_file(file_name='searched_emails.txt', header='Found emails with "{}" in email')
    def get_searched_emails(self, search):
        return list(filter(lambda x: search in x, self.get_filtered_valid_emails(self.emails)))

class GroupByDomain(EmailManager):

    @save_to_file(file_name='grouped_emails.txt', header='Emails grouped by domain')
    def get_grouped_emails(self):
        valid_emails = self.get_filtered_valid_emails(self.emails)
        domains = sorted(set(map(lambda x: x.rsplit('@')[1], valid_emails)))
        grouped_emails =  {domain: list(filter(lambda email: email.rsplit('@')[1] == domain,
                                               valid_emails))
                           for domain in domains}

        return [f'Domain {domain[0]} ({len(domain[1])})\n\t' + '\n\t'.join(domain[1])
                for domain in grouped_emails.items()]

class EmailsNotInLogs(EmailManager):

    @save_to_file(file_name='emails_not_in_logs.txt', header='Emails not sent')
    def get_emails_not_in_log_file(self, log_files, text_files):
        self.get_emails_from_file(text_files)
        txt_emails = self.get_filtered_valid_emails(self.emails)
        self.get_emails_from_log_file(log_files)
        log_emails = self.get_filtered_valid_emails(self.emails)

        return sorted(list(filter(lambda x: x not in log_emails, txt_emails)))
