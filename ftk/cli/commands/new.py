from argparse import _SubParsersAction,Namespace,ArgumentParser
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.completion import PathCompleter
from pathlib import Path
import json
import os
import subprocess
import platform

import ftk.config as config
from ftk.styles.prints import *
from ftk.styles.prompt_toolkit import *
from . import validators

def register(subparsers: _SubParsersAction) -> None:
	parser: ArgumentParser = subparsers.add_parser(
		"new",
		help="Create a new Figura Avatar"
	)
	
	parser.add_argument(
		"path",
		help="Path to create the avatar in",
		nargs="?"
	)
	
	parser.add_argument(
		"name",
		help="Name",
		nargs="?"
	)
	
	parser.add_argument(
		"color",
		help="the Color of the Avatar badge in hex format",
		nargs="?"
	)
	
	parser.add_argument(
		"author",
		help="the author(s) of the avatar, separated by a comma (,)",
		nargs="?"
	)
	
	parser.add_argument(
		"desc",
		help="description",
		nargs="?"
	)
	
	parser.set_defaults(func=run)


def run(args: Namespace) -> None:
	
	avatar_path = Path(config.get_property("figura_path")).resolve() / "avatars"
	if avatar_path == "":
		warn("No figura root found, please set one with the following command:\nfigura-toolkit config set figura_path <path>")
		return
	if Path(avatar_path).exists() == False:
		warn("Figura path is invalid, please change it with the following command:\nfigura-toolkit config set figura_path <path>\nCurrent path: "+str(avatar_path))
		return
	
	# TUI
	note("You are creating an avatar in the following path:\n"+str(avatar_path))
	if args.name is None: # TUI
		args.path = prompt(
			"Location (optional): ",
			validator=validators.FolderNameValidator(),
			completer=PathCompleter(
				min_input_len=0,
				get_paths=lambda: [str(avatar_path)],
				only_directories=True,
				),
			)
		
		args.name = prompt(
			"Avatar Name: ",
			validator=validators.NameValidator(),
			validate_while_typing=True,
			)
		
		args.color = prompt(
			"Badge color (in hex) ?: ",
			validator=validators.HexColorValidator(),
			validate_while_typing=True,
			)
		
		args.author = prompt(
			"Author(s) (separated by ,): ",
			default=config.get_property("author") or "",
			)
		
		args.desc = prompt("Description (optional): ")
	
	
	target_path = avatar_path / Path(args.path) / Path(args.name)
	
	if target_path.exists():
		if not confirm("Avatar already exists in this path, overwrite?"):
			warn("Aborted")
			return
	target_path.mkdir(parents=True)
	
	avatar_json = {}
	if args.color is not None:
		avatar_json["color"] = args.color
	if args.author is not None and args.author != "":
		avatar_json["author"] = args.author
	if args.desc is not None:
		avatar_json["description"] = args.desc
	
	with (target_path / "avatar.json").open("w", encoding="utf-8") as f:
		json.dump(avatar_json, f, indent=4)
	(target_path / "main.lua").touch()
	
	success("Avatar created in "+str(target_path))
	
	input("Press enter to continue...")
	open_folder(target_path)


def open_folder(path: Path):
	system = platform.system()

	if system == "Windows":
		os.startfile(path)
	elif system == "Darwin":  # macOS
		subprocess.run(["open", path])
	else:  # Linux
		subprocess.run(["xdg-open", path])