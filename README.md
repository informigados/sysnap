# 📸 SYSNAP

A Python CLI for capturing and comparing system snapshots. The System Snapshot Tool exports detailed JSON and readable text reports for technical support, diagnostics, and auditing.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey) 
[![DeepWiki](https://img.shields.io/badge/DeepWiki-informigados%2Fsysnap-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAyCAYAAAAnWDnqAAAAAXNSR0IArs4c6QAAA05JREFUaEPtmUtyEzEQhtWTQyQLHNak2AB7ZnyXZMEjXMGeK/AIi+QuHrMnbChYY7MIh8g01fJoopFb0uhhEqqcbWTp06/uv1saEDv4O3n3dV60RfP947Mm9/SQc0ICFQgzfc4CYZoTPAswgSJCCUJUnAAoRHOAUOcATwbmVLWdGoH//PB8mnKqScAhsD0kYP3j/Yt5LPQe2KvcXmGvRHcDnpxfL2zOYJ1mFwrryWTz0advv1Ut4CJgf5uhDuDj5eUcAUoahrdY/56ebRWeraTjMt/00Sh3UDtjgHtQNHwcRGOC98BJEAEymycmYcWwOprTgcB6VZ5JK5TAJ+fXGLBm3FDAmn6oPPjR4rKCAoJCal2eAiQp2x0vxTPB3ALO2CRkwmDy5WohzBDwSEFKRwPbknEggCPB/imwrycgxX2NzoMCHhPkDwqYMr9tRcP5qNrMZHkVnOjRMWwLCcr8ohBVb1OMjxLwGCvjTikrsBOiA6fNyCrm8V1rP93iVPpwaE+gO0SsWmPiXB+jikdf6SizrT5qKasx5j8ABbHpFTx+vFXp9EnYQmLx02h1QTTrl6eDqxLnGjporxl3NL3agEvXdT0WmEost648sQOYAeJS9Q7bfUVoMGnjo4AZdUMQku50McDcMWcBPvr0SzbTAFDfvJqwLzgxwATnCgnp4wDl6Aa+Ax283gghmj+vj7feE2KBBRMW3FzOpLOADl0Isb5587h/U4gGvkt5v60Z1VLG8BhYjbzRwyQZemwAd6cCR5/XFWLYZRIMpX39AR0tjaGGiGzLVyhse5C9RKC6ai42ppWPKiBagOvaYk8lO7DajerabOZP46Lby5wKjw1HCRx7p9sVMOWGzb/vA1hwiWc6jm3MvQDTogQkiqIhJV0nBQBTU+3okKCFDy9WwferkHjtxib7t3xIUQtHxnIwtx4mpg26/HfwVNVDb4oI9RHmx5WGelRVlrtiw43zboCLaxv46AZeB3IlTkwouebTr1y2NjSpHz68WNFjHvupy3q8TFn3Hos2IAk4Ju5dCo8B3wP7VPr/FGaKiG+T+v+TQqIrOqMTL1VdWV1DdmcbO8KXBz6esmYWYKPwDL5b5FA1a0hwapHiom0r/cKaoqr+27/XcrS5UwSMbQAAAABJRU5ErkJggg==)](https://deepwiki.com/informigados/sysnap)

## 🚀 Features

- **Comprehensive Snapshots**: Captures OS details, CPU, Memory, Disk, and Network configurations.
- **Dual Output**: Generates both machine-readable **JSON** and human-readable **TXT** reports.
- **Snapshot Comparison**: Built-in diff engine to compare two snapshots and highlight changes (e.g., RAM upgrades, disk usage shifts).
- **Cross-Platform**: Works seamlessly on Windows, Linux, and macOS.
- **Zero-Bloat**: Minimal dependencies, focused on core functionality.

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/informigados/sysnap.git
   cd sysnap
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## 🛠️ Usage

SYSNAP provides a clear CLI interface for managing system snapshots.

### 1. Take a Snapshot

**Print to Screen (JSON):**
By default, the `snapshot` command prints the JSON output to the terminal (stdout).
```bash
python -m sysnap.cli snapshot
```

**Save to File (Default Naming):**
Use the `--save` (or `-s`) flag to automatically generate a snapshot in the `snapshots/` folder. 
The filename will follow the pattern `snapshot-YYYY-MM-DD-HH-MM-SS`.
```bash
python -m sysnap.cli snapshot --save
```
*Output:*
- `snapshots/snapshot-2023-10-27-14-30-00.json`
- `snapshots/snapshot-2023-10-27-14-30-00.txt`

**Save to Custom File:**
Specify a custom filename using `-o` or `--output`. Do not include the extension; the tool will generate both `.json` and `.txt`.
```bash
python -m sysnap.cli snapshot --output my_server_backup
```
*Output:*
- `my_server_backup.json`
- `my_server_backup.txt`

### 2. Compare Snapshots
Compare an old snapshot with a new one to see what changed:
```bash
python -m sysnap.cli compare old.json new.json
```

**Example Output:**
```
Comparing old.json -> new.json...

RAM Free: -512.00 MB (4.50 GB -> 4.00 GB)
Disk Free (C:\): -1.20 GB (50.00 GB -> 48.80 GB)
```

### 3. Help
View available commands and options:
```bash
python -m sysnap.cli --help
```

## 📂 Project Structure

```
sysnap/
├── sysnap/
│   ├── cli.py              # CLI Entry point
│   ├── engine.py           # Core orchestrator
│   ├── snapshot.py         # Data aggregation logic
│   ├── compare.py          # Diff logic
│   ├── utils.py            # Helpers & Report Generators
│   └── collectors/         # Hardware probes
│       ├── system.py       # OS & Uptime
│       ├── cpu.py          # Processor stats
│       ├── memory.py       # RAM usage
│       ├── disk.py         # Storage stats
│       └── network.py      # Interfaces & IPs
├── snapshots/              # Default storage for generated snapshots
├── tests/                  # Unit tests
├── examples/               # Sample outputs
├── pyproject.toml          # Project metadata
└── requirements.txt        # Dependencies
```

## 📜 Changelog

### v0.1.0 - Initial Release
- **Core**: Implementation of data collectors (CPU, Memory, Disk, Network, System).
- **CLI**: Command-line interface with `snapshot` and `compare` commands.
- **Reports**: Support for JSON (machine) and TXT (human) output formats.
- **Diff Engine**: Logic to compare two system snapshots and report differences.

## 👥 Authors

- [Alex Brito](https://github.com/alexbritodev)
- [INformigados](https://github.com/informigados)

Websites: [Alex Brito](https://alexhpbrito.com.br) · [INformigados](https://informigados.com.br)

## 📄 License

This project is licensed under the [MIT License](LICENSE).
