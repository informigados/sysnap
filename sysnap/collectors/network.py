import psutil
import socket

def collect_network_info() -> dict:
    """Collects Network information."""
    interfaces = {}
    try:
        addrs = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
    except Exception:
        return {}

    for nic, addrs_list in addrs.items():
        if_info = {
            "is_up": stats[nic].isup if nic in stats else False,
            "speed_mbps": stats[nic].speed if nic in stats else 0,
            "addresses": []
        }
        
        for addr in addrs_list:
            if addr.family == socket.AF_INET:  # IPv4
                if_info["addresses"].append({
                    "family": "IPv4",
                    "address": addr.address,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast
                })
            elif addr.family == socket.AF_INET6: # IPv6
                if_info["addresses"].append({
                    "family": "IPv6",
                    "address": addr.address.split('%')[0], # Remove scope id if present
                })
            elif hasattr(psutil, "AF_LINK") and addr.family == psutil.AF_LINK: # MAC
                if_info["mac_address"] = addr.address

        interfaces[nic] = if_info
        
    return {"interfaces": interfaces}
