

# Create data dashboards and visualizations for Nebraska Lifespan Respite Network program.# (https://nrrs.ne.gov/respite/data/dashboard_index.php)
Dashboard Features are:

* Centralized data
* Preserve historical data by type and year
* Normalize and process all data types using DHHS-approved business rules
* Collect and apply numerous value-added data elements to ensure consistency
* Operates in a secure computing environment

Data is collected in .csv / excel files. We used Elasticsearch for data indexing, creating data pipeline and visualization.
(https://www.elastic.co/). Elasticsearch is the heart of Elasticstack.
Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. In the initial stage of this project we tried to create dashboards in Splunk software. We were able to migrate some dashboards from the above website using Splunk 6.6.3. Using Elasticsearch we are able to feed new data automatically. We use logstash for creating data pipeline by creating configuration file for each index. Then we use Kibana for data visualization and dashboards.



So we summerize the work as follow:

* Data cleaning using Python programming language
* Develop config file for each dataset to create index in Elasticsearch
* Develop and optimize Big data pipelines using Logstash. 
* Generating Data Visualization and Dashboards using Kibana
* Analyzing data from heterogeneous data sources such as querying multiple tables from Oracle, PostgreSQL databases. 
* Indexing, analyzing unstructured data with Elasticsearch, Logstash and Kibana. 
* Querying indexed data in Dev tool for Data Integration and Aggregation 

# List of Dashboards & Kibana Links #

1. NFOUS (https://ccfl-elk.unl.edu/app/kibana#/dashboard/60970950-8890-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
2. AGING (https://ccfl-elk.unl.edu/app/kibana#/dashboard/64a41f90-b231-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
3. SUBSIDY (https://ccfl-elk.unl.edu/app/kibana#/dashboard/dc1486b0-563c-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
4. CampKesem (Gender&Age) (https://ccfl-elk.unl.edu/app/kibana#/dashboard/4eac4910-b547-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
5. CampKesem (Has your child lost a parent or primary caregiver to cancer?) (https://ccfl-elk.unl.edu/app/kibana#/dashboard/6298aae0-b952-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
6. CampKesem (Participant's Primary and Secondary City) (https://ccfl-elk.unl.edu/app/kibana#/dashboard/4286f920-b54a-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
7. CampKesem ( Number of child attended CampKesem before) (https://ccfl-elk.unl.edu/app/kibana#/dashboard/5e3a2b50-b537-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
8. Medically Handicapped Children's Program (MHCP0 - Disabled Children's Program (DCP) (https://ccfl-elk.unl.edu/app/kibana#/dashboard/14a276f0-70f9-11e9-b6fd-8d7acfd50b3e?_g=(refreshInterval%3A(display%3AOff%2Cpause%3A!f%2Cvalue%3A0)%2Ctime%3A(from%3A'2013-08-15T18%3A27%3A16.632Z'%2Cmode%3Aabsolute%2Cto%3A'2019-08-15T18%3A42%3A16.632Z')))
9. **** Dashboard name starts with DB are for postgres database ***


# Procedure for ingesting data to Elastcisearch and create Dashboard: #
* Process the data (Add Date column, Delete column, merge similar .csv files) then store the data file under ccfl-data folder in ccfl-elk.unl.edu server (/home/snayak/ccfl-data)
* Create logstash configuration file and store it in under logstash folder (/home/snayak/ccfl-elastic/logstash)
* Run the config file inside logstash folder under /usr/share/logstash
* Command to run the config file : sudo bin/logstash -f configurationfilelocation. ,
   Example : sudo bin/logstash -f /home/snayak/ccfl-elastic/logstash/camp.config
* Once the configuration file completly runs, it creat an index in Elasticsearch. The new index can be found in Management tab in Elasticsearch
* Create index pattern at the Management tab in Elasticsearch, at the configuration settings, click at the ****+Create Index Pattern**** In step1 enter the index name and go the next step open the time filter field name dropdown and select @timestamp /Date, then click ****Create index pattern****
* To create visualization, please go to visualize tab in the Elasticsearch and then choose a chart style and select the index. Then save the visualization
* In Dashboard tab, click on the ****+**** sign to add visualizations to the dashboard. Then save the dashboard by entering name in the Title bar and describe about the dahboard in the description box and then save it.


# Adding Logo in the Dashboard #
* Encode the image Logo using any online tool. (https://www.base64-image.de/)
* Choose markdown visualization in elastcisearch and then use below syntax 
* ![imageName] ( data : image/png;base64,encodedImage)
* Once the logo visualization is created add to the dashboard
# Documentation Link #
* https://discuss.elastic.co/t/uploading-images-in-kibana-dashboard/27999
* https://logz.io/blog/kibana-hacks/


