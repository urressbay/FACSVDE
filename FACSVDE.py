#Introducing FortiAnalyzer CSV Data Explorer (FACSVDE)

#Are you tired of manually sifting through massive amounts of log data from your FortiAnalyzer? Do you 
#wish you had an easier way to analyze and visualize and export small specific subsets of the large datasets, so you can quickly identify trends, 
#patterns, and potential security threats?

#Look no further! This tool is designed specifically for reading and analyzing FortiAnalyzer 
#exported data - perfect for managing and monitoring your network's activity over a specific period of 
#time. Whether it's a week's worth of data or a month's worth, our app makes it easy to navigate and 
#extract insights from large datasets.  Fortianalyzer exports top out at 5 million rows.  

#Key Features:
#Read and analize large exported logs from fortianalizer, and select open large file and let it do the heavy lifting.
#Preview - 10 rows of selected filtered data prior to exporting.
#Click load file again, without having to wait for the data to change category or user info!
#Find what the users have been up to by user name.
#Searching by category displays in the console a list of all unquie categories found.

####APP START####

#Import & Print Panda's
import pandas as pd
print("Panda's Version:", pd.__version__)  #Print Pandas Version

#Import Tkinter
import tkinter
import os

#Function: Create a tracker for file load once, filter many
global dfTrack
dfTrack = None

#Function:  Export Filtered content to CSV
def export_to_csv():
    filename = filedialog.asksaveasfilename(defaultextension=".csv", 
filetypes=[("CSV Files", "*.csv")])
    if filename:
        user_output.to_csv(filename, index=False)


#Define Variables
filepath = ""
user_filter = ""
user_output = ""

#Function:  Preview Data In App Window
def show_output():
    # Insert the CSV data into the Text widget
    output_text.insert("1.0", preview)

#Function:  Get Username Prompt
def get_username():
    return sd.askstring("User Input", "Enter Username:", parent=window)  # Open a dialog box

#Function:  Get requested category desc prompt
def get_category():
    return sd.askstring("User Input", "Enter Category:", parent=window)  # Open a dialog box

#Function:  Get requested srcIP prompt
def get_srcIP():
    return sd.askstring("User Input", "Enter SrcIP:", parent=window)  # Open a dialog box

#Function: Close App
def closeApp():
    import sys
    sys.exit()

