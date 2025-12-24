from appdirs import user_config_dir
from importlib.metadata import metadata
from pathlib import Path
import json

REQUIRED_CHILDREN = {"avatar","config","data"}
ROOT_NAME = "figura"

_data = {}
_data_overrides = {}


CONFIG_FILE: Path = Path(user_config_dir("figura-toolkit")) / "config.json"


def _find_figura_root(start: Path | None = None) -> Path | None:
	if start is None:
		start = Path.cwd()
	start = start.resolve()
	
	for current in [start, *start.parents]:
		if current.name == ROOT_NAME:
			return current


def get_config_path() -> Path:
	return CONFIG_FILE

def reset_config():
	print("Resetting config")
	_data.clear()
	_data["figura_path"] = ""
	save_config()


def load_config() -> None:
	with CONFIG_FILE.open("r") as f:
		global data
		_data.update(json.load(f))
		
	
	if CONFIG_FILE.read_text() == "{}":
		print("Config file is empty.")
		reset_config()
	
	if _data.get("figura_path") == "":
		path = _find_figura_root()
		if path is not None:
			_data_overrides["figura_path"] = path


def save_config() -> None:
	CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
	
	with CONFIG_FILE.open("w", encoding="utf-8") as f:
		json.dump(_data, f)


def set_property(key: str, value, verbose: bool = False):
	last_value = _data[key]
	_data[key] = value
	if verbose:
		print(f"set {key} to {value}\nold value: {last_value}")


def get_property(key: str):
	if key in _data_overrides:
		return _data_overrides[key]
	else:
		return _data.get(key)

load_config()