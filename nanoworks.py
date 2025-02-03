import os
import ctypes
import platform
import subprocess

def check_smart_status(drive_letter):
    """
    Check SMART status of the drive using Windows Management Instrumentation Command-line (WMIC).
    """
    try:
        command = f"wmic diskdrive where \"DeviceID like '{drive_letter}%'\" get Status"
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if "Status" in result.stdout:
            status_lines = result.stdout.splitlines()
            # Assuming the status is in the second line
            if len(status_lines) > 1:
                return status_lines[1].strip()
        return "Unknown"
    except Exception as e:
        return f"Error: {e}"

def check_disk_health():
    """
    Scans all disk drives and reports on their health.
    """
    print("Scanning disk health...\n")
    drives = [f"{d}:" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:")]
    
    health_report = {}
    for drive in drives:
        status = check_smart_status(drive)
        health_report[drive] = status
        print(f"Drive {drive} - SMART Status: {status}")
    
    return health_report

def display_preemptive_alerts(health_report):
    """
    Displays preemptive alerts based on disk health.
    """
    print("\nPreemptive Alerts:\n")
    alerts = []
    for drive, status in health_report.items():
        if status.lower() != "ok":
            alert_message = f"Warning: Drive {drive} may be failing. Status: {status}"
            print(alert_message)
            alerts.append(alert_message)
    
    if not alerts:
        print("All drives are healthy.")

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("NanoWorks is designed to run on Windows systems only.")
    else:
        health_report = check_disk_health()
        display_preemptive_alerts(health_report)