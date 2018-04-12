
import dns.name
import dns.query
import dns.dnssec
import dns.message
import dns.resolver
import dns.rdatatype
import dns.exception
# import csv

# dns_resolver_filename = '../data/opendns.csv'
write_to_file = open('timeouttest.txt','w')

# with open(dns_resolver_filename) as dns_resolver_file:
#     reader = csv.reader(dns_resolver_file)
#     dns_resolvers = list(reader)
request = dns.message.make_query('baidu.com',
                                 dns.rdatatype.ANY,
                                 want_dnssec=True)
    # for row in dns_resolvers:
try:
    response = dns.query.udp(request, "8.8.8.7", timeout=2)
    write_to_file.write(response.to_text())
# write_to_file.write()
except dns.exception.DNSException as e:  
    write_to_file.write(str(e))
finally:
    write_to_file.write("\n\n----------\n\n")

write_to_file.close()

# get nameservers for target domain
# response = dns.resolver.query('example.com.',dns.rdatatype.NS)

# we'll use the first nameserver in this example
# nsname = response.rrset[0] # name
# response = dns.resolver.query(nsname,dns.rdatatype.A)
# nsaddr = response.rrset[0].to_text() # IPv4

# get DNSKEY for zone

# request = dns.message.make_query('baidu.com',
#                                  dns.rdatatype.ANY,
#                                  want_dnssec=True)

# # send the query
# response = dns.query.udp(request,nsaddr)
# if response.rcode() != 0:
#     # HANDLE QUERY FAILED (SERVER ERROR OR NO DNSKEY RECORD)

# # answer should contain two RRSET: DNSKEY and RRSIG(DNSKEY)
# answer = response.answer
# if len(answer) != 2:
#     # SOMETHING WENT WRONG

# # the DNSKEY should be self signed, validate it
# name = dns.name.from_text('example.com.')
# try:
#     dns.dnssec.validate(answer[0],answer[1],{name:answer[0]})
# except dns.dnssec.ValidationFailure:
#     # BE SUSPICIOUS
# else:
#     # WE'RE GOOD, THERE'S A VALID DNSSEC SELF-SIGNED KEY FOR example.com