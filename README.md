# 💀 IP CHANGER EXTREME v3.0 💀

Advanced IP Address Rotator with ASCII Skull Art!

## 🎯 Features

- **💀 ASCII Skull Art** - Cool skull graphics
- **🌍 Public IP Tracking** - Shows your real external IP address
- **🏠 Local IP Tracking** - Shows your internal network IP
- **📊 Real-time Statistics** - Track successful/failed attempts
- **⏱️ Custom Intervals** - Choose your rotation timing
- **🎨 Colorful Interface** - Beautiful colored terminal output
- **📜 IP History** - View last 5 IP changes
- **⏳ Countdown Timer** - See time until next change
- **🔄 Multiple Methods** - Uses 4-5 different techniques to force IP change

## 🚀 Installation

### Linux (Ubuntu/Debian)
```bash
# Install required package
pip3 install requests

# Make executable
chmod +x ip_changer.py

# Run with sudo (REQUIRED for network changes)
sudo python3 ip_changer.py
```

### Windows
```bash
# Install required package
pip install requests

# Run as Administrator (RIGHT-CLICK on cmd/powershell -> Run as Administrator)
python ip_changer.py
```

## 💡 How It Works

### Public IP vs Local IP
- **Public IP** (🌍): Your IP address visible to the internet
- **Local IP** (🏠): Your IP address on your home/office network

### Methods Used

**Linux (5 Methods):**
1. Release DHCP lease
2. Shut down network interface
3. Bring interface back up
4. Request new DHCP lease
5. Flush DNS cache

**Windows (4 Methods):**
1. Release IP address
2. Flush DNS cache
3. Renew IP address
4. Reset network stack

## ⚠️ Important Notes

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
