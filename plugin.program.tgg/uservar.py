import os, xbmc, xbmcaddon

#########################################################
### Global Variables ####################################
#########################################################
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][COLOR teal]TGG Wizard[/COLOR][/B] Wizard'
BUILDERNAME    = 'TGG'
EXCLUDES       = [ADDON_ID, 'repository.aftermath']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 45
# Text File with build info in it.
BUILDFILE      = 'https://raw.githubusercontent.com/unknownTGG/unknownTGG.github.io/master/plugin.program.tgg/resources/text/builds.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'http://' 
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'
#########################################################

#########################################################
### Theming Menu Items ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://'
ICONMAINT      = 'http://'
ICONSPEED      = 'http://'
ICONAPK        = 'http://'
ICONADDONS     = 'http://'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'http://'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'http://'
ICONSETTINGS   = 'http://'
# Hide the section seperators 'Yes' or 'No'
HIDESPACERS    = 'Yes'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'teal'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']TGG[/COLOR])[/I][/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'Yes'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Aftermath Wizard.\n\nContact us on Github at http://www.github.com/drinfernoo/plugin.program.aftermath/'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'qricon.png')
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### Auto Update                   #######################
###        For Those With No Repo #######################
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = BUILDFILE
#########################################################

#########################################################
### Auto Install                 ########################
###        Repo If Not Installed ########################
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.tgg'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/drinfernoo/repository.aftermath/master/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/drinfernoo/repository.aftermath/master/zips/repository.aftermath/'
#########################################################

#########################################################
### Notification Window #################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = '[B][COLOR teal]TGG Wizard[/COLOR][/B] Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = 'http://'
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = 'http://'
#########################################################
