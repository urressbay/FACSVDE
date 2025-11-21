# FACSVDE
FortiAnalyzer CSV Data Explorer - Specifically, large web filter logs exported from FortiAnalyzer. 

#Introducing FortiAnalyzer CSV Data Explorer (FACSVDE)

#Problem:

I needed a solution to review monthly weblogs that are being captured by FortiAnalyzer.  One of the limitations of it is 5 million rows.  So when trying to run a report for the month, I was not getting all the data.  So I started to extract all of the data weekly, as this is under the 5 million row limit.  The problem is that the files are too large for Excel to read, and creating multiple different unique filters and creating multiple reports was cumbersome, thus the creation of FACSVDE.  This tool imports an extracted webfilter extract for a week, and allows me to slice and dice the data based on user, category or source IP address.  It also allows me to preview the data prior to exporting the smaller files needed for audit purposes.  For example, who clicked what in the phishing category?  Then switch it to what else did that IP click on?  What about my admin accounts, why are they browsing the web with elevated privileges?  I was able to find this and more very quickly thanks to the power of python pandas.  

#This is my 1st attempt at creating a Python program, so please be kind. Constructive feedback is welcome!

#Key Features:
  *Read and analyze large exported logs from fortianalizer, select and open a large file, and let it do the heavy lifting.
  *Preview - 10 rows of selected filtered data before exporting.
  *Click the load file again, without having to wait for the data to change category or user info!
  *Find what the users have been up to by user name.
  *Searching by category displays in the console a list of all unique categories found.

#Usernames should be in ALL CAPS!  The problem is that computer accounts have the 1st part lowered...still working on creating an exception for workstation names.
