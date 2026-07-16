# FINAL FANTASY VII REBIRTH - Linux Stutter

## Problem
The problem appears to stem from the fact that SQUARE ENIX uses the proprietary tool "MassiveEnvironment" to render objects within the game. When moving the camera, GPU usage spikes to 100%, resulting in constant freezing, making the game unplayable.

## Current Fix - Working as of 06/14/2026
DX12 Async Shader Compile Mod by Phroster

There are two things that seemed to significantly reduce the stuttering I was experiencing.

- First, I updated my kernel from 6.17 to 7.0. I noticed that many of the positive reports from ProtonDB were running a newer kernel than mine, and it was one of the only differences I could see between my system and theirs. This update mostly solved the problem. While the game is still what I would consider unoptimized, it is now playable.

- Second, after troubleshooting Red Dead Redemption 2 for a while, I discovered that enabling Async Compute fixed most of the stutter I was experiencing in that game. I had seen this mod earlier in my testing, but never tried it as the author said it would not work on linux. After fixing RDR2, I decided to look into this mod again.

Steps:
1. Install the mod [FF7 Rebirth DX12 Async Shader Compile](https://www.nexusmods.com/finalfantasy7rebirth/mods/2107)
2. Extract the file into the following directory: `~/.steam/steam/steamapps/compatdata/2909400/pfx/drive_c/users/steamuser/Documents/My Games/FINAL FANTASY VII REBIRTH/End/Binaries/Win64/`
3. Rename the file to d3d11.dll
4. Add `WINEDLLOVERRIDES="d3d11=n,b"` to the game's launch options

## Previous Attempt

### VKD3D Pipeline Mismatch
FFVII Rebirth stores compiled shader pipelines in the file:
```
~/.steam/steam/steamapps/compatdata/2909400/pfx/drive_c/users/steamuser/Documents/My Games/FINAL FANTASY VII REBIRTH/Saved/D3DDriverByteCodeBlob_V4098_D29772_S0_R0.ushaderprecache
```
 
Under current VKD3D-Proton, this file is created at only 3MB, which is incorrect.
 
This can be confirmed with the following steps:
 
1. Delete `D3DDriverByteCodeBlob_V4098_D29772_S0_R0.ushaderprecache`.
2. Add `PROTON_LOG=1 VKD3D_CONFIG=pipeline_library_log %command%` to the game's launch options.
3. Open the game and allow it to compile shaders.
4. Close the game and check the logs.
 
The log will show:
 
```
Write cache is invalid (hr #887e0001), nuking it.
Cannot load existing on-disk cache due to driver version mismatch.
Loading stream pipeline library (3942224 bytes): Unique VkPipelineCache count: 0
Pipeline "EB9363C19C999E87" does not exist.
```
 
This is the same bug reported in this [vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton/issues/2918) bug report for Wuthering Waves.

### Fixes Applied
Add `pipeline_library_ignore_mismatch_driver` to your `VKD3D_CONFIG` launch option. This tells VKD3D to ignore the driver version mismatch instead of nuking the cache, allowing pipeline objects to actually accumulate between sessions.
 
With this fix, the cache file is allowed to grow beyond 3MB, up to 459MB in my case. This has improved my game's performance, but to be completely transparent, it is still far from perfect.

#### Steam Config
##### Launch Options
```
SteamDeck=0 RADV_PERFTEST=nggc VKD3D_CONFIG=pipeline_library_app_cache,shader_cache_sync,pipeline_library_ignore_mismatch_driver,nodxr VKD3D_FEATURE_LEVEL=12_2 mangohud gamemoderun %command% -nodirectstorage
```
- `SteamDeck=0` prevents the game from applying its Steam Deck performance profile.
- `RADV_PERFTEST=nggc` can improve AMD GPU performance in some titles.
- `RADV_PERFTEST=gpl` enables Graphics Pipeline Library on RADV for faster pipeline compilation.
- `VKD3D_CONFIG=pipeline_library_app_cache` enables the persistent caching of compiled shader pipelines.
- `VKD3D_CONFIG=shader_cache_sync` ensures shader cache writes are synchronized properly
- `VKD3D_CONFIG=pipeline_library_ignore_mismatch_driver` prevents VKD3D from nuking the pipeline cache when it detects a driver version mismatch, allowing the cache to accumulate properly between sessions.
- `VKD3D_CONFIG=nodxr`
- `VKD3D_FEATURE_LEVEL=12_2`
- `mangohud` for performance monitoring.
- `gamemoderun` for general performance improvements.
- `-nodirectstorage` bypasses DirectStorage and allows Proton to handle asset streaming. ~~This is done because the game ships with an outdated DirectStorage 1.1.1 DLL.~~ SQUARE ENIX apparently updated the DirectStorage version soon after the game's launch on PC, but it seems that Proton still handles this better without DirectStorage.

#### In-Game Settings
If you are still having issues, set "Background Model Detail" to low. This will introduce severe pop-in, but the game should run much smoother. I have this setting on Medium. Capping the game to 60fps (or even 30 if you can stomach it) should help further as the game will have more time to render each frame.

### Final Thoughts
I have spent more time trying to troubleshoot this game than I would like to admit. At this point, I believe that the problem is pretty far removed from what I am currently capable of. I would encourage anyone reading this to try these fixes, and to also experiment with the various mods out there for this game. I have tried just about every one of them, but with no success. The issue isn't a performance problem, so while many mods improve performance, they do not address what is happening here. I believe the solution to this problem would lie in an update from SQUARE ENIX or possibly a more mature VKD3D.

## Appendix
### Game Version
1.0.0.5

### Proton
GE-Proton10-34

### Links
- [FF7Rebirth PC Optimization Repo](https://github.com/Zenardi/ff7rebirth-pc-optimization)
- [FF7-Rebirth-Optimized-Clarity](https://github.com/marcValdz/FF7-Rebirth-Optimized-Clarity)
- [VKD3D-Proton Bug Report](https://github.com/HansKristian-Work/vkd3d-proton/issues/2918)
- [FF7 Rebirth DX12 Async Shader Compile](https://www.nexusmods.com/finalfantasy7rebirth/mods/2107)
