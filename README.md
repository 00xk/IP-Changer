# 💀 IP CHANGER ULTIMATE v5.0 💀

**The ONLY IP changer that ACTUALLY changes your public IP address!**

## 🎯 Why This Version is Different

Previous versions failed because they only reset your LOCAL network - which doesn't change your PUBLIC IP (the one websites see). This version uses **TOR NETWORK** to guarantee IP changes!

## 🚀 Features

- ✅ **TOR Integration** - Routes traffic through TOR network (GUARANTEED IP CHANGE!)
- ✅ **MAC Spoofing** - Changes hardware address
- ✅ **Network Reset** - Complete DHCP renewal
- ✅ **Auto-Install** - Installs TOR and dependencies automatically
- ✅ **Giant Skull Art** - Maximum death mode aesthetics
- ✅ **Works with/without root** - Some features require sudo, but TOR works for all users
- ✅ **Real IP Verification** - Actually checks if your IP changed

## 📦 Installation

### Quick Install (Ubuntu/Debian)

```bash
# Download the script
wget https://your-url/ip_changer_ultimate.py

# Make executable
chmod +x ip_changer_ultimate.py

# Run (with sudo for best results)
sudo python3 ip_changer_ultimate.py
```

### Manual Install

```bash
# Install dependencies
sudo apt update
sudo apt install -y tor python3-pip

# Install Python packages
pip3 install requests stem --break-system-packages

# Run the script
sudo python3 ip_changer_ultimate.py
```

## 🎮 Usage

### Basic Usage

```bash
sudo python3 ip_changer_ultimate.py
```

The script will:
1. Check your current IP
2. Install TOR if not present
3. Start TOR service
4. Route your traffic through TOR
5. Verify your new IP address
6. Repeat every X seconds (you choose)

### Without Root (Limited Mode)

```bash
python3 ip_changer_ultimate.py
```

TOR routing will still work, but MAC spoofing and network reset won't be available.

## 🔥 How It Works

### The Problem with Other IP Changers

Most IP changers only do this:
```
1. Release DHCP lease
2. Renew DHCP lease
3. Hope ISP gives you new IP (SPOILER: They don't!)
```

**Why this fails:** Your ISP controls your public IP. Most ISPs use:
- Static IP assignments (same IP forever)
- Long-term DHCP leases (weeks/months)
- MAC address binding (tracks your router)

### Our Solution: TOR Network

```
1. Install TOR service
2. Route ALL traffic through TOR
3. Your IP is now a TOR exit node IP
4. Change TOR circuit = Change IP
5. GUARANTEED new IP every time!
```

## 🧅 What is TOR?

**TOR (The Onion Router)** is a free anonymity network used by:
- Journalists in oppressive countries
- Privacy advocates
- Security researchers
- Anyone who values privacy

When you use TOR:
- Your traffic is encrypted 3 times
- It bounces through 3+ random servers worldwide
- Websites see the exit node's IP, not yours
- You get a different IP address

## 🛡️ Security & Privacy

### What This Script Does

✅ Changes your public IP address via TOR
✅ Encrypts your traffic through TOR network
✅ Spoofs your MAC address (with sudo)
✅ Clears network caches

### What This Script Doesn't Do

❌ Make you 100% anonymous (use TOR Browser for that)
❌ Encrypt non-TOR traffic automatically
❌ Protect against all tracking methods
❌ Bypass all network restrictions

### Legal Notice

This tool is for:
- ✅ Privacy protection
- ✅ Network testing
- ✅ Educational purposes
- ✅ Legitimate research

NOT for:
- ❌ Illegal activities
- ❌ Bypassing terms of service
- ❌ Harassment or abuse
- ❌ Copyright infringement

**You are responsible for how you use this tool.**

## 📊 Understanding the Output

### Successful IP Change

