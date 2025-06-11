# Simple Port Scanner (Python)

This is a simple Python-based port scanner that checks a host for commonly used open TCP ports.

---

## 🔍 Features

- Scans for 11 common ports including FTP, SSH, HTTP, HTTPS, MySQL, and more.
- Displays port number and corresponding service name for any open ports.
- Handles user interruption and DNS resolution errors gracefully.
- Displays timestamp of when the scan starts.

---

## ⚙️ How It Works

The script uses the built-in `socket` library to:
- Attempt TCP connections to well-known ports.
- Print ports that are open and return their common service name.

---

## 📦 Requirements

This script uses only standard Python libraries:
- `socket`
- `datetime`

No external installation is required.

---

## 🚀 How to Run

1. Copy the code into a file named `port_scanner.py`
2. Open your terminal or command prompt.
3. Run the script:

```bash
python port_scanner.py
```

4. Enter the target IP address or hostname when prompted.

---

## 📘 Example Output

```
Enter IP address or hostname to scan: 127.0.0.1

[+] Scanning 127.0.0.1 on 11 ports...
Started at: 2025-06-11 18:33:12
  [OPEN] Port 22 (SSH)
  [OPEN] Port 80 (HTTP)
```

---

## 🧠 Notes

- Default timeout is set to 1 second per port.
- You can modify the `common_ports` dictionary to scan additional or custom ports.
- This is a basic educational tool, not a full-fledged scanner like Nmap.

---

## 👨‍💻 Author

**Yash Naik**  
Cybersecurity Student | Python Enthusiast  
[GitHub Profile](https://github.com/Yashnaik70)

---

## 📜 License

This project is for educational and ethical use only.
