# ORION

ORION is a lightweight, local, command-based assistant written in Python.

## Requirements

- Python 3.11 or newer
- No runtime third-party dependencies

## Run from source

PowerShell:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m orion
```

## Install locally

```powershell
python -m pip install -e .
python -m orion
```

## Commands

| Command | Description |
|---|---|
| `help` | Show available commands |
| `time` or `/time` | Show local date and time |
| `system` or `/system` | Show basic OS and Python information |
| `list` or `/list` | List entries in `C:\ORION` |
| `about` | Show application version |
| `exit` | Quit ORION |

Unknown slash commands return an explicit tool error. Unknown plain-text commands show help guidance.

## Tests

Run from the project root:

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m unittest discover -s tests -v
```

## Scope and security

ORION is a command-based assistant, not a general-purpose AI model.
Its built-in listing tool reads the configured `C:\ORION` directory.
It does not provide a general shell-execution command.

Review code and test behavior before using ORION with sensitive data.

## License

MIT. See `LICENSE`.

