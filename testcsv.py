#!/usr/bin/env python
# coding=utf-8

import csv

resolver_filename = "./sdata/opendns.csv"
domain_filename = "./sdata/top-10k.csv"
query_file = open("query_file.txt", "w")

resolver_file = open(resolver_filename, "r")
domain_file = open(domain_filename, "r")

domains = csv.reader(domain_file)
resolvers = csv.reader(resolver_file)

domains = list(domains)
resolvers = list(resolvers)

for m in range(0, 100):
    for n in range(0, len(resolvers)):
        query_file.write(domains[m][1]+" "+resolvers[n][0]+"\n")