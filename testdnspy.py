#!/usr/bin/env python
# coding=utf-8

import csv
import dns.name
import dns.query
import dns.dnssec
import dns.message
import dns.resolver
import dns.rdatatype
import dns.exception
import pymysql

resolver_filename = "./sdata/opendns.csv"
domain_filename = "./sdata/top-10k.csv"
query_file = open("./dnsdata/query_file_tcp.txt", "w+")

resolver_file = open(resolver_filename, "r")
domain_file = open(domain_filename, "r")

domains = csv.reader(domain_file)
resolvers = csv.reader(resolver_file)

domains = list(domains)
resolvers = list(resolvers)

db = pymysql.connect(host="127.0.0.1", user="root", passwd="ludics", db="dnsdata")
# cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


for m in range(20, 30):
    for n in range(0, len(resolvers)):
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        aNum = 0
        aaaaNum = 0
        cnameNum = 0
        hasDnssec = 0
        isTimeout = 0
        ttl = 0
        addr = '0.0.0.0'
        t_pos = [0,0,0,0]
        protocolType = 1
        print(domains[m][1]+" "+resolvers[n][0])
        query_file.write(domains[m][1]+" "+resolvers[n][0]+"\n")
        try:
            request = dns.message.make_query(domains[m][1], 
                                             dns.rdatatype.A, 
                                             want_dnssec=True)
            response = dns.query.tcp(request, resolvers[n][0], timeout=10)
            answer = response.answer
            for m1 in range(0, len(answer)):
                if answer[m1].to_rdataset().rdtype == dns.rdatatype.A:
                    aNum = len(answer[m1])
                    t_pos[0] = m1
                elif answer[m1].to_rdataset().rdtype == dns.rdatatype.CNAME:
                    cnameNum = len(answer[m1])
                    t_pos[1] = m1
                elif answer[m1].to_rdataset().rdtype == dns.rdatatype.RRSIG:
                    hasDnssec = 1

            sql = "INSERT INTO query(domainName, resolverAddr, aNum, cnameNum, hasDnssec, protocolType) \
                    VALUES ('%s', '%s', '%d', '%d', '%d', '%d')" % \
                    (domains[m][1], resolvers[n][0], aNum, cnameNum, hasDnssec, protocolType)
            # cursor.execute(sql)
            # db.commit()
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

            query_id = cursor.lastrowid

            if aNum is not 0:
                for m1 in range(0, len(answer[t_pos[0]])):
                    ttl = answer[t_pos[0]].to_rdataset().ttl
                    addr = answer[t_pos[0]][m1]
                    sql = "INSERT INTO a_record (queryID, domainName, resolverAddr, ttl, addr, protocolType) \
                            VALUES ('%d', '%s', '%s', '%d', '%s', '%d')" % \
                            (query_id, domains[m][1], resolvers[n][0], ttl, addr, protocolType)
                    # cursor.execute(sql)
                    # db.commit()
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            if cnameNum is not 0:
                for m1 in range(0, len(answer[t_pos[1]])):
                    ttl = answer[t_pos[1]].to_rdataset().ttl
                    cnameData = answer[t_pos[1]][m1]
                    sql = "INSERT INTO cname_record (queryID, domainName, resolverAddr, ttl, cnameData, protocolType) \
                            VALUES ('%d', '%s', '%s', '%d', '%s', '%d')" % \
                            (query_id, domains[m][1], resolvers[n][0], ttl, cnameData, protocolType)
                    # cursor.execute(sql)
                    # db.commit()
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()        
            query_file.write("\n"+response.to_text()+"\n")
        except dns.exception.DNSException as e:
            sql = "INSERT INTO timeout_record (domainName, resolverAddr, exceptionData, protocolType) \
                        VALUES ('%s', '%s', '%s', '%d')" % \
                        (domains[m][1], resolvers[n][0], str(e), protocolType)
            # cursor.execute(sql)
            # db.commit()
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
            query_file.write("\nException\n")
            query_file.write(str(e))
        try:
            request = dns.message.make_query(domains[m][1], 
                                             dns.rdatatype.AAAA, 
                                             want_dnssec=True)
            response = dns.query.tcp(request, resolvers[n][0], timeout=10)

            answer = response.answer
            for m1 in range(0, len(answer)):
                if answer[m1].to_rdataset().rdtype == dns.rdatatype.AAAA:
                    aaaaNum = len(answer[m1])
                    t_pos[2] = m1
            if aaaaNum is not 0:
                sql = "UPDATE query SET aaaaNum = '%d' WHERE queryID = '%d'" \
                        % (aaaaNum, query_id)
                # cursor.execute(sql)
                # db.commit()
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()

                for m1 in range(0, len(answer[t_pos[2]])):
                    ttl = answer[t_pos[2]].to_rdataset().ttl
                    addr = answer[t_pos[2]][m1]
                    sql = "INSERT INTO aaaa_record (queryID, domainName, resolverAddr, ttl, addr, protocolType) \
                        VALUES ('%d', '%s', '%s', '%d', '%s', '%d')" % \
                        (query_id, domains[m][1], resolvers[n][0], ttl, addr, protocolType)
                    # cursor.execute(sql)
                    # db.commit()
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        db.rollback()

            query_file.write("\n"+response.to_text()+"\n")
        except dns.exception.DNSException as e: 
            sql = "INSERT INTO timeout_record (domainName, resolverAddr, exceptionData, protocolType) \
                        VALUES ('%s', '%s', '%s', '%d')" % \
                        (domains[m][1], resolvers[n][0], str(e), protocolType)
            # cursor.execute(sql)
            # db.commit()
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback() 
            query_file.write("\nException\n")
            query_file.write(str(e))
        query_file.write("\n\n----------\n\n")
        db.commit()
        cursor.close()



db.close()
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