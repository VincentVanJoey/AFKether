## AFKether

==== Disclaimer ====

AFKether is intended for fun and personal use only. 
Use at your own risk. While it does not modify game files or memory, using automation software in online competition or competitively in any way may violate the Rivals of Aether 2 TOS or event rulesets.
This was made with the intention of being used OFFLINE, eliminating "the grind" for cosmetics not everyone has time to grind for, not to hurt the online game in any way. 

Use this tool responsibly, SUPPORT THE OFFICIAL RELEASE!!! PLAY RIVALS 2!!!!!!!!!!

(Also I recommend getting the starter bundle! +20% coins goes crazy bonkers mode after even just a bit) 

===================================

### Intro
AFKether is an automated farming tool designed to earn Aether Coins passively in Rivals of Aether 2. Whether you're looking to unlock cosmetics for tournaments, casual play, or for the drip, this is the tool.
I made this tool because I rarely have time to play and wanted a chance to unlock cosmetics that either...
- A: Take a lot of time to grind the Aether Coins/Bucks for
- B: Are only rewarded for character progression for characters I hate playing
- C: Are the favorites of friends/tournament go-ers that I just don't have on my set-up

While an incredibly simple python program, I thought it worked great as something I left on while I was either at work or asleep to get quite the handsome sum of coins.

### How It Works

AFKether uses a virtual input driver ViGEm Bus Driver to simulate a player's ocassonal in-game input when they are AFK farming. It cycles through a set behavior pattern to keep the match going while accumulating coins.
At the same time, I used library wxPython to make a simple GUI where players can click one button after a bit of set-up and just let it run.

In order to use this tool, do the following:

    - Launch Rivals of Aether 2
    - Enter local versus mode
    - Set the match to be:
      - Teams (Team Attack ON),
      - No Stocks
      - Whatever time you'd like (4/5 minutes is the sweetspot)
    - Open P1's slot as a HMN and select any character, set them to RED team
      - NOTE: this character will bet the one that gains exp as it runs
    - Select all three other characters to be lvl 9 CPU Kraggs on BLUE team
    - Click the "HMN" Tag on player 1's portrait and swap yourself to a CPU at lvl 9
    - DO NOT press anything else, just wait on the select screen

    - NOW: in the Tool Window:
     - Match the time you set in minutes on the GUI
     - Hit the Start Loop Button
     - The app should grab focus :)
     - Leave for a while
     - Profit!

### Installation/Building

- Download and extract the latest release executable zip from the Releases page
- Run AFKether.exe (or python afkether.py if using source code)
- If it prompts you to install the driver, do so (Needed to work)

If building the .exe with changes
  - make sure the main logic script runs at least once
  - put the latest exe from [here](https://github.com/nefarius/ViGEmBus/releases/tag/v1.22.0) and include it as a binary when building (see code)

### Current Features

    - Simulated button presses to repeatedly start local CPU vs matches and click through the relevant menus

    - Adjustable match length form 0-10 minutes to mirror the in-game options 

    - Adds a cosmetic calculator that can tell you the collective price of items in Coins/Bucks/USD

    - Allows the current background color to be changed with a HEX picker (and saves!)

    - Includes hyperlinks to important community resources (Dragdown Wiki / NOLT Board) and to this repo


### Dream Features

    - Automating the character selection part at the beginning

    - A little gif picker for your favorite rivals 1 characters' idle animations on the GUI's corner or something


### Third-Party Components

This project includes third-party software:

- [Nefarius Driver](https://github.com/nefarius/ViGEmBus/releases/tag/v1.22.0) – Licensed under the BSD 3-Clause License (see LICENSES/Nefarius-Driver-License.txt)
