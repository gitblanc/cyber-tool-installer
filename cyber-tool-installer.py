import platform
import subprocess
import os
import sys

# ANSI escape sequence for colors
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Define available tools with descriptions
TOOLS = {
    "SecLists": {
        "description": "SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments, collected in one place. List types include usernames, passwords, URLs, sensitive data patterns, fuzzing payloads, web shells, and many more.",
        "file": "seclists.sh"
    },
    "Sherlock": {
        "description": "🔎 Hunt down social media accounts by username across social networks",
        "file": "sherlock.sh"
    },
    "NoSQLMap": {
        "description": "Automated NoSQL database enumeration and web application exploitation tool.",
        "file": "nosqlmap.sh"
    },
    "PayloadsAllTheThings": {
        "description": "A list of useful payloads and bypass for Web Application Security and Pentest/CTF.",
        "file": "payloadsallthethings.sh"
    },
    "GhostTrack": {
        "description": "Useful tool to track location or mobile number.",
        "file": "ghosttrack.sh"
    },
    "XSStrike": {
        "description": "Most advanced XSS scanner.",
        "file": "xssstrike.sh"
    },
    "XSSPayloads": {
        "description": "List of XSS Vectors/Payloads.",
        "file": "xsspayloads.sh"
    },
    "xsser": {
        "description": "Cross Site Scripter (aka XSSer) is an automatic -framework- to detect, exploit and report XSS vulnerabilities in web-based applications.",
        "file": "xsser.sh"
    },
    "PEASS.ng": {
        "description": "PEASS - Privilege Escalation Awesome Scripts SUITE (with colors)",
        "file": "peass.sh"
    },
    "Default-Creds-Cheat-Sheet": {
        "description": "One place for all the default credentials to assist the Blue/Red teamers activities on finding devices with default password 🛡️",
        "file": "default-creds.sh"
    },
    "Haiti": {
        "description": "🔑 Hash type identifier (CLI & lib)",
        "file": "haiti.sh"
    },
    "Wordlistctl": {
        "description": "Fetch, install and search wordlist archives from websites and torrent peers.",
        "file": "wordlistctl.sh"
    },
    "Mentalist": {
        "description": "Mentalist is a graphical tool for custom wordlist generation. It utilizes common human paradigms for constructing passwords and can output the full wordlist as well as rules compatible with Hashcat and John the Ripper.",
        "file": "mentalist.sh"
    },
    "TTPassgen": {
        "description": "密码生成 flexible and scriptable password dictionary generator which can support brute-force、combination、complex rule mode etc...",
        "file": "ttpassgen.sh"
    },
    "lyricpass": {
        "description": "Password wordlist generator using song lyrics for targeted bruteforce audits / attacks. Useful for penetration testing or security research.",
        "file": "lyricpass.sh"
    },
    "Brave Browser": {
        "description": "Secure and fast web browser.",
        "file": "brave.sh"
    },
    "KeepassXC": {
        "description": "Password Manager.",
        "file": "keepass.sh"
    },
    "OWASP ZAP": {
        "description": "The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by a dedicated international team of volunteers. Great for pentesting.",
        "file": "zap.sh"
    },
    "Obsidian": {
        "description": "A powerful knowledge base that works on top of a local folder of plain text Markdown files.",
        "file": "obsidian.sh"
    }
    # Add more tools here
}

def get_pc_user():
    """Prompt the user for the PC user's name."""
    pc_user = input(f"{RED}Enter the PC user's name for the installation: {RESET}")
    return pc_user

def get_os():
    """Determine the operating system."""
    return platform.system().lower()

def print_color(text, color):
    """Print text in specified color."""
    print(f"{color}{text}{RESET}")

def install_tool(tool_name):
    """Read the tool's installation command from its file, replace the PC user placeholder, and execute it. Returns False if installation failed."""
    pc_user = get_pc_user()  # Prompt for the PC user's name
    tool_info = TOOLS.get(tool_name, {})
    command_file_path = f"./tools/{tool_info.get('file', '')}"
    try:
        with open(command_file_path, "r") as file:
            install_command = file.read().strip()
        # Replace the PC user placeholder with the actual PC user's name
        install_command = install_command.replace("{pc_user}", pc_user)
        print_color(f"Installing {tool_name} for user {pc_user} without requiring user intervention...", RED)
        subprocess.run(install_command, shell=True, check=True)
        print_color(f"{tool_name} installed successfully for user {pc_user}.", RED)
        return True
    except Exception as e:
        print_color(f"Error installing {tool_name}: {e}", RED)
        return False


def show_tool_description(tool_name):
    """Show the description of a specific tool."""
    tool_info = TOOLS.get(tool_name)
    if tool_info:
        print_color(f"{tool_name} - {tool_info['description']}", RED)
    else:
        print_color(f"Tool {tool_name} not found.", RED)

def install_tools(failed_installs):
    print_color("\nAvailable tools to install:", RED)
    print_color("0. Go back to the main menu", RED)
    for i, tool_name in enumerate(TOOLS.keys(), start=1):
        print_color(f"{i}. {tool_name}", RED)
    choice = input(f"{RED}Enter your choice (or 'all' for all tools): {RESET}")

    if choice == '0':
        return  # Go back to the main menu
    elif choice.lower() == 'all':
        for tool_name in TOOLS.keys():
            if not install_tool(tool_name):
                failed_installs.append(tool_name)
    else:
        selected_tool_indices = choice.split(',')
        for index in selected_tool_indices:
            try:
                if index.strip() == '0':
                    return  # Go back to the main menu
                tool_index = int(index) - 1
                tool_name = list(TOOLS.keys())[tool_index]
                if not install_tool(tool_name):
                    failed_installs.append(tool_name)
            except (ValueError, IndexError):
                print_color("Invalid selection.", RED)

def print_logo():
    logo = """
    _________       ___.                  .__                __         .__  .__                
    \_   ___ \___.__\_ |__   ___________  |__| ____   ______/  |______  |  | |  |   ___________ 
    /    \  \<   |  || __ \_/ __ \_  __ \ |  |/    \ /  ___\   __\__  \ |  | |  | _/ __ \_  __ \\
    \     \___\___  || \_\ \  ___/|  | \/ |  |   |  \\\\___ \ |  |  / __ \|  |_|  |_\  ___/|  | \/
    \______  / _____||___  /\___  |__|    |__|___|  /____  >|__| (____  |____|____/\___  |__|   
           \/\/          \/     \/                \/     \/           \/               \/       v.1.0 by @gitblanc    
    """
    print_color(logo, RED)

def main_menu():
    # Check if the script is run with root privileges
    # if os.geteuid() != 0:
    #     print_color("This script needs to be run as root. Please run again with sudo.", RED)
    #     sys.exit(1)
    print_logo()
    
    failed_installs = []
    print_color(f"\nDetected OS: {get_os().capitalize()}", RED)
    while True:
        print_color("\nMain Menu:", RED)
        print_color("1. Install Tools", RED)
        print_color("2. Get Tool Information", RED)
        print_color("3. Exit", RED)
        choice = input(f"{RED}Enter your choice: {RESET}")

        if choice == '1':
            install_tools(failed_installs)
        elif choice == '2':
            tool_name = input(f"{RED}Enter the name of the tool for information: {RESET}")
            show_tool_description(tool_name)
        elif choice == '3':
            if failed_installs:
                print_color("The following tools could not be installed properly:", YELLOW)
                for tool in failed_installs:
                    print_color(f"- {tool}", YELLOW)
            break
        else:
            print_color("Invalid option, please try again.", RED)

if __name__ == "__main__":
    main_menu()
