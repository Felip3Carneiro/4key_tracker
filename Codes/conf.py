import os, sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from PIL import Image

def vel(height, skin):
    if skin == "circ0":
        return 20
    if skin == "line0":
        return 15
    if skin == "round0":
        return 15
    
    else:
        if height >= 70:
            return 20
        if height < 70:
            return 15
        
def skins(skin_0, skin_1, background):
    note_skins = []
    note_xy = []

    back_skins = []
    back_xy = []

    #Organização
    for file in os.listdir("images"):
        if "0" in file or "1" in file:
            note_skins.append(file[:-4])
            with Image.open(f"Images/{file}") as img:
                note_xy.append(img.size)  # (largura, altura)
        else:
            back_skins.append(file[:-4])
            with Image.open(f"Images/{file}") as img:
                back_xy.append(img.size)  # (largura, altura)

    #A parte daora
    console = Console()

    #Notes
    table_n = Table(title="[underline blue]Note Skins[/underline blue]")
    table_n.add_column("Name")
    table_n.add_column("Size")

    for name, size in zip(note_skins, note_xy):
        table_n.add_row(name, f"{size[0]}x{size[1]}")

    #Backgrounds
    table_b = Table(title="[underline blue]Note Skins[/underline blue]")
    table_b.add_column("Name")
    table_b.add_column("Size")
    
    for name, size in zip(back_skins, back_xy):
        table_b.add_row(name, f"{size[0]}x{size[1]}")

    #Print final
    console.print(table_n)
    console.print(table_b)

    if skin_0 and skin_1 in note_skins and background in back_skins:
        console.print("\n[bold green][underline green]All skins found![/]")
    else:
        error()

def error():
    console = Console()
    console.print(Panel("[bold red][ERROR]Nome do arquivo não existe, tente novamente[/bold red]", title="Aviso"))
    sys.exit()
