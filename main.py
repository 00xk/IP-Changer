#!/usr/bin/env python3
"""
IP CHANGER - Professional Network Tool
GitHub: https://github.com/00xk/IP-Changer
Author: 00xk
Version: 7.0 OPTIMIZED

Fast and reliable IP changing using TOR network.
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
try:
    from stem import Signal
    from stem.control import Controller
    STEM_AVAILABLE = True
except:
    STEM_AVAILABLE = False

# Color codes
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    PURPLE = '\033[35m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    """Display clean professional banner"""
    banner = f"""{Colors.CYAN}{Colors.BOLD}
    ================================================================
    
                      IP CHANGER v7.0 OPTIMIZED
    
              Fast, Reliable IP Rotation via TOR Network
    
                 GitHub: github.com/00xk/IP-Changer
                        Author: 00xk
    
    ================================================================
    {Colors.END}"""
    print(banner)

def log(message, level="INFO"):
    """Professional logging"""
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

def run_command(cmd, silent=True):
    """Run command silently"""
    try:
        if silent:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
        else:
            subprocess.run(cmd, check=True, timeout=10)
        return True
    except:
        return False

def get_public_ip(timeout=5):
    """Get public IP quickly"""
    apis = [
        'https://api.ipify.org',
        'https://icanhazip.com',
        'https://ifconfig.me/ip'
    ]
    
    for api in apis:
        try:
            response = requests.get(api, timeout=timeout)
            if response.status_code == 200:
                ip = response.text.strip()
                if '.' in ip and len(ip) < 20:
                    return ip
        except:
            continue
    return None

def get_tor_ip(max_retries=3):
    """Get IP through TOR with retries"""
    tor_proxy = 'socks5h://127.0.0.1:9050'
    
    for attempt in range(max_retries):
        try:
            session = requests.Session()
            session.proxies = {
                'http': tor_proxy,
                'https': tor_proxy
            }
            response = session.get('https://check.torproject.org/api/ip', timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('IsTor'):
                    return data.get('IP')
        except:
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
    return None

def check_tor_running():
    """Quick check if TOR is running"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', 9050))
        sock.close()
        return result == 0
    except:
        return False

def install_tor():
    """Install TOR quickly"""
    log("Installing TOR service...", "SYSTEM")
    
    # Try apt-get first (most common)
    if run_command(['apt-get', 'update']):
        if run_command(['apt-get', 'install', '-y', 'tor']):
            log("TOR installed successfully", "SUCCESS")
            return True
    
    # Try other package managers
    for cmd in [['yum', 'install', '-y', 'tor'], 
                ['dnf', 'install', '-y', 'tor'],
                ['pacman', '-S', '--noconfirm', 'tor']]:
        if run_command(cmd):
            log("TOR installed successfully", "SUCCESS")
            return True
    
    log("Failed to install TOR. Please install manually: sudo apt install tor", "ERROR")
    return False

def start_tor():
    """Start TOR service quickly"""
    log("Starting TOR service...", "SYSTEM")
    
    # Try systemctl
    if run_command(['systemctl', 'start', 'tor']):
        time.sleep(3)
        if check_tor_running():
            log("TOR service started", "SUCCESS")
            return True
    
    # Try service command
    if run_command(['service', 'tor', 'start']):
        time.sleep(3)
        if check_tor_running():
            log("TOR service started", "SUCCESS")
            return True
    
    log("Failed to start TOR service", "ERROR")
    return False

def setup_tor():
    """Setup TOR if not running"""
    if check_tor_running():
        log("TOR is already running", "SUCCESS")
        return True
    
    # Check if installed
    if not run_command(['which', 'tor']):
        if not install_tor():
            return False
    
    # Start service
    return start_tor()

def change_tor_ip():
    """Change TOR IP by requesting new circuit"""
    try:
        # Try using stem control
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            time.sleep(3)
            return True
    except:
        # Fallback: restart TOR
        if run_command(['systemctl', 'restart', 'tor']):
            time.sleep(5)
            return True
        elif run_command(['service', 'tor', 'restart']):
            time.sleep(5)
            return True
    return False

def perform_ip_change():
    """Main IP change function - optimized"""
    print("\n" + "="*60)
    log("STARTING IP CHANGE", "SYSTEM")
    print("="*60 + "\n")
    
    # Setup TOR if needed
    if not setup_tor():
        log("TOR setup failed. Cannot change IP.", "ERROR")
        return False, None, None
    
    # Get current TOR IP
    log("Getting current TOR IP...", "INFO")
    old_ip = get_tor_ip()
    
    if not old_ip:
        log("Cannot connect to TOR network", "ERROR")
        log("Try: sudo systemctl restart tor", "WARNING")
        return False, None, None
    
    log(f"Current IP: {old_ip}", "INFO")
    
    # Request new circuit
    log("Requesting new TOR circuit...", "SYSTEM")
    if not change_tor_ip():
        log("Failed to change TOR circuit", "ERROR")
        return False, old_ip, None
    
    # Get new IP
    log("Verifying new IP...", "SYSTEM")
    new_ip = get_tor_ip()
    
    if not new_ip:
        log("Failed to verify new IP", "ERROR")
        return False, old_ip, None
    
    # Check if changed
    print("\n" + "="*60)
    log("RESULTS", "SYSTEM")
    print("="*60)
    
    if old_ip != new_ip:
        log(f"Old IP: {old_ip}", "INFO")
        log(f"New IP: {new_ip}", "SUCCESS")
        log("IP SUCCESSFULLY CHANGED", "SUCCESS")
        return True, old_ip, new_ip
    else:
        log(f"IP: {old_ip}", "WARNING")
        log("IP DID NOT CHANGE - Retrying in next cycle", "WARNING")
        return False, old_ip, new_ip

