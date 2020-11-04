# sites-available/000-default.conf:	CustomLog ${APACHE_LOG_DIR}/access.log combined
# apache2.conf:LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
# https://httpd.apache.org/docs/2.4/mod/mod_log_config.html#formats

# %h	Remote hostname. Will log the IP address if HostnameLookups is set to Off, which is the default.
# %l	Remote logname (from identd, if supplied).
# %u	Remote user if the request was authenticated.
# %t	Time the request was received, in the format [18/Sep/2011:19:18:28 -0400].
#       The last number indicates the timezone offset from GMT
# %r	First line of request.
# %s	Status. Use %>s for the final status.
# %O	Bytes sent, including headers.
# %{VARNAME}i	The contents of VARNAME: header line(s) in the request sent to the server.

import re
from collections import defaultdict

filename = "/var/log/apache2/access.log"
sample = '::1 - - [04/Nov/2020:13:00:49 +0300] "GET // HTTP/1.1" 200 4482 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"'
regex = '(.*?) (.*?) (.*?) \[(.*?)\] "(.*?)" (\d*) (\d*) "(.*?)" "(.*?)"'

pos_request = 5

def request_type(parsed):
    request = parsed.group(pos_request)
    found = re.match('\A\D+? ', request).group()
    if not found:
        print('BAD REQUEST', request)
        assert 0
    return found

request_overall = 0
request_by_type = defaultdict(int)

lines = open(filename, 'r').readlines()
for line in lines:
    parsed = re.match(regex, line)
    if not parsed:
        print('BAD LINE', line)
        assert 0
    rt = request_type(parsed)
    request_overall += 1
    request_by_type[rt] += 1
print(request_by_type)
