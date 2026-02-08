#!/usr/bin/env python3
"""
IP CHANGER - Professional Network Tool
GitHub: https://github.com/00xk/IP-Changer
Author: 00xk
Version: 6.0 FINAL

This tool uses TOR network and advanced techniques to change your public IP address.
"""

import subprocess
import sys
import time
import platform
import os
import random
import socket
from datetime import datetime

# Auto-install required packages
required_packages = ['requests', 'stem', 'PySocks']
for package in required_packages:
    try:
        __import__(package if package != 'PySocks' else 'socks')
    except ImportError:
        print(f"[*] Installing {package}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--break-system-packages'], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import requests
import socks
import socket as sock
try:
    from stem import Signal
    from stem.control import Controller
    STEM_AVAILABLE = True
except:
    STEM_AVAILABLE = False

# Color codes for professional terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[35m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'

def print_banner():
    """Display professional banner"""
    banner = f"""{Colors.CYAN}{Colors.BOLD}
    ============================================================
    
         IP CHANGER - Advanced Network Identity Tool
    
         GitHub: https://github.com/00xk/IP-Changer
         Author: 00xk
         Version: 6.0 FINAL
    
    ============================================================
    {Colors.END}"""
    print(banner)

def print_skull():
    """Display skull ASCII art"""
    skull = f"""{Colors.GRAY}
                       _,.-------.,_
                   ,;~'             '~;,
                 ,;                     ;,
                ;                         ;
               ,'                         ',
              ,;                           ;,
              ; ;      .           .      ; ;
              | ;   ______       ______   ; |
              |  `/~"     ~" . "~     "~\'  |
              |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
               |   |        :::       |   |
               |   l       / | \\       !   |
               .~  (__,.--" .^. "--.,__)  ~.
               |     ---;' / | \\ `;---     |
                \\__.       \\/^\\/       .__/
             V| \\                   / |V
              | |T~\\___!___!___!___/~T| |
              | |`IIII_I_I_I_I_IIII'| |
              |  \\,III I I I I III,/  |
               \\   `~~~~~~~~~~'    /
                 \\   .       .   /
                   `;         ;'
                     '~,___,~'
    {Colors.END}"""
    print(skull)

def log(message, level="INFO"):
    """Professional logging function"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    colors = {
        "INFO": Colors.CYAN,
        "SUCCESS": Colors.GREEN,
        "WARNING": Colors.YELLOW,
        "ERROR": Colors.RED,
        "SYSTEM": Colors.PURPLE
    }
    color = colors.get(level, Colors.WHITE)
    print(f"{Colors.GRAY}[{timestamp}]{Colors.END} {color}[{level}]{Colors.END} {message}")

def check_root():
    """Check if running as root"""
    if os.geteuid() != 0:
        log("Running without root privileges - some features may be limited", "WARNING")
        log("For full functionality, run with: sudo python3 ip_changer.py", "WARNING")
        return False
    return True

def get_public_ip(use_proxy=None):
    """Get public IP address from multiple reliable sources"""
    apis = [
        'https://api.ipify.org?format=json',
        'https://ifconfig.me/ip',
        'https://icanhazip.com',
        'https://ident.me',
        'https://ipecho.net/plain',
        'https://myexternalip.com/raw'
    ]
    
    session = requests.Session()
    if use_proxy:
        session.proxies = {
            'http': use_proxy,
            'https': use_proxy
        }
    
    for api in apis:
        try:
            response = session.get(api, timeout=10)
            if response.status_code == 200:
                ip_text = response.text.strip()
                # Extract IP from JSON if needed
                if 'ip' in ip_text:
                    import json
                    ip_text = json.loads(ip_text)['ip']
                # Validate IP format
                parts = ip_text.split('.')
                if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
                    return ip_text
        except:
            continue
    return None

def get_interface():
    """Get default network interface"""
    try:
        result = subprocess.run(['ip', 'route'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'default' in line:
                parts = line.split()
                if 'dev' in parts:
                    idx = parts.index('dev')
                    return parts[idx + 1]
    except:
        pass
    return None

def generate_random_mac():
    """Generate random valid MAC address"""
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

def run_command(cmd, silent=True):
    """Run shell command with error handling"""
    try:
        if silent:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(cmd, check=True)
        return True
    except:
        return False

def check_tor_status():
    """Check if TOR is installed and running"""
    tor_installed = run_command(['which', 'tor'])
    if not tor_installed:
        return "NOT_INSTALLED"
    
    tor_running = run_command(['systemctl', 'is-active', 'tor'])
    if tor_running:
        return "RUNNING"
    
    return "INSTALLED"

def install_tor():
    """Install TOR service"""
    log("Attempting to install TOR...", "SYSTEM")
    
    # Try different package managers
    package_managers = [
        (['apt-get', 'update'], ['apt-get', 'install', '-y', 'tor']),
        (None, ['yum', 'install', '-y', 'tor']),
        (None, ['dnf', 'install', '-y', 'tor']),
        (None, ['pacman', '-S', '--noconfirm', 'tor']),
        (None, ['zypper', 'install', '-y', 'tor']),
    ]
    
    for update_cmd, install_cmd in package_managers:
        if update_cmd:
            run_command(update_cmd)
        
        if run_command(install_cmd):
            log("TOR installed successfully", "SUCCESS")
            return True
    
    log("Failed to install TOR automatically", "ERROR")
    log("Please install manually: sudo apt install tor", "WARNING")
    return False

def start_tor_service():
    """Start TOR service"""
    log("Starting TOR service...", "SYSTEM")
    
    # Try systemctl first
    if run_command(['systemctl', 'start', 'tor']):
        time.sleep(5)
        if run_command(['systemctl', 'is-active', 'tor']):
            log("TOR service started successfully", "SUCCESS")
            return True
    
    # Try service command
    if run_command(['service', 'tor', 'start']):
        time.sleep(5)
        log("TOR service started successfully", "SUCCESS")
        return True
    
    # Try running tor directly
    if run_command(['tor', '--runasdaemon', '1', '--quiet']):
        time.sleep(5)
        log("TOR daemon started successfully", "SUCCESS")
        return True
    
    log("Failed to start TOR service", "ERROR")
    return False

def get_new_tor_identity():
    """Request new TOR identity to change IP"""
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            log("Requested new TOR circuit", "SUCCESS")
            time.sleep(5)
            return True
    except:
        # Fallback: restart TOR
        log("Using TOR restart method...", "SYSTEM")
        if run_command(['systemctl', 'restart', 'tor']):
            time.sleep(8)
            return True
        elif run_command(['service', 'tor', 'restart']):
            time.sleep(8)
            return True
    return False

def verify_tor_connection():
    """Verify that TOR is working"""
    try:
        # Check TOR port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('127.0.0.1', 9050))
        sock.close()
        return result == 0
    except:
        return False

def setup_tor_method():
    """Setup TOR for IP changing"""
    log("Initializing TOR method...", "SYSTEM")
    
    # Check TOR status
    status = check_tor_status()
    
    if status == "NOT_INSTALLED":
        log("TOR is not installed", "WARNING")
        if not install_tor():
            return False
    
    if status != "RUNNING":
        if not start_tor_service():
            return False
    
    # Verify TOR is accessible
    if not verify_tor_connection():
        log("TOR service is not accessible on port 9050", "ERROR")
        return False
    
    log("TOR setup complete", "SUCCESS")
    return True

def change_ip_via_tor():
    """Change IP using TOR network"""
    log("Changing IP via TOR network...", "SYSTEM")
    
    # Setup TOR if needed
    if not setup_tor_method():
        return False, None, None
    
    # Get current IP through TOR
    tor_proxy = 'socks5h://127.0.0.1:9050'
    old_ip = get_public_ip(use_proxy=tor_proxy)
    
    if not old_ip:
        log("Failed to get current TOR IP", "ERROR")
        return False, None, None
    
    log(f"Current TOR IP: {old_ip}", "INFO")
    
    # Request new identity
    if not get_new_tor_identity():
        log("Failed to request new TOR identity", "ERROR")
        return False, old_ip, None
    
    # Get new IP
    log("Verifying new IP address...", "SYSTEM")
    time.sleep(3)
    new_ip = get_public_ip(use_proxy=tor_proxy)
    
    if not new_ip:
        log("Failed to verify new IP", "ERROR")
        return False, old_ip, None
    
    # Check if IP actually changed
    if old_ip != new_ip:
        log(f"IP successfully changed: {old_ip} -> {new_ip}", "SUCCESS")
        return True, old_ip, new_ip
    else:
        log("IP did not change, retrying...", "WARNING")
        # Retry once more
        get_new_tor_identity()
        time.sleep(5)
        new_ip = get_public_ip(use_proxy=tor_proxy)
        
        if old_ip != new_ip:
            log(f"IP changed on retry: {old_ip} -> {new_ip}", "SUCCESS")
            return True, old_ip, new_ip
        else:
            log("IP still did not change", "ERROR")
            return False, old_ip, new_ip

def method_mac_spoof(interface):
    """Spoof MAC address to potentially trigger new DHCP lease"""
    if not interface:
        return False
    
    log(f"Spoofing MAC address on {interface}...", "SYSTEM")
    new_mac = generate_random_mac()
    
    success = False
    
    # Try macchanger if available
    if run_command(['which', 'macchanger']):
        if run_command(['macchanger', '-r', interface]):
            log(f"MAC changed using macchanger", "SUCCESS")
            success = True
    
    # Manual method
    if not success:
        if run_command(['ip', 'link', 'set', interface, 'down']):
            if run_command(['ip', 'link', 'set', interface, 'address', new_mac]):
                if run_command(['ip', 'link', 'set', interface, 'up']):
                    log(f"MAC changed to {new_mac}", "SUCCESS")
                    success = True
    
    if not success:
        log("MAC spoofing failed (requires root)", "WARNING")
    
    return success

def method_network_reset(interface):
    """Reset network to request new DHCP lease"""
    if not interface:
        return False
    
    log("Performing network reset...", "SYSTEM")
    
    # Kill existing DHCP clients
    run_command(['killall', 'dhclient'])
    time.sleep(1)
    
    # Release and renew
    success = False
    if run_command(['dhclient', '-r', interface]):
        time.sleep(2)
        run_command(['ip', 'addr', 'flush', 'dev', interface])
        run_command(['ip', 'link', 'set', interface, 'down'])
        time.sleep(2)
        run_command(['ip', 'link', 'set', interface, 'up'])
        time.sleep(2)
        if run_command(['dhclient', interface]):
            log("Network reset complete", "SUCCESS")
            success = True
    
    # Try NetworkManager
    if run_command(['systemctl', 'restart', 'NetworkManager']):
        time.sleep(5)
        log("NetworkManager restarted", "SUCCESS")
        success = True
    
    return success

def change_ip_complete():
    """Complete IP change using all available methods"""
    print("\n" + "="*60)
    log("INITIATING IP CHANGE SEQUENCE", "SYSTEM")
    print("="*60 + "\n")
    
    # Get interface
    interface = get_interface()
    if interface:
        log(f"Network interface: {interface}", "INFO")
    
    # Get initial IP (direct connection)
    log("Checking initial public IP...", "INFO")
    initial_direct_ip = get_public_ip()
    if initial_direct_ip:
        log(f"Current direct IP: {initial_direct_ip}", "INFO")
    
    # Apply network-level changes if root
    if os.geteuid() == 0 and interface:
        log("Applying network-level changes...", "SYSTEM")
        method_mac_spoof(interface)
        time.sleep(2)
        method_network_reset(interface)
        time.sleep(3)
    
    # Primary method: TOR
    success, old_ip, new_ip = change_ip_via_tor()
    
    print("\n" + "="*60)
    log("IP CHANGE RESULTS", "SYSTEM")
    print("="*60)
    
    if success and old_ip and new_ip:
        log(f"OLD IP: {old_ip}", "INFO")
        log(f"NEW IP: {new_ip}", "SUCCESS")
        log("STATUS: IP SUCCESSFULLY CHANGED", "SUCCESS")
        log("METHOD: TOR Network", "INFO")
        log("Your traffic is now routed through TOR", "INFO")
        return True, old_ip, new_ip
    else:
        log("STATUS: IP CHANGE FAILED", "ERROR")
        log("Possible reasons:", "WARNING")
        log("  1. TOR service not running properly", "WARNING")
        log("  2. Network connectivity issues", "WARNING")
        log("  3. TOR ports blocked by firewall", "WARNING")
        log("\nTroubleshooting steps:", "INFO")
        log("  1. Check TOR: sudo systemctl status tor", "INFO")
        log("  2. Restart TOR: sudo systemctl restart tor", "INFO")
        log("  3. Check logs: sudo journalctl -u tor -n 50", "INFO")
        return False, old_ip if old_ip else "Unknown", new_ip if new_ip else "Unknown"

def print_stats(successful, failed, start_time, ip_history):
    """Print session statistics"""
    runtime = time.time() - start_time
    hours, remainder = divmod(int(runtime), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print("\n" + "="*60)
    print(f"{Colors.BOLD}SESSION STATISTICS{Colors.END}")
    print("="*60)
    print(f"Successful changes: {Colors.GREEN}{successful}{Colors.END}")
    print(f"Failed attempts: {Colors.RED}{failed}{Colors.END}")
    print(f"Total runtime: {hours:02d}:{minutes:02d}:{seconds:02d}")
    print("\nIP Change History:")
    print("-"*60)
    
    for old_ip, new_ip, timestamp in ip_history[-10:]:
        if old_ip != new_ip:
            status = f"{Colors.GREEN}SUCCESS{Colors.END}"
        else:
            status = f"{Colors.YELLOW}NO CHANGE{Colors.END}"
        print(f"[{timestamp}] {status} | {old_ip} -> {new_ip}")
    
    print("="*60 + "\n")

def check_for_updates():
    """Check for updates from GitHub"""
    log("Checking for updates...", "SYSTEM")
    try:
        response = requests.get('https://api.github.com/repos/00xk/IP-Changer/releases/latest', timeout=5)
        if response.status_code == 200:
            latest_version = response.json().get('tag_name', 'unknown')
            log(f"Latest version on GitHub: {latest_version}", "INFO")
            log("To update, run: git pull origin main", "INFO")
    except:
        log("Could not check for updates", "WARNING")

def main():
    """Main program loop"""
    # Check root
    is_root = check_root()
    
    # Display banner
    print_banner()
    print_skull()
    
    # Check for updates
    check_for_updates()
    
    # System info
    print("\n" + "="*60)
    log("SYSTEM INFORMATION", "SYSTEM")
    print("="*60)
    log(f"Platform: Linux", "INFO")
    log(f"Root access: {'Yes' if is_root else 'No (limited features)'}", "INFO")
    
    interface = get_interface()
    if interface:
        log(f"Network interface: {interface}", "INFO")
    
    direct_ip = get_public_ip()
    if direct_ip:
        log(f"Current public IP: {direct_ip}", "INFO")
    
    print("="*60)
    
    # Configuration
    print(f"\n{Colors.BOLD}CONFIGURATION{Colors.END}")
    try:
        interval_input = input(f"{Colors.CYAN}[?]{Colors.END} Enter rotation interval in seconds (default: 10): ").strip()
        interval = int(interval_input) if interval_input else 10
        if interval < 5:
            log("Minimum interval is 5 seconds", "WARNING")
            interval = 5
    except:
        interval = 10
        log("Using default interval: 10 seconds", "INFO")
    
    log(f"IP rotation interval set to {interval} seconds", "SUCCESS")
    log("Press Ctrl+C to stop", "INFO")
    
    # Main loop
    successful = 0
    failed = 0
    start_time = time.time()
    ip_history = []
    
    try:
        while True:
            result, old_ip, new_ip = change_ip_complete()
            
            timestamp = datetime.now().strftime('%H:%M:%S')
            ip_history.append((old_ip, new_ip, timestamp))
            
            if result:
                successful += 1
            else:
                failed += 1
            
            log(f"Next rotation in {interval} seconds...", "INFO")
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n")
        log("Stopping IP rotation service...", "WARNING")
        print_stats(successful, failed, start_time, ip_history)
        log("Session terminated", "SYSTEM")
        log("GitHub: https://github.com/00xk/IP-Changer", "INFO")

if __name__ == "__main__":
    if platform.system() != "Linux":
        print("ERROR: This tool is designed for Linux only")
        sys.exit(1)
    
    try:
        main()
    except Exception as e:
        print(f"\nFATAL ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
