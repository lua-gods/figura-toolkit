from . import ansi

def warn(msg: str):
	msg = str(msg)
	print(f"{ansi.YELLOW}│ ⚠ Warning\n│  {msg.replace("\n","\n│  ")}{ansi.RESET}")

def note(msg: str):
	msg = str(msg)
	print(f"{ansi.BLUE}│ 🛈 Note\n│  {msg.replace("\n","\n│  ")}{ansi.RESET}")
	

def success(msg: str):
	msg = str(msg)
	print(f"{ansi.GREEN}│ ✔ Success\n│  {msg.replace("\n","\n│  ")} {ansi.RESET}")
