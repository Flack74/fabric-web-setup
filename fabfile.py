from fabric.api import task, run, sudo, local, lcd, cd, put

@task
def greetings(msg):
    print("Good, {}".format(msg))

@task
def system_info():
    print("Disk Space:")
    local("df -h")

    print("\nMemory Info:")
    local("free -m")

    print("\nSystem Uptime:")
    local("uptime")

@task
def remote_exec():
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")
    sudo("yum install unzip zip wget -y")

@task
def web_setup(WEBURL, DIRNAME):
    print("###############################")
    print("Installing dependencies")
    print("###############################")
    sudo("yum install httpd wget unzip -y")

    print("###############################")
    print("Starting and enabling Apache")
    print("###############################")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print("###############################")
    print("Downloading website archive")
    print("###############################")
    local("wget -O website.zip {}".format(WEBURL))
    local("unzip -o website.zip")

    print("###############################")
    print("Zipping website and uploading")
    print("###############################")
    with lcd(DIRNAME):
        local("zip -r tooplate.zip *")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)

    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")
    print("✅ Website setup is complete.")
