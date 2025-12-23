from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.styles import Style

style = Style.from_dict(
	{
		"input-selection": "fg:#ff0000",
		"number": "fg:#884444 bold",
		"selected-option": "underline",
	}
)

def make(args):
	avatar_name = prompt("Avatar Name (and subfolder path)")