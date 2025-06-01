#!/bin/bash

# Nome del database
DB_NAME="Magazzino_TCP_delega"

# Script MongoDB per creare il database e le collezioni
echo "📁 Creazione database e collezioni..."

mongosh <<EOF
use $DB_NAME
db.createCollection("smartphone")
db.createCollection("laptop")
show collections
EOF

echo "✅ Database '$DB_NAME' creato con le collezioni 'smartphone' e 'laptop'."

#mongo Magazzino_TCP_delega --eval "db.dropDatabase()" to drop the DB
