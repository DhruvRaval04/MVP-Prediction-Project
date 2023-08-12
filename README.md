# MVP-Prediction-Project

This is a comprehensive project designed to predict an MVP for the NBA season given particular data. It relies on multiple ML models, that use both incremental learning
and traditional learning in order to be able to predict the MVP. 

The 'gatherstats' and 'teststats' are python files written by me, that webscrape data using the website : https://www.basketball-reference.com/, and compile them into csv files for data analysis. 'testmvp', 'testmvp2', 'trainmvp' and 'trainmvp2' are also scrapers that use Beautiful Soup to extract all the MVPS of every season of the NBA from 1960 to 2019. The reason for splitting up the scraper into all these files is due to a firewall on the website, which bans an IP for one minute if it access the website more than 1000 times per minute. Splitting it up, allows the program to get all the data without running into the firewall. It is important to run all these scrapers to collect the data required. 

All the csv files will be autocreated once you run the scrapers, the ones that are present can be deleted, but function as examples to reference. 

Ignore the files 'basketballreftop50scores...' and 'trialanderror' as they are simply old versions and are present as references for further improvement of the model.

Once the data is gather, make sure to run either the 'model' file or the 'model2.0/3.0' file. I have currently only written about 3 ML models that predict using this data, but I'm sure you can use any type of classification learning model for this discrete data set. These files also include all the pre-processing and data cleaning required. 


