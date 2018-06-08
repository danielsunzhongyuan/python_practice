#!/usr/bin/python

from bloom_filter import Bloomfilter
from splunk import Splunk, SplunkM


def bf_test():
    bf = Bloomfilter(10)
    bf.add_value('dog')
    bf.add_value('fish')
    bf.add_value('cat')
    bf.print_contents()

    bf.add_value('bird')
    bf.print_contents()

    for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
        print '{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term))


def splunk_test():
    s = Splunk()
    s.add_event('src_ip = 1.2.3.4')
    s.add_event('src_ip = 5.6.7.8')
    s.add_event('dst_ip = 1.2.3.4')

    for event in s.search('1.2.3.4'):
        print event
    print '***********'
    for event in s.search('src_ip'):
        print event
    print '***********'
    for event in s.search('ip'):
        print event


def splunk_multi_test():
    s = SplunkM()
    s.add_event('src_ip = 1.2.3.4')
    s.add_event('src_ip = 5.6.7.8')
    s.add_event('dst_ip = 1.2.3.4')

    for event in s.search_all(['src_ip', '5.6']):
        print event
    print '***********'
    for event in s.search_any(['src_ip', 'dst_ip']):
        print event


def main():
    bf_test()
    print '#############\n'
    splunk_test()
    print '#############\n'
    splunk_multi_test()


if __name__ == "__main__":
    main()
