from sysnap.utils import format_bytes

def compare_snapshots(old: dict, new: dict) -> list:
    """
    Compares two snapshots and returns a list of differences strings.
    """
    diffs = []

    # System
    old_sys = old.get("system", {})
    new_sys = new.get("system", {})
    if old_sys.get("hostname") != new_sys.get("hostname"):
        diffs.append(f"Hostname: {old_sys.get('hostname')} -> {new_sys.get('hostname')}")
    if old_sys.get("os") != new_sys.get("os"):
        diffs.append(f"OS: {old_sys.get('os')} -> {new_sys.get('os')}")

    # Memory
    old_mem = old.get("memory", {}).get("virtual_memory", {})
    new_mem = new.get("memory", {}).get("virtual_memory", {})
    
    if old_mem.get("total") != new_mem.get("total"):
        diffs.append(f"RAM Total: {old_mem.get('total_human')} -> {new_mem.get('total_human')}")
    
    # Calculate free memory diff
    mem_diff = new_mem.get("free", 0) - old_mem.get("free", 0)
    if abs(mem_diff) > 1024 * 1024 * 10: # Only show if diff > 10MB
        sign = "+" if mem_diff > 0 else ""
        diffs.append(f"RAM Free: {sign}{format_bytes(mem_diff)} ({old_mem.get('free_human')} -> {new_mem.get('free_human')})")

    # CPU
    old_cpu = old.get("cpu", {})
    new_cpu = new.get("cpu", {})
    if old_cpu.get("model") != new_cpu.get("model"):
        diffs.append(f"CPU Model: {old_cpu.get('model')} -> {new_cpu.get('model')}")

    # Disk
    old_disks = {d["mountpoint"]: d for d in old.get("disk", {}).get("partitions", [])}
    new_disks = {d["mountpoint"]: d for d in new.get("disk", {}).get("partitions", [])}
    
    all_mounts = set(old_disks.keys()) | set(new_disks.keys())
    
    for mount in all_mounts:
        if mount not in old_disks:
            diffs.append(f"Disk New Partition: {mount} ({new_disks[mount].get('total_human')})")
            continue
        if mount not in new_disks:
            diffs.append(f"Disk Removed Partition: {mount}")
            continue
            
        old_d = old_disks[mount]
        new_d = new_disks[mount]
        
        # Space free diff
        free_diff = new_d.get("free", 0) - old_d.get("free", 0)
        if abs(free_diff) > 1024 * 1024 * 100: # Only show if diff > 100MB
            sign = "+" if free_diff > 0 else ""
            diffs.append(f"Disk Free ({mount}): {sign}{format_bytes(free_diff)} ({old_d.get('free_human')} -> {new_d.get('free_human')})")

    # Network
    old_net = old.get("network", {}).get("interfaces", {})
    new_net = new.get("network", {}).get("interfaces", {})
    
    for iface in new_net:
        if iface not in old_net:
             diffs.append(f"Network New Interface: {iface}")
        else:
            # Check IPs
            old_ips = [a["address"] for a in old_net[iface].get("addresses", [])]
            new_ips = [a["address"] for a in new_net[iface].get("addresses", [])]
            
            added = set(new_ips) - set(old_ips)
            removed = set(old_ips) - set(new_ips)
            
            if added:
                diffs.append(f"Network {iface} Added IPs: {', '.join(added)}")
            if removed:
                diffs.append(f"Network {iface} Removed IPs: {', '.join(removed)}")

    return diffs
