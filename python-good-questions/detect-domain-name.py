# Detect the Domain Name:
# https://www.hackerrank.com/challenges/detect-the-domain-name/problem

import re, itertools

regex = re.compile(("https?:\/\/((?:[\-a-zA-Z0-9]+\.)*[\-a-zA-Z0-9]+\.[a-zA-Z0-9]+(?:[a-zA-Z0-9]+)?)"))

def getPotentialDomains(lines):
    temp = [re.findall(regex, line) for line in lines]
    domains = set(itertools.chain.from_iterable(temp))
    
    domain_list = sorted(map(lambda x: re.sub(r"^(web|ww[w\d])\.", "", x), domains))
    return ';'.join(domain_list)


if __name__ == '__main__':
	print getPotentialDomains(['http://www.google.com/search?=blah', 'http://codex.wordpress.org/functions/v2', 'http://wikipedia.org'])