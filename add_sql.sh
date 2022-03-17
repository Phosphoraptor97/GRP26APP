# Construct the URI from the .env
DB_HOST=ec2-34-205-46-149.compute-1.amazonaws.com
DB_NAME=d7ufnr0fb76bhd
DB_USER=yrkwhxgdwlhjle
DB_PORT=5432
DB_PASSWORD=a0b1967e79b01ff4b172b12b9fa1afaeed60d4d0a59b10b0b6480439334602f0

while IFS= read -r line
do
  if [[ $line == DB_HOST* ]]
  then
    DB_HOST=$(cut -d "=" -f2- <<< $line | tr -d \')
  elif [[ $line == DB_NAME* ]]
  then
    DB_NAME=$(cut -d "=" -f2- <<< $line | tr -d \' )
  elif [[ $line == DB_USER* ]]
  then
    DB_USER=$(cut -d "=" -f2- <<< $line | tr -d \' )
  elif [[ $line == DB_PORT* ]]
  then
    DB_PORT=$(cut -d "=" -f2- <<< $line | tr -d \')
  elif [[ $line == DB_PASSWORD* ]]
  then
    DB_PASSWORD=$(cut -d "=" -f2- <<< $line | tr -d \')
  fi
done < ".env"

URI="postgres://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"

# Run the scripts to insert data.
psql ${URI} -f sql/AppStoreClean.sql
psql ${URI} -f sql/AppStoreSchema.sql
psql ${URI} -f sql/AppStoreCustomers.sql
psql ${URI} -f sql/AppStoreGames.sql
psql ${URI} -f sql/AppStoreDownloads.sql
