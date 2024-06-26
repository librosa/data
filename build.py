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
    
    known_tracks = set(t['path'] for t in trackmap.values())

    for track in tracks:
        if track not in known_tracks and track != "version_index":
            try:
                key = input('Enter a key for {}: '.format(track))
                desc = input('Enter a description for {}: '.format(track))
                trackmap[key] = dict(path=track, desc=desc)
            except KeyboardInterrupt:
                pass
    with open(keymap, 'w') as fd:
        json.dump(trackmap, fd)


if __name__ == '__main__':
    main()
