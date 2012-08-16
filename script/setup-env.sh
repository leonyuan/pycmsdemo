mkdir -p /tmp/$USER
PYTHON=python2.6

function dump_dbconfig {
    $PYTHON >/tmp/$USER/dbenv <<EOF
    from django.conf import settings
    print "DB_NAME='%s'" % settings.DATABASE_NAME
    print "DB_USER='%s'" % settings.DATABASE_USER
    print "DB_HOST='%s'" % (settings.DATABASE_HOST or 'localhost')
    print "DB_PORT='%s'" % (settings.DATABASE_PORT or 3306)
    print "DB_PASSWD='%s'" % (settings.DATABASE_PASSWORD)

    EOF
        source /tmp/$USER/dbenv
    }
