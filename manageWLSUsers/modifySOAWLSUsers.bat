@ECHO OFF
SETLOCAL
goto endcomment

# Script Name  :	modifyOBIEEHOLUsers.bat


##---------------------------------------------------------
# NOTES
##---------------------------------------------------------
#	1.  	...
#
##---------------------------------------------------------

REM ===================================
REM Modify SOA Users AutoMagically
REM ===================================

:endcomment

set createOrRemove=remove 
set wlsURL=t3://localhost:7001
set wlsUser=weblogic
set wlsPassword=welcome1
set namePrefix=SOA
set namePassword=welcome1
set prefixStartNum=1
set prefixFinishNum=10
set userGroupAssign=WLSGroup
set useZeroPaddingCount=0
set fmwHome=C:\SOA12c\Middleware\Oracle_Home


REM C:/Oracle/FMW/oracle_common/common/bin

call %fmwHome%/oracle_common/common/bin/wlst.cmd wlstScripts/modifyWLSSOAUsers.py %wlsURL% %wlsUser% %wlsPassword% %createOrRemove% %namePrefix% %namePassword% %prefixStartNum% %prefixFinishNum% %userGroupAssign% %useZeroPaddingCount%


ENDLOCAL