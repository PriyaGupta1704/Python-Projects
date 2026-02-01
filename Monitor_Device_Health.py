import subprocess  # To run OS Level Commands
from datetime import datetime  # Timestamps
import time  # Latency/sleep
import platform
import re

###############Device Class##########
class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.status = "UNKNOWN"
        self.latency = None

    def __str__(self):
        return f"{self.name}({self.ip})-{self.status}"

########Alert Manager#########
class AlertManager:
    @staticmethod  # Not depending on object state
    def send_alert(device, reason):
        alert = f"[ALERT] {device.name}({device.ip}) - {reason}"
        print(alert)
        with open("health_report.txt", "a") as f:
            f.write(alert + "\n")

######Health Monitor###########
class HealthMonitor:
    def __init__(self, latency_threshold=100):
        self.devices = []
        self.latency_threshold = latency_threshold

    def load_devices(self, file_path):
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 2:
                    continue
                name, ip = parts[0].strip(), parts[1].strip()
                self.devices.append(Device(name, ip))

    def ping_device(self, device):
        try:
            if platform.system().lower() == "windows":
                args = ["ping", "-n", "1", device.ip]
            else:
                args = ["ping", "-c", "1", device.ip]

            result = subprocess.run(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=5,
            )

            if result.returncode == 0:
                device.status = "UP"
                device.latency = self.extract_latency(result.stdout)
                if device.latency is not None and device.latency > self.latency_threshold:
                    AlertManager.send_alert(device, f"High Latency: {device.latency} ms")
            else:
                device.status = "DOWN"
                AlertManager.send_alert(device, "Device Unreachable")
        except Exception as e:
            device.status = "ERROR"
            AlertManager.send_alert(device, f"Monitoring failed: {e}")

    @staticmethod
    def extract_latency(output):
        for line in output.splitlines():
            # unix style: time=12.3 ms ; windows style may contain time=12ms or Average = 12ms
            m = re.search(r"time[=<]\s*([\d.]+)", line)
            if m:
                try:
                    return float(m.group(1))
                except ValueError:
                    continue
            m2 = re.search(r"Average\s*=\s*([\d.]+)ms", line)
            if m2:
                try:
                    return float(m2.group(1))
                except ValueError:
                    continue
        return None

    def run_monitoring(self):
        with open("health_report.txt", "w") as f:
            f.write(f"==Network Report {datetime.now()}==\n")
        for device in self.devices:
            self.ping_device(device)
            time.sleep(1)
        print("Monitoring Completed")

##########Main Function ############
def main():
    monitor = HealthMonitor(latency_threshold=100)
    monitor.load_devices("devices.txt")
    monitor.run_monitoring()

if __name__ == "__main__":
    main()


















