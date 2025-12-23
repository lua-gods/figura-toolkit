from appdirs import user_config_dir
from importlib.metadata import metadata
from pathlib import Path
import json

REQUIRED_CHILDREN = {"avatar","config","data"}
ROOT_NAME = "figura"

data = {}

CONFIG_FILE: Path = Path(user_config_dir("figura-toolkit")) / "config.json"


def is_figura_root():
	if path.name != "figura":
		return False


def find_figura_root(start: Path | None = None) -> Path | None:
	if start is None:
		start = Path.cwd()
	
	start = start.resolve()
	
	for current in [start, *start.parents]:
		if current.name == ROOT_NAME:
			return current


def make_default_config():
	return save_config({
		"figura_path": "",
	})


def load_config() -> None:
	if not CONFIG_FILE.exists():
		make_default_config()
		return 
	
	with CONFIG_FILE.open("r") as f:
		return json.load(f)
	
	if data["figura_path"] == "":
		data["figura_path"] = find_figura_root()


def save_config(config: dict) -> None:
	CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
	
	with CONFIG_FILE.open("w", encoding="utf-8") as f:
		json.dump(config, f)


config = load_config()
