# Figura tool-kit

>[!CAUTION]
> This is a work in progress, it is not ready for use yet


## Roadmap
- [x] Config editor
	- [x] `config Set <key> <value>` sets the value of the given key
	- [x] `config get <key>` returns the value of the given key
	- [x] `config reset` resets the config
	- [x] `config open` opens the config file in a default text editor
- [ ] Avatar wizard
- [ ] Package Layout (how a package is declared)
- [ ] Package Manager

## Setting up workspace
simply run the `setup.sh` in bash
```
bash setup.sh
```
then enter the venv

```
# for people
> source .venv/bin/activate

# for fish people
> .venv/bin/activate.fish
```

to run the tool out from source
```
python -m ftk <args>
```
## Building from source
> [!NOTE]
> only a linux build is available at this time

### Linux build
simply run the build.sh, if it doesn't work, try it in bash
```
bash build.sh
```
and it should pop out a binary in the `dist` folder
