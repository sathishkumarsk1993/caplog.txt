# caplog.txt

Caplog.txt is a simple set of rules to format and structure the log entries in a text file. It is both machine-readable and human-readable. 
Since it is plain text, it is future-proof and interoperable with multiple applications. 

Log entries are important not just for the captains of starships but for everyone who wishes to have a record of their personal or work life. Caplog.txt provides a system to capture time-based logs that can be referenced later. To boldly go where no one has gone before, it is vital to have a record of events in a format that will never go obsolete in the future.  

( The sample log is filled with log entries from Star Trek: The Next Generation)

# Semantics

The following are the semantics of caplog.txt :

* A log is a text file that contains the log entries. 
* An entry is a basic unit of information contained in a log. 
* An entry consists of two parts - Timestamp, Message 
* The entry timestamp indicates the time at which the entry is made. The first line of an entry must be a timestamp. 
* The entry message contains the actual message of the entry. It can contain one or more non-blank lines of text. It immediately follows the timestamp and cannot be empty. 
* Each entry is associated with exactly one date. A date can be associated with one or more entries.  Each date appears once in a log and it precedes the associated entries. 
* Timestamp should be precisely the time the entry is made. It is unconventional to log an entry with a custom timestamp. 
* However, log entries can be made for the past dates retroactively. The current timestamp goes with those entries. Therefore it is valid to have a log entry for a past date with a future timestamp. 

# Syntax

One or more blank lines are used to delimit different parts of the log.

* Each date must be preceded by exactly two blank lines.
* Each entry must be preceded by exactly one blank line. 
* Entry message cannot be empty. It cannot contain a blank line. 

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