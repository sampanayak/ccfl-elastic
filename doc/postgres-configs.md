# Set up PostgreSQL connectors and Elasticsearch indexing

## Install the Logstash JDBC input plugin
First install the Logstash JDBC input plugins using:
```bash
cd /usr/share/logstash/
sudo bin/logstash-plugin install logstash-input-jdbc
```

## Download the PostgreSQL JDBC drivers
Download the JDBC drivers from PostgreSQL website from https://jdbc.postgresql.org/

## Logstash configuration example for _reading_ a remote PostgreSQL database
```javascript
input {
    jdbc {
        jdbc_connection_string => "jdbc:postgresql://<URI>:<PORT>/<DB>"
        jdbc_user => "<DBUSER>"
	jdbc_password => "<DBPASS>"

        jdbc_driver_library => "<PATH_TO_JDBC_DRIVER.jar>"
        jdbc_driver_class => "org.postgresql.Driver"

	# Query Statement
        statement => "SELECT * FROM TABLE"
    }
}
output {
    stdout { codec => json_lines }
}
```

## Logstash configuration example for _indexing_ a PostgreSQL database 
```javascript
input {
    jdbc {
        jdbc_connection_string => "jdbc:postgresql://<URI>:<PORT>/<DB>"
        jdbc_user => "<DBUSER>"
        jdbc_password => "<DBPASS>"

        jdbc_driver_library => "<PATH_TO_JDBC_DRIVER.jar>"
        jdbc_driver_class => "org.postgresql.Driver"

        # Query Statement
        statement => "SELECT * FROM TABLE"
    }
}

output {
    elasticsearch {
#	protocol => http
        index => "indexname"
#	document_type => "Doc Type"
#	document_id => "%{uid}"
        hosts => "http://localhost:9200"
    }
    stdout { codec => json_lines }
}
```

