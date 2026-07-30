import argparse
from pathlib import Path
import pooch

def parse_args():
    parser = argparse.ArgumentParser(description="Regenerate Pooch registry.")
    parser.add_argument(
        '--datadir', 
        type=Path, 
        default=Path('.'), 
        help="Root directory containing all data files to index."
    )
    parser.add_argument(
        '--registry', 
        type=Path, 
        default=Path('index/registry.txt'), 
        help="Target path for the registry file."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    # pooch.make_registry overwrites the target file with hashes of all files in datadir.
    # Hidden files/directories (e.g., .git) are ignored by default.
    pooch.make_registry(args.datadir, args.registry)

if __name__ == "__main__":
    main()
