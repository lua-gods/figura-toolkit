import re
from pathlib import Path
from prompt_toolkit.validation import Validator
from ftk.styles.prompt_toolkit import PrefixedValidator


HEX_RE = re.compile(r"^#?[0-9a-fA-F]{6}$")
ILLEGAL_CHARS = '<>:"|?*'  # Windows-safe


class HexColorValidator(PrefixedValidator):
	def validate(self, document):
		text = document.text.strip()
		if text is None or text == "": return # allow empty
		if not HEX_RE.match(text):
			raise self.error(
				"Enter a hex color like #RRGGBB")


class FolderNameValidator(PrefixedValidator):
	def validate(self, document):
		text = document.text.strip()

		if any(c in text for c in ILLEGAL_CHARS):
			raise self.error("Invalid character in path")

		p = Path(text)

		if p.is_absolute():
			raise self.error("Use a relative path")

		if ".." in p.parts:
			raise self.error("Parent paths (..) are not allowed")




class NameValidator(PrefixedValidator):
	def validate(self, document):
		text = document.text.strip()

		if text == "":
			raise self.error("Name cannot be empty")