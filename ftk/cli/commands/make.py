from argparse import _SubParsersAction,Namespace


def register(subparsers: _SubParsersAction) -> None:
	parser = subparsers.add_parser(
		"make",
		help="Create a new Figura Avatar"
	)
	
	parser.add_argument(
		"name",
		help="Avatar Name (and subfolder path)"
	)
	
	parser.set_defaults(func=run)

def run(args: Namespace) -> None:
	pass