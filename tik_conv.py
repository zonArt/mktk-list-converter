import argparse
import sys

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', dest='source', help='The source file (list of domains for instance)')
    parser.add_argument('-d', '--destination', dest='destination', help='The destination file (.rsc script to create for Mikrotik)')

    return parser

def convert_list(options):
    print('Source: ' + options.source)
    print('Destination: ' + options.destination)
    fhs = open(options.source)
    fhd = open(options.destination)
    for line in fhs:
        print(line)
        # do stuff

def main(argv=None):

    # We default argv to None and assign to sys.argv[1:] below because having
    # an argument default value be a mutable type in Python is a gotcha. See
    # http://bit.ly/1o18Vff
    if argv is None:
        argv = sys.argv[1:]

    parser = make_parser()
    options = parser.parse_args(argv)
    if not options.source:
        parser.error("Must specify a 'source' file")
    if not options.destination:
        parser.error("Must specify a 'destination' file")

    convert_list(options)

if __name__ == '__main__':
    sys.path.insert(0, '.')
    main()
