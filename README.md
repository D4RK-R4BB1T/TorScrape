## TOR SCRAPE: A HIDDEN SERVICE ARCHIVE TOOL
[![](https://files.catbox.moe/utcpus.png)](https://files.catbox.moe/utcpus.png)

---
Welcome everyone for the long overdue edition to the Evil Rabbit Security Inc. Toolbox. Slimmed down and will need some tweaks and your attention to ensure functionality and stability.

## Features:
- Supports Tor & Clear Net Services
- Can bypass 403 Client forbidden since it piggy backs off the browser
- Is immune to CloudFlare WAF 
- Protected Content maybe saved on the fly

## How to use:

**BEFORE YOU EVEN START: OPEN YOUR WEB BROWSER, NAVIGATE TO YOUR SETTINGS AND FIND THE "ASK BEFORE SAVING PROMPT" ENABLE IT IF IT'S OFF.
GO TO ANY PAGE, PRESS CTRL S AND SELECT "WEB PAGE COMPLETE" AND NOT "WEB PAGE, HTML ONLY" **

**THIS WILL SAVE YOU A LOT OF HEADACHES IF YOU WISH TO FULLY ACHIEVE GREATNESS. YOU MAY NEED TO DO SOME "ADDITIONAL WORK" BUT THIS IS JUST FOR FUNCTIONALITY FOR NOW.**


1. Open the script in whatever editor you like (I use VSCODE but anything works)
2. Proceed to edit pathing. for BASE_DIRECTORY to where you wish to save your files
3. Edit the TXT file path to whatever text file you've got your links in
4. Save the script and run it.
5. Enter the base URL without subdomains, http/https or / 
6. Jump back into tor right after you hit enter 
7. Sit back, Relax and pay attention to your script
8. Check files

WINDOWS USERS: It's THERE IS A DOUBLE SLASH IN THE PATHING E.G. C:\ \ (I ADDED A SPACE BC GITHUB ISN'T COOPERATING) NOT C:\ please ensure your pathing is correct. (X = WHATEVER YOU'D WANT IT TO BE)

## Extra tips & Info:
1. Use [Link Gopher](http://https://addons.mozilla.org/en-US/firefox/addon/link-gopher/ "Link Gopher") (I know extentions and tor are bad but you're not doing anything illegal) Just make sure you enable "Allow in Private Tabs" or this won't work

2. Sometime after you're done with saving it maybe a great thing to check the HTML for JavaScript, External files like fonts and etc. These may improve functionality

3. At the time the script does not allow a user to change links within the HTML file which i a pain in the ass. Either wait for us to create a working python script that utilizes BeautifulSoup4 to manage said issue or create your own.

4. The Script is able to bypass CF & 403 Client Forbidden due to it using the browser to automate the tasks and yes, Selenium * exists * but it's garbage since it's detected by CloudFlare really quickly and configuring Tor to work with it isn't fun.

5. Logins & Protected content you can actually bypaass this because if you're authorized/having an account on something it does work. Now DRM and HLS Content may not render or be saved there is tools for this and we do have a working one that Utilizes BS4 to deal with it some specific HTML snippits using BS4 and RE to target and begin downloading MP4 files amongst other things.

# Known issues:
- May Double Save (Increase time/pay attention to it)
- Can sometimes attempt to save despite having numerous file explorer tabs open leading to a mass confussion 
- May attempt to save the first page instead of loading the correct page
