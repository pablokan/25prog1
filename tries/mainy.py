from typer import run

def main(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    run(main)