#Function: Open file - also change filters
def Openfile():
    global user_output
    global preview
    global cat_filter
    global dfTrack
    global all_header
    all_header = ""
    #Load Selected file one time:
    if dfTrack == None:
        filepath = filedialog.askopenfilename()
        print(filepath)
        print("Currently Reading File...")
        global df
        df = pd.read_csv(filepath,sep=',',dtype='unicode',index_col=False)
        dfTrack = 1
    #for row labeling - check the output of columns
    print(df.columns) #prints the index
    colsplit = ",".join(df.columns)  #Splits the index into values as a string
    print(colsplit) #prints the new string
    colsplit = colsplit.split(",")
    for col in colsplit:
        #print(f"Processing: {col}")
        col_header = col.split("=")
        col_header = col_header[0]
        all_header +=  col_header  + ","
    print("All Headers:")
    all_header = all_header[:-1]
    #all_header = all_header + "]"
    print(all_header)
    
    
    #Define Column Headers for Webfilter Results File:
    #df.columns = ["itime","date","time","devid","vd","type","subtype","action","agent","authserver","bid","cat","catdesc","unnamed:13","unnamed:14","unnamed:15","devname","direction","dstcountry","dstepid","dsteuid","dstintf","dstintfrole","dstip","dstport","dstuuid","dvid","epid","euid","unname:28","eventtime","eventtype","Unnamed:32","unnamed:33","hostname","httpmethod","id","level","logid","logver","msg","policyid","policytype","poluuid","profile","proto","reatemethod","rcvdbyte","referenalurl","reqtype","sentbyte","service","sessionid","srccountry","unnamed:54","srcintf","srcintfrole","srcip","srcport","srcuuid","tz","unnamed:61","unnamed:62","url","unnamed64","unnamed65","unnamed66","user"]
    df.columns = all_header.split(",")
    #Samples of failed ones:
    #df = pd.read_csv(filepath,sep=',',dtype="unicode",index_col=["itime", 'date', 'time','devid', 'vd', 'type','subtype','action','agent','authserver','bid', 'cat','catdesc', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15','devname','direction','dstcountry', 'dstepid', 'dsteuid','dstintf', 'dstintfrole', 'dstip','dstport', 'dstuuid','dvid', 'epid','Unnamed: 28', 'euid','eventtime', 'eventtype','Unnamed: 32', 'Unnamed: 33', 'hostname','httpmethod','id','level','logid', 'logver','msg=', 'policyid','policytype','poluuid','profile', 'proto', 'ratemethod', 'rcvdbyte','referralurl', 'reqtype','sentbyte', 'service', 'sessionid','srccountry', 'Unnamed', 'srcintf','srcintfrole', 'srcip', 'srcport','srcuuid', 'tz','Unnamed: 61', 'Unnamed: 62','url','Unnamed: 64','Unnamed: 65','Unnamed: 66', 'user'])
    #df.columns=["itime", 'date', 'time','devid', 'vd', 'type','subtype','action','agent','authserver','bid', 'cat','catdesc', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15','devname','direction','dstcountry', 'dstepid', 'dsteuid','dstintf', 'dstintfrole', 'dstip','dstport', 'dstuuid','dvid', 'epid','Unnamed: 28', 'euid','eventtime', 'eventtype','Unnamed: 32', 'Unnamed: 33', 'hostname','httpmethod','id','level','logid', 'logver','msg=', 'policyid','policytype','poluuid','profile', 'proto', 'ratemethod', 'rcvdbyte','referralurl', 'reqtype','sentbyte', 'service', 'sessionid','srccountry', 'Unnamed', 'srcintf','srcintfrole', 'srcip', 'srcport','srcuuid', 'tz','Unnamed: 61', 'Unnamed: 62','url','Unnamed: 64','Unnamed: 65','Unnamed: 66', 'user']

    #Show were we are in the code:
    print("Displaying Results:")

    #Printing Examples:    
    #print(df.to_string())  #Prints all data
    #print(df.info)
    #print(df.head)
    #print(df.tail)
    #print(user_filter)
    #print(df.sum)
    #print(set(df['catdesc="Information Technology"'])) #List unique columns based on name

    #Define Preview Data:
    preview = (df.iloc[0:10]).to_string() #print top 10 rows

    #Grab User Filter Input if radio button is set to user
    if radio_var.get() == 0:
        username = get_username()
        #username = username.upper()
        username = "user=" + '"' + username + '"'
        print(username)
        user_filter = df[df["user"]== username] #Filter User
        user_output = (user_filter[["srcip","user","date","url","catdesc","action"]])  #LimitColunms
        uniqueCatDesc = df['user'].drop_duplicates().unique()
        print(uniqueCatDesc)
        preview = (user_output.iloc[0:10]).to_string() #print top 10 rows
    if radio_var.get() == 1:
        #Grab Category Filter Input if radio button is set to category
        catFilter = get_category()
        catFilter = "catdesc=" + '"' + catFilter + '"'
        print(catFilter)
        user_filter = df[df["catdesc"]== catFilter] #Filter Category
        user_output = (user_filter[["srcip","user","date","url","catdesc","action"]])  #LimitColunms
        uniqueCatDesc = df['catdesc'].drop_duplicates().unique()
        print(uniqueCatDesc)
        preview = (user_output.iloc[0:10]).to_string() #print top 10 rows
    if radio_var.get() == 2:
        #Grab Category Filter Input if radio button is set to category
        catFilter = get_srcIP()
        catFilter = "srcip=" + '"' + catFilter + '"'
        print(catFilter)
        user_filter = df[df["srcip"]== catFilter] #Filter Category
        user_output = (user_filter[["srcip","user","date","url","catdesc","action"]])  #LimitColunms
        uniqueCatDesc = df['srcip'].drop_duplicates().unique()
        print(uniqueCatDesc)
        preview = (user_output.iloc[0:10]).to_string() #print top 10 rows

#GUI Open Dialog File Selector Single Box with a single button
#GUI Imports
from tkinter import Tk,filedialog, Label, Button, ttk
from tkinter import simpledialog as sd

#GUI Create Winodw
window = Tk()

#GUI Set Title & Size
window.wm_title("FortiAnalyzer CSV Data Explorer")
window.geometry("800x600")

#GUI Open Button - Runs the core application
openButton = Button(text="Open Large CSV",command=Openfile)

#GUI Close Button - Closes the app
closeButton = Button(text="Close This App",command=closeApp)

#GUI Show Button - Displays the preview text
showButton = Button(text="Show Sample CSV Ouput",command=show_output)

#GUI Export Button - Exports selected data to CSV
export_button = Button(text="Export to Filtered Data to CSV", command=export_to_csv)

#GUI Creates an area for preview data to show up
output_label = Label(window, text="")
output_text = tkinter.Text(window, width=80, height=20)

#Radio Button
global radio_var
radio_var = tkinter.IntVar(value=0)  # Initialize the variable to 0, corresponding to "User" filter
filter_by_user_radio = ttk.Radiobutton(
    window,
    text="Filter by User",
    variable=radio_var,
    value=0
)
filter_by_categorydesc_radio = ttk.Radiobutton(
    window,
    text="Filter by Category Desc",
    variable=radio_var,
    value=1
)
filter_by_srcIPradio = ttk.Radiobutton(
    window,
    text="Filter by Source IP",
    variable=radio_var,
    value=2
)
#Load Packs (GUI Widgets)
filter_by_user_radio.pack(),filter_by_categorydesc_radio.pack(),filter_by_srcIPradio.pack(),output_text.pack(),openButton.pack(),closeButton.pack(),showButton.pack(),output_label.pack(),export_button.pack()

#Starts the GUI app
window.mainloop()


