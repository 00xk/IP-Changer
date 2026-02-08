# IP-Changer

**Fast and reliable IP rotation tool using TOR network**

[![GitHub](https://img.shields.io/badge/GitHub-00xk%2FIP--Changer-blue)](https://github.com/00xk/IP-Changer)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)](https://www.linux.org/)
[![Version](https://img.shields.io/badge/Version-7.0-brightgreen.svg)](https://github.com/00xk/IP-Changer)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Menu Options](#menu-options)
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

IP-Changer is an **optimized and fast** network tool that changes your public IP address using the TOR network. 

**Version 7.0 Improvements:**
- **Menu System** - Easy menu to Start, Update, or Exit
- **Faster Startup** - Optimized TOR connection (3-5 seconds instead of 30+)
- **Better Error Handling** - Clear messages when things go wrong
- **No Skull Art** - Clean, professional output only
- **Quick IP Verification** - Uses TOR's own API for instant verification

Unlike other IP changers that only reset your local network, this tool uses TOR to guarantee IP changes.

---

## Features

- **Guaranteed IP Change** - Uses TOR network for 100% reliable IP rotation
- **Fast Operation** - Optimized to change IP in 5-10 seconds
- **Interactive Menu** - Choose to Start, Update, or Exit
- **Auto-Installation** - Automatically installs TOR and dependencies
- **Session Statistics** - Track all IP changes during session
- **Update Checker** - Check and update from GitHub
- **Professional Output** - Clean logging with timestamps
- **No Root Required** - TOR method works without sudo (recommended with sudo)

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/00xk/IP-Changer.git
cd IP-Changer

# Make executable
chmod +x main.py

# Run (sudo recommended)
sudo python3 main.py
```

**Menu will appear with options:**
1. Start IP Changer
2. Update from GitHub
3. Exit

---

## Menu Options

### Option 1: Start IP Changer

Starts the IP rotation service. You will be asked:
- Rotation interval (default: 10 seconds)

Then the tool will:
- Check TOR status (install/start if needed)
- Begin rotating your IP
- Show statistics after each change
- Press Ctrl+C to stop and see session stats

### Option 2: Update from GitHub

Checks for updates and pulls latest version from GitHub.

Requirements:
- Must have cloned with git (not downloaded as ZIP)
- Internet connection

### Option 3: Exit

Cleanly exits the program.

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
chmod +x main.py

# Run with sudo (recommended)
sudo python3 main.py
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

### Running the Tool

```bash
sudo python3 main.py
```

### Menu Interface

```
================================================================

                  IP CHANGER v7.0 OPTIMIZED

          Fast, Reliable IP Rotation via TOR Network

             GitHub: github.com/00xk/IP-Changer
                    Author: 00xk

================================================================

MAIN MENU

  [1] Start IP Changer
  [2] Update from GitHub
  [3] Exit

[?] Select option:
```

### Starting IP Rotation (Option 1)

After selecting option 1:

1. System check runs automatically
2. TOR installation/startup (if needed)
3. You choose rotation interval
4. IP rotation begins
5. Press Ctrl+C to stop

**Example Session:**

```
============================================================
[14:23:15] [SYSTEM] SYSTEM CHECK
============================================================
[14:23:15] [INFO] Your direct IP: 203.0.113.45
[14:23:15] [SUCCESS] TOR is running
============================================================

CONFIGURATION
[?] Rotation interval in seconds (default: 10): 15

[14:23:20] [SUCCESS] Interval set to 15 seconds
[14:23:20] [INFO] Press Ctrl+C to stop and return to menu

============================================================
[14:23:20] [SYSTEM] STARTING IP CHANGE
============================================================

[14:23:20] [SUCCESS] TOR is already running
[14:23:21] [INFO] Getting current TOR IP...
[14:23:22] [INFO] Current IP: 198.51.100.23
[14:23:22] [SYSTEM] Requesting new TOR circuit...
[14:23:25] [SYSTEM] Verifying new IP...

============================================================
[14:23:27] [SYSTEM] RESULTS
============================================================
[14:23:27] [INFO] Old IP: 198.51.100.23
[14:23:27] [SUCCESS] New IP: 185.220.101.52
[14:23:27] [SUCCESS] IP SUCCESSFULLY CHANGED

[14:23:27] [INFO] Stats: 1 success, 0 failed
[14:23:27] [INFO] Next change in 15 seconds...
[WAIT] 15s
```

### Updating (Option 2)

Select option 2 to update from GitHub:

```
[14:25:00] [SYSTEM] Updating from GitHub...
[14:25:02] [SUCCESS] Update successful!
[14:25:02] [INFO] Please restart the script

Press Enter to continue...
```

### Exiting (Option 3)

Select option 3 to cleanly exit the program.

---

## Updating

### Method 1: Using the Menu (Easiest)

1. Run the tool: `sudo python3 main.py`
2. Select option 2 (Update from GitHub)
3. Restart the tool after update

### Method 2: Git Pull from Terminal

```bash
cd IP-Changer
git pull origin main
```

### Method 3: Manual Download

```bash
# Download latest version
wget https://github.com/00xk/IP-Changer/archive/refs/heads/main.zip

# Extract
unzip main.zip

# Replace old files
cd IP-Changer-main
chmod +x main.py
sudo python3 main.py
```

### Method 4: Re-clone

```bash
# Remove old version
rm -rf IP-Changer

# Clone latest version
git clone https://github.com/00xk/IP-Changer.git
cd IP-Changer
chmod +x main.py
```

---

## Technical Details

### Version 7.0 Optimizations

- **Faster TOR Connection** - Uses TOR's check API for instant verification
- **Reduced Timeouts** - Smart timeout management (5-10 seconds vs 30+ seconds)
- **Better Error Recovery** - Automatic retry mechanisms
- **Simplified Code** - Removed unnecessary features for speed

### TOR Network

- **Port:** 9050 (SOCKS proxy)
- **Control Port:** 9051 (for requesting new circuits)
- **Verification:** https://check.torproject.org/api/ip
- **Protocol:** SOCKS5

### IP Change Process

1. **Connect to TOR** - Verify TOR is running on port 9050
2. **Get Current IP** - Request IP through TOR SOCKS proxy
3. **Request New Circuit** - Signal TOR to create new circuit
4. **Wait for Circuit** - 3-5 seconds for new route
5. **Verify New IP** - Check IP through TOR again
6. **Confirm Change** - Compare old vs new IP

### Dependencies

- **Python 3.6+**
- **requests** - HTTP library for IP checking
- **stem** - Python library for TOR control
- **PySocks** - SOCKS proxy support
- **TOR** - The Onion Router service

### File Structure

```
IP-Changer/
├── main.py             # Main script
├── README.md           # This file
└── LICENSE             # MIT License
```

---

## Troubleshooting

### Issue: "Cannot connect to TOR network"

**Solution:**
```bash
# Check if TOR is running
sudo systemctl status tor

# If not running, start it
sudo systemctl start tor

# Check if port 9050 is open
netstat -tuln | grep 9050

# Restart TOR if needed
sudo systemctl restart tor
```

### Issue: "Failed to get current TOR IP"

**Causes:**
- TOR service not running
- TOR still starting up (wait 10 seconds)
- Network connectivity issues

**Solution:**
```bash
# Wait a bit after starting TOR
sudo systemctl restart tor
sleep 10

# Then try again
sudo python3 main.py
```

### Issue: "IP DID NOT CHANGE"

**This is normal sometimes.** TOR may give you the same exit node if:
- Limited exit nodes available in your region
- Recent circuit change (TOR rate-limits)
- Exit node pool is small

**Solution:**
- Wait for next cycle (it will try again)
- Increase rotation interval to 20+ seconds
- The tool will eventually get a new IP

### Issue: "TOR is not installed"

**Solution:**
```bash
sudo apt update
sudo apt install tor
```

### Issue: "Permission denied"

**Solution:**
```bash
# Run with sudo
sudo python3 main.py
```

### Issue: Tool is slow

**Possible causes:**
1. TOR network is congested
2. Your internet connection is slow
3. Using too short interval

**Solutions:**
- Increase rotation interval to 15-30 seconds
- Check your internet speed
- TOR is naturally slower than direct connection

### Issue: Some websites block TOR

**This is expected.** Many websites block TOR exit nodes:
- Streaming services (Netflix, Hulu)
- Banking websites
- Some social media

**Solution:**
- Use a VPN for those websites instead
- Use your direct connection (stop the tool)
- This tool is for privacy/testing, not bypassing restrictions

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
