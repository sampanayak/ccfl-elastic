Create data dashboards and visualizations for Nebraska Lifespan Respite Network program. (https://nrrs.ne.gov/respite/data/dashboard_index.php)
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

• Data cleaning using Python programming language
• Develop config file for each index
•	Developing and optimizing Big data pipelines using Logstash. 
•	Generating Data Visualization and Dashboards using Kibana
•	Analyzing data from heterogeneous data sources such as querying multiple tables from Oracle, PostgreSQL databases. 
•	Indexing, analyzing unstructured data with Elasticsearch, Logstash and Kibana. 
• Querying indexed data in Dev tool for Data Integration and Aggregation 




