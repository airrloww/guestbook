import click
import json

@click.group()
def guestbook():
    pass

@guestbook.command()
@click.argument('note', type=str)
def new(note):
    """Add a new note to the guestbook"""
    try:
        with open("guestbook.txt", "r") as f:
            guestbook = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        guestbook = []
    guestbook.append(note)
    with open("guestbook.txt", "w") as f:
        json.dump(guestbook, f)
    click.echo(f"[+] Successfully added note: {note}")

@guestbook.command()
def list():
    """Show all notes in the guestbook"""
    try:
        with open("guestbook.txt", "r") as f:
            guestbook = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        click.echo("[+] No notes found in guestbook.")
        return
    for idx, note in enumerate(guestbook):
        click.echo(f"[{idx}]: {note}")

@guestbook.command()
@click.argument('index', type=int)
@click.argument('note', type=str)
def edit(index, note):
    """Edit a note in the guestbook"""
    try:
        with open("guestbook.txt", "r") as f:
            guestbook = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        click.echo("[+] No notes found in guestbook.")
        return
    try:
        guestbook[index] = note
        with open("guestbook.txt", "w") as f:
            json.dump(guestbook, f)
        click.echo(f"[+] Successfully edited note '{index}' to '{note}'")
    except IndexError:
        click.echo(f"[+] Invalid index: {index}. Please enter")

@guestbook.command()
@click.argument('index', type=int)
def delete(index):
    """Delete a note in the guestbook"""
    try:
        with open("guestbook.txt", "r") as f:
            guestbook = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        click.echo("[+] No notes found in guestbook.")
        return
    try:
        del guestbook[index]
        with open("guestbook.txt", "w") as f:
            json.dump(guestbook, f)
        click.echo(f"[+] Successfully deleted note {index}")
    except IndexError:
        click.echo(f"[+] Invalid index: {index}. Please enter a valid index")

@guestbook.command()
def export():
    """Export the guestbook in json format"""
    try:
        with open("guestbook.txt", "r") as f:
            guestbook = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        click.echo("No messages found in guestbook.")
        return
    json_guestbook = json.dumps(guestbook)
    click.echo(json_guestbook)


if __name__ == '__main__':
    guestbook()
