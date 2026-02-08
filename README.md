# IP-Changer

**Professional network tool for changing your public IP address on Linux**

[![GitHub](https://img.shields.io/badge/GitHub-00xk%2FIP--Changer-blue)](https://github.com/00xk/IP-Changer)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)](https://www.linux.org/)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Updating](#updating)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Legal Notice](#legal-notice)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

IP-Changer is a professional-grade network tool that **actually changes your public IP address** using the TOR network. Unlike other IP changers that only reset your local network (which rarely changes your ISP-assigned IP), this tool routes your traffic through TOR to guarantee a different public IP address.

**Why This Tool?**

Most "IP changers" fail because they only:
1. Release your DHCP lease
2. Renew your DHCP lease
3. Hope your ISP gives you a new IP (they usually don't)

**Our Solution:**

We use the **TOR (The Onion Router)** network to:
1. Route ALL traffic through TOR
2. Your public IP becomes a TOR exit node IP
3. Change TOR circuits to get new IPs
4. **Guaranteed IP change every time**

---

## Features

- **Guaranteed IP Change** - Uses TOR network for reliable IP rotation
- **Auto-Installation** - Automatically installs TOR and dependencies
- **MAC Address Spoofing** - Changes hardware address (with root)
- **Network Reset** - Complete DHCP renewal (with root)
- **Professional Logging** - Clean, timestamped output
- **Session Statistics** - Track successful/failed IP changes
- **Update Checker** - Automatically checks for new versions
- **No Emojis** - Professional, clean terminal output
- **Open Source** - Fully transparent code

---

## How It Works

### The Problem

Your ISP (Internet Service Provider) controls your public IP address. Most ISPs use:

- **Static IP Assignment** - Same IP forever
- **Long-Term DHCP Leases** - IP stays the same for weeks/months
- **MAC Address Binding** - Tracks your router's hardware address

Simply restarting your network connection won't change your IP because your ISP recognizes your router and gives you the same IP.

### Our Solution: TOR Network

**TOR (The Onion Router)** is a free, open-source anonymity network:

```
Your Computer --> TOR Node 1 --> TOR Node 2 --> TOR Node 3 --> Internet
```

When you use TOR:
- Traffic is encrypted 3 times (onion routing)
- Bounces through 3+ random servers worldwide
- Websites see the TOR exit node's IP, not yours
- Each new circuit = different exit node = different IP

**This tool:**
1. Installs and starts TOR service
2. Routes traffic through TOR
3. Requests new TOR circuit
4. Verifies new IP address
5. Repeats on schedule

---

## Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/00xk/IP-Changer.git

# Navigate to directory
cd IP-Changer

# Make executable
chmod +x ip_changer.py

# Run with sudo (recommended)
sudo python3 ip_changer.py
```

### Manual Dependencies

If auto-install fails:

```bash
# Install TOR
sudo apt update
sudo apt install tor

# Install Python packages
pip3 install requests stem PySocks --break-system-packages
```

### Supported Distributions

- Ubuntu / Debian
- Fedora / RedHat / CentOS
- Arch Linux
- openSUSE
- Any Linux with systemd

---

## Usage

### Basic Usage

```bash
sudo python3 ip_changer.py
```

The script will:
1. Check if TOR is installed (install if needed)
2. Start TOR service
3. Display your current IP
4. Ask for rotation interval (default: 10 seconds)
5. Begin rotating your IP

### Without Root

```bash
python3 ip_changer.py
```

TOR routing will work, but MAC spoofing and network reset will be disabled.

### Example Output

```
============================================================

     IP CHANGER - Advanced Network Identity Tool

     GitHub: https://github.com/00xk/IP-Changer
     Author: 00xk
     Version: 6.0 FINAL

============================================================

[14:23:15] [SYSTEM] Checking for updates...
[14:23:15] [INFO] Latest version on GitHub: v6.0

============================================================
[14:23:15] [SYSTEM] SYSTEM INFORMATION
============================================================
[14:23:15] [INFO] Platform: Linux
[14:23:15] [INFO] Root access: Yes
[14:23:15] [INFO] Network interface: eth0
[14:23:16] [INFO] Current public IP: 203.0.113.45
============================================================

CONFIGURATION
[?] Enter rotation interval in seconds (default: 10): 15

[14:23:20] [SUCCESS] IP rotation interval set to 15 seconds
[14:23:20] [INFO] Press Ctrl+C to stop

============================================================
[14:23:20] [SYSTEM] INITIATING IP CHANGE SEQUENCE
============================================================

[14:23:20] [INFO] Network interface: eth0
[14:23:20] [INFO] Checking initial public IP...
[14:23:21] [INFO] Current direct IP: 203.0.113.45
[14:23:21] [SYSTEM] Applying network-level changes...
[14:23:21] [SYSTEM] Spoofing MAC address on eth0...
[14:23:21] [SUCCESS] MAC changed to 00:16:3e:4a:2b:1c
[14:23:23] [SYSTEM] Performing network reset...
[14:23:25] [SUCCESS] Network reset complete
[14:23:28] [SYSTEM] Changing IP via TOR network...
[14:23:28] [SYSTEM] Initializing TOR method...
[14:23:28] [SUCCESS] TOR setup complete
[14:23:29] [INFO] Current TOR IP: 198.51.100.23
[14:23:29] [SUCCESS] Requested new TOR circuit
[14:23:34] [SYSTEM] Verifying new IP address...
[14:23:37] [SUCCESS] IP successfully changed: 198.51.100.23 -> 185.220.101.52

============================================================
[14:23:37] [SYSTEM] IP CHANGE RESULTS
============================================================
[14:23:37] [INFO] OLD IP: 198.51.100.23
[14:23:37] [SUCCESS] NEW IP: 185.220.101.52
[14:23:37] [SUCCESS] STATUS: IP SUCCESSFULLY CHANGED
[14:23:37] [INFO] METHOD: TOR Network
[14:23:37] [INFO] Your traffic is now routed through TOR

[14:23:37] [INFO] Next rotation in 15 seconds...
```

### Stopping

Press `Ctrl+C` to stop. You'll see session statistics:

```
============================================================
SESSION STATISTICS
============================================================
Successful changes: 12
Failed attempts: 0
Total runtime: 00:03:45

IP Change History:
------------------------------------------------------------
[14:23:37] SUCCESS | 198.51.100.23 -> 185.220.101.52
[14:23:52] SUCCESS | 185.220.101.52 -> 192.42.116.16
[14:24:07] SUCCESS | 192.42.116.16 -> 199.249.230.88
============================================================
```

---

## Updating

### Method 1: Git Pull (Recommended)

If you cloned the repository:

```bash
cd IP-Changer
git pull origin main
```

### Method 2: Manual Download

```bash
# Download latest version
wget https://github.com/00xk/IP-Changer/archive/refs/heads/main.zip

# Extract
unzip main.zip

# Navigate and run
cd IP-Changer-main
chmod +x ip_changer.py
sudo python3 ip_changer.py
```

### Method 3: Re-clone

```bash
# Remove old version
rm -rf IP-Changer

# Clone latest version
git clone https://github.com/00xk/IP-Changer.git
cd IP-Changer
chmod +x ip_changer.py
```

### Checking for Updates

The script automatically checks for updates on GitHub when you run it. If a new version is available, you'll see:

```
[14:23:15] [INFO] Latest version on GitHub: v6.1
[14:23:15] [INFO] To update, run: git pull origin main
```

---

## Technical Details

### TOR Network

- **Port:** 9050 (SOCKS proxy)
- **Control Port:** 9051 (for requesting new circuits)
- **Protocol:** SOCKS5

### IP Change Methods

1. **TOR Circuit Rotation** (Primary)
   - Requests new TOR identity via control port
   - Fallback: Restart TOR service
   
2. **MAC Address Spoofing** (Requires root)
   - Generates random MAC address
   - Uses macchanger or manual IP commands
   
3. **Network Reset** (Requires root)
   - Releases DHCP lease
   - Flushes IP addresses
   - Brings interface down/up
   - Renews DHCP lease

### Dependencies

- **Python 3.6+**
- **requests** - HTTP library for IP checking
- **stem** - Python library for TOR control
- **PySocks** - SOCKS proxy support
- **TOR** - The Onion Router service

### File Structure

```
IP-Changer/
├── ip_changer.py       # Main script
├── README.md           # This file
└── LICENSE             # MIT License
```

---

## Troubleshooting

### Issue: "TOR is not installed"

**Solution:**
```bash
sudo apt update
sudo apt install tor
```

### Issue: "TOR service is not accessible on port 9050"

**Solution:**
```bash
# Check TOR status
sudo systemctl status tor

# Start TOR
sudo systemctl start tor

# Enable TOR on boot
sudo systemctl enable tor
```

### Issue: "IP did not change"

**Possible Causes:**
1. TOR service not running properly
2. Network connectivity issues
3. Firewall blocking TOR ports

**Solution:**
```bash
# Check TOR logs
sudo journalctl -u tor -n 50

# Restart TOR
sudo systemctl restart tor

# Check firewall
sudo ufw status
```

### Issue: "Permission denied"

**Solution:**
```bash
# Run with sudo
sudo python3 ip_changer.py
```

### Issue: TOR is slow

**This is normal.** TOR routes traffic through multiple servers for anonymity, which reduces speed. This is the trade-off for privacy.

### Issue: Some websites block TOR

**This is common.** Many websites (Netflix, banking sites) block TOR exit nodes. For those sites:
- Use a VPN instead
- Use your direct connection
- This tool is for privacy/testing, not bypassing geo-restrictions

---

## FAQ

### Q: Is this legal?

**A:** Yes. TOR is legal in most countries and is used by journalists, activists, and privacy advocates. However, what you do with anonymity matters. Use responsibly.

### Q: Does this make me anonymous?

**A:** Partially. Your public IP is hidden, but full anonymity requires:
- Using HTTPS websites only
- Not logging into personal accounts
- Using TOR Browser (not just this script)
- Following proper OPSEC practices

### Q: Will my ISP know I'm using TOR?

**A:** Yes, they can see you're connecting to TOR nodes, but they can't see what you're doing.

### Q: Can I choose which country my IP is from?

**A:** No. TOR randomly selects exit nodes. This is intentional for anonymity. If you need specific countries, use a VPN.

### Q: Is this better than a VPN?

**A:** Different use cases:

| Feature | TOR (This Tool) | VPN |
|---------|-----------------|-----|
| Cost | Free | $5-15/month |
| IP Change | Yes | Yes |
| Speed | Slower | Fast |
| Anonymity | High | Medium |
| Choose Country | No | Yes |

### Q: Will this work on Windows/Mac?

**A:** No, this is Linux-only. For Windows/Mac:
- Use TOR Browser
- Use a VPN service
- Use a proxy service

### Q: How often should I rotate my IP?

**A:** Depends on your use case:
- Privacy: Every 5-10 minutes
- Testing: As needed
- Normal browsing: 30+ minutes

### Q: Does this protect against tracking?

**A:** It protects against IP-based tracking, but websites can still track you via:
- Cookies
- Browser fingerprinting
- Login information
- Payment methods

---

## Legal Notice

This tool is provided for:
- Educational purposes
- Privacy protection
- Network testing
- Security research

**NOT for:**
- Illegal activities
- Bypassing terms of service
- Harassment or abuse
- Copyright infringement

**You are responsible for your actions. The author is not liable for misuse.**

---

## Contributing

Contributions welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

**Areas for contribution:**
- Additional IP change methods
- Support for more Linux distributions
- Better error handling
- Performance improvements
- Documentation improvements

---

## License

MIT License

Copyright (c) 2024 00xk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Links

- **GitHub Repository:** https://github.com/00xk/IP-Changer
- **Report Issues:** https://github.com/00xk/IP-Changer/issues
- **TOR Project:** https://www.torproject.org/
- **Author:** [@00xk](https://github.com/00xk)

---

**Made with professional standards by 00xk**

**Star the repo if you find it useful!**
