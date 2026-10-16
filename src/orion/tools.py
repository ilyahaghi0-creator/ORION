
"""Built-in tools and tool registry for ORION."""

import platform
from datetime import datetime
from pathlib import Path
from typing import Callable

ToolFunction = Callable[[], str]


class ToolRegistry:
    """Register and execute explicitly approved tools."""

    def __init__(self) -> None:
        self._tools: dict[str, ToolFunction] = {}

    def register(self, name: str, function: ToolFunction) -> None:
        name = name.strip().lower()

        if not name or not name.isidentifier():
            raise ValueError("Tool name must be a valid identifier.")
        if name in self._tools:
            raise ValueError(f"Tool already registered: {name}")

        self._tools[name] = function

    def execute(self, name: str) -> str:
        function = self._tools.get(name.strip().lower())

        if function is None:
            return f"Unknown tool: {name}"

        try:
            return str(function())
        except Exception:
            return "Tool execution failed. Check the application logs."


def get_time() -> str:
    """Return the local date and time."""
    return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")


def get_help() -> str:
    return (
        "Available commands:\n"
        "  help   - Show available commands\n"
        "  time   - Show local date and time\n"
        "  system - Show system information\n"
        "  list   - List entries in C:\\ORION\n"
        "  about  - Show information about ORION\n"
        "  exit   - Close ORION"
    )


def get_system_info() -> str:
    """Return basic operating system information."""
    return (
        f"OS: {platform.system()}\n"
        f"OS version: {platform.version()}\n"
        f"Architecture: {platform.machine()}\n"
        f"Python: {platform.python_version()}"
    )


def get_list() -> str:
    """List entries in the explicitly allowed ORION directory."""
    allowed_path = Path(r"C:\ORION")

    try:
        entries = sorted(
            allowed_path.iterdir(),
            key=lambda entry: (
                not entry.is_dir(),
                entry.name.lower(),
            ),
        )

        if not entries:
            return "The directory is empty."

        return "\n".join(
            f"[DIR]  {entry.name}"
            if entry.is_dir()
            else f"[FILE] {entry.name}"
            for entry in entries
        )
    except OSError:
        return "Unable to read the allowed directory."
