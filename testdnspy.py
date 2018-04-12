
import dns.name
import dns.query
import dns.dnssec
import dns.message
import dns.resolver
import dns.rdatatype
import csv

resolver_filename = "./sdata/opendns.csv"
domain_filename = "./sdata/top-10k.csv"
query_file = open("./dnsdata/query_file2.txt", "w")

resolver_file = open(resolver_filename, "r")
domain_file = open(domain_filename, "r")

domains = csv.reader(domain_file)
resolvers = csv.reader(resolver_file)

domains = list(domains)
resolvers = list(resolvers)

for m in range(0, 3):
    for n in range(0, len(resolvers)):
        print(domains[m][1]+" "+resolvers[n][0])
        query_file.write(domains[m][1]+" "+resolvers[n][0]+"\n")
        try:
            request = dns.message.make_query(domains[m][1], dns.rdatatype.A, want_dnssec=True)
            response = dns.query.udp(request, resolvers[n][0], timeout=10)
            query_file.write(response.to_text()+"\n")
        except dns.exception.DNSException as e:  
            query_file.write("Exception")
            query_file.write(str(e))
        try:
            request = dns.message.make_query(domains[m][1], dns.rdatatype.AAAA, want_dnssec=True)
            response = dns.query.udp(request, resolvers[n][0], timeout=10)
            query_file.write(response.to_text()+"\n")
        except dns.exception.DNSException as e:  
            query_file.write("\nException\n")
            query_file.write(str(e))
        query_file.write("\n\n----------\n\n")

query_file.close()
resolver_file.close()
domain_file.close()

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