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

# а этого параметра нет в моих логах
# топ 10 самых долгих запросов, должно быть видно метод, url, ip, время запроса
# %T	The time taken to serve the request, in seconds.

import re
from collections import defaultdict

filename = "/var/log/apache2/access.log"
regex = '(.*?) (.*?) (.*?) \[(.*?)\] "(.*?)" (\d*) (\d*) "(.*?)" "(.*?)"'

pos_ip = 0
pos_request = 4
pos_status = 5
client_error = '4..'
server_error = '5..'

request_overall = 0  # общее количество выполненных запросов
ip_addrs = defaultdict(int)  # топ 10 IP адресов, с которых были сделаны запросы
request_by_type = defaultdict(int)  # количество запросов по типу: GET - 20, POST - 10 и т.п.
request_client_err = list()
request_server_err = list()


def split_request(request_line):
    gr = re.match('(\A[A-Z]+?) (.+?) ', request_line).groups()
    return {'met': gr[0], 'url': gr[1]}


# должно быть видно метод, url, статус код, ip адрес
def extract_data(parsed_mobj):
    pg = parsed_mobj.groups()
    split = split_request(pg[pos_request])
    return (split['met'],
            split['url'],
            pg[pos_status],
            pg[pos_ip])


lines = open(filename, 'r').readlines()
for line in lines:
    parsed = re.match(regex, line)
    if not parsed:
        print('BAD LINE', line)
        assert 0
    groups = parsed.groups()
    # общее количество выполненных запросов
    request_overall += 1
    # топ 10 IP адресов, с которых были сделаны запросы
    ip_addrs[groups[pos_ip]] += 1
    # количество запросов по типу: GET - 20, POST - 10 и т.п.
    request_type = split_request(groups[pos_request])['met']
    request_by_type[request_type] += 1
    # топ 10 не получится, потому что не задан критерий сортировки, значит будут просто первые 10
    # топ 10 запросов, которые завершились клиентской ошибкой, должно быть видно метод, url, статус код, ip адрес
    if re.match(client_error, groups[pos_status]):
        request_client_err.append(extract_data(parsed))
    # топ 10 запросов, которые завершились ошибкой со стороны сервера, должно быть видно метод, url, статус код, ip адрес

ip_addrs_sorted = {k: v for k, v in sorted(ip_addrs.items(), key=lambda item: item[1])}
ip_items = ip_addrs_sorted.items()
ip_first_ten = list(ip_items)[:10]
print(request_overall)
print(request_by_type)
print(ip_first_ten)
print(request_client_err)