this is from branch
WebLogic-Automated-Bulk-User-Management
=======================================

Scripts provides a means to automate the creation, etc. of a bulk set of users within the WebLogic Server Default Identity Provider

How-To Use It
-------------
1. Download the Repo using git clone
2. Navigate to the manageWLSUsers directory
3. Edit the createSOAWLSUsers.bat file by updating the local environment variables.  
The naming convention is fairly straightforward.  Updated your WLS admin information your Fusion Middleware (FMWHome) directory.  Also update the variables which indicate the prfix for the new users to be created and the start and finish number of users.
4. Execute createSOAWLSUsers.bat from the command line.
5. Remove (clean up) users by editing the modifySOAWLSUsers.bat file variables and running it from the command line.

