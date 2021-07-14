import os

import click
from rich.console import Console

from samgr import util
from samgr import constant
from samgr.alias import Alias

console = Console()


@click.group()
def cli():
    pass


@cli.command('list')
def command_list():
    aliases = util.load_samgrrc()
    if not len(aliases):
        console.print(f'[red bold]No alias found :(')
        return
    max_length = max([len(alias.alias) for alias in aliases])
    console.print(f'[bright_red bold]Current aliases managed by samgr:')
    for alias in aliases:
        space_cnt = max_length - len(alias.alias)
        console.print(f'[bold]{alias.alias}[/bold]{" " * space_cnt}  [bright_red]->[/bright_red]  {alias.command}')


@cli.command('set')
@click.argument('alias')
@click.argument('command')
def command_set(alias, command):
    aliases = util.load_samgrrc()
    aliases = list(filter(lambda x: x.alias != alias, aliases))
    aliases.append(Alias(alias, command))
    util.save_aliases(aliases)
    console.print(f'[green]🎉 Alias:\n{alias}  ->  {command}\nhas been added!')


@cli.command('delete')
@click.argument('alias')
def command_delete(alias):
    aliases = util.load_samgrrc()
    util.save_aliases(filter(lambda x: x.alias != alias, aliases))
    console.print(f'[green]🎉 Alias {alias} has been deleted!')


@cli.command('reload')
def command_reload():
    os.system(f'source {constant.SAMGRRC_PATH}')
    console.print('[green]🎉 Your aliases have been reloaded!')


if __name__ == '__main__':
    cli()
