import psutil
from sysnap.utils import format_bytes

def collect_memory_info() -> dict:
    """Collects Memory information."""
    vm = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    return {
        "virtual_memory": {
            "total": vm.total,
            "available": vm.available,
            "used": vm.used,
            "free": vm.free,
            "percent": vm.percent,
            "total_human": format_bytes(vm.total),
            "used_human": format_bytes(vm.used),
            "free_human": format_bytes(vm.free),
        },
        "swap_memory": {
            "total": swap.total,
            "used": swap.used,
            "free": swap.free,
            "percent": swap.percent,
            "total_human": format_bytes(swap.total),
        }
    }
