from . import ansi

def warn(msg: str):
	msg = str(msg)
	print(f"{ansi.YELLOW}│ ⚠ Warning\n│  {msg.replace("\n","\n│  ")}")

def note(msg: str):
	msg = str(msg)
	print(f"{ansi.BLUE}│ 🛈 Note\n│  {msg.replace("\n","\n│  ")}")
