from fabric import task
from invoke import Responder
from fabric.transfer import Transfer
import os

@task
def greetings(c, msg):
    print(f"Good, {msg}")

@task
def system_info(c):
    print("Disk Space:")
    c.local("df -h")

    print("\nMemory Info:")
    c.local("free -m")

    print("\nSystem Uptime:")
    c.local("uptime")

@task
def remote_exec(c):
    c.run("hostname")
    c.run("uptime")
    c.run("df -h")
    c.run("free -m")
    c.sudo("yum install unzip zip wget -y")

@task
def web_setup(c, WEBURL, DIRNAME):
    print("###############################")
    print("Installing dependencies")
    print("###############################")
    c.sudo("yum install httpd wget unzip -y")

    print("###############################")
    print("Starting and enabling Apache")
    print("###############################")
    c.sudo("systemctl start httpd")
    c.sudo("systemctl enable httpd")

    print("###############################")
    print("Downloading and unpacking site locally")
    print("###############################")
    os.system(f"wget -O website.zip {WEBURL}")
    os.system("unzip -o website.zip")

    print("###############################")
    print("Zipping and transferring files")
    print("###############################")
    os.chdir(DIRNAME)
    os.system("zip -r tooplate.zip *")
    os.chdir("..")

    transfer = Transfer(c)
    transfer.put(f"{DIRNAME}/tooplate.zip", "/var/www/html/", preserve_mode=False)

    print("###############################")
    print("Unpacking on remote server")
    print("###############################")
    with c.cd("/var/www/html/"):
        c.sudo("unzip -o tooplate.zip")

    c.sudo("systemctl restart httpd")
    print("✅ Website setup is complete.")
