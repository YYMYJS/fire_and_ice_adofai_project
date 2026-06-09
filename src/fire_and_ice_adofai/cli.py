import typer

from .adofai_builder import write_adofai
from .rule_generator import generate_angles

app = typer.Typer()


@app.command()
def demo(output: str = "demo.adofai", bpm: float = 120.0, beats: int = 64):
    angles = generate_angles(beats)
    write_adofai(output, angles, bpm, 0.0, "song.ogg")
    typer.echo(f"wrote {output}")


if __name__ == "__main__":
    app()
