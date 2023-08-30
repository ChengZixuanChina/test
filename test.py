from textual.app import App, ComposeResult
from textual.widgets import *
from textual.screen import Screen

class AuthorInfo(Screen):
    def compose(self):
        yield Label("作者：程子轩")
        yield Label("版权所有，盗版必究。")

class DemoApp(App):
    """A Textual app."""

    CSS_PATH = "test.css"
    BINDINGS = [
            ("d", "toggle_dark", "切换模式"),
            ("o", "show_author", "作者信息:)")
                ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_show_author(self):
        self.push_screen(AuthorInfo())


if __name__ == "__main__":
    app = DemoApp()
    app.run()
