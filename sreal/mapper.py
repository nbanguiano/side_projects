# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 23:47:54 2014

@author: nanguiano
"""

import sys
import pandas as pd

def MapCsv2Html(filename_in, filename_out):
    '''
    This is a very custom helper that can only be used to map a given CSV file into a specific HTML table.
    '''   
    
    # Check file types
    assert '.csv' in filename_in.lower()[-4:], 'Input file type must be CSV'
    assert '.html' in filename_out.lower()[-5:], 'output file should be HTML'
      
    # Reading the CSV file into a data frame
    rawData = pd.read_csv(filename_in, sep=',', skiprows=1)
    
    # Initializing the final HTML content to "nothing" yet
    htmlMetaTable = ''
    
    # Iterating over the CSV rows and creating the HTML table rows
    for i in xrange(len(rawData)):
        htmlMetaTable += '<tr mc:repeatable><td align="center"><table border="0" align="center" width="590" cellpadding="0" cellspacing="0" bgcolor="#ffffff" class="container590"><tr><td><table width="150" border="0" align="left"  cellpadding="0" cellspacing="0" class="container590" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; border:2px solid #ebeae6;"><tr><td align="center"><img editable="true" mc:edit="icon1" width="150" height="70" border="0" style="display: block; width: 150px; height: 70px;" src="http://www.axiscorporate.com/boletines/interna/axisreportandsales/logos/msf.jpg" /></td></tr><tr><td align="center" class="blog-title" style="font-size: 22px; font-family:Arial, sans-serif; mso-line-height-rule: exactly; line-height: 20px;" mc:edit="title1">&nbsp;</td></tr><tr><td align="center" class="blog-title" style="font-size: 22px; font-family:Arial, sans-serif; mso-line-height-rule: exactly; line-height: 20px;" mc:edit="title1"><span style="line-height: 23px; font-family: Arial, Helvetica, sans-serif; color: #ecaa00; font-weight:bold;"> '+rawData.Amount[i]+' € </span></td></tr></table><table border="0" width="4" align="left" cellpadding="0" cellspacing="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;"class="container590 hide-for-iphone"><tr><td height="10" width="4" style="font-size: 10px; line-height: 10px;">&nbsp;</td></tr></table><table border="0" align="right" width="420" cellpadding="0" cellspacing="0" bgcolor="#ffffff" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;" class="container580"><tr><td><table border="0" align="right" width="410" cellpadding="0" cellspacing="0" bgcolor="ffffff" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;" class="container580 gris"><tr><td align="left" mc:edit="title3" bgcolor="#ebe9e7" style="font-size: 15px; font-family:"Trebuchet MS", Arial, Helvetica, sans-serif; line-height: 20px; font-weight:bold; color: #383a3f;">&nbsp; <span style="color: #383a3f; text-decoration: none; outline: none;">'+rawData.Project_Title[i]+'</span></td></tr><tr><td height="10" style="font-size: 10px; line-height: 10px;">&nbsp;</td></tr><tr><td align="left" mc:edit="title111" style="font-size: 12px; line-height: 20px; font-family: Helvetica, Arial, sans-serif; color: #747578;" class="gris container590"><table border="0" width="310" align="left" cellpadding="0" cellspacing="0" class="container590" bgcolor="#ebe9e7"><tr><td style="font-size: 12px; line-height: 12px;">&nbsp;</td><td height="12" style="font-size: 12px; line-height: 12px;">&nbsp;</td></tr><tr><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">&nbsp;</td><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">Country:<span class="pain"> '+rawData.Country[i]+'</span></td></tr><tr><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">&nbsp;</td><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">Sector:<span style="color: #ecaa00"> '+rawData.Sector[i]+'</span></td></tr><tr><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">&nbsp;</td><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">Service Line: <span style="text-decoration:none;color:#ecaa00; font-weight:bold;"> '+rawData.Service_Line[i]+'</span></td></tr><tr><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">&nbsp;</td><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px; font-weight:bold;">&nbsp;</td></tr><tr><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px">&nbsp;</td><td mc:edit="text1" style="color:#383a3f;font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;font-size:11px; font-weight:bold;">&nbsp;</td></tr></table><table border="0" width="90" align="right" cellpadding="0" cellspacing="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;" class="container580 gris" bgcolor="#FFFFFF"><tr><td><table border="0" bgcolor="#ffffff" width="72"  align="center" cellpadding="0" cellspacing="0" style="border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;" ><tr><td align="center" valign="top" class="sidebar"><table border="0" width="72" height="100" align="right" cellpadding="0" cellspacing="0" style="border:1px solid #ebe9e7;" bgcolor="#ebe9e7"><tr><td align="center" valign="top"><img editable="true" mc:edit="incorpo-image" width="75" height="57" border="0" style="display: block; width: 70px; height: 53px;" src="http://www.axiscorporate.com/boletines/interna/axisreportandsales/lideres/jjaques.jpg" alt="" /></td></tr><tr><td mc:edit="text1" align="center" valign="top" style="font-size: 10px; font-family: Helvetica, Arial, sans-serif; color: #383a3f; mso-line-height-rule: exactly; line-height: 14px;"><strong>'+rawData.Consultant1[i]+'</strong></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr><tr mc:repeatable><td align="center" bgcolor="#FFFFFF"><table border="0" cellpadding="0" cellspacing="0"><tr><td align="center" class="main-image">&nbsp;</td></tr></table></td></tr>'
        
    # Writing table into output file
    htmlTable = open(filename_out , "w")
    htmlTable.write(htmlMetaTable)
    htmlTable.close()
    
    # Confimation that everything worked ok
    print 'Your file "%s" should be ready' % filename_out
    
    
    
if __name__ == '__main__':
    args = sys.argv
    print len(args)    
    
    if len(args)!=3:
        print 'Both input and output filenames are mandatory'

    elif len(args) > 3:
        print 'Too many arguments'

    else:
        MapCsv2Html(args[1], args[2])