# FINAL FANTASY VII REBIRTH - Performance Optimization

## Problem
From my research, the problem appears to stem from the fact that SQUARE ENIX uses the proprietary tool "MassiveEnvironment" to render objects within the game. When moving the camera, GPU usage spikes to 100%, resulting in constant freezing, making the game unplayable.

## Fixes Applied
### Mods
- [FFVIIHook](https://www.nexusmods.com/finalfantasy7rebirth/mods/4): Allows editing of Engine.ini.
- [Ultimate Engine Tweaks (UET)](https://www.nexusmods.com/finalfantasy7rebirth/mods/3): A preset for Engine.ini that provides many performance improvements on its own.

Engine.ini location: `~/.steam/steam/steamapps/compatdata/2909400/pfx/drive_c/users/steamuser/Documents/My Games/FINAL FANTASY VII REBIRTH/Saved/Config/WindowsNoEditor/Engine.ini`

### Steam Config
#### Launch Options
`WINEDLLOVERRIDES="d3d9=n,b;dsound=n,b" RADV_PERFTEST=nggc,gpl VKD3D_CONFIG=pipeline_library_app_cache,shader_cache_sync taskset -c 0-15 mangohud gamemoderun %command%`
- `WINEDLLOVERRIDES="d3d9=n,b` is for the dll that ships with FFVIIHook. By default, it is xinput1_3.dll; but I renamed it to d3d9.dll to remove the conflict with controller input.
- `WINEDLLOVERRIDES="dsound=n,b` is needed for FF7RebirthFix.
- `RADV_PERFTEST=nggc` can improve AMD GPU performance in some titles.
- `RADV_PERFTEST=gpl`
- `VKD3D_CONFIG=pipeline_library_app_cache` enables the persistent caching of compiled shader pipelines.
- `VKD3D_CONFIG=shader_cache_sync`
- `taskset -c 0-15` to prevent the game from using the i7-12700K's, slower, E-cores.
- `mangohud` for performance monitoring.
- `gamemoderun` for general performance improvements.
- ~~`-nodirectstorage` bypasses DirectStorage and allows Proton to handle asset streaming. This is done because the game ships with an outdated DirectStorage 1.1.1 DLL.~~ Doesn't seem to help and may even be detrimental. I believe SQUARE ENIX released a patch soon after the PC release to address this issue.

#### Proton
Proton 10.0-4 (Stable)

### In-Game Settings
If you are still having issues, set "Background Model Detail" to low. This will introduce severe pop-in, but the game should run much smoother. Capping the game to 60fps (or even 30 if you can stomach it) should help further as the game will have more time to render each frame.

## Testing
I am still testing different configurations with several LOD mods. Since the lag seems to be occuring when pop-in occurs, I am trying to see if I can effectively eliminate pop-in, therefore eliminating stutter.

## Resources
### Mods
#### Important
- [FFVIIHook](https://www.nexusmods.com/finalfantasy7rebirth/mods/4)
- [FF7RebirthFix](https://www.nexusmods.com/finalfantasy7rebirth/mods/22)

#### Performance
- [Ultimate Engine Tweaks (UET)](https://www.nexusmods.com/finalfantasy7rebirth/mods/3)
- [Fantasy Optimizer](https://www.nexusmods.com/finalfantasy7rebirth/mods/1)

#### LOD
- [LOD Fix - Optimized Clarity](https://www.nexusmods.com/finalfantasy7rebirth/mods/38)
- [Ultimate Graphics Quality Engine Best LOD FPS and Foliage Fix](https://www.nexusmods.com/finalfantasy7rebirth/mods/397)
- [7 Rebirth Engine Tweaks](https://www.nexusmods.com/finalfantasy7rebirth/mods/16)

#### Other
- [FFVII DLSS4-FSR4-XeSS-FrameGen and AVX2 Emulation](https://www.nexusmods.com/finalfantasy7rebirth/mods/15)
- [FF7 Rebirth DX12 Async Compile](https://www.nexusmods.com/finalfantasy7rebirth/mods/2107)

### Info
- [FF7Rebirth PC Optimization Repo](https://github.com/Zenardi/ff7rebirth-pc-optimization)
- [FF7-Rebirth-Optimized-Clarity](https://github.com/marcValdz/FF7-Rebirth-Optimized-Clarity)
