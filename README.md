# ccfl-elastic
Date: 11/14/2018
Index Data Directly from the unl box to ElasticStack. Can we directly index data from UNL box to Elastic so that when new data comes it automatically feeds to the perticular Index in Elastic Stack.

Step by step procedure for Subsidy Dashboard

1 - Getting data from the avaibale data source :  \\ccfl-print\answers4families\respite\data_dashboard\Subsidy data
      For subsidy data we have 5 types of .csv file
2- Data Preprocessing: Adding Date column, Merging similar csv files (Done with python scripts) in the  local computer
3- Writing a config file in the local computer
4- Transferring Data to the ccfl-elk server (Path for the data: /home/snayak/ccfl-data/subsidy-data)
5- Transferring config files (Total 5 config files) to the ccfl-elk server (Path for config file: /home/snayak/ccfl-elastic/logstash) 
6- Running the config file to create logstash pipeline for indexing data 
7- Once Data got indexed, create Index pattern in Elasticsearch in the Management tab of the Kibana. For subsidy, we have 5 index patterns.
8- From Index pattern create visualizations. For subsidy data, we have 5 visualizations.
     ActiveClientbyAge
    ActiveClientbyGender
    ActiveClientbyRelationshiptoAuthRep
    ActiveClientbyServiceAreaCounty
   VeteranStatus (Yes/No)
8- Combine all visualization to create aDashboard
