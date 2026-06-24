# FINAL FANTASY VII REBIRTH - Performance Optimization

## Problem
From my research, the problem appears to stem from the fact that SQUARE ENIX uses the proprietary tool "MassiveEnvironment" to render objects within the game. When moving the camera, GPU usage spikes to 100%, resulting in constant freezing, making the game unplayable.

## Fixes Applied
### Prerequisites
- [FFVIIHook](https://www.nexusmods.com/finalfantasy7rebirth/mods/4): Allows editing of Engine.ini.
- [Ultimate Engine Tweaks (UET)](https://www.nexusmods.com/finalfantasy7rebirth/mods/3): A preset for Engine.ini that provides many performance improvements on its own.

Engine.ini location: `~/.steam/steam/steamapps/compatdata/2909400/pfx/drive_c/users/steamuser/Documents/My Games/FINAL FANTASY VII REBIRTH/Saved/Config/WindowsNoEditor/Engine.ini`


### Changes made to UET's Engine.ini
Custom changes made to Engine.ini:
```
[/Script/Engine.StreamingSettings]
s.EventDrivenLoaderEnabled=1 ; Redundant as UE4 supposedly already does this.
s.LevelStreamingActorsUpdateTimeLimit=10.0

[ConsoleVariables]
r.Streaming.PoolSize=12288
r.Streaming.MassiveEnvironmentPoolSizeMB=10240
r.Streaming.MaxTempMemoryAllowed=1024
foliage.LODDistanceScale=1
r.MassiveEnvironment.CoverageLODScale=1
r.Streaming.MaxNumTexturesToStreamPerFrame=200
r.RenderTargetPoolMin=6144
```
- Removed PoolSizeVRAMPercentage=60 and replaced it with r.Streaming.PoolSize=12288.
- Changed s.AsyncLoadingTimeLimit=3.0 to 10 in both locations.
- Changed r.IO.UseDirectStorage=1 to r.IO.UseDirectStorage=0
- Changed r.Streaming.LimitPoolSizeToVRAM=1 to r.Streaming.LimitPoolSizeToVRAM=0

I would recommend adding these to the bottom of their respective sections, but it should be fine either way.

#### IMPORTANT
If you make any changes to Engine.ini, be sure to make it read-only before launching the game. The game WILL overwrite the file.

### Steam Config
#### Launch Options
`WINEDLLOVERRIDES="dxgi=n,b" RADV_PERFTEST=nggc VKD3D_CONFIG=pipeline_library_app_cache mangohud gamemoderun %command% -nodirectstorage`
- `WINEDLLOVERRIDES="dxgi=n,b` is for the dll that ships with FFVIIHook. By default, it is xinput1_3.dll; but I renamed it to dxgi.dll to remove the conflict with controller input.
- `RADV_PERFTEST=nggc` can improve AMD GPU performance in some titles.
- `VKD3D_CONFIG=pipeline_library_app_cache` enables the persistent caching of compiled shader pipelines.
- `-nodirectstorage` bypasses DirectStorage and allows Proton to handle asset streaming. This is done because the game ships with an outdated DirectStorage 1.1.1 DLL.

#### Proton
Proton 10.0-4 (Stable)

### In-Game Settings
If you are still having issues, set "Background Model Detail" to low. This will introduce severe pop-in, but the game should run much smoother. Capping the game to 60fps (or even 30 if you can stomach it) should help further as the game will have more time to render each frame.

## Result
With my current config, I am seeing GPU usage up to 85% rather than 100%. Freezes/stuttering has seemingly stopped, though my testing is not yet thorough.
~~All of this has been done within the starting location Nibelheim.~~ After playing through the first chapter of the game, I can say that the game is still heavily bound by the Background Model Detail setting. for the smoothest experience, I have to set it to low, though this causes some of the worst pop-in i have ever seen in a game.

## Resources
- [FF7Rebirth PC Optimization Repo](https://github.com/Zenardi/ff7rebirth-pc-optimization)
- [FFVIIHook](https://www.nexusmods.com/finalfantasy7rebirth/mods/4)
- [Ultimate Engine Tweaks (UET)](https://www.nexusmods.com/finalfantasy7rebirth/mods/3)
- [Fantasy Optimizer](https://www.nexusmods.com/finalfantasy7rebirth/mods/1)
- [FFVII DLSS4-FSR4-XeSS-FrameGen and AVX2 Emulation](https://www.nexusmods.com/finalfantasy7rebirth/mods/15)
- [FF7 Rebirth DX12 Async Compile](https://www.nexusmods.com/finalfantasy7rebirth/mods/2107)
