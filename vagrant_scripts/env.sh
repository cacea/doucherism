echo 'Exporting DB ENV VAR'

if ! (source /etc/profile; [[ $DATABASE_URL ]]);
then echo 'export DATABASE_URL="postgres://postgres:password@localhost:5432/postgres"' >> /etc/profile;
fi
