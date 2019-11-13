# NewspaperManager

- Will help Megan to manager her newspaper customers



# Technical documentaion

- NEED the app to be called application in the python file and the file name!
	- Application doesnt work but application doesnt

- to deploy zip requirements.txt and all .py files and upload to elastic beanstalk

- need the application object to be defined before if __name__=="__main__":
- need app.run() after that



- For data base connection to mysql through aws
	- the connection string should go  mysql+pymysql://{username}:{endpoint (without the port number)}/{database name}
	- NOTE: the data base has to all ready be created
	- make sure you run "pip install pymysql"
	- I made sure the security group had incoming IP address set to all (0.0.0.0.0)
		- not sure if this is nesseccary

