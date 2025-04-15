import typer

app = typer.Typer()

@app.command()
def main():
    print('This is a snap SSCCE')

if __name__ == "__main__":
    app()
