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
I have had this issue occur with several different games.
This problem was extremely hard to troubleshoot as I was never able to recreate the problem on demand.

###Here is an example of a crash log obtained by running `journalctl -b -1` after a crash while playing Red Dead Redemption 2:
```
amdgpu 0000:03:00.0: ring gfx_0.0.0 timeout, signaled seq=170251, emitted seq=170253
amdgpu 0000:03:00.0:  Process RDR2.exe pid 15741 thread RDR2.exe pid 16003
amdgpu 0000:03:00.0: Starting gfx_0.0.0 ring reset
amdgpu 0000:03:00.0: MES failed to respond to msg=RESET
amdgpu 0000:03:00.0: failed to reset legacy queue
amdgpu 0000:03:00.0: reset via MES failed and try pipe reset -110
amdgpu 0000:03:00.0: The CPFW hasn't support pipe reset yet.
amdgpu 0000:03:00.0: Ring gfx_0.0.0 reset failed
amdgpu 0000:03:00.0: GPU reset begin!. Source:  1
amdgpu 0000:03:00.0: MES failed to respond to msg=REMOVE_QUEUE
amdgpu 0000:03:00.0: failed to unmap legacy queue
[drm:gfx_v11_0_cp_gfx_enable.isra.0 [amdgpu]] *ERROR* failed to halt cp gfx

```

## Testing
I looked all over for fixes. Many sources gave me ideas, but none fixed the issue. To make things worse, for each fix i tried, I had to open one of the problem games and let it run for sometimes up to 9 hours before it would freeze. I eventaully found a list of grub commands to try. I applied all of them at once, and the issue has not happened since. I am not sure which variable is the reason for the fix, but as figuring it out could take several days of testing, I have simply accepted that at least one of them is working to prevent it.

## Current Config
1. Add these variables to GRUB_CMDLINE_LINUX_DEFAULT in /etc/default/grub
- amdgpu.gfx_off=0
- amdgpu.runpm=0
- amdgpu.gpu_recovery=1
- amdgpu.tmz=0
- amdgpu.sg_display=0"

Should look like this: `GRUB_CMDLINE_LINUX_DEFAULT="amdgpu.gfx_off=0 amdgpu.runpm=0 amdgpu.gpu_recovery=1 amdgpu.tmz=0 amdgpu.sg_display=0"`

2. Run sudo update-grub after to apply

### Potential Steam Launch Option
~~RADV_DEBUG=nocompute~~

## Result
Since adding the variables to my grub config, my GPU hangs have been reduced drastically.
For RDR2 specifically, I have seemingly fixed the crashes by turning MSAA off (this setting is actually off by default, so you should not have do change anything).

## Resources
This repo was vital to finding the fix to my issue. A big thank you to [danielrosehill](https://gist.github.com/danielrosehill).
- [A Dummy's Guide to AMD GPU Issues on Linux](https://gist.github.com/danielrosehill/6a531b079906f160911a87dea50e1507#common-symptoms)
