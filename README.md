# caplog.txt
Caplog.txt is a simple set of rules to format and structure the log entries in a text file. It is both machine-readable and human-readable. 
Since it is plain text, it is future-proof and interoperable with different applications. 

# semantics

The following are the semantics of caplog.txt :

* A log is a text file that contains the log entries. 
* An entry is a basic unit of information contained in a log. 
* An entry consists of two parts - Timestamp, Message 
* Entry timestamp indicates the time at which the entry is made. The first line of an entry must be a timestamp. 
* Entry message contains the actual message of the entry. It can contain one or more non-blank lines of text. It cannot be empty. 
* One or more entries are grouped together under a date. 
* Timestamp should be precisely the time of the log entry. It should not be possible to record an entry with a past timestamp. 
* Entries can be made for the past dates retroactively. Although the current timestamp goes with those entries. Therefore it is valid to have a future timestamp with a past date entry. 

# syntax 

One or more blank lines are used to delimit different parts of the log.

* Each date must be preceded by exactly two blank lines.
* Each entry timestamp must be preceded by exactly one blank line. 
* Entry message cannot be empty. It cannot contain a blank line. 

## Structure 


DATE1

ENTRY TIMESTAMP1
ENTRY TEXT1

TIMESTAMP2
ENTRY TEXT2


DATE2

ENTRY TIMESTAMP3
ENTRY TEXT3

TIMESTAMP4
ENTRY TEXT4

