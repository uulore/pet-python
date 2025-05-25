from app.client.cli import create_parser
from app.services.add import factory

parser = create_parser()
args = parser.parse_args()


def main():
    if args.command == "add":
        factory.add(name=args.name, model=args.model, year=args.year)
    elif args.command == "delete":
        factory.delete(id=args.id)
    elif args.command == "list":
        factory.list()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()