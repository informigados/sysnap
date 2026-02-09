import psutil
from sysnap.utils import format_bytes

def collect_disk_info() -> dict:
    """Collects Disk information."""
    disks = []
    try:
        partitions = psutil.disk_partitions(all=False)
    except Exception:
        partitions = []

    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            disks.append({
                "device": p.device,
                "mountpoint": p.mountpoint,
                "fstype": p.fstype,
                "opts": p.opts,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent,
                "total_human": format_bytes(usage.total),
                "free_human": format_bytes(usage.free),
            })
        except PermissionError:
            continue
        except Exception:
            continue
            
    return {"partitions": disks}
