# SYSNAP (System Snapshot Tool)

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey)

**SYSNAP** is a lightweight, professional command-line utility designed to capture, record, and compare system states. Built with Python, it provides a simple yet powerful way to generate detailed JSON snapshots and human-readable reports of your machine's configuration and resources, making it ideal for technical support, diagnostics, and auditing.

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

## 👤 Author

**Alex H. P. Brito**  
[Professor, Programmer, Speaker]  
**CEO & Founder — INformigados**

- 🌐 **Personal Website**: [alexhpbrito.com.br](https://alexhpbrito.com.br)
- 🏢 **Business Website**: [informigados.com.br](https://informigados.com.br)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
