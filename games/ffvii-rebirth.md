# FINAL FANTASY VII REBIRTH - Performance Optimization

## Problem
When moving the camera, my GPU usage would spike to 100%, resulting in constant freezing, making the game unplayable.

## Testing
I installed various mods, lowered Background Model Detail in the game's settings, and changed the game's launch options.
Setting Background Model Detail to low in-game seemed to have the most obvious effect, but did not fully fix the issue on its own.
OptiScaler had no effect.
DX12 Async Compile would not work, but from what I understand, the mod cannot work on Linux as stated by Phroster, the mod's creator: "But Proton as far as I know uses the same d3d12.dll to translate to Vulkan, so this .dll won't work in combination with that."
UET and Fantasy Optimizer did not seem to have any noticable effect on my game, but they did not hurt it at all either.

## Current Config
I believe that the true fix was adding one of these variables to UET's Engine.ini file:
[/Script/Engine.StreamingSettings]
s.EventDrivenLoaderEnabled=1

[ConsoleVariables]
r.Streaming.MaxTempMemoryAllowed=256
r.MipMapLODBias=-1
foliage.LODDistanceScale=0.5
r.SkeletalMeshLODBias=1

I have not done further testing, so I cannot confirm which variable is responsible.

In my current config:
- My launch options are WINEDLLOVERRIDES="dxgi=n,b" RADV_PERFTEST=nggc VKD3D_CONFIG=pipeline_library_app_cache mangohud gamemoderun %command% -nodirectstorage.
- I have FFVIIHook, Ultimate Engine Tweaks (with added variables in Engine.ini), and Fantasy Optimizer installed.
- My Proton version is Valve's Proton 10 Stable.
- Background Model Detail is set to low in-game.

## Result
With my current config, I am seeing GPU usage up to 85% rather than 100%. Freezes/stuttering has seemingly stopped, though my testing is not yet thorough.
All of this has been done within the starting location Nibelheim.

## Resources
- [FF7Rebirth PC Optimization Repo](https://github.com/Zenardi/ff7rebirth-pc-optimization)
- [FFVIIHook](https://www.nexusmods.com/finalfantasy7rebirth/mods/4)
- [Ultimate Engine Tweaks (UET)](https://www.nexusmods.com/finalfantasy7rebirth/mods/3)
- [Fantasy Optimizer](https://www.nexusmods.com/finalfantasy7rebirth/mods/1)
- [FFVII DLSS4-FSR4-XeSS-FrameGen and AVX2 Emulation](https://www.nexusmods.com/finalfantasy7rebirth/mods/15)
- [FF7 Rebirth DX12 Async Compile](https://www.nexusmods.com/finalfantasy7rebirth/mods/2107)
