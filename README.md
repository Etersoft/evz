
== EVZ ==

evz operates in console with follow autodetected engines:
 * vzctl (OpenVZ)
 * docker (Docker)
 * qm (QEMU/PVE)
 * pct (LXC)
 * vboxmanage (VirtualBox)
 
Just use the same command for any virtualization system.

Examples:

 evz list
  N1
  N2

 evz start N1

 evz show N1

 evz enter N1

and so on.
