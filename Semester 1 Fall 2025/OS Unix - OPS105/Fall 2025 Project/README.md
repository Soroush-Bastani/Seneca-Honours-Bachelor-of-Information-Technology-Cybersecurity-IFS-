\# Initial Project Spec



\## Virtual Machines \& Networking



\- Install \*\*Kali (Graphical Desktop)\*\* in a VirtualBox VM.

\- Change network settings of VMs created during the first six weeks from \*\*CIDR /30\*\* (glue network) to \*\*CIDR /29\*\* (smallest multi-host network).

\- Add the \*\*Kali VirtualBox VM\*\* as a node within the \*\*CIDR /29\*\* network.

&nbsp; - After Kali is added, the internal network will consist of:

&nbsp;   - Two nodes

&nbsp;   - One gateway



\### Kali Configuration



Configure Kali to:



\- Run in \*\*full screen\*\* after boot and user login.

\- Have \*\*Internet access only when the gateway VM is running\*\* and configured to route traffic to the internal network.



\### Go Pro



\- Configure your gateway VM to run \*\*Minimal Ubuntu Server LTS 24.04\*\* in \*\*VirtualBox stealth mode\*\*.

&nbsp; - Stealth mode has \*\*no graphical window\*\* on the host OS (Windows/macOS/Linux).

&nbsp; - Startup and shutdown of VMs are managed using \*\*VirtualBox command-line utilities\*\*.



---



\## OpenSSH Server and MySeneca User Account



\- Install \*\*OpenSSH server\*\* on the gateway VM.

\- Configure OpenSSH to \*\*disallow SSH connections from the root user\*\*.

\- On \*\*all VMs\*\*, create an \*\*unprivileged (non-root) user\*\* that matches your \*\*MySeneca username\*\*.

\- Verify that the MySeneca-named user can:

&nbsp; - Log in to the gateway VM from node VMs’ graphical desktops (Ubuntu and Kali)

&nbsp; - Log in to `matrix.senecapolytechnic.ca` when \*\*GlobalProtect VPN\*\* is running and connected to \*\*Student VPN\*\* on the host OS



\### Go Pro



\- Configure the MySeneca-named user to log in to the gateway (Minimal Ubuntu Server LTS 24.04) \*\*without a password\*\*  

&nbsp; \*(Hint: research password-less SSH access)\*



---



\## Using `sudo`



\- Confirm availability of the `sudo` package; install it if missing.

\- Configure the MySeneca-named user to run administrative commands using `sudo`.

\- Using `sudo`, log in as the MySeneca-named user and:

&nbsp; - Bring packages \*\*up to date\*\*

&nbsp; - Complete all other privileged tasks below

\- Understand why using `sudo` is better than using `su` and `su -`.



---



\## File Sharing Network



\- Create a \*\*file-sharing server\*\* for users on this network.

\- Create the following users on \*\*all three VMs\*\*:

&nbsp; - `alice`

&nbsp; - `bob`

&nbsp; - `cyan`

&nbsp; - \*MySeneca-named user\*

\- There are \*\*four users total\*\*, excluding `root`.



\### Groups



Create three groups:



\- `attack`

\- `defend`

\- `opsec`



Group membership:



\- \*\*MySeneca-named user\*\*

&nbsp; - Member of: `MySeneca-named group`, `attack`, `defend`, `opsec`

\- \*\*alice\*\*

&nbsp; - Member of: `alice`, `attack`

\- \*\*bob\*\*

&nbsp; - Member of: `bob`, `defend`

\- \*\*cyan\*\*

&nbsp; - Member of: `cyan`, `opsec`



---



\## SSH \& `/pub` Directory



\- Log in as each user on all three VMs.

\- Configure the SSH server on the gateway so that:

&nbsp; - `alice`, `bob`, `cyan`, and the MySeneca-named user can \*\*upload to and download from\*\* the `/pub` directory.



\### Access Testing



