mysqldump -u$1 -p$2 $3 | gzip > $3-`date +%Y%m%d%H%M`.sql.gz
