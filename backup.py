import os
import config

# How to Install
'''
	1. mkdir /var/database_backups
	2. cd /var/database_backups
	3. wget [link](Linux build from https://github.com/prasmussen/gdrive)
	4. sudo -i
	5. chmod +x (NAME OF DOWNLOADED FILE)
	6. mv (NAME OF DOWNLOADED FILE) /usr/local/bin/gdrive
	7. run `gdrive about` and authenticate
'''

def log(msg):
	print(msg)
	file.write("\n" + msg)

file = open('backup.log', 'w+')

log("== " + config.date_format + "==")

if os.system("mysqldump -u'" + config.db_user + "' '-p" + config.db_pass + "' --all-databases > " + config.backup_name) == 0:
	log(config.backup_name + " created successfully!")
	
	# Upload the newly created file to Google Drive 
	if os.system("/usr/local/bin/gdrive upload --parent " + config.gdrive_folder_id + " " + config.backup_name) == 0:
		log("Successfully uploaded " + config.backup_name + " to server")
		# Delete local sql file
		os.remove(config.backup_name)
		log(config.backup_name + " successfully deleted locally")
	else:
		log("Couldn't upload " + config.backup_name + " to server!")
		log("Closing...")
		exit(1)
else:
	log("Error: " +  config.backup_name + " failed to be created")
	log("Closing...")
	exit(1)