def check_for_updates():
    """Check GitHub for updates"""
    try:
        response = requests.get('https://api.github.com/repos/00xk/IP-Changer/commits/main', timeout=5)
        if response.status_code == 200:
            commit = response.json()
            log(f"Latest commit: {commit['commit']['message'][:50]}", "INFO")
            return True
    except:
        pass
    return False

def update_tool():
    """Update from GitHub"""
    log("Updating from GitHub...", "SYSTEM")
    
    if run_command(['git', 'pull', 'origin', 'main'], silent=False):
        log("Update successful!", "SUCCESS")
        log("Please restart the script", "INFO")
        return True
    else:
        log("Update failed. Make sure you cloned the repo with git.", "ERROR")
        log("Manual update:", "INFO")
        print("  1. cd IP-Changer")
        print("  2. git pull origin main")
        return False

def show_menu():
    """Display main menu"""
    clear_screen()
    print_banner()
    print(f"\n{Colors.BOLD}MAIN MENU{Colors.END}\n")
    print(f"  {Colors.CYAN}[1]{Colors.END} Start IP Changer")
    print(f"  {Colors.YELLOW}[2]{Colors.END} Update from GitHub")
    print(f"  {Colors.RED}[3]{Colors.END} Exit")
    print()

def run_ip_changer():
    """Run the IP changer main loop"""
    clear_screen()
    print_banner()
    
    # Check root
    if os.geteuid() != 0:
        log("Running without root - this is OK for TOR method", "WARNING")
    
    # System info
    print("\n" + "="*60)
    log("SYSTEM CHECK", "SYSTEM")
    print("="*60)
    
    direct_ip = get_public_ip()
    if direct_ip:
        log(f"Your direct IP: {direct_ip}", "INFO")
    
    # Check TOR
    if check_tor_running():
        log("TOR is running", "SUCCESS")
    else:
        log("TOR is not running - will attempt to start", "WARNING")
    
    print("="*60)
    
    # Configuration
    print(f"\n{Colors.BOLD}CONFIGURATION{Colors.END}")
    try:
        interval = input(f"{Colors.CYAN}[?]{Colors.END} Rotation interval in seconds (default: 10): ").strip()
        interval = int(interval) if interval else 10
        if interval < 5:
            log("Using minimum interval: 5 seconds", "WARNING")
            interval = 5
    except:
        interval = 10
    
    log(f"Interval set to {interval} seconds", "SUCCESS")
    log("Press Ctrl+C to stop and return to menu", "INFO")
    
    # Main loop
    successful = 0
    failed = 0
    start_time = time.time()
    ip_history = []
    
    try:
        while True:
            result, old_ip, new_ip = perform_ip_change()
            
            timestamp = datetime.now().strftime('%H:%M:%S')
            if old_ip and new_ip:
                ip_history.append((old_ip, new_ip, timestamp))
            
            if result:
                successful += 1
            else:
                failed += 1
            
            log(f"Stats: {successful} success, {failed} failed", "INFO")
            log(f"Next change in {interval} seconds...", "INFO")
            
            for remaining in range(interval, 0, -1):
                print(f"\r{Colors.GRAY}[WAIT]{Colors.END} {remaining}s ", end='', flush=True)
                time.sleep(1)
            print()
            
    except KeyboardInterrupt:
        # Show statistics
        runtime = time.time() - start_time
        hours, remainder = divmod(int(runtime), 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print("\n\n" + "="*60)
        print(f"{Colors.BOLD}SESSION STATISTICS{Colors.END}")
        print("="*60)
        print(f"Successful changes: {Colors.GREEN}{successful}{Colors.END}")
        print(f"Failed attempts: {Colors.RED}{failed}{Colors.END}")
        print(f"Runtime: {hours:02d}:{minutes:02d}:{seconds:02d}")
        
        if ip_history:
            print(f"\nLast 5 IP changes:")
            print("-"*60)
            for old_ip, new_ip, ts in ip_history[-5:]:
                status = f"{Colors.GREEN}OK{Colors.END}" if old_ip != new_ip else f"{Colors.YELLOW}SAME{Colors.END}"
                print(f"[{ts}] {status} | {old_ip} -> {new_ip}")
        
        print("="*60)
        input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.END}")

def main():
    """Main program with menu"""
    if platform.system() != "Linux":
        print("ERROR: This tool is for Linux only")
        sys.exit(1)
    
    while True:
        show_menu()
        
        try:
            choice = input(f"{Colors.CYAN}[?]{Colors.END} Select option: ").strip()
            
            if choice == "1":
                run_ip_changer()
            
            elif choice == "2":
                clear_screen()
                print_banner()
                print()
                check_for_updates()
                update_tool()
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
            
            elif choice == "3":
                clear_screen()
                log("Exiting IP Changer", "SYSTEM")
                log("GitHub: https://github.com/00xk/IP-Changer", "INFO")
                print()
                sys.exit(0)
            
            else:
                log("Invalid option. Please select 1, 2, or 3.", "ERROR")
                time.sleep(2)
        
        except KeyboardInterrupt:
            print()
            sys.exit(0)
        except Exception as e:
            log(f"Error: {str(e)}", "ERROR")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nFATAL ERROR: {str(e)}")
        sys.exit(1)
