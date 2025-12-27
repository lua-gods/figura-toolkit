> [!NOTE]
> This readme is a proof of concept, message me on the thread about the repo if you have any questions or suggestions

# Package Examples

### Example Package Repo Source (Multiple Files)


```jsonc
{
	"name": "user.package",

	// history snapshots of the package
	"versions": [
		{
			"version": "3.0.0",
			"hash": "f1d6268e5dce8597128d78dc17d72501b58e7032"
		},
		{
			"version": "2.0.0",
			"hash": "516a6ed6225b9a9d46c1f6d7eae809aed87892d2",
		},

		// the first version has alot more entries compared to the newer version entries, because it declares everything about the packages
		// entries can still be added into the newer versions to dictate changes in that given entry in question (dependencies,src,paths)
		{
			"version": "1.0.0",
			"hash": "90ca0aa251aa73e0e0c1dfae6b43de9ddfa7ec71",
			"layout": {
				// layout declared as an array
				"paths": ["example.lua", "src/folder.lua", "src/other/folder.lua"]
			},
			// tells what packages needs to be installed for this to work
			// this is in the version entry because dependencies can change, newer dependency entries will override this value
			"dependencies": ["user.package2"],

			// works alongside the hash to grab a specific version of the file in the given repository link
			"repo": "https://repo.com/repo/"
		}
	]
}

```

### Example Package Direct link (Single File)


```jsonc
{
	"name": "user.package",

	// tells which is the default version to install
	"latest": "3.0.0",

	// the different versions of the file
	"versions": [
		{
			"version": "3.0.0",
			"src": "https://example.com/package-3.0.0.lua"
		},
		{
			"version": "2.0.0",
			"src": "https://example.com/package-2.0.0.lua"
		},

		// the first version has alot more entries compared to the newer version entries, because it declares everything about the packages
		// entries can still be added into the newer versions to dictate changes in that given entry in question (dependencies,src,paths)
		{
			"version": "1.0.0",
			"src": "https://example.com/package-1.0.0.lua",
			"dependencies": ["user.package2"]
		}
	]
}

```

# Repository of packages Example

```jsonc
// the one that holds the list of all the packages
{
	"user.package": "example_package_single.json",
	"user.package2": "example_package_multi.json"
}
```

# Per Avatar files

### avatar_manifest.json

- a list of the required packages
- this tells the figura toolkit what to look for

```jsonc
{
	"packages": {
		"user.package": "1.0.0"
	}
}
```

### avatar_manifest.json.lock

- this json is automatically generated and handled by the figura-toolkit,
- not meant to be touched by the user

```jsonc
{
	// tells what version of the figura toolkit is used to manage this project
	"ftk-version": "0.0.1",
	
	//a list of all the currently installed packages and dependencies
	"packages": {
		"user.package": "1.0.0"
	}
}
```
