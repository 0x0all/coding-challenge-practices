#!/usr/bin/env python
from optparse import OptionParser
from collections import OrderedDict
import os.path
import json
import re


def file_to_str(filename):
    """Returns the contents of filename as a list."""
    with open(filename, 'r') as f:
        return f.readlines()


def format_phone_number(s):
    """Returns phone number in xxx-xxx-xxxx format."""
    s = s.replace(' ', '').replace('-', '').replace(')', '').replace('(', '')
    return '%s-%s-%s' % (s[:3], s[3:6], s[6:])


def make_entry(color, firstname, lastname, phonenumber, zipcode):
    """Returns an OrderedDict of an entry."""
    return OrderedDict([('color', color), ('firstname', firstname), ('lastname', lastname), ('phonenumber', phonenumber), ('zipcode', zipcode)])


def process_entries(lines):
    """Returns a dictionary containing correct entires and errors."""
    res = OrderedDict()
    res['entries'] = list()
    res['errors'] = list()

    for count, line in enumerate(lines):
        entry = map(lambda s: s.strip(), line.split(','))
        if len(entry) < 4:
            res['errors'].append(count)
        elif re.match('^(\d{5})$', entry[-1]):
            # Matches Lastname, Firstname, (703)-742-0996, Blue, 10013
            phone = format_phone_number(entry[2])
            if len(phone) == 12:
                res['entries'].append(make_entry(entry[3], entry[1], entry[0], phone, entry[4]))
            else:
                res['errors'].append(count)
        elif re.match('^([a-z])', entry[-1]):
            # Matches Firstname, Lastname, 10013, 646 111 0101, Green
            phone = format_phone_number(entry[3])
            if len(phone) == 12 and len(entry[2]) == 5:
                res['entries'].append(make_entry(entry[4], entry[0], entry[1], phone, entry[2]))
            else:
                res['errors'].append(count)
        elif len(entry) > 1:
            # Matches Firstname Lastname, Red, 11237, 703 955 0373
            name = entry[0].split(' ')
            phone = format_phone_number(entry[3])

            if len(name) < 2:
                res['errors'].append(count)
            elif len(phone) != 12 or len(entry[2]) != 5:
                res['errors'].append(count)
            else:
                res['entries'].append(make_entry(entry[1], ' '.join(name[:-1]), name[-1], phone, entry[2]))
        else:
            res['errors'].append(count)

    res['entries'] = sorted(res['entries'], key=lambda k: (k['lastname'], k['firstname']))

    return res



if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]...")
    
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    for arg in args:
        if os.path.isfile(arg):
            f = open('result.out', 'w')
            print >> f, json.dumps(process_entries(file_to_str(arg)), indent=2)
        else:
            print '"{}" is not a file.'.format(arg)
            parser.print_usage()