\- Log in as `bob` on the gateway and attempt to:

&nbsp; - Read from and write to files created by `alice` and `cyan` in `/pub`

\- Repeat the process by logging in as:

&nbsp; - `cyan`

&nbsp; - `alice`

&nbsp; - MySeneca-named user



---



\## Permission Scenarios



\### Scenario 1



\- `bob` can \*\*read but not write\*\* to `/pub/alice.txt` (owned by `alice`).

\- `bob` and `alice` can read but not write to each other’s files.

\- `cyan` cannot read or write any files owned by `alice` or `bob`.

\- `cyan` wants read/write access to files owned by `alice` or `bob`.



\### Scenario 2



\- `alice` can \*\*write but not read\*\* `/pub/bob.txt`.

\- `bob` and `alice` can write to some of each other’s files.

\- Neither `bob` nor `alice` can:

&nbsp; - Read

&nbsp; - Delete

&nbsp; - Modify files they do not own

\- `cyan` cannot read or write any files owned by `alice` or `bob`.



\### Scenario 3



\- `cyan` attempts any and all means to access other users’ files.

\- Configure permissions so:

&nbsp; - `cyan` can \*\*only read and write files owned by cyan\*\*

&nbsp; - `cyan` cannot access files owned by others



\### Scenario 4



\- The MySeneca-named user:

&nbsp; - Is a member of `attack`, `defend`, and `opsec`

&nbsp; - Has \*\*read/write access\*\* to files permitted by those groups



\### Ownership Rule



\- `alice`, `bob`, and the MySeneca-named user \*\*cannot change permissions\*\* on files they do not own.

&nbsp; - Example: If `/pub/bob.txt` is owned by `bob`, neither `alice` nor the MySeneca-named user can change its permissions.



---



\## Go Pro: Bash Scripting



\- Complete the lab on \*\*Bash scripting\*\* when available.

\- Copy your Bash script and name it `publish.bash`.

\- Modify `publish.bash` so that:



\### Script Behavior



\- \*\*No arguments\*\*  

&nbsp; - Display a usage message and exit

\- \*\*One argument that is not an existing file\*\*  

&nbsp; - Display an error message using the argument and exit

\- \*\*One argument that is an existing file\*\*  

&nbsp; - Copy the file to `/pub` on the gateway

\- \*\*Multiple arguments (some files)\*\*  

&nbsp; - Copy valid files to `/pub`

&nbsp; - Display error messages for invalid arguments

\- \*\*Multiple arguments (all files)\*\*  

&nbsp; - Copy all files to `/pub`



\### Environment Configuration



\- Configure login shells so `$HOME/bin` is included in `$PATH`.

\- Place `publish.bash` in `$HOME/bin` for each user on:

&nbsp; - Ubuntu VM

&nbsp; - Kali VM

\- Personalize `publish.bash` per user.

&nbsp; - Example:  

&nbsp;   - If `alice` uploads a file meant to be shared with `bob` but not `cyan`, modify `publish.bash` in `alice`’s `$HOME/bin` to:

&nbsp;     - Verify correct permissions

&nbsp;     - Warn `alice` if permissions are incorrect



---



\## Tips



\### Kali



\- \*\*Tip #1:\*\* When creating your Kali VM, allocate:

&nbsp; - At least \*\*2048 MB RAM\*\*

&nbsp; - \*\*2 virtual CPUs\*\*

&nbsp; - \*\*32 GB disk space\*\*



\- \*\*Tip #2:\*\* When running the gateway in stealth mode:

&nbsp; - Use VirtualBox CLI commands to \*\*start\*\* the VM

&nbsp; - \*\*Shut down the gateway from inside the VM itself\*\*

&nbsp;   - Do not shut it down using VirtualBox CLI or GUI on the host

&nbsp;   - SSH into the gateway from Windows, Ubuntu, or Kali before shutting it down



---



\*\*End of project spec\*\*



