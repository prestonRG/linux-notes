# Steam Launch Options

## Global Variables
For every game i play on steam, at minimum, I use the launch options:
```
mangohud gamemoderun %command%
```

## Inside of %command%
1. `RADV_PERFTEST=nggc` (Next-Gen Geometry Culling)
What it is: Enables the "Primitive Shader" hardware path on RDNA3 cards.

The Function: It identifies and discards "invisible" triangles (geometry behind walls or facing away from the camera) much earlier in the rendering pipeline.

When to use: Use in modern, high-fidelity games with complex environments (RE4 Remake, Cyberpunk, etc.).

The Benefit: Reduces the "Front-end" load on the GPU and stabilizes frame times in mesh-heavy areas.

2. `RADV_DEBUG=nodcc` (Disable Delta Color Compression)
What it is: Turns off the GPU’s internal color data compression.

The Function: Normally, GPUs compress color data to save memory bandwidth. Some game engines (like RDR2) have bugs where this compression causes "checkerboard" artifacts or micro-stutters.

When to use: Only if you see visual glitches (blocks in the sky/shadows) or experience unexplained "memory-related" hitches.

The Benefit: Improves stability/image accuracy in specific buggy engines at the cost of slightly higher VRAM bandwidth usage.

3. `RADV_PERFTEST=transfer_queue` (Hardware-Level Streaming)
What it is: Forces the driver to use the GPU’s dedicated SDMA (System Direct Memory Access) engine.

The Function: It creates a "HOV Lane" for data. It moves textures from your SSD/RAM into VRAM on a secondary hardware path so it doesn't interrupt the main graphics engine while it's drawing frames.

When to use: Use in "Open World" or "Streaming" games where you feel hitches when moving between map zones (traversal stutter).

The Benefit: Decouples asset loading from frame rendering, significantly reducing "stuttering while walking."

4. `taskset -c 0-15` (CPU Affinity / P-Core Pinning)
What it is: A Linux command that restricts a process to specific CPU logical cores.

The Function: On Intel Hybrid CPUs (like your 12700K), it forces the game to stay on the 8 high-performance "P-Cores" and ignores the 4 efficiency "E-Cores."

When to use: Use for games with erratic frame pacing or games that aren't "Hybrid-aware" and accidentally put critical tasks (like hair physics) on slow cores.

The Benefit: Prevents "scheduling stutters" caused by the OS moving game threads between fast and slow cores.

5. `WINE_CPU_TOPOLOGY=8:0,1,2,3,4,5,6,7` only consider for certain games like FROM Software games.

## Outside of %command%
- -gc-max-time-slice=3: This is a Unity-specific tweak that tells the game to perform garbage collection in smaller, more frequent chunks, which can significantly reduce those "rhythmic" stutters
- -force-vulkan: For AMD users on Linux, Vulkan often provides smoother frame pacing than the default DX11-to-Vulkan translation.

### WINEDLLOVERRIDES
If using a mod that adds a .dll file, make sure to use WINEDLLOVERRIDES.
- Example:
1. Mod uses dxgi.dll
2. Add `WINEDLLOVERRIDES=dxgi="n,b" %command%` to launch options
