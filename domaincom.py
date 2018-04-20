#!/usr/bin/env python
# coding=utf-8

import pymysql
import re

db = pymysql.connect(host="127.0.0.1", user="root", passwd="ludics", db="dnsdata")

cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

sql = "SELECT tldName from domain_list where tldName = 'com'"


# tldDict = {'com':0}
# count = 0
# cursor.execute(sql)
# results = cursor.fetchall()
# for row in results:
#     tldName = row['tldName']
#     if tldName in tldDict:
#         tldDict[tldName] = tldDict[tldName] + 1
#     else:
#         tldDict[tldName] = 1
#     count = count + 1
#     # print(count)
# print(count)
# print(tldDict)


# print(sorted(tldDict.items(), key=lambda d: d[1]))
# tldDict2 = sortedDictValues2(tldDict)
#     domainName = row['domainName']
#     domainID = row['domainID']
#     tldName = re.search(r'[^\.]+$', domainName)
#     sql = "UPDATE domain_list SET tldName = '%s' WHERE domainID = '%d'" \
#                                 % (tldName.group(0), domainID)
#     cursor.execute(sql)
#     db.commit()

# myDict = {'tn': 3, 'pink': 3, 'trade': 1, 'online': 13, 'np': 2, 'jobs': 1, 'sexy': 2, 'pr': 2, 'edu': 145, 'gt': 3, 'systems': 2, 'al': 10, 'tt': 2, 'ec': 4, 'tl': 2, 'live': 3, 'box': 1, 'sg': 12, 'sex': 2, 'ninja': 1, 're': 3, 'ar': 21, 'com': 5747, 'ac': 8, 'by': 10, 'net': 525, 'gh': 2, 'pw': 4, 'sc': 5, 'am': 6, 'jo': 2, 'ae': 2, 'ltd': 1, 'kh': 4, 'video': 3, 'xn--p1ai': 2, 'bid': 3, 'vn': 26, 'website': 3, 'bf': 1, 've': 12, 'bnpparibas': 1, 'sx': 3, 'kr': 45, 'mm': 2, 'th': 8, 'fun': 3, 'uno': 2, 'uy': 3, 'nl': 28, 'iq': 2, 'cy': 3, 'biz': 20, 'us': 21, 'xyz': 17, 'ke': 10, 'la': 9, 'bz': 7, 'ru': 336, 'sh': 7, 'ch': 19, 'to': 61, 'zone': 1, 'gs': 2, 'dk': 14, 'hk': 24, 'ni': 3, 'gg': 5, 'earth': 1, 'ba': 4, 'tv': 131, 'no': 27, 'li': 3, 'ag': 5, 'my': 18, 'sk': 22, 'bn': 2, 'club': 16, 'ee': 7, 'fi': 12, 'gr': 66, 'lu': 2, 'org': 384, 'media': 5, 'hr': 10, 'cz': 54, 'az': 19, 'su': 4, 'fr': 106, 'io': 76, 'uk': 91, 'store': 2, 'date': 2, 'today': 3, 'pg': 2, 'il': 12, 'pe': 12, 'bw': 2, 'mx': 38, 'cl': 11, 'recipes': 2, 'ph': 8, 'zm': 2, 'cc': 46, 'nz': 12, 'xxx': 4, 'ca': 60, 'pro': 16, 'za': 21, 'tw': 82, 'porn': 8, 'mz': 1, 'mp': 1, 'tr': 44, 'dhl': 1, 'se': 42, 'si': 6, 'cr': 2, 'cm': 2, 'lat': 1, 'team': 2, 'cu': 6, 'cd': 5, 'kz': 15, 'guru': 2, 'link': 2, 'ge': 2, 'win': 1, 'adult': 4, 'mobi': 5, 'py': 3, 'hu': 26, 'pub': 1, 'ro': 12, 'lb': 2, 'bg': 6, 'download': 2, 'eg': 8, 'mn': 2, 'best': 1, 'info': 46, 'ml': 2, 'id': 33, 'gov': 106, 'group': 2, 'int': 2, 'be': 15, 'pl': 75, 'es': 61, 'va': 1, 'sa': 14, 'st': 7, 'do': 3, 'ws': 8, 'fo': 2, 'nu': 4, 'br': 151, 'tj': 2, 'money': 1, 'na': 2, 'space': 1, 'movie': 1, 'wiki': 1, 'tc': 2, 'ma': 10, 'it': 97, 'tk': 2, 'cafe': 1, 'bd': 5, 'stream': 3, 'jm': 2, 'gal': 1, 'qa': 2, 'mu': 4, 'in': 193, 'im': 7, 'ht': 2, 'bo': 2, 'lol': 2, 'cn': 161, 'rs': 5, 'mil': 2, 'lt': 9, 'is': 15, 'de': 147, 'cg': 2, 'tf': 1, 'me': 96, 'sv': 3, 'ua': 42, 'kw': 3, 'ao': 9, 'tm': 2, 'co': 93, 'ir': 64, 'eu': 17, 'pt': 24, 'mt': 5, 'at': 16, 'site': 8, 'td': 2, 'bh': 2, 'plus': 2, 'lk': 7, 'watch': 1, 'film': 2, 'af': 2, 'cat': 4, 'ng': 11, 'hn': 2, 'cool': 2, 'red': 2, 'mg': 2, 'au': 62, 'fm': 10, 'press': 2, 'ly': 7, 'vc': 1, 'mk': 8, 'jp': 188, 'dz': 3, 'bradesco': 2, 'top': 17, 'bj': 2, 'yt': 1, 'uz': 3, 'dog': 2, 'sncf': 1, 'rocks': 2, 'lv': 6, 'pk': 25, 'ie': 11, 'news': 7, 'cam': 2, 'gl': 2, 'sn': 2}

# a = [v for v in sorted(myDict.values())]
# c = []
# b = ['com', 'net', 'org', 'ru', 'in', 'jp', 'cn', 'br', 'de', 'edu']
# for item in b:
#     c.append(myDict[item])

# print(c)
# print(sum(c))
# print(10883-sum(c))
