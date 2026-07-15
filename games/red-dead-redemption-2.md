# Red Dead Redemption 2

## Problem
While the game runs pretty well, it suffers from very small stutters during gameplay. These aren't big enough to ruin the game, but are very annoying, especially throughout a game as big as this one.

## Fix
Open the following file in your prefered editor
```
/mnt/1cc5a8bd-d0fc-48ff-87fd-f548aa872948/SteamLibrary/steamapps/compatdata/1174180/pfx/drive_c/users/steamuser/Documents/Rockstar Games/Red Dead Redemption 2/Settings/system.xml
```
and change the line `<asyncComputeEnabled value="false" />` to `<asyncComputeEnabled value="true" />`

## Result
The stutters should be significantly reduced if not completely gone.

## Resources
- https://www.youtube.com/watch?v=-pRTweQp2uw&t=954s