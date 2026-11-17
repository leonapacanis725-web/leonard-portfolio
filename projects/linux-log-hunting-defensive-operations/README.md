# Linux Log Hunting & Defensive Operations

## Project Overview

This project documents a hands-on investigation of Linux system logs and authentication-related records using command-line tools in a ChromeOS Linux (Crostini) environment.

The investigation focused on reviewing system events, filtering errors, examining login and reboot records, and identifying limitations in the available log data.

## Tools and Commands

- `journalctl` — Review system journal entries.
- `journalctl -p err` — Filter error-priority messages.
- `journalctl --since today` — Review recent events.
- `last` — Examine recorded login and reboot history.
- `lastb` — Check available failed-login records.
- `who` — Check currently logged-in users.
- `whoami` — Identify the current account.
- `sudo` — Run commands requiring elevated permissions.

## Investigation Findings

- Reviewed system journal entries and recent service activity.
- Identified error messages involving PackageKit, `vshd`, and Sommelier.
- Examined recorded reboot and login history.
- Used elevated permissions to access the `btmp` failed-login record.
- No failed-login records were displayed in the available `lastb` output.

## Limitations

- Some journal entries were not visible under the current user's permissions.
- The environment uses ChromeOS Crostini, so some service errors may be specific to that environment.
- The available failed-login output did not establish whether unauthorized access had occurred.
- A failed search against a nonexistent placeholder log file was not treated as a successful finding.

## Conclusion

This exercise demonstrated practical Linux log review, command-line filtering, authentication-history checks, and evidence-based documentation.

The findings are limited to the records available in the environment during the investigation. No confirmed security breach was established.
