# SRE_ScreenCloud_Challenge
SRE Challenge for screenCloud

## Prerequisites ## 

Install LibreOffice for Windows here:
https://www.libreoffice.org/download/download/

Install Python3, version used at time of writing this "Python 3.8.8", select option Windows installer (64-bit) & add Python ENV var to PATH
https://www.python.org/downloads/release/python-397/

Install VisualStudio Code IDE, select Windows Installer
https://code.visualstudio.com/download

Checkout remote GitHub repository containing source files to run parser
$: git clone https://github.com/michaels0184/SRE_ScreenCloud_Challenge.git

## Run the parser ##

Open VSCode and start a new Terminal session within editior, once open make sure to change directory to remote repo
```bash
$: cd SRE_ScreenCloud_Challenge
```

Now to run the parser, which will parse and format the information from the logfile "sre-challenge" and output results into seperate .csv files within the output dir

```bash
$: python parse_logfile.py
```

## View results ##

Now open any of the .csv files located within the output dir to find relevant results for a specific path contained within the logs. eg "facebook"

- Combined findings using parser (parse_logfile.py)


| Path          | 200 count     | 403 count | 500 count | Total responseTime(ms) | Total no Bytes |
|:-------------|:--------------|:----------|:-----------|:-----------------------|:---------------|
|Facebook      |295            |666        |30          |129051                  |9839302         | 
|Instagram     |0              |0          |570         |17130000                |5801806         |
|Weather       |4328           |43         |1412        |2543298                 |86127640        |
|Profile       |1525           |2          |3           |197031                  |15240137        |
|Upload-media  |275            |0          |0           |2092026                 |413564759       |
|Profle        |745            |28         |72          |451304                  |8370824         |


## SRE Challenge ##

**Where should engineering focus first to reduce errors?**
A: The Weather component has the highest count of 500 internal server error message which could be a number of things on the server side.

**If performance on this box is slow, which service should we investigate first?**
A: Instagram, as this service is having the highest total count of combined responseTime and 2nd highest count of 500 errors.
Instagram also has 0 recorded successfull 200 logs found which is concerning and perhaps timing out causing the high response time. I would then look at the weather application next as it has the second highest responseTime and the highest 500 error message count.


**If we were going to split this application into multiple, what setup might give a good
effort/reward ratio?**
A: Due to the nature of upload-media component, it would be wise to split this into it’s own service potentially on another server as it requires the highest no of combined bytes across compared to other components. It might be good also splitting Weather into it's own MicroService and keeping both Facebook & Instagram as one as they are similar.
