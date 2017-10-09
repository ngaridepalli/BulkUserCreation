# Script Name   :	modifyWLSSOAUsers.py

##---------------------------------------------------------
# NOTES
##---------------------------------------------------------
#	1.  	...
#
##---------------------------------------------------------

##---------------------------------------------------------
# DO NOT EDIT BELOW THIS LINE UNLESS ADVISED BY SUPPORT
##---------------------------------------------------------


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
def modifyUserLoop() :
	try:
	
		i = int(userNamePrefixNumberStart)
		#for i in range(1000):
		while (i <= int(userNamePrefixNumberFinish)):
		
			userToModify = userNamePrefix + "%s" % str(i).zfill(int(useZeroPaddingCount))
			print userToModify
			dauth=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
			
			
			dauth.removeMemberFromGroup(groupToAssignUsers, userToModify)
			print "modify user at group " + groupToAssignUsers + "..."
			
			
			dauth.removeUser(userToModify)
			print "deleted user " + userToModify
			
			
			### // if adding to a application role directly
			###if len(appRoleToAssignUsers) > 1
			###	grantAppRole("obi", groupToAssignUsers, "weblogic.security.principal.WLSUserImpl", userToModify)
			
			
			i = i + 1
			print "User Modified"
			
	except:
		print "Exception Occurred.  The user showing above may have some issues. Check the security realm."



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


print "[INFO] Modifying Users..."
modifyUserLoop()


print "[INFO] Disconnecting..."
disconnect()

print "[INFO] End WLST Work"
####################################
