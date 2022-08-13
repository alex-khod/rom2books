# rom2books
Exploratory notebooks to be used in conjunction with rom2py resource getters.

# Notebook content
* `a2alm_to_xlsx` - dump scenario maps (.alm) content (units, objects, sacks, etc.) to xlsx.__
* `a2atlas_objects` - draw all objects possible (trees, stumps, etc.) into one image.
* `a2atlas_structures` - draw all structures/buildings possible into one image.
* `a2reg_to_xlsx` - dump every possible object\structure into xlsx.
* `a2sprite` - draw some `.256` sprites, make gifs.
* `a2terrain` - example of tile extraction/drawing.
* `a2databin` - just some `world.res\data\data.bin` exploration, ie. file that defines logical state of monsters, units and item stats.
* `a2res` - just some `.res` exploration.
* `a2compile_struct` - just a bunch of commands to compile `orom-file-formats` into python readers.

# Installation
Install Python 3.7x, then git clone or download and unpack source like so:
```
git clone https://github.com/alex-khod/rom2py.git
cd rom2py
pip install -r requirements.txt
git clone https://github.com/alex-khod/rom2books.git
python -m jupyterlab
```
Select notebook from rom2books, run cells with CTRL+Enter, etc.
