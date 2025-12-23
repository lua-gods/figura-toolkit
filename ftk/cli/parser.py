import argparse
import pkgutil
import importlib
from . import commands

def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(prog="figura-toolkit")
	subparsers = parser.add_subparsers(required=True)
	
	for command in pkgutil.iter_modules(commands.__path__):
		if command.name.startswith("_"): continue
		module_name = f"{commands.__name__}.{command.name}"
		module = importlib.import_module(module_name)
		
		if hasattr(module,"register"):
			module.register(subparsers)
		else:
			RuntimeError(f"Module {module_name} does not have a register function!!!")
	
	return parser