# Description
This tool adds the following key-combinations for rectangular and curly brackets for Mac OS (Macbook):

- CMD + 8 = {
- CMD + 9 = }
- CMD + SHIFT + 8 = [
- CMD + SHIFT + 9 = ]


# Installation:
1. 
```bash
brew install python
python3 -m pip install --uprade pip
python3 -m pip install pynput
git pull 
```
2. System Settings -> Privacy & Security -> Accessibility:
   - Add your terminal here.
3. System Settings -> Privacy & Security -> Input Monitoring:
   - Add your terminal here.

# Start / Stop the Script:
```bash
./keymap-start.sh
./keymap-stop.sh
```

# Advice:
1. Write an Alias for the .sh scripts.
   That way you don't have to enter the directory every time you wanna start it.
- keymap-start
- keymap-stop


# Motivation:
I hate using 5 + 6 for the rectangular brackets.
It disturbs my flow when coding.

I just haven't found a good solution anywhere for that.
Either its some third-party-software that is not open-source while wanting full access to ALL my keyboard-input => Eh, no :D
Or it just wasn't working the way I wanted it to..

I bound those keys on 8 / 9 because the "normal" brackets => () are mapped on those keys.
You can just change the python script if you want to remap those.

If you have security concerns regarding the permissions you give to the terminal:
- You can check the python script -> It's basically just a pynput script that creates the new keybinds. There is no traffic going out to anywhere.
- If you're really sceptical, you could use the default terminal installed on Mac.
- If you're super sceptical; Copy the idea, write your own variant.

# Troubleshoots:
- .sh files are not excecutable:
```bash
sudo chmod a+x ./keymap-start.sh
sudo chmod a+x ./keymap-stop.sh
```
