# caplog.txt

Caplog.txt is an open-source, plaintext syntax for formating and structuring log entries in a logbook. It is both machine-readable and human-readable. 
It is future-proof and interoperable with multiple implementations, including on a paper-based logbook. 

Logbooks are important not just for the captains of starships but for everyone who wishes to have a record of their personal or work life. Caplog.txt enables the users to write time-based logs that can be referenced later. To boldly go where no one has gone before, it is important to store our daily logs in a format that will never go obsolete in the future.  

( The sample logbook is filled with log entries from Star Trek: The Next Generation)

https://medium.com/@sathishstarlord/caplog-txt-a-simple-plaintext-future-proof-personal-logging-format-19cb5cdcfb4a

# Semantics

The following are the semantics of caplog.txt :

* A 'Logbook' is a text file that contains the log entries. 
* A 'log entry' or 'entry' is a basic unit of information contained in a logbook. 
* To 'log an entry' means to add an entry to a logbook. 
* An entry consists of two parts - Timestamp, Message 
* Timestamp indicates the time at which the entry was logged. The first line of an entry must always be a timestamp. 
* Message indicates the actual message of the entry. It can contain one or more non-blank lines of text. It immediately follows the timestamp and cannot be empty. 
* The related entries are grouped together under a Date. Each entry must be associated with exactly one date. A date can be associated with multiple entries.  Each date appears once in a log in its own line and it precedes the associated entries. 
* Timestamp must always be the time at which the entry was logged. It is unconventional to log an entry with a custom timestamp. However, log entries can be made for the past dates retroactively. The current timestamp goes with those entries. 

# Syntax

One or more blank lines are used to delimit different parts of the log.

* Each date must be preceded by exactly two blank lines.
* Each entry must be preceded by exactly one blank line. 
* Entry message cannot be empty. It also cannot contain a blank line within it. 

## Structure

```text
DATE1

ENTRY TIMESTAMP1
ENTRY MESSAGE1

ENTRY TIMESTAMP2
ENTRY MESSAGE2


DATE2

ENTRY TIMESTAMP3
ENTRY MESSAGE3

ENTRY TIMESTAMP4
ENTRY MESSAGE4
```

![caplog semantics](./caplog%20semantics.png)

# Implementation

A reference implementation in python is provided in this repository. Python3 is required. The script uses os, datetime, dateutil, sys modules from the standard library.

Pass the path of the log file as the argument in the command line.

```python
python main.py /home/user/caplog.txt
```

A new file file is created if it does not exist. If the given file already exists, the file is validated and parsed into a dict object. A new entry is received from the user interactively in the command line and is written into the log file. 

```
Enter the entry date (Press enter to accept the default 2022-09-18) :
Enter the entry message (empty line to exit) :Hello World!
This is my first log entry.
I am going to maintain my logs in caplog.txt format
```

The caplog.txt emphasises on the syntax and semantics of the log. Therefore it is possible to develop applications for a variety of platforms in any language of choice, that adhere to the specifications. 

# License

Refer LICENSE file for license information. 
