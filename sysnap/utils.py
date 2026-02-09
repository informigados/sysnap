import logging
import sys

def setup_logging(verbose: bool = False):
    """Configures the logging for the application."""
    level = logging.DEBUG if verbose else logging.INFO
    format_str = "%(message)s"
    logging.basicConfig(level=level, format=format_str, stream=sys.stdout)

def format_bytes(size: float) -> str:
    """Formats bytes into human readable string."""
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    abs_size = abs(size)
    while abs_size > power:
        abs_size /= power
        n += 1
    return f"{size/ (power**n):.2f} {power_labels.get(n, '')}B"

def generate_text_report(data: dict) -> str:
    """Generates a human-readable text report from the snapshot data."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"SYSNAP SYSTEM SNAPSHOT REPORT")
    lines.append("=" * 60)
    
    meta = data.get("meta", {})
    lines.append(f"Generated at: {meta.get('timestamp', 'N/A')}")
    lines.append(f"Version:      {meta.get('version', 'N/A')}")
    lines.append("")

    # System
    sys = data.get("system", {})
    lines.append("[SYSTEM]")
    lines.append(f"Hostname:     {sys.get('hostname', 'N/A')}")
    lines.append(f"OS:           {sys.get('os', 'N/A')} {sys.get('release', '')} ({sys.get('version', '')})")
    lines.append(f"Architecture: {sys.get('architecture', 'N/A')}")
    lines.append(f"Boot Time:    {sys.get('boot_time', 'N/A')}")
    lines.append(f"Uptime:       {sys.get('uptime_seconds', 0) // 3600} hours")
    lines.append("")

    # CPU
    cpu = data.get("cpu", {})
    lines.append("[CPU]")
    lines.append(f"Model:        {cpu.get('model', 'N/A')}")
    lines.append(f"Cores:        {cpu.get('physical_cores', 'N/A')} Physical / {cpu.get('logical_cores', 'N/A')} Logical")
    lines.append(f"Frequency:    {cpu.get('current_frequency_mhz', 0):.2f} MHz (Max: {cpu.get('max_frequency_mhz', 0):.2f} MHz)")
    lines.append(f"Usage:        {cpu.get('usage_percent', 0)}%")
    lines.append("")

    # Memory
    mem = data.get("memory", {}).get("virtual_memory", {})
    lines.append("[MEMORY]")
    lines.append(f"Total:        {mem.get('total_human', 'N/A')}")
    lines.append(f"Used:         {mem.get('used_human', 'N/A')} ({mem.get('percent', 0)}%)")
    lines.append(f"Free:         {mem.get('free_human', 'N/A')}")
    lines.append("")

    # Disk
    lines.append("[DISK]")
    partitions = data.get("disk", {}).get("partitions", [])
    if not partitions:
        lines.append("No partitions detected.")
    else:
        for p in partitions:
            lines.append(f"Mount: {p.get('mountpoint')} ({p.get('fstype')})")
            lines.append(f"  Total: {p.get('total_human')} | Free: {p.get('free_human')} | Used: {p.get('percent')}%")
    lines.append("")

    # Network
    lines.append("[NETWORK]")
    interfaces = data.get("network", {}).get("interfaces", {})
    if not interfaces:
        lines.append("No interfaces detected.")
    else:
        for name, info in interfaces.items():
            status = "UP" if info.get("is_up") else "DOWN"
            lines.append(f"Interface: {name} [{status}]")
            for addr in info.get("addresses", []):
                lines.append(f"  {addr.get('family')}: {addr.get('address')}")
    
    lines.append("")
    lines.append("=" * 60)
    lines.append("End of Report")
    
    return "\n".join(lines)
