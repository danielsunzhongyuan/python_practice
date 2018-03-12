#!/usr/bin/python

from bloom_filter import Bloomfilter


def main():
    bf = Bloomfilter(10)
    bf.add_value('dog')
    bf.add_value('fish')
    bf.add_value('cat')
    bf.print_contents()

    bf.add_value('bird')
    bf.print_contents()

    for term in ['dog', 'fish', 'cat', 'bird', 'duck', 'emu']:
        print '{}: {} {}'.format(term, bf.hash_value(term), bf.might_contain(term))


if __name__ == "__main__":
    main()
