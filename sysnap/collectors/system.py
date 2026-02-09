import platform
import socket
import psutil
import datetime

def collect_system_info() -> dict:
    """Collects general system information."""
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    uptime_seconds = int(datetime.datetime.now().timestamp() - boot_time_timestamp)

    return {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.machine(),
        "hostname": socket.gethostname(),
        "boot_time": boot_time,
        "uptime_seconds": uptime_seconds,
        "platform_details": platform.platform()
    }