```
💀 INITIATING ULTIMATE IP CHANGE SEQUENCE 💀

📍 Current IP: 203.0.113.45

⚡ METHOD MAC: HARDWARE ADDRESS SPOOFING
   ✅ MAC address spoofed

⚡ METHOD RESET: FULL NETWORK RESTART
   ✅ Network reset complete

⚡ METHOD TOR: ONION ROUTING IP CHANGE
   ✅ Tor service running
   ✅ Tor IP: 198.51.100.23

📊 RESULTS:
📍 Old IP: 203.0.113.45
📍 New IP: 198.51.100.23        ← CHANGED!
🔧 Method: Tor Network
🕐 Time: 14:23:45

💀💀💀 SUCCESS! IP CHANGED! 💀💀💀
🧅 You are now connected through TOR network!
```

### Failed IP Change (Without TOR)

```
⚠️  IP CHANGE VERIFICATION FAILED

💡 TOR method failed. Try:
   1. Run with sudo
   2. Manually install: sudo apt install tor
   3. Use a VPN service
```

## 🔧 Troubleshooting

### "Tor not found"

The script will try to auto-install TOR. If it fails:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install tor

# Fedora/RedHat
sudo dnf install tor

# Arch
sudo pacman -S tor
```

### "Permission denied"

Run with sudo:
```bash
sudo python3 ip_changer_ultimate.py
```

### "IP didn't change"

If TOR fails to install/start:
1. Manually install TOR: `sudo apt install tor`
2. Start TOR: `sudo systemctl start tor`
3. Check status: `sudo systemctl status tor`
4. Re-run the script

### TOR is slow

Yes, TOR is slower than direct connection because:
- Traffic goes through 3+ servers
- Encryption/decryption at each hop
- Exit nodes may be far away

This is the trade-off for anonymity.

### I want my original IP back

Stop the script (Ctrl+C) and:

```bash
# Stop TOR
sudo systemctl stop tor

# Reset network
sudo systemctl restart NetworkManager

