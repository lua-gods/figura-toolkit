
from urllib.parse import urlparse

# Github
# https://github.com/lua-gods/GNUI/blob/d49b1c062e2124a31d03bfb6dcb994c5f9afd3ea/nineslice.lua
# https://raw.githubusercontent.com/lua-gods/GNUI/d49b1c062e2124a31d03bfb6dcb994c5f9afd3ea/nineslice.lua

# Codeberg
# https://codeberg.org/small-hack/argocd-apps/src/commit/77fb58f3b18a36859b2374f96399200c097108ea/cert-manager/README.md
# https://codeberg.org/small-hack/argocd-apps/raw/commit/77fb58f3b18a36859b2374f96399200c097108ea/cert-manager/README.md


def get_file_from_commit(url : str, commit : str):
	raw = to_raw(url)
	


def to_raw(url : str):
	if url is None: raise ValueError("No URL given")
	
	parsed = urlparse(url)
	if parsed.netloc == "github.com":
		parts = parsed.path.strip("/").split("/")
		
		if len(parts) < 5 or parts[2] != "blob":
			raise ValueError("Invalid GitHub URL")
		
		return (
			url
			.replace("https://github.com/", "https://raw.githubusercontent.com/")
			.replace("/blob/", "/")
		)
		
	elif parsed.netloc == "codeberg.org":
		url.replace("/src/commit/","/raw/commit/")
		return url