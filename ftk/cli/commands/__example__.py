from argparse import _SubParsersAction,Namespace,ArgumentParser
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.completion import PathCompleter
from pathlib import Path
import ftk.config as config

BASE_PATH = Path(config.get_property("figura_path"))

def register(subparsers: _SubParsersAction) -> None:
	parser: ArgumentParser = subparsers.add_parser(
		"make",
		help="Create a new Figura Avatar"
	)
	
	parser.add_argument(
		"name",
		help="Avatar Name (and subfolder path)",
		nargs="?"
	)
	
	parser.add_argument(
		"color",
		help="the Color of the Avatar badge in hex format",
		nargs="?"
	)
	
	parser.add_argument(
		"author",
		help="separated by a comma (,) the author(s) of the avatar",
		nargs="?"
	)
	
	parser.set_defaults(func=run)

def run(args: Namespace) -> None:
	if args.name is None: # TUI
		args.name = prompt(
			default=str(BASE_PATH),
			completer=PathCompleter(
				expanduser=True,
				only_directories=True
			),
		)