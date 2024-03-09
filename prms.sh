#!/bin/bash

parent=Personal_Record_System
chld_cred=credentials
chld_note=notes
backup=backups
zip1='backup_2023-06-13.tar.gzip'
zip2='backup_2023-06-20.tar.gzip'


mkdir $parent
if [ $? = 0 ]
then
	cd $parent
	mkdir $chld_cred; chmod 644 /$child_cred
	cd $chld_cred;touch ./usernames.txt ./passwords.txt ./email_addresses.txt
	cd ..
	mkdir $chld_note;cd $chld_note
	touch personal_notes.txt important_dates.txt
	cd ..
	mkdir $backup #;cd $backup
	tar -zcvf ./$backup/$zip1 ./$chld_cred
	tar -zcvf ./$backup/$zip2 ./$chld_note
	
	exit 0
else
	echo `pwd` :error!!
	exit 1
fi
#
echo `pwd`

