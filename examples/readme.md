# Package Examples

### Example Package (Multiple Files)

```jsonc
{
	"name": "user.package",

	// tells which is the default version to install
	"latest": "3.0.0",
	
	// history snapshots of the package
	// entries in the base dictionary can also be added into a version, as overrides
	// note that the overrides will affect every version to itself to the oldest that dosent have that entry,
	// so you only have to put an override when that said entry has changed
	"versions": {
		"3.0.0": {"hash": "f1d6268e5dce8597128d78dc17d72501b58e7032"},
		"2.0.0": {"hash": "516a6ed6225b9a9d46c1f6d7eae809aed87892d2"},
		"1.0.0": {
			"hash": "90ca0aa251aa73e0e0c1dfae6b43de9ddfa7ec71",
			"layout": {// layout declared as an array
				"paths": ["example.lua", "src/folder.lua", "src/other/folder.lua"]
			},
			// tells what packages needs to be installed for this to work
			// this is in the version entry because dependencies can change, newer dependency entries will override this value
			"dependencies": ["user.package2"]
		}
	},

	// the values here can also be supplied in a version entry, as seen in example_package_single.json
	// but it acts as a global default value if its supplied down here at the root dictionary.
	"src": "https://example.com/package-1.0.0.lua",

	// this tells which files to grab from the given repository link, based on the hash entry.
	// its so that we dont have to copy paste the same layout for different versions.
	"layout": "example_package_layout.json"
}
```

### Example Package (Single File)

```jsonc
{
	"name":"user.package",
	
	// tells which is the default version to install
	"latest": "3.0.0",
	
	// the different versions of the file
	"versions":{
		"3.0.0":{"src":"https://example.com/package-3.0.0.lua"},
		"2.0.0":{"src":"https://example.com/package-2.0.0.lua"},
		"1.0.0":{"src":"https://example.com/package-1.0.0.lua"}
	}
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
