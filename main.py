import os
import sys
import datetime
from dateutil import parser

DATE_FORMAT="%Y-%m-%d"
TIMESTAMP_FORMAT="%Y-%m-%dT%H:%M:%S %Z"

def read_log(log):
    """
    Parse a log file and return a dictionary of logs
    """
    with open(log,'r') as f:
        contents=f.readlines()
    blanks=0
    log_dict={} 

    for line in contents:
        if line == '\n':
            # encountered a blank line
            blanks+=1
            continue
        if blanks == 2:
            # encountered a date
            date=parser.parse(line.strip('\n'))
            date=date.strftime(DATE_FORMAT)
            log_dict.update({date: {}})
            blanks=0 
        elif blanks == 1: 
            # encountered an entry timestamp
            timestamp=parser.parse(line.strip('\n'))
            timestamp=timestamp.strftime(TIMESTAMP_FORMAT)
            log_dict[date].update({timestamp :''})
            blanks=0
        elif blanks == 0:
            # encountered entry message
            log_dict[date][timestamp]+=line
    return log_dict
        

def write_log(log_dict,log):
    """
    Write the log dictionary as a caplog.txt file 
    """
    log_dict = dict(sorted(log_dict.items()))
    with open(log, 'w') as f:
        for date,entries in log_dict.items():
            f.write('\n')
            f.write('\n')
            f.write(date+'\n')
            for entry_timestamp,entry_message in entries.items():
                f.write('\n')
                f.write(entry_timestamp + '\n')
                f.write(entry_message)

def validate_log(log):
    """
    Validate the log file and raises an exception for syntax or parsing error
    """
    try:
        if not os.path.exists(log):
            with open(log,'w') as f:
                print("Log file doesn't exist. Creating an empty file..")
                return True
        with open(log,'r') as f:
            contents=f.readlines()
        blanks=0
        date=False
        timestamp=False
        expect_nonblank=False
        
        for line in contents:
            if line == '\n': 
                if expect_nonblank:
                    raise Exception("Syntax error: Log entry text cannot be empty")
                blanks+=1  #count the blanks
                continue
                
            expect_nonblank=False
            
            if blanks == 2:
                # expect a date
                parser.parse(line.strip('\n'))
                blanks=0
                date=True
                timestamp=False
            elif blanks == 1:
                # expect an entry timestamp
                if not date:
                    raise Exception("Syntax error: No date associated with this entry : " + line)
                parser.parse(line.strip('\n'))
                blanks=0
                timestamp=True
                expect_nonblank=True
            elif blanks == 0:
                # expect an entry text
                if not timestamp:
                    raise Exception("Syntax error: No timestamp associated with this entry :"+line)
            elif blanks > 2:
                raise Exception("Syntax error: Too many blank lines")
    except Exception as e:
        print(str(e))
        return False
    except ParseError as e:
        print(str(e))
        print("Expecting a date or a timestamp at this line")
        return False
    return True

def add_entry(log):
    """
    Add an entry to the log. Calls validate_log(), read_log() and write_log()
    """
    if not validate_log(log):
        print("invalid log file. Exiting..")
        return 
    log_dict=read_log(log)
    today=datetime.date.today()
    today = today.strftime(DATE_FORMAT)
    entry_date = input(f"Enter the entry date (Press enter to accept the default {today}) :")
    if entry_date == '':
        entry_date = today
    else:
        entry_date = parser.parse(entry_date)
        entry_date = entry_date.strftime(DATE_FORMAT)
        
    entry_message = input("Enter the entry message (empty line to exit) :")
    if entry_message == '':
        print("Error: log entry cannot be empty. Exiting...") 
        exit()
    inp = [] 
    while entry_message != '':
        inp.append(entry_message) 
        entry_message=input()
    entry_message="\n".join(inp) + '\n'
    
    entry_timestamp = datetime.datetime.now(tz=datetime.timezone.utc)

    entry_timestamp = entry_timestamp.strftime(TIMESTAMP_FORMAT)
    
    log_dict.setdefault(entry_date, {})
    log_dict[entry_date].update({entry_timestamp: entry_message})
    
    write_log(log_dict, log)
        
if __name__ == '__main__':
    """ 
    specify the path to the log file as a command line argument
    """
    if len(sys.argv) != 2: 
        print("Invalid arguments. Please specify the path to the log file") 
        exit()
    LOG_FILE=sys.argv[1]


    add_entry(LOG_FILE)