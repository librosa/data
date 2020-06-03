#!/usr/bin/env python
'''Index data files for distribution'''

from pathlib import Path
import pooch
import json


def main():
    # Build the pooch registry
    regfile = Path('index') / Path('registry.txt')
    pooch.make_registry('audio', regfile)

    # Parse the registry into the keyword manifest
    tracks = set()
    with open(regfile, 'r') as fd:
        for line in fd:
            base = line.split('.', 2)[0]
            tracks.add(base)

    keymap = Path('index') / Path('index.json')
    if keymap.exists():
        with open(keymap, 'r') as fd:
            trackmap = json.load(fd)
    else:
        trackmap = dict()
    
    for track in tracks:
        if track not in trackmap:
            trackmap[track] = input('Enter a key for {}: '.format(track))

    with open(keymap, 'w') as fd:
        json.dump(trackmap, fd)


if __name__ == '__main__':
    main()
