import argparse
import sys
import json
from sysnap.engine import SysnapEngine
from sysnap.compare import compare_snapshots
from sysnap import __version__

def main():
    parser = argparse.ArgumentParser(
        description="SYSNAP - System Snapshot Tool",
        epilog="Example: sysnap snapshot --output my_pc.json"
    )
    parser.add_argument("--version", action="version", version=f"sysnap {__version__}")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Snapshot command
    snap_parser = subparsers.add_parser("snapshot", help="Take a system snapshot")
    snap_parser.add_argument("-o", "--output", help="Output file path (without extension). If not provided, prints to stdout unless --save is used.", default=None)
    snap_parser.add_argument("-s", "--save", action="store_true", help="Save to 'snapshots/' folder with timestamp if no output path is provided.")
    snap_parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    # Compare command
    comp_parser = subparsers.add_parser("compare", help="Compare two snapshots")
    comp_parser.add_argument("old", help="Path to the old snapshot JSON")
    comp_parser.add_argument("new", help="Path to the new snapshot JSON")
    comp_parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    if args.command == "snapshot":
        engine = SysnapEngine(verbose=args.verbose)
        try:
            data = engine.take_snapshot(args.output, save=args.save)
            if not args.output and not args.save:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            elif args.output:
                 print(f"Snapshot successfully saved to {args.output}.json and {args.output}.txt")
            elif args.save:
                 print(f"Snapshot successfully saved to snapshots/ folder.")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "compare":
        engine = SysnapEngine(verbose=args.verbose)
        try:
            old_data = engine.load_snapshot(args.old)
            new_data = engine.load_snapshot(args.new)
            
            print(f"Comparing {args.old} -> {args.new}...\n")
            diffs = compare_snapshots(old_data, new_data)
            
            if not diffs:
                print("No significant differences found.")
            else:
                for diff in diffs:
                    print(diff)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
