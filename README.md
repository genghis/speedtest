# Speed Test App

This is straight up robbing the speedtest-cli project, and just saving its results. The important part here is actually the 'Cron' section later, which shows you how to schedule this to run hourly (or whatever).

## Running the app once

Pretty simple, to run you just need to pull down this repo (and have Python3 installed), and run the following.

`python3 -m venv ./` - This creates a Python virtual environment so you don't install dependencies system-wide

`source bin/activate` - This actually gets you up in that venv

`pip3 install -r requirements.txt` - This installs any dependencies from this project (right now that's just speedtest-cli, but who knows!)

`python3 speedy.py` - This actually runs the script. It'll take a little bit to run, so if it looks like it's stalling out, that means it's working.

You can see the results printed ugly in the terminal, but importantly, you can find the topline numbers in `results.txt` and the entirety of the `results_dictionary` (in case your ISP wants more info) in `verbose.txt`

## Cron

Alright, so now that you know your system can run this bad boy.

I'm stealing these instructions from: https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e

From the command line, in the directory you've installed this repo and its virtual environment to, run the following command and paste the results in a notepad or something:

`pwd` 

This gives you the absolute path to your directory. [^1]

[^1]: I'm going to use `[pwd_string]` as a placeholder later, so if `pwd` gives you `/usr/bin/genghis/speedtest`, then `[pwd_string]/bin` would be `usr/bin/genghis/speedtest/bin`

Great! Now, let's do some Cron stuff.

You're gonna run the command below, and then it's gonna open up VIM. Which is dumb but here we are.

`crontab -e`

Now that you're in VIM, hit the `I` key so you can start inserting.

Enter the following (you'll need to fill in the variable I mention above) into the file:

```
SHELL=/bin/bash
0 * * * * cd [pwd_string] && [pwd_string]/bin/python3 [pwd_string]/speed.py
```
(A note! You can change the '0' to be any number between 0 and 59, and that is the minute it will run in each hour.)

Now hit the `esc` key

Type `:w` (that's pre-pended with a colon)

Type `:q` to exit.

MacOs may ask you if you want to give a terminal permission to change your system. Say "Okay" or "yes" or whatever.

Ideally, this then just runs on the hour. WOOOOOOOO!