# Emails Filter
### Cezary Banaczyk
## Commands
### Incorrect emails
Return invalid emails

Saving in: `incorrect_emails.txt`

`-ic` or `--incorrect-emails`
### Search
Search for emails containing provided string

Saving in: `searched-emails.txt`

`-s <string>` or `--search <string>`
### Group emails by domain
Returns grouped emails by domain sorted alphabetically

Saving in: `grouped_emails.txt`

`-gbd` or `--group-by-domain`
### Emails not in logs file
Finding emails that are not in provided logs file

Saving in: `emails_not_in_logs.txt`

`-feil <path_to_log_file>` or `--find-emails-not-in-logs <path_to_log_file>`


## Usage/Example
All command results will be saved in the directory "results".

Emails are stored in the files in the "emails" directory.

`$ py main.py` - base of all commands

### Example
#### Provide
`$ py main.py -ic`
#### Recive
results/incorrect_emails.txt
```
Incorrect Emails (10)
brad84gmail.com
yahoo.com
.com
com
@hegmann.info
nernserhickle.biz
com
com
wyman.com
ynolanjones.com
```
#### Provide
`$ py main.py -search agustin`
#### Recive
results/search_emails.txt
```
Found emails with "agustin" in email (5)
agustin.dare@kreiger.biz
agustin.ziemann@hilpert.info
agustin16@gmail.com
marquardt.agustina@bins.org
agustina.reilly@yahoo.com
```
#### Provide
`$ py main.py -feil emails/email-sent.logs`
#### Recive
results/emails_not_in_logs.txt
```
Emails not sent (240)
abogisich@skiles.com
addie.okon@oconnell.com
aditya.murazik@gorczany.com
ahagenes@gmail.com
alayna29@gmail.com
alexandra.bayer@larkin.com
alfreda.cremin@kassulke.com
alvah45@rice.com
...
```
