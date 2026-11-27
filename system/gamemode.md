# Fixing `gamemoderun` Crashes & CPU Thread Throttling

## Summary of the Issue
Using Feral GameMode on Linux with my CPU (**i7-12700K**) can cause severe CPU thread throttling in games and hard startup crashes in specific titles like ***Elden Ring***.

## My Solution: Set a global default and override when necessary.

### 1. Disable Automatic Core Pinning Globally
This should be sufficient in most cases as I think games typically handle my P and E cores just fine.

Create or edit `~/.config/gamemode.ini`:

```
[cpu]
pin_cores=no
```

Restart the GameMode daemon so it reloads the configuration:

```
systemctl --user restart gamemoded
gamemoded -t
```
Ensure gamemoded -t passes all checks. If it does not, you may also need to run `sudo usermod -aG gamemode $USER` first.

### 2. Per-Game CPU Pinning (Optional)
Sometimes, it is recommended to limit the cores a game is using to reduce issues such as stutters.\
\
As an example, let's use ***Dark Souls III***.\
\
I have seen recommendations to disable my CPU's E-cores to fix stuttering in the game.\
My CPU has a total of **20** cores. The first **16** (0-15) are P-cores while the remaining **4** (16-19) are E-cores.\
So, If I wanted the game to only use my P-cores (a fairly common recommendation), I would set `taskset -c 0-15 %command%` in the game's launch options.\
You can, of course, use any combination of cores that you want, but I would not recommend it without cause.
