from rich.console import Console
from rich.panel import Panel
import datetime

console = Console()

class Logger:
    @staticmethod
    def log_agent_action(agent_name: str, action: str, details: str):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        console.print(Panel(f"[{timestamp}] [bold]{agent_name}[/bold]: {action}\n\n{details}", title="Agent Trace", border_style="cyan"))

    @staticmethod
    def log_error(agent_name: str, error: str):
        console.print(Panel(f"[bold red]ERROR in {agent_name}:[/bold red] {error}", border_style="red"))

    @staticmethod
    def log_system(message: str):
        console.print(f"[dim]{message}[/dim]")
