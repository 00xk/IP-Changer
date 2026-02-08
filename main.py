#!/usr/bin/env python3
"""
Advanced IP Address Rotator - AUTO-INSTALL VERSION
Automatically installs required packages
"""

import subprocess
import sys
import time
import platform
import os
from datetime import datetime

# Auto-install requests if missing
try:
    import requests
except ImportError:
    print("📦 Installing required package 'requests'...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    import requests

# Color codes for terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    GREEN = '\033[92m'

def print_skull():
    """Display ASCII skull art"""
    skull = f"""
{Colors.RED}                    {Colors.BOLD}
                   .--.
                  /.-. '----------.
                  \'-' .--"--""-"-'
                   '--'
                      
            {Colors.WHITE}       .---.
            {Colors.WHITE}      /. ./|
            {Colors.WHITE}      '. '\" |  {Colors.RED}uuuu {Colors.YELLOW}_____{Colors.RED} uuuu
            {Colors.WHITE}       '---'  {Colors.RED}u\" u \"{Colors.YELLOW}|   |{Colors.RED}u\" u\"
            {Colors.WHITE}       .---.  {Colors.RED} >u<  {Colors.YELLOW}|   |{Colors.RED} >u<
            {Colors.WHITE}      /. ./|  {Colors.RED}u\" u \"{Colors.YELLOW}|   |{Colors.RED}u\" u\"
            {Colors.WHITE}      '. '\" |  {Colors.RED} >u<  {Colors.YELLOW}|___|{Colors.RED} >u<
            {Colors.WHITE}       '---'  {Colors.RED}u\" u \"{Colors.YELLOW} |_| {Colors.RED}u\" u\"
            {Colors.WHITE}              {Colors.RED} >u<   {Colors.YELLOW}'-'{Colors.RED}  >u<
            {Colors.WHITE}              {Colors.RED}u\" u\"      u\" u\"
{Colors.ENDC}"""
    print(skull)

def print_banner():
    """Display colorful ASCII art banner"""
    banner = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║ {Colors.BOLD}{Colors.PURPLE}██╗██████╗      ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗{Colors.ENDC}{Colors.CYAN}  ║
║ {Colors.BOLD}{Colors.PURPLE}██║██╔══██╗    ██╔════╝ ██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗{Colors.ENDC}{Colors.CYAN} ║
║ {Colors.BOLD}{Colors.PURPLE}██║██████╔╝    ██║      ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝{Colors.ENDC}{Colors.CYAN} ║
║ {Colors.BOLD}{Colors.PURPLE}██║██╔═══╝     ██║      ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗{Colors.ENDC}{Colors.CYAN} ║
║ {Colors.BOLD}{Colors.PURPLE}██║██║         ╚██████╗ ██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║{Colors.ENDC}{Colors.CYAN} ║
║ {Colors.BOLD}{Colors.PURPLE}╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝{Colors.ENDC}{Colors.CYAN} ║
║                                                                       ║
║            {Colors.YELLOW}⚡ Advanced IP Address Rotator v3.0 EXTREME ⚡{Colors.ENDC}{Colors.CYAN}            ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝{Colors.ENDC}
"""
    print(banner)
    print_skull()

def print_colored(message, color=Colors.WHITE, end='\n'):
    """Print colored message"""
    print(f"{color}{message}{Colors.ENDC}", end=end)

def get_public_ip():
    """Get public IP address from external API"""
    apis = [
        'https://api.ipify.org',
        'https://icanhazip.com',
        'https://ipinfo.io/ip',
        'https://ident.me',
        'https://checkip.amazonaws.com'
    ]
    
    for api in apis:
        try:
            response = requests.get(api, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            continue
    return "Unable to fetch"

def get_local_ip():
    """Get local IP address"""
    try:
        if platform.system() == "Linux":
            result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
            ip = result.stdout.split()[0]
        elif platform.system() == "Windows":
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if 'IPv4' in line:
                    ip = line.split(':')[1].strip()
                    break
            else:
                ip = "Unknown"
        else:
            ip = "Unknown"
        return ip
    except:
        return "Unknown"

def change_ip_linux():
    """Change IP on Linux using multiple methods"""
    try:
        print_colored("\n┌──────────────────────────────────────────────┐", Colors.CYAN)
        print_colored("│  💀 INITIATING IP ROTATION (Linux)...       │", Colors.CYAN)
        print_colored("└──────────────────────────────────────────────┘", Colors.CYAN)
        
        # Get the default network interface
        result = subprocess.run(['ip', 'route'], capture_output=True, text=True)
        interface = result.stdout.split()[4]
        
        old_public_ip = get_public_ip()
        old_local_ip = get_local_ip()
        
        print_colored(f"   📡 Interface: {interface}", Colors.OKCYAN)
        print_colored(f"   📍 Old Public IP: {old_public_ip}", Colors.WARNING)
        print_colored(f"   🏠 Old Local IP: {old_local_ip}", Colors.WARNING)
        
        # Method 1: Release DHCP lease
        print_colored("   ⚡ Method 1: Releasing DHCP lease...", Colors.YELLOW)
        subprocess.run(['sudo', 'dhclient', '-r', interface], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(2)
        
        # Method 2: Bring interface down
        print_colored("   ⚡ Method 2: Shutting down interface...", Colors.YELLOW)
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], 
                      check=True, stderr=subprocess.DEVNULL)
        time.sleep(3)
        
        # Method 3: Bring interface up
        print_colored("   ⚡ Method 3: Bringing interface back up...", Colors.YELLOW)
        subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], 
                      check=True, stderr=subprocess.DEVNULL)
        time.sleep(2)
        
        # Method 4: Request new DHCP lease
        print_colored("   ⚡ Method 4: Requesting new DHCP lease...", Colors.YELLOW)
        subprocess.run(['sudo', 'dhclient', interface], 
                      check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        
        # Method 5: Flush DNS and renew
        print_colored("   ⚡ Method 5: Flushing DNS cache...", Colors.YELLOW)
        subprocess.run(['sudo', 'systemd-resolve', '--flush-caches'], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        
        time.sleep(3)
        
        new_public_ip = get_public_ip()
        new_local_ip = get_local_ip()
        
        print_colored("\n   ═══════════════════════════════════════════", Colors.GREEN)
        print_colored(f"   ✅ New Public IP: {new_public_ip}", Colors.OKGREEN)
        print_colored(f"   🏠 New Local IP: {new_local_ip}", Colors.OKGREEN)
        print_colored(f"   🕐 Changed at: {datetime.now().strftime('%H:%M:%S')}", Colors.OKBLUE)
        print_colored("   ═══════════════════════════════════════════", Colors.GREEN)
        
        if old_public_ip != new_public_ip:
            print_colored(f"   💀 PUBLIC IP SUCCESSFULLY CHANGED! 💀", Colors.BOLD + Colors.GREEN)
            return True, old_public_ip, new_public_ip
        else:
            print_colored(f"   ⚠️  WARNING: Public IP didn't change", Colors.WARNING)
            print_colored(f"   ℹ️  Your ISP may not assign new IPs on reconnect", Colors.WARNING)
            print_colored(f"   💡 Consider using a VPN for true IP rotation", Colors.CYAN)
            return False, old_public_ip, new_public_ip
            
    except subprocess.CalledProcessError as e:
        print_colored(f"   ❌ Error: Failed to change IP", Colors.FAIL)
        print_colored(f"   ℹ️  Make sure you run with 'sudo'", Colors.WARNING)
        return False, "Error", "Error"
    except Exception as e:
        print_colored(f"   ❌ Error: {str(e)}", Colors.FAIL)
        return False, "Error", "Error"

def change_ip_windows():
    """Change IP on Windows using multiple methods"""
    try:
        print_colored("\n┌──────────────────────────────────────────────┐", Colors.CYAN)
        print_colored("│  💀 INITIATING IP ROTATION (Windows)...     │", Colors.CYAN)
        print_colored("└──────────────────────────────────────────────┘", Colors.CYAN)
        
        old_public_ip = get_public_ip()
        old_local_ip = get_local_ip()
        
        print_colored(f"   📍 Old Public IP: {old_public_ip}", Colors.WARNING)
        print_colored(f"   🏠 Old Local IP: {old_local_ip}", Colors.WARNING)
        
        # Method 1: Release IP
        print_colored("   ⚡ Method 1: Releasing IP address...", Colors.YELLOW)
        subprocess.run(['ipconfig', '/release'], 
                      check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
        
        # Method 2: Flush DNS
        print_colored("   ⚡ Method 2: Flushing DNS cache...", Colors.YELLOW)
        subprocess.run(['ipconfig', '/flushdns'], 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)
        
        # Method 3: Renew IP
        print_colored("   ⚡ Method 3: Renewing IP address...", Colors.YELLOW)
        subprocess.run(['ipconfig', '/renew'], 
                      check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)
        
        # Method 4: Reset Winsock
        print_colored("   ⚡ Method 4: Resetting network stack...", Colors.YELLOW)
        subprocess.run(['netsh', 'winsock', 'reset'], 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        time.sleep(2)
        
        new_public_ip = get_public_ip()
        new_local_ip = get_local_ip()
        
        print_colored("\n   ═══════════════════════════════════════════", Colors.GREEN)
        print_colored(f"   ✅ New Public IP: {new_public_ip}", Colors.OKGREEN)
        print_colored(f"   🏠 New Local IP: {new_local_ip}", Colors.OKGREEN)
        print_colored(f"   🕐 Changed at: {datetime.now().strftime('%H:%M:%S')}", Colors.OKBLUE)
        print_colored("   ═══════════════════════════════════════════", Colors.GREEN)
        
        if old_public_ip != new_public_ip:
            print_colored(f"   💀 PUBLIC IP SUCCESSFULLY CHANGED! 💀", Colors.BOLD + Colors.GREEN)
            return True, old_public_ip, new_public_ip
        else:
            print_colored(f"   ⚠️  WARNING: Public IP didn't change", Colors.WARNING)
            print_colored(f"   ℹ️  Your ISP may not assign new IPs on reconnect", Colors.WARNING)
            print_colored(f"   💡 Consider using a VPN for true IP rotation", Colors.CYAN)
            return False, old_public_ip, new_public_ip
            
    except subprocess.CalledProcessError:
        print_colored(f"   ❌ Error: Failed to change IP", Colors.FAIL)
        print_colored(f"   ℹ️  Make sure you run as Administrator", Colors.WARNING)
        return False, "Error", "Error"
    except Exception as e:
        print_colored(f"   ❌ Error: {str(e)}", Colors.FAIL)
        return False, "Error", "Error"

def print_stats(successful, failed, start_time, ip_history):
    """Print statistics"""
    runtime = time.time() - start_time
    hours, remainder = divmod(int(runtime), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print_colored("\n" + "💀" * 35, Colors.RED)
    print_colored("\n┌──────────────────────────────────────────────┐", Colors.PURPLE)
    print_colored("│           💀 SESSION STATS 💀                │", Colors.PURPLE)
    print_colored("├──────────────────────────────────────────────┤", Colors.PURPLE)
    print_colored(f"│  ✅ Successful IP changes: {successful:<16} │", Colors.OKGREEN)
    print_colored(f"│  ❌ Failed attempts: {failed:<23} │", Colors.FAIL)
    print_colored(f"│  ⏱️  Runtime: {hours:02d}:{minutes:02d}:{seconds:02d}                       │", Colors.OKCYAN)
    print_colored("├──────────────────────────────────────────────┤", Colors.PURPLE)
    print_colored("│  📜 IP CHANGE HISTORY:                       │", Colors.YELLOW)
    
    for i, (old_ip, new_ip, timestamp) in enumerate(ip_history[-5:], 1):
        if old_ip != new_ip:
            status = "✅"
            color = Colors.OKGREEN
        else:
            status = "⚠️ "
            color = Colors.WARNING
        print_colored(f"│  {status} {timestamp} │ {old_ip[:15]:<15} → {new_ip[:15]:<15} │", color)
    
    print_colored("└──────────────────────────────────────────────┘", Colors.PURPLE)
    print_colored("\n" + "💀" * 35, Colors.RED)

def main():
    """Main function"""
    print_banner()
    
    system = platform.system()
    
    # Get initial IPs
    print_colored("🔍 Fetching current IP information...", Colors.CYAN)
    current_public_ip = get_public_ip()
    current_local_ip = get_local_ip()
    
    # System information
    print_colored("\n╔════════════════════════════════════════════════════════════════════╗", Colors.CYAN)
    print_colored(f"║  💻 System: {system:<56} ║", Colors.CYAN)
    print_colored(f"║  🌍 Current Public IP: {current_public_ip:<43} ║", Colors.CYAN)
    print_colored(f"║  🏠 Current Local IP: {current_local_ip:<44} ║", Colors.CYAN)
    print_colored("╚════════════════════════════════════════════════════════════════════╝", Colors.CYAN)
    
    if system not in ["Linux", "Windows"]:
        print_colored("\n❌ Unsupported operating system!", Colors.FAIL)
        return
    
    # Get interval from user
    print_colored("\n⚙️  Configuration", Colors.YELLOW, end='')
    print_colored(" (Press Ctrl+C to stop at any time)", Colors.WARNING)
    
    try:
        interval = input(f"\n{Colors.OKCYAN}⏱️  Enter interval in seconds (default: 5): {Colors.ENDC}").strip()
        interval = int(interval) if interval else 5
        
        if interval < 1:
            print_colored("⚠️  Interval too short! Using 5 seconds.", Colors.WARNING)
            interval = 5
    except ValueError:
        print_colored("⚠️  Invalid input! Using default 5 seconds.", Colors.WARNING)
        interval = 5
    
    print_colored(f"\n💀 Starting EXTREME IP rotation every {interval} seconds...", Colors.BOLD + Colors.RED)
    print_colored("Press Ctrl+C to stop", Colors.WARNING)
    print_colored("═" * 70, Colors.CYAN)
    
    successful = 0
    failed = 0
    start_time = time.time()
    ip_history = []
    
    try:
        while True:
            if system == "Linux":
                result, old_ip, new_ip = change_ip_linux()
            elif system == "Windows":
                result, old_ip, new_ip = change_ip_windows()
            
            timestamp = datetime.now().strftime('%H:%M:%S')
            ip_history.append((old_ip, new_ip, timestamp))
            
            if result:
                successful += 1
                print_colored(f"\n🎯 Total successful changes: {successful}", Colors.OKGREEN)
            else:
                failed += 1
                print_colored(f"\n⚠️  Total failed attempts: {failed}", Colors.WARNING)
            
            print_colored(f"\n⏳ Waiting {interval} seconds until next rotation...", Colors.CYAN)
            print_colored("─" * 70, Colors.CYAN)
            
            # Countdown
            for remaining in range(interval, 0, -1):
                print(f"\r{Colors.YELLOW}💀 Next change in: {remaining} seconds...{Colors.ENDC}", end='', flush=True)
                time.sleep(1)
            print()  # New line after countdown
            
    except KeyboardInterrupt:
        print_colored("\n\n⏹️  Stopping IP rotation...", Colors.WARNING)
        print_stats(successful, failed, start_time, ip_history)
        print_colored("\n💀 Thanks for using IP CHANGER EXTREME! 💀", Colors.BOLD + Colors.RED)
        print_colored("═" * 70 + "\n", Colors.CYAN)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print_colored(f"\n❌ Unexpected error: {str(e)}", Colors.FAIL)
        sys.exit(1)
