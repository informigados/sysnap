import datetime
from sysnap.collectors import system, cpu, memory, disk, network

def create_snapshot() -> dict:
    """
    Orchestrates the collection of data from all collectors.
    Returns a dictionary representing the system snapshot.
    """
    return {
        "meta": {
            "timestamp": datetime.datetime.now().isoformat(),
            "version": "1.0"
        },
        "system": system.collect_system_info(),
        "cpu": cpu.collect_cpu_info(),
        "memory": memory.collect_memory_info(),
        "disk": disk.collect_disk_info(),
        "network": network.collect_network_info(),
    }
