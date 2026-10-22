# Dual Booting Linux and Windows 11

## Hardware
I am working on an MSI [MPG Z690 CARBON WIFI](https://www.msi.com/Motherboard/MPG-Z690-CARBON-WIFI). Many or all of my BIOS keys may be different from yours.

## Note
I think it is easier to setup a bootable USB for Windows 11 if you already have access to a Windows PC. This is because instead of finding a USB writer that works on Linux, and is capable of making a Windows stick, you can just use their [Create Windows 11 Installation Media](https://www.microsoft.com/en-us/software-download/windows11) option. Otherwise, I would recommend using a tool such as [Ventoy](https://github.com/ventoy/Ventoy/releases). Here is Linux Mint's guide for using Ventoy: https://linuxmint-user-guide.readthedocs.io/en/latest/winiso.html. I would also recommend having a separate drive for each OS, but this is not required. If using one drive for both installs, just be extra careful when partitioning. If using two separate drives, I would recommend unplugging any that you are not actively installing to; to avoid sharing EFI system partitions. For this section, I will assume you have access to a Windows PC.

## Installation

### Pre-Install
1. As with anything, it is recommended to create a backup of any important data before making any changes.

2. You may need to disable Secure Boot before making any changes. If you do, remember to re-enable it later as Windows 11 requires it.

3. Make sure you have a USB drive with ample storage (I typically have seen 8GB as the minimum recommended).

4. Download the Windows 11 Media Creation Tool from this page: https://www.microsoft.com/en-us/software-download/windows11.

5. Follow the wizard and you should end up with a bootable USB for Windows 11.

#### If you are installing Windows on the same drive as Linux, read this.
If you are planning to install Windows on the same drive as Linux, I would recommend partitioning that drive now rather than trying to do it from the Windows install wizard. Your Linux Distro likely has an app for viewing and formatting your disks. If you do not have one, are unable to get one, or would simply rather use the terminal, this link may help: https://linuxconfig.org/how-to-partition-a-drive-on-linux.

### Install
1. With the USB plugged in, reboot your computer and enter BIOS.

2. Boot from the USB and follow the Windows 11 installation wizard.

3. You can choose to install Windows on an empty drive or in a partition. I would strongly suggest using a separate drive from the one you are using for Linux (or anything else), if possible.

4. When selecting a drive, ensure that you are not selecting the one that Linux is installed on.

5. From here, you are done, and can unplug the USB, but there are [steps you can take to make the setup more seamless](#setting-up-grub). Otherwise, press F11 on startup to open a menu which will allow you to select your boot.

### From Windows
1. Disable Windows Fast Startup as this prevents proper shutdown and can cause filesystem corruption on shared drives.

2. Check `Settings > Privacy & Security > Device Encryption`, and save the recovery key somewhere off the machine.

### Post-Install
- Run the command `sudo timedatectl set-local-rtc 1` to force Linux to use local time to avoid conflicts with Windows.

You are now done. Windows and Linux are installed and accessible, though probably not in the most ideal way. In my experience, Windows WILL become the primary boot. As a result, you will likely need to enter your boot menu on startup every time you want to use Linux (mine is entered by pressing F11, though yours is likely different).
#### The below method reorders the boot priority so Linux loads first. On some motherboards (including mine) the firmware ignores or resets this change. If that happens on your system, using the boot menu (F11 on MSI) is a reliable alternative.

### Setting Up GRUB
GRUB can be used as a menu for selecting which OS you want to use. It does a great job at making Dual Booting feel more intentional.
1. From Linux, run `sudo apt install os-prober`, then, `update-grub`. This should return:
```
Found Windows Boot Manager on /dev/[drive]`
```

2. Run `sudo nano /etc/default/grub`

3. Change `GRUB_TIMEOUT_STYLE=hidden` to `GRUB_TIMEOUT_STYLE=menu` to show the GRUB menu on boot.

4. Change `GRUB_TIMEOUT=0` to the amount of seconds you would like the menu to show for. You can also set it to `-1` to show indefinitely.

5. Uncomment `GRUB_DISABLE_OS_PROBER=false` to allow scanning for Windows.

6. Press `CTRL + O` (then Enter) then `CTRL + X` to save your changes.

7. Type `sudo update-grub` to apply the changes.
From here, you will need to ensure that your Linux OS is set as the default boot option so that GRUB will appear instead of immediately launching into Windows.

### Setting Up efibootmgr
1. From your Linux terminal, type `sudo efibootmgr -v`. If you have redundant entries, use `sudo efibootmgr -b XXXX -B` to remove one to avoid issues.

2. Take note of BootOrder.

3. To utilize GRUB, Linux needs to be booted first, so set the boot order to Linux -> Windows using `efibootmgr -o XXXX,YYYY,etc.`.

#### Example (the asterisks notate the currently active boot)
#### Check current boot order:
```
user > sudo efibootmgr
BootOrder: 0000,0001
Boot0000 windows
Boot0001* ubuntu
```
#### Rearrange boot order:
```
user > sudo efibootmgr -o 0001,0000
BootOrder: 0001,0000
Boot0000 windows
Boot0001* ubuntu
```
After this, reboot to test. If GRUB boots, it worked. if Windows boots, it did not. You can go back into Linux and run `efibootmgr` again to see if the order was reset. Unfortunately, I have not found a way to fix this. Again, to bypass the need for GRUB, you can look up your motherboards boot menu key to select from there.
