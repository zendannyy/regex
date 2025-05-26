## Regex Lifestyle  Class 10/26

Joff Thyer 

https://dev.antisyphontraining.com/regular-expressions-your-new-lifestyle-w-joff-thyer/


## Going over POSIX, BRE, ERE, and PCRE syntax 

BRE(basic regex) ERE(extended regex)


## Capture Groups
use () 

vs 

## Char Classes
Character classes try to match ind characters within []. 

use []
Ex: to match 800 or 900 numbers
[8-9]00

Allow for use of ranges [a-zA-Z] [0-9] etc. 

OR is implied 
Ex: To match on an a or an e, use [ae]


Alterations 
Using | to match what is on the lft of the pipe, then will try to match from left ot right.


Caveat is Prefixes

cat vs caterpillar 

cat | dog | bird | caterpillar 

Iteration 
Uses curly braces {}

Ex: 
[0-9]{3}
matches a sequence of 3 numbers, all in one match group.

Non-Capture Groups
(?:pattern)

Ex: 
(?:https?|ftp)://([^/\r\n]+)
in this case, the regex is not looking for https or ftp (protocol), only for // and the rest of pattern

Lookarounds 

Positive Lookeaheads
(Assert that hte regex matches)
Ex: (?=HTML)

Negative Lookaheads
(Assert that the regex does NOT match)
Ex: (?!HTML)

Anchors 

^		Beginning of string 

$ 		End of string


### Modifiers 
(?i)  :disables case sensitivity when matching the pattern (ignore case)
(?m)  :match beyond the end of a line in a string (multiline) . 
It makes ^ and $ match the beginning and end of a line, respectively, instead of matching the beginning and end of the input.
(?s)	:the wildcard ”.” will match line breaks also. (dotall)
(?x)  :known as comment mode or whitespace mode




### Metacharacters
Characters with special meaning

. 	matches ANY single character, zero or more. AKA wildcard

\. matches the period character


"+"      Matches 1 or more repetitions of the preceding character (greedy)

? 		Matches prev character 0 or 1 time.	makes the prev token before the "?" optional. 

+?		Matches character one or more times (non-greedy)

		*?,+?,?? Non-greedy versions of the previous three special characters.

\d	single digit

\D	NOT a single digit

\w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
why would not use \w then?
i.e [A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3} vs \w+@\w+\.\w{1,3} for email addresses

\W		NOT a single word character

\s 		space character (tab, space, newline)

\S 		Not whitespace

\t 		matches tab character

{}		A specified number of occurences of the character within the curly brackets

^		Beginning of string 

$ 		End of string

Ex:
gns
^gns 
vs gns$

234-431-9876
234.431.9876

SSN's
sequence is 3-2-4 
ony digits 
xxx-xx-xxxx

'\d\d\d-\d\d-\d\d\d\d’
## Use Cases

### IP addresses 

From splunk regex 
  regex ip="\d{1,3}.\d{1,3}\.\d{1,3}\.\d{1,3}"

(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)

Matches 250 - 255
Matches 200 – 249
Matches 0 – 199
Disable capturing group behavior. Prior character match is optional

### Card Addresses

Searching on a specific card type

Visa pattern matching 

<img src="/images/visa_regex.png" alt="visa_regex" style="height: 440px;">


Mastercard pattern matching 

<img src="/images/mastercard_regex.png" alt="mastercard_regex" style="height: 420px;">



CSV Data

Looking for anything that is not a comma 
[^ ,]+
anything that is not a newline 

[^ , \n]+

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
![Sed Regex](/images/sed_regex.png)

<br>

### vim regex 

![Vim Regex](/images/vim_regex.png)

LOL
:syntax enable
Is pretty cool. Color codes like an IDE editor would

<br>

### PowerShell
		 	 	 				
PowerShell Examples
						
● Search for U.S. SSN in files
						
PS C:\> Get-ChildItem -Path X:\ | Select-String -Pattern '\d\d\d-\d\d-\d\d\d\d’ PS C:\> ’192.168.99.1’ –match ’[\d\.]{7,15}’						
True
						
PS C:\> $m = “My CC number is 1234-4321-9876-1212” PS C:\> $m –replace ‘\d{4}’, ‘xxxx’
My CC number is xxxx-xxxx-xxxx-xxxx 
					
				
			


<br>

### Javascript support for PCRE 

![JS Regex](/images/JS_Regex.png)



Bash-regex script in class folder matches on email or IP addresses 
Given an argument, it outputs if it matches 

<br>

### Python Regex 

Import re 
re.findall(r’BHIS’, r’Yee, we love BHIS’)
Would return 
[‘BHIS’]

re.findall()
returns all matches for a pattern in the output of a list type

Experiment with re.findall 

Given the string, 'From: using the : char'

Compare the following 
re.findall('^F.+:', x)
vs
re.findall('^F.+?:', x)

The first is using Greedy mode, the second using non-Greedy mode.  

Capture Groups 

![Python Regex](/images/Python_Regex.png)


Looking for pattern of 4 digits, 2 digits, 2 digits 


The re.search() expression scans through a string looking for the first location where the regex pattern produces a match.
The re.match() expression only matches at the beginning of the string.

Using re.search requires more computing power than re.match. Is there an easy way to test the "cost" of your regex expression?

Not really, besides /bib /time ? test the time of script runtime 


Python, unlike GREP 

![Python Regex](/images/Python_unlike_grep.png)


SAME example as 



Side-by-side

Grep reuters urls

![Grep Regex](/images/grep_https.png) 

Python reuters urls 

![Python RE Reuters](/images/Python_grep.png)




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




### Phone number
Through regex101 came up with 
\d\d\d-\d\d\d-\d\d\d\d
and
^\d[-]|((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}$

FWIW GPT came up with this one for the prompt 
write a regex matching against phone numbers with or without parenthesis for the first 3 digits. 
(\d{3})?-?\d{3}-\d{4}


RE2 (Google)
<br>
https://github.com/google/re2/wiki/Syntax