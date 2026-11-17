# Linux Log Hunting & Defensive Operations
## Investigation Report

### 1. Objective

Review available Linux system and authentication-related records to identify notable system activity, examine error messages, and assess what the available evidence can establish.

### 2. Environment

- Platform: ChromeOS Linux (Crostini)
- Account: `leonapacanis725`
- Tools: Linux terminal, `journalctl`, `last`, `lastb`, `who`, and `sudo`

### 3. Investigation Procedures

| Command | Purpose |
|---|---|
| `journalctl` | Review system journal activity |
| `journalctl -n 20` | Inspect the 20 most recent journal entries |
| `journalctl -p err` | Filter error-priority entries |
| `journalctl --since today` | Review entries from the current day |
| `last` | Examine recorded login and reboot history |
| `last -n 10` | Review the 10 most recent history records |
| `who` | Check for currently logged-in users |
| `lastb` | Review available failed-login records |
| `sudo lastb` | Access failed-login records with elevated permissions |
| `whoami` | Confirm the active account |

### 4. Observations

**System journal**

The journal contained service and session activity, including systemd components, user sessions, PipeWire, and Sommelier.

**Error-level entries**

Filtering with `journalctl -p err` returned entries involving:

- PackageKit update-related errors and timeouts.
- D-Bus disconnection messages.
- Sommelier X11 service startup failures.

These entries identify service-level problems, but do not independently establish malicious activity.

**Crostini-specific activity**

Additional journal entries included `vshd` errors involving `/dev/kmsg` and socket read or receive operations. These were observed in the ChromeOS Linux environment and should be interpreted in that context.

**Login and reboot history**

The `last` command displayed recorded system boot and reboot history. The `who` command returned no currently logged-in users at the time it was run.

**Failed-login records**

Running `lastb` without elevated permissions returned a permission-denied message. Running `sudo lastb` succeeded, but no failed-login records were displayed in the available output.

### 5. Investigation Limitations

- The current account could not access all journal messages.
- Access to the `btmp` record required elevated permissions.
- No displayed failed-login records does not prove that no failed login attempts ever occurred.
- Crostini service errors may reflect the virtualized environment rather than a security incident.
- The investigation did not establish unauthorized access or a confirmed compromise.

### 6. Conclusion

The investigation demonstrated practical Linux log review, error filtering, account-history inspection, and permission-aware troubleshooting.

The available evidence showed system and service errors, recorded boot history, and no failed-login records in the displayed `lastb` output.

**Final assessment:** No confirmed security breach was established from the records examined.

### 7. Skills Demonstrated

- Linux command-line investigation
- System journal analysis
- Error filtering and review
- Authentication-history inspection
- Privilege-aware log access
- Evidence-based reporting
- Documentation of investigative limitations
