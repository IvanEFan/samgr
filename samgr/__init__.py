import os
from samgr import constant

# Create .samgrrc file is it is not exist
if not os.path.isfile(constant.SAMGRRC_PATH):
    with open(constant.SAMGRRC_PATH, 'w+'):
        pass

# Write source ~/.samgrrc to .zshrc
if not os.path.isfile(constant.ZSHRC_PATH):
    with open(constant.SAMGRRC_PATH, 'w+') as f:
        f.write('source ~/.samgrrc')
else:
    with open(constant.ZSHRC_PATH, 'r') as f:
        ctx = f.read()
        if 'source ~/.samgrrc' not in ctx:
            os.system(f'echo "\nsource ~/.samgrrc" >> {constant.ZSHRC_PATH}')
