import argparse

def create_parser():

    parser = argparse.ArgumentParser(
                    prog='CarBot',
                    description="You can here create a cars and etc.",
                    epilog='Thanks')
    subparser = parser.add_subparsers(dest='command')


    add_parser = subparser.add_parser('add',
                     help='add car (Brand, Model, Year)')
    add_parser.add_argument('name', type=str, help='brand of car')
    add_parser.add_argument('model', type=str, help='model of car')
    add_parser.add_argument('year', type=int, help='year of car')
    delete_parser = subparser.add_parser('delete',
                     help='delete car (car id)')
    delete_parser.add_argument('id', type=int, help='id of car')
    list_parser = subparser.add_parser('list',
                    help='list of exists cars')
    list_parser.add_argument("list", help="List all cars")

    return parser


