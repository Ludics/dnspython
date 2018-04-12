#!/usr/bin/env python
# coding=utf-8

import dns.name
import dns.query
import dns.dnssec
import dns.message
import dns.resolver
import dns.rdatatype
import dns.exception

request = dns.message.make_query('soso.com', 
                                 dns.rdatatype.A, 
                                 want_dnssec=True)
response = dns.query.udp(request, '8.8.8.8', timeout=10)
answer = response.answer
print(len(answer))
print(answer[0][0])
print(answer[0].to_rdataset().ttl)