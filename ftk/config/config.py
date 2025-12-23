from appdirs import user_config_dir
from importlib.metadata import metadata
from pathlib import Path
import json

REQUIRED_CHILDREN = {"avatar","config","data"}
ROOT_NAME = "figura"

_data = {}

CONFIG_FILE: Path = Path(user_config_dir("figura-toolkit")) / "config.json"


def _is_figura_root():
	if path.name != "figura":
		return False


def _find_figura_root(start: Path | None = None) -> Path | None:
	if start is None:
		start = Path.cwd()
	start = start.resolve()
	
	for current in [start, *start.parents]:
		if current.name == ROOT_NAME:
			return current


def reset_config():
	return save_config({
		"figura_path": "",
	})


def load_config() -> None:
	if not CONFIG_FILE.exists():
		reset_config()
		return 
	
	with CONFIG_FILE.open("r") as f:
		return json.load(f)
	
	if _data["figura_path"] == "":
		_data["figura_path"] = _find_figura_root()


def save_config(config: dict) -> None:
	CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
	
	with CONFIG_FILE.open("w", encoding="utf-8") as f:
		json.dump(config, f)


def set_property(key: str, value):
	if _data.get(key) is not None:
		_data[key] = value


def get_property(key: str):
	return _data.get(key)

config = load_config()