# Or just reboot
sudo reboot
```

## 🌍 TOR Exit Node Countries

Your new IP will be from a TOR exit node, which could be in:
- 🇩🇪 Germany
- 🇺🇸 United States
- 🇫🇷 France
- 🇳🇱 Netherlands
- 🇸🇪 Sweden
- 🇨🇭 Switzerland
- And many others!

You can't choose the country (that's part of TOR's anonymity), but you'll get a different IP each rotation.

## 🆚 Comparison: This vs VPN vs Regular Changers

| Feature | This Script | VPN | Regular Changers |
|---------|------------|-----|-----------------|
| Changes Public IP | ✅ Yes (via TOR) | ✅ Yes | ❌ Maybe |
| Free | ✅ Yes | ❌ No (paid) | ✅ Yes |
| Guaranteed | ✅ Yes (if TOR works) | ✅ Yes | ❌ No |
| Speed | ⚠️ Slower | ✅ Fast | ✅ Fast |
| Anonymity | ✅ High | ⚠️ Depends | ❌ None |
| Encryption | ✅ Yes (TOR) | ✅ Yes | ❌ No |

## 💡 Best Practices

### For Privacy
1. Run the script with sudo
2. Let it install TOR
3. Verify IP changed successfully
4. Use HTTPS websites only
5. Don't log into personal accounts

### For Testing
1. Run without sudo first
2. Check if TOR installs properly
3. Verify IP rotation works
4. Adjust interval as needed

### For Maximum Anonymity
1. Use TOR Browser instead
2. Don't use this for illegal activities
3. Combine with HTTPS everywhere
4. Avoid logging into accounts

## 📚 Additional Resources

- [TOR Project Official](https://www.torproject.org/)
- [How TOR Works](https://2019.www.torproject.org/about/overview.html.en)
- [TOR FAQ](https://support.torproject.org/faq/)
- [EFF - TOR Guide](https://ssd.eff.org/en/module/how-use-tor-linux)

## 🐛 Known Issues

1. **TOR installation may fail** on some distros
   - Solution: Manually install TOR first
   
2. **Slow speed** when using TOR
   - This is normal for TOR
   
3. **Some websites block TOR** exit nodes
   - Use a VPN instead for those sites
   
4. **MAC spoofing requires root**
   - Run with sudo, or skip MAC method

## 🤝 Contributing

Found a bug? Have a suggestion? Want to add features?

Issues and improvements welcome!

## ⚖️ License

This script is provided AS-IS for educational purposes.

**Use responsibly and legally.**

## 💀 Final Notes

**This script ACTUALLY changes your IP using TOR.**

If TOR doesn't install/work:
- You can still use VPN services (NordVPN, ProtonVPN, etc.)
- You can still restart your router manually
- You can still contact your ISP

But this is the only **free, automated, guaranteed** way to change your public IP on Linux!

Stay anonymous! 💀

---

**Version:** 5.0 ULTIMATE  
**Platform:** Linux  
**Requirements:** Python 3, TOR (auto-installed)  
**Status:** MAXIMUM DEATH MODE ACTIVATED 💀
### Why Public IP Might Not Change

Your **public IP** is controlled by your ISP (Internet Service Provider). Here's why it might not change:

1. **Static IP Assignment** - Your ISP gives you the same IP every time
2. **Long DHCP Leases** - Your ISP's DHCP lease might last days/weeks
3. **MAC Address Binding** - ISP assigns IP based on your router's MAC address
4. **Business Connection** - Business internet often has static IPs

### How to ACTUALLY Change Your Public IP

If you need to change your public IP address, try these methods:

1. **VPN Service** (Most Reliable)
   - NordVPN, ExpressVPN, ProtonVPN, etc.
   - Changes IP instantly to different countries
   - **This script can't do this for you**

2. **Restart Your Router**
   - Unplug router for 5-10 minutes
   - ISP might assign new IP when you reconnect
   - Works better with cable/DSL than fiber

3. **Contact Your ISP**
   - Ask for a new IP assignment
   - Some ISPs can do this remotely

4. **Change Router MAC Address**
   - Some routers allow MAC cloning
   - ISP may assign new IP to new MAC

### What This Script DOES Do

✅ Releases and renews your local network connection
✅ Forces your computer to request a new DHCP lease
✅ Might get new IP if ISP uses dynamic assignment
✅ Will definitely refresh your local network connection
✅ Looks cool with skulls! 💀

### What This Script DOESN'T Do

❌ Cannot bypass ISP IP assignment policies
❌ Cannot force ISP to give you new IP
❌ Cannot provide VPN-like IP masking
❌ Cannot guarantee public IP change

## 🎮 Usage

1. Run the script with admin privileges
2. Enter desired interval (or press Enter for 5 seconds)
3. Watch as it attempts to rotate your IP
4. Press Ctrl+C to stop and see statistics

## 📊 Output Explanation

```
💀 INITIATING IP ROTATION
📍 Old Public IP: 203.0.113.45    ← Your current internet IP
🏠 Old Local IP: 192.168.1.100    ← Your computer's network IP
⚡ Method 1: Releasing DHCP lease...
⚡ Method 2: Shutting down interface...
⚡ Method 3: Bringing interface back up...
⚡ Method 4: Requesting new DHCP lease...
⚡ Method 5: Flushing DNS cache...
✅ New Public IP: 203.0.113.46    ← Success! IP changed
🏠 New Local IP: 192.168.1.101    ← Local IP also changed
```

If you see "⚠️ WARNING: Public IP didn't change" - this is NORMAL for most ISPs!

## 🛡️ Security & Privacy

- This tool is for **legitimate purposes** only
- Changing IPs doesn't make you anonymous
- For real privacy, use a trusted VPN service
- Always respect website terms of service

## 🐛 Troubleshooting

**"Permission denied" error:**
- Linux: Run with `sudo`
- Windows: Run as Administrator

**"requests module not found":**
- Run: `pip install requests`

**IP never changes:**
- This is normal! Your ISP controls public IP assignment
- Consider using a VPN for reliable IP rotation

## 📝 License

Free to use for educational and legitimate purposes.

---

💀 **Made with skull power!** 💀
