from samgr import constant
from samgr.alias import Alias

import re
from typing import *


def load_samgrrc():
    aliases = []
    with open(constant.SAMGRRC_PATH, 'r') as f:
        for line in f.readlines():
            if not line.strip():
                continue
            result = re.search('alias (.*)=\'(.*)\'', line)
            aliases.append(Alias(result.group(1), result.group(2)))

    return aliases


def save_aliases(aliases: Iterator[Alias]):
    with open(constant.SAMGRRC_PATH, 'w') as f:
        for alias in aliases:
            f.write(f'alias {alias.alias}=\'{alias.command}\'\n')
