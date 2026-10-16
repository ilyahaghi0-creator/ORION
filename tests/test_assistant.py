
"""Tests for ORION's core assistant."""

import unittest

from orion.assistant import Assistant


class TestAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = Assistant()

    def test_help_command(self):
        self.assertIn("Available commands", self.assistant.respond("help"))

    
    def test_registered_time_tool(self):
        self.assertNotIn("Unknown tool", self.assistant.respond("/time"))

    def test_unknown_tool(self):
        self.assertEqual(
            self.assistant.respond("/missing"),
            "Unknown tool: missing",
        )

    def test_tool_registry(self):
        from orion.tools import ToolRegistry

        registry = ToolRegistry()
        registry.register("greeting", lambda: "Hello from ORION")
        self.assertEqual(registry.execute("greeting"), "Hello from ORION")

    def test_about_command(self):
        self.assertIn("ORION", self.assistant.respond("about"))

    def test_unknown_command(self):
        self.assertIn("don't recognize", self.assistant.respond("something"))

    def test_empty_input(self):
        self.assertIn("enter a command", self.assistant.respond(""))

    def test_input_length_limit(self):
        self.assertIn(
            "too long",
            self.assistant.respond("x" * 2001),
        )


if __name__ == "__main__":
    unittest.main()
