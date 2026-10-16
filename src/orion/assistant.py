"""Core conversation loop for ORION."""

from .config import APP_NAME, VERSION, MAX_INPUT_LENGTH
from .tools import ToolRegistry, get_help, get_time, get_system_info, get_list


class Assistant:
    """A command-based assistant with explicitly registered tools."""

    def __init__(self) -> None:
        self.tools = ToolRegistry()
        self.tools.register("time", get_time)
        self.tools.register("system", get_system_info)
        self.tools.register("list", get_list)

    def respond(self, user_input: str) -> str:
        raw_input = user_input.strip()

        if not raw_input:
            return "Please enter a command."

        if len(user_input) > MAX_INPUT_LENGTH:
            return f"Input is too long (maximum {MAX_INPUT_LENGTH} characters)."

        is_tool_request = raw_input.startswith("/")
        command = raw_input.lstrip("/").lower() if is_tool_request else raw_input.lower()

        if command in {"help"}:
            return get_help()

        if command == "about":
            return f"{APP_NAME} v{VERSION} - a local Python assistant."

        if command in {"time", "system", "list"}:
            return self.tools.execute(command)

        if is_tool_request:
            return self.tools.execute(command)

        return (
            "I don't recognize that command yet.\n"
            "Type 'help' to see available commands."
        )

    def run(self) -> None:
        print(f"\n{APP_NAME} v{VERSION}")
        print("Type 'help' for commands or 'exit' to quit.\n")

        while True:
            try:
                user_input = input("You > ")

                if user_input.strip().lower() in {"exit", "quit"}:
                    print("ORION > Goodbye!")
                    break

                print(f"ORION > {self.respond(user_input)}\n")

            except (KeyboardInterrupt, EOFError):
                print("\nORION > Goodbye!")
                break
