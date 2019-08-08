
********Please go to the Raw option for better readable format.*******

# Create data dashboards and visualizations for Nebraska Lifespan Respite Network program.# (https://nrrs.ne.gov/respite/data/dashboard_index.php)
Dashboard Features are:

1- Centralized data
2- Preserve historical data by type and year
3- Normalize and process all data types using DHHS-approved business rules
4- Collect and apply numerous value-added data elements to ensure consistency
5- Operates in a secure computing environment

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


#Adding Logo in the markdown#

https://discuss.elastic.co/t/uploading-images-in-kibana-dashboard/27999
https://logz.io/blog/kibana-hacks/

# Procedure to inject data to elastcisearch and create Dashboard: #
* Process the data (Add Date column, Delete column, merge similar .csv files) then store the data file under ccfl-data folder in ccfl-elk.unl.edu server (/home/snayak/ccfl-data)
* Create logstash configuration file and store it in under logstash folder (/home/snayak/ccfl-elastic/logstash)
* Run the config file inside logstash folder under /usr/share/logstash
* Command to run the config file : sudo bin/logstash -f configurationfilelocation
   Example : sudo bin/logstash -f /home/snayak/ccfl-elastic/logstash/camp.config
* Once the logstash file completly run it creat an index in Elasticsearch
* To create visualization/dashboard we need to create index pattern at the Management tab in Elasticsearch
* Create visualization under visualize tab in the Elasticsearch and then combine all visualization to create Dashboards

