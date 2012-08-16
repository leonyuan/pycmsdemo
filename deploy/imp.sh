gzip -d -c $1 | mysql -u$2 -p$3 $4
