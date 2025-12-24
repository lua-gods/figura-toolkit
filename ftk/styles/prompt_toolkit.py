
from prompt_toolkit.styles import Style
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.formatted_text import ANSI

style = Style.from_dict({
	# Validation toolbar
	"validation-toolbar": "bg:default #ffffff",
	"validation-toolbar.error": "ansiyellow",
})

class PrefixedValidator(Validator):
	def error(self, message: str):
		raise ValidationError(
			message=f"[!] {message}",
		)

