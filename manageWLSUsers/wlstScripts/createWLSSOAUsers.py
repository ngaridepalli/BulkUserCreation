# Script Name   :	createWLSSOAUsers.py


##---------------------------------------------------------
# NOTES
##---------------------------------------------------------
#	1.  	...
#
##---------------------------------------------------------

##---------------------------------------------------------
# DO NOT EDIT BELOW THIS LINE UNLESS ADVISED BY SUPPORT
##---------------------------------------------------------

# -- Usage of arguments per getopt import (http://davidmichaelkarr.blogspot.com/2008/10/make-wlst-scripts-more-flexible-with.html) --
def usage():
    print "Usage:"
    print "Must be used from the install command only"


# -- Connect to WLS Server --
def connectToWLSAdmin():
	try:
		connect(adminUserName, adminPassword, adminURL)
		print('Successfully connected')
	except:
		print 'Unable to find admin server...'
		exit()


		

# -- Generate Users Application --
def createUserLoop() :
	try:
	
		i = int(userNamePrefixNumberStart)
		#for i in range(1000):
		while (i <= int(userNamePrefixNumberFinish)):
			userToCreate = userNamePrefix + "%s" % str(i).zfill(int(useZeroPaddingCount))
			print userToCreate
			dauth=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
			dauth.createUser( userToCreate , userPassword, 'User for SOA: ' + userToCreate + ' (password: ' + userPassword + ')')
			print "created..."
			dauth.addMemberToGroup(groupToAssignUsers, userToCreate)
			print "added to group " + groupToAssignUsers + "..."
			
			print "updating some user attributes"
			dauth.setUserAttributeValue( userToCreate, 'preferredlanguage', 'EN-US') 
			dauth.setUserAttributeValue( userToCreate, 'displayname', 'Mr. ' + userToCreate) 
			
			### // if adding to a application role directly
			###if len(appRoleToAssignUsers) > 1
			###	grantAppRole("obi", groupToAssignUsers, "weblogic.security.principal.WLSUserImpl", userToCreate)
			
			i = i + 1
			print "User Created"
			
	except:
		print "Exception Occurred.  The user showing above most likely already exists. Check the security realm."



###############     Main Script   #####################################
#if __name__ == "__main__":
#    import sys
import sys
import getopt

adminURL=sys.argv[1]
adminUserName=sys.argv[2]
adminPassword=sys.argv[3]
createOrRemove=sys.argv[4]
userNamePrefix=sys.argv[5]
userPassword=sys.argv[6]
userNamePrefixNumberStart=sys.argv[7]
userNamePrefixNumberFinish=sys.argv[8]
groupToAssignUsers=sys.argv[9]
useZeroPaddingCount=sys.argv[10]



print "[INFO] Starting Script"
connectToWLSAdmin()


print "[INFO] Creating Users..."
createUserLoop()


print "[INFO] Disconnecting..."
disconnect()

print "[INFO] End WLST Work"
####################################
