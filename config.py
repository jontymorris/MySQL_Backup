from time import gmtime, strftime

# Folder ID for backup
gdrive_folder_id = "GOOGLE_DRIVE_ID"

# Name of Backup
date_format      = strftime("%Y%m%d%H%M%S", gmtime())
backup_name      = "DBBackup-" + str(date_format) + ".sql"

# DB Creds
db_user = "root"
db_pass = "PASSWORD_HERE"
