# Linux Log Hunting & Defensive Operations
## Evidence Transcript

**Source:** Saved terminal session output  
**Environment:** ChromeOS Linux (Crostini)  
**Account:** `leonapacanis725`

This file preserves selected command output from the investigation. Some lines contain `>` because the original terminal capture shortened them. They have not been reconstructed.

### 1. System journal

**Command:** `journalctl`

```text
Hint: You are currently not seeing messages from other users and the system.
      Users in groups 'adm', 'systemd-journal' can see all messages.
      Pass -q to turn off this notice.
Sep 18 20:39:33 penguin systemd[142]: Queued start job for default target default.target.
Sep 18 20:39:33 penguin systemd[142]: Created slice app.slice - Slice.
Sep 18 20:39:33 penguin systemd[142]: Reached target paths.target - Paths.
Sep 18 20:39:33 penguin systemd[142]: Reached target timers.target - Timers.
Sep 18 20:39:33 penguin systemd[142]: Reached target basic.target - Basic System.
Sep 18 20:39:33 penguin systemd[142]: Started pipewire.service - PipeWire Multimedia Serv>
```

### 2. Recent journal entries

**Command:** `journalctl -n 20`

```text
Nov 06 17:24:36 penguin sudo[17305]: pam_unix(sudo:session): session opened for user root>
Nov 06 17:25:01 penguin garcon[283]: [283]: sftp: accepted connection from vsock:2:325755>
Nov 06 17:25:01 penguin garcon[283]: [283]: sftp: forked child process
Nov 06 17:25:12 penguin sudo[17305]: pam_unix(sudo:session): session closed for user root
Nov 06 17:25:15 penguin garcon[283]: [283]: PackageKit GetUpdates transaction has complet>
Nov 06 17:42:57 penguin garcon[283]: [283]: Received request to launch vshd in container
Nov 06 17:42:57 penguin vshd[17752]: Failed to open /dev/kmsg: No such file or directory >
Nov 06 17:42:57 penguin vshd[17752]: vshd started
Nov 06 17:49:50 penguin vshd[13416]: Failed to read message from socket
Nov 06 17:49:50 penguin vshd[13416]: Failed to receive message from client: Success (0)
```

### 3. Error-priority entries

**Command:** `journalctl -p err`

```text
Sep 18 20:45:38 penguin garcon[274]: [274]: Error occurred with GetUpdates: PackageKit D->
Sep 18 20:52:04 penguin garcon[274]: [274]: Timeout waiting on Linux package info
Oct 03 18:07:58 penguin garcon[283]: [283]: D-Bus connection was disconnected. Aborting.
Oct 05 16:54:13 penguin vshd[4555]: Failed to read message from socket
Oct 05 19:31:28 penguin systemd[142]: Failed to start sommelier-x@0.service - X11 sommeli>
Oct 05 19:31:28 penguin systemd[142]: Failed to start sommelier-x@1.service - X11 sommeli>
Oct 06 16:33:50 penguin systemd[142]: Failed to start sommelier-x@1.service - X11 sommeli>
```

The original output contained additional repeated Sommelier startup errors.

### 4. Date-filtered journal entries

**Command:** `journalctl --since today`

```text
Nov 06 17:24:36 penguin garcon[283]: [283]: Refreshing the remote repository packages
Nov 06 17:24:36 penguin sudo[17305]: pam_unix(sudo:session): session opened for user root>
Nov 06 17:25:01 penguin garcon[283]: [283]: sftp: forked child process
Nov 06 17:25:12 penguin sudo[17305]: pam_unix(sudo:session): session closed for user root
Nov 06 17:25:12 penguin garcon[283]: [283]: Successfully performed refresh of package cache
Nov 06 17:25:15 penguin garcon[283]: [283]: PackageKit GetUpdates transaction has completed with 0 available managed updates
Nov 06 17:42:57 penguin vshd[17752]: Failed to open /dev/kmsg: No such file or directory (2)
Nov 06 17:42:57 penguin vshd[17752]: vshd started
Nov 06 17:49:50 penguin vshd[13416]: Failed to read message from socket
```

### 5. Login and reboot history

**Command:** `last -n 10`

```text
reboot   system boot  6.6.30-02726-gb8 Wed Oct 28 18:26   still running
reboot   system boot  6.6.30-02726-gb8 Tue Oct  6 17:21   still running
reboot   system boot  6.6.30-02726-gb8 Sat Oct  3 18:10   still running
reboot   system boot  6.6.30-02726-gb8 Wed Sep 30 17:40   still running
reboot   system boot  6.6.30-02726-gb8 Sat Sep 19 17:54   still running
reboot   system boot  6.6.30-02726-gb8 Fri Sep 18 20:39   still running

wtmp begins Fri Sep 18 20:39:28 2026
```

### 6. Current session check

**Command:** `who`

```text
leonapacanis725@penguin:~$ who
leonapacanis725@penguin:~$
```

No logged-in users were displayed.

### 7. Failed-login record inspection

**Command:** `lastb`

```text
lastb: cannot open /var/log/btmp: Permission denied
```

**Command:** `sudo lastb`

```text
btmp begins Fri Sep 18 20:39:22 2026
```

No failed-login records were displayed.

### 8. Account verification

**Command:** `whoami`

```text
leonapacanis725
```

### Evidence handling notes

- These are excerpts from the saved terminal output, not simulated events.
- Truncated lines remain visibly truncated.
- The failed-login output contains no displayed entries; this does not establish that failed attempts never occurred.
- The unsuccessful `grep` command using the placeholder filename `some-log-file` is excluded from the investigation evidence.
- Interpret service errors in the context of ChromeOS Linux (Crostini).
