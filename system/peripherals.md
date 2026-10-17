# Setting up Peripherals

## Corsair
### Tool
For Corsair, I would recommend using [OpenLinkHub](https://github.com/jurkovic-nikola/OpenLinkHub) by [jurkovic-nikola](https://github.com/jurkovic-nikola)
### Setup
1. Install the latest version from https://github.com/jurkovic-nikola/OpenLinkHub
2. Run `sudo systemctl enable OpenLinkHub.service` in the terminal
3. Go to http://localhost:27003 in your browser to edit

## Mouse Settings
### Tool
I use [Piper](https://github.com/libratbag/piper) for my Logitech G502 mouse. The device has onboard memory, so I can usually set it and it stays with the mouse across devices after.
- This software lets you change your mouse DPI, key binds, and lighting all in one.

## Notes
OpenRGB is frequently recommended for lighting changes, but I have had several devices across Corsair and Logitech that are not supported by it. OpenLinkHub works well with all of my corsair devices.