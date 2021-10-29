## Regex Lifestyle  Class 10/26

Joff Thyer 

https://dev.antisyphontraining.com/regular-expressions-your-new-lifestyle-w-joff-thyer/


## Going over POSIX, BRE, ERE, and PCRE syntax 

BRE(basic regex) ERE(extended regex)

### IP addresses 

From splunk regex 
  regex ip="\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}"

(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)

Matches 250 - 255
Matches 200 – 249
Matches 0 – 199
Disable capturing group behavior. Prior character match is optional


### Linux/Unix 

Grep understand 3 diff versions of regex 

-E for extended 
-P for Perl (PCRE)

Sed 
-E 





### Awk (aho, Weibegererm Kernighan) 
![Awk Regex](/images/Awk_Regex.png)


Searching for the first field, username. .+ is one or more ,the end has to be “bash”
Printing a subscript 1



### Grep

![Grep Regex](/images/grep_regex.png)

Searching for traceroute packets with a low TTL 

<br>
More advanced grep 
![Grep Regex](/images/grep_https.png)

What's called a lookahead for single and double quotes 
?=[‘\“[] at the end of expression means its looking for anything that looks like an https link 

![Grep Regex](/images/grep_advanced_explanation.png)


<br>
### sed

File with weird spaces 
Clean it up with 


<br>
### vim regex 



LOL
:syntax enable
Is pretty cool 

<br>
### PowerShell
		 	 	 				
PowerShell Examples
						
● Search for U.S. SSN in files
						
PS C:\> Get-ChildItem -Path X:\ | Select-String -Pattern '\d\d\d-\d\d-\d\d\d\d’ PS C:\> ’192.168.99.1’ –match ’[\d\.]{7,15}’						
True
						
PS C:\> $m = “My CC number is 1234-4321-9876-1212” PS C:\> $m –replace ‘\d{4}’, ‘xxxx’
My CC number is xxxx-xxxx-xxxx-xxxx 
					
				
			
		


<br>
Javascript support for PCRE 





Bash-regex script in class folder matches on email or IP addresses 
Given an argument, it outputs if it matches 

<br>
### Python Regex 

Import re 
re.findall(r’BHIS’, r’Yee, we love BHIS’)
Would return 
[‘BHIS’]

Experiment with re.findall 

Capture Groups 


Looking for pattern of 4 digits, 2 digits, 2 digits 


Using re.search requires more computing power than re.match. Is there an easy way to test the "cost" of your regex expression?

Not really, besides /bib /time ? test the time of script runtime 


Python, unlike GREP 




Same example as 




Side-by-side


Grep reuters urls
Python reuters urls







<br>
### Log File Analysis with Python 

Opening a file 							
						
The open() method is a built in Python function					 								
	○  Specify a relative or full filename path as the first argument
	○  Specify the file “mode” as the second argument
 																 										
Modes include “r”: read, “w”: write, “a”:append
 									
Modes can be qualified with “t” for text or “b” for binary
								 		
A binary file returns a byte object rather than a UTF8 encoded string.
											
○  open() returns a file handle object which is “iterable”
 											
○  iterable means I can use a loop to read data from the file handle created 

from datetime import datetime

>>> d = datetime.fromtimestamp(1616077207.252)
>>> d.strftime('%Y-%m-%d-%H:%M%S')
'2021-03-18-07:2007'



Course Material 
 "Completed Anti Training" Category will have course material and recording access for 6 months
