import json
import os
import datetime
from sysnap import snapshot
from sysnap.utils import setup_logging, generate_text_report
import logging

class SysnapEngine:
    """
    Main orchestrator for SYSNAP operations.
    """
    def __init__(self, verbose=False):
        setup_logging(verbose)
        self.logger = logging.getLogger(__name__)

    def take_snapshot(self, output_path: str = None, save: bool = False) -> dict:
        """
        Generates a system snapshot and optionally saves it to a file.
        
        Args:
            output_path: Specific path to save the JSON file.
            save: If True and no output_path is provided, saves to default snapshots/ folder.
        """
        self.logger.info("Starting system snapshot collection...")
        data = snapshot.create_snapshot()
        
        if output_path or save:
            self.save_snapshot(data, output_path)
            
        self.logger.info("Snapshot collection completed.")
        return data

    def save_snapshot(self, data: dict, path: str = None):
        """
        Saves snapshot data to JSON and TXT files.
        If path is None, generates a default timestamped filename in 'snapshots/' folder.
        """
        if not path:
            # Default naming: snapshots/snapshot-YYYY-MM-DD-HH-MM-SS
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            filename = f"snapshot-{timestamp}"
            folder = "snapshots"
            if not os.path.exists(folder):
                os.makedirs(folder)
                self.logger.info(f"Created directory: {folder}")
            
            base_path = os.path.join(folder, filename)
        else:
            # Strip extension if present to use as base
            base_path = os.path.splitext(path)[0]
            # Ensure directory exists if path contains one
            directory = os.path.dirname(base_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)

        # Define file paths
        json_path = f"{base_path}.json"
        txt_path = f"{base_path}.txt"

        try:
            # Save JSON
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            self.logger.info(f"Snapshot JSON saved to: {json_path}")
            
            # Save TXT
            text_report = generate_text_report(data)
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text_report)
            self.logger.info(f"Snapshot TXT saved to: {txt_path}")
            
        except Exception as e:
            self.logger.error(f"Failed to save snapshot: {e}")
            raise

    def load_snapshot(self, path: str) -> dict:
        """Loads a snapshot from a JSON file."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Snapshot file not found: {path}")
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load snapshot from {path}: {e}")
            raise
