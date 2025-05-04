# 🌐 fabric-web-setup

A Fabric 3.x-based Python script to automate remote Linux server setup, system diagnostics, and website deployment over SSH.  
Built for developers and sysadmins who want fast, repeatable web provisioning using modern Fabric.

---

## 🚀 Features

- ✅ Local system checks: disk, memory, uptime
- 🔧 Remote system info and package installation
- 📦 Package and push a website to a remote Apache server
- 🔁 Uses Fabric 3.x with `Connection` objects and `Invoke` tasks
- 🛡️ `sudo` support and safe zip handling via SSH

---

## 📦 Requirements

- Python 3.x
- Fabric 3.x (`fabric>=3.0.0`)
- `wget`, `zip`, `unzip` on local machine (installed via system package manager)

Install the Python dependencies:

```bash
pip install -r requirements.txt
````

**requirements.txt**

```
fabric==3.0.0
```

---

## 🧾 Usage

Make sure `fabfile.py` is in the same directory and you have SSH access to the remote server.

### Run Local System Info:

```bash
fab system_info
```

### Run Remote Setup:

```bash
fab -H user@remotehost remote_exec
```

### Deploy a Website:

```bash
fab -H user@remotehost web_setup --WEBURL="https://example.com/site.zip" --DIRNAME="your-local-site-folder"
```

> Replace `remotehost` with your actual IP or domain, and adjust the `WEBURL` and `DIRNAME` accordingly.

---

## 📂 What It Does

1. Installs Apache, wget, unzip on the remote server (via `yum`)
2. Downloads and unzips a website archive locally
3. Zips and uploads content to `/var/www/html/` on the server
4. Unpacks it and restarts Apache

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Pull requests and issues are welcome. Feel free to fork the project and submit your improvements!
