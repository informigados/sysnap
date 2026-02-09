import psutil
import cpuinfo

def collect_cpu_info() -> dict:
    """Collects CPU information."""
    try:
        info = cpuinfo.get_cpu_info()
        model_name = info.get('brand_raw', 'Unknown')
        arch = info.get('arch', 'Unknown')
    except Exception:
        model_name = "Unknown"
        arch = "Unknown"

    freq = psutil.cpu_freq()
    
    return {
        "model": model_name,
        "architecture": arch,
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "min_frequency_mhz": freq.min if freq else 0,
        "max_frequency_mhz": freq.max if freq else 0,
        "current_frequency_mhz": freq.current if freq else 0,
        "usage_percent": psutil.cpu_percent(interval=0.1)
    }
