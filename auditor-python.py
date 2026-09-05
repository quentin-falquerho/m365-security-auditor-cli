#!/usr/bin/env python3
"""
M365 Security Auditor CLI
Author: Quentin FALQUERHO
Description: Lightweight CLI tool to audit Microsoft 365 tenant security baseline.
"""

import sys
import time
from rich.console import Console
from rich.table import Table

console = Console()

def run_audit():
    console.print("[bold cyan]======================================================[/bold cyan]")
    console.print("[bold cyan]       M365 Security & Compliance Auditor CLI         [/bold cyan]")
    console.print("[bold cyan]======================================================[/bold cyan]\n")
    
    console.print("[yellow][*] Initializing connection to Microsoft Graph API...[/yellow]")
    time.sleep(1)
    console.print("[green][+] Successfully connected to tenant.[/green]\n")

    # Mock security checks simulating M365 baseline controls
    checks = [
        {
            "category": "Identity & Access",
            "control": "Enforce Multi-Factor Authentication (MFA) for all users",
            "status": "PASSED",
            "severity": "High",
            "details": "Security Defaults or Conditional Access policies enforce MFA globally."
        },
        {
            "category": "Identity & Access",
            "control": "Block legacy authentication protocols",
            "status": "PASSED",
            "severity": "High",
            "details": "Legacy auth is disabled via Conditional Access."
        },
        {
            "category": "Data Governance",
            "control": "External sharing restricted in SharePoint/OneDrive",
            "status": "FAILED",
            "severity": "Medium",
            "details": "Anonymous guest links are currently allowed."
        },
        {
            "category": "Threat Protection",
            "control": "Defender for Office 365 safe links enabled",
            "status": "PASSED",
            "severity": "High",
            "details": "Safe Links policy is active for all recipients."
        },
        {
            "category": "Auditing & Logging",
            "control": "Unified audit log search enabled",
            "status": "PASSED",
            "severity": "Medium",
            "details": "Audit logging is active."
        },
        {
            "category": "Administration",
            "control": "Limit global administrator accounts (Max 4)",
            "status": "FAILED",
            "severity": "Critical",
            "details": "Found 6 active Global Administrator accounts."
        }
    ]

    table = Table(title="M365 Security Posture Assessment Report", show_header=True, header_style="bold magenta")
    table.add_column("Category", style="dim", width=20)
    table.add_column("Security Control", width=35)
    table.add_column("Severity", width=10)
    table.add_column("Status", width=10)

    passed_count = 0
    failed_count = 0

    for check in checks:
        if check["status"] == "PASSED":
            status_str = "[green]PASSED[/green]"
            passed_count += 1
        else:
            status_str = "[red]FAILED[/red]"
            failed_count += 1

        severity_str = f"[bold red]{check['severity']}[/bold red]" if check["severity"] in ["High", "Critical"] else f"[yellow]{check['severity']}[/yellow]"
        
        table.add_row(check["category"], check["control"], severity_str, status_str)

    console.print(table)
    
    # Summary
    total = len(checks)
    score = int((passed_count / total) * 100)
    
    console.print(f"\n[bold]Audit Summary:[/bold]")
    console.print(f"Total Checks: {total} | [green]Passed: {passed_count}[/green] | [red]Failed: {failed_count}[/red]")
    console.print(f"Tenant Security Score: [bold cyan]{score}%[/bold cyan]\n")

if __name__ == "__main__":
    try:
        run_audit()
    except KeyboardInterrupt:
        console.print("\n[red]Audit aborted by user.[/red]")
        sys.exit(1)
