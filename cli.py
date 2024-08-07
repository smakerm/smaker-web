from typer import Typer, echo
import subprocess

app = Typer()


@app.command()
def migration(message):
    echo(f"make migrations info: {message}")
    subprocess.run(
        ["alembic", "revision", "--autogenerate", "-m", f"{message}"])


@app.command()
def migrate():
    echo("migrate hard")
    subprocess.run(["alembic", "upgrade", "head"])


def main():
    print("Hello World")


if __name__ == "__main__":
    app()
