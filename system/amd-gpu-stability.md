# AMD GPU Linux Fix

## Relevant Specs
- GPU: AMD Radeon RX 7900XTX (RDNA3 GPU)
- Driver: RADV
- OS: Linux Mint 22.2 Cinnamon
- Kernel: 6.17.0-29-generic
- Display Server: X11

## Problem
When playing certain games, my GPU would crash seemingly at random.

## Details
The games I was having issues with were World of Warcraft, The Division 2, and Lies of P. I am posiive other games would have had the same problem, but these were the only three I experienced the issue with.
This problem was extremely hard to troubleshoot as I was never able to recreate the problem on demand.

## Testing
I looked all over for fixes. Many sources gave me ideas, but none fixed the issue. To make things worse, for each fix i tried, I had to open one of the problem games and let it run for sometimes up to 9 hours before it would freeze. I eventaully found a list of grub commands to try. I applied all of them at once, and the issue has not happened since. I am not sure which variable is the reason for the fix, but as figuring it out could take several days of testing, I have simply accepted that at least one of them is working to prevent it.

## Current Config
1. Add these variables to GRUB_CMDLINE_LINUX_DEFAULT in /etc/default/grub
- amdgpu.gfxoff=0
- amdgpu.runpm=0
- amdgpu.gpu_recovery=1
- amdgpu.tmz=0
- amdgpu.sg_display=0"

Should look like this: `GRUB_CMDLINE_LINUX_DEFAULT="amdgpu.gfxoff=0 amdgpu.runpm=0 amdgpu.gpu_recovery=1 amdgpu.tmz=0 amdgpu.sg_display=0"`

2. Run sudo update-grub after to apply

## Result
This is one of the worst issues I have had and was at the point of requesting an RMA for my GPU. Since adding the variables to my grub config, I have not had any more issues with my GPU.

## Resources
This repo was vital to finding the fix to my issue. A big thank you to [danielrosehill](https://gist.github.com/danielrosehill).
- [A Dummy's Guide to AMD GPU Issues on Linux](https://gist.github.com/danielrosehill/6a531b079906f160911a87dea50e1507#common-symptoms)
