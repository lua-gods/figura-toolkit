import os
import sys
import subprocess
from pathlib import Path
from argparse import _SubParsersAction,Namespace,ArgumentParser
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.completion import PathCompleter
import ftk.config as config

def register(subparsers: _SubParsersAction) -> None:
	parser: ArgumentParser = subparsers.add_parser(
		"config",
		help="Create a new Figura Avatar"
	)
	
	config_subparsers = parser.add_subparsers(
		required=True,
		dest="config_command"
		)
	
	set_parser = config_subparsers.add_parser("set",help="set a config property")
	set_parser.add_argument("key",help="key to set")
	set_parser.add_argument("value",help="value (leave empty for a TUI path auto complete)",nargs="?")
	set_parser.set_defaults(func=run_set)
	
	reset_parser = config_subparsers.add_parser("reset",help="resets the config file")
	reset_parser.set_defaults(func=run_reset)
	
	open_parser = config_subparsers.add_parser("open",help="resets the config file")
	open_parser.set_defaults(func=run_open)
	
	get_parser = config_subparsers.add_parser("get",help="get a config property")
	get_parser.add_argument("key",help="key to get")
	get_parser.set_defaults(func=run_get)



def run_set(args: Namespace) -> None:
	if args.value is None: # TUI
		value = prompt(
			completer=PathCompleter(
				expanduser=True,
				only_directories=True
			),
		)
		config.set_property(args.key, value,True)
	else:
		config.set_property(args.key, args.value,True)
	config.save_config()


def run_reset(args: Namespace) -> None:
	if not confirm("Are you sure you want to reset the config?"):
		return
	config.reset_config()


def run_open(args: Namespace) -> None:
	path = config.get_config_path()
	if sys.platform.startswith("win"): # windowz
		os.startfile(path)  # type: ignore[attr-defined]
	elif sys.platform == "darwin": # mac
		subprocess.run(["open", path], check=False)
	else:  # Linux
		subprocess.run(["xdg-open", path], check=False)


def run_get(args: Namespace) -> None:
	print(config.get_property(args.key))