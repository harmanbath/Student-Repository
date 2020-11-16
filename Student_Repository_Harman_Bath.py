
from datetime import datetime
from datetime import timedelta
from typing import Tuple,List,Iterator,Dict
import os
from prettytable import PrettyTable


"""
Part 1: Date Arithmetic
"""
def date_arithmetic() -> Tuple[datetime, datetime, int]:

    # 1.1 What is the date three days after Feb 27, 2000
    date_1 = datetime.strptime("Feb 27, 2020", '%b %d, %Y')
    three_days_after_02272020: datetime = date_1 + timedelta(days = 3)

    # 1.2 What is the date three days after Feb 27, 2019
    date_2 = datetime.strptime("Feb 27, 2019", '%b %d, %Y')
    three_days_after_02272019: datetime = date_2 + timedelta(days = 3)

    # 1.3 How many days passed between Feb 1, 2019 and Sep 30, 2019
    date_3 = datetime.strptime("Feb 1, 2019", '%b %d, %Y')
    date_4 = datetime.strptime("Sep 30, 2019", '%b %d, %Y')
    days_passed_02012019_09302019: int = (date_4 - date_3).days
    
    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019
    


"""
Part 2: Field separated file reader
Reading text files with a fixed number of fields, separated by a pre-defined character. 
Write a generator function to read text files and return all of the values on a single 
line on each call to next(). 
"""
def file_reader(path, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    """
    parameters: 
    path: the file to be read
    fields: the number of fields to be expected for each line
    sep: to specify the field separator, defaults: comma
    header: to specify if the first line in the file is a header line, default: False
    """
    try:
        fp = open(path)
    except FileNotFoundError:
        print("Invalid file path!", path)
    else:
        line_number = 0
        with fp:
            for line in fp:
                line_number =+ 1
                try:
                    seperate_line = tuple(line.strip('\n').split(sep))
                    if len(seperate_line) != fields:
                        raise ValueError
                
                except ValueError:
                    print(f"{path} has {len(seperate_line)} fields on line {line_number}, but expected {fields} fields.")

                else:
                    if header == True:
                        header = False
                        continue
                    else:
                        yield seperate_line


"""
Part 3: Scanning directories and files
Write a Python program that given a directory name, searches that directory for Python files 
(i.e. files ending with .py).  For each .py file, open each file and calculate a summary of 
the file.
"""
class FileAnalyzer:
    
    def __init__(self, directory: str) -> None:
        self.directory: str = directory 
        self.files_summary: Dict[str, Dict[str, int]] = dict() 

        self.analyze_files() # summerize the python files data
    def analyze_files(self) -> None:
        """ return the information of a file """
        
        try:
            files = [file for file in os.listdir(self.directory) if file.endswith('.py')] # get all python files

        except FileNotFoundError:
            print('{} cannot be found'.format(self.directory))

        else:
            for file in files:
                try:
                    f = open(self.directory+'\\'+file, 'r')

                except FileNotFoundError:
                    print('{} cannot be opened'.format(file))
                else:
                    with f:
                        characters = f.read()
                        lines = characters.strip('\n').split('\n')

                        functions = 0
                        classes = 0
                        for line in lines:
                            if line.strip(' ').startswith('class '):
                                classes += 1
                            elif line.strip(' ').startswith('def '):
                                functions += 1
                count = dict()
                count['classes'] = classes
                count['functions'] = functions
                count['line'] = len(lines)
                count['char'] = len(characters)

                self.files_summary[file] = count

    def pretty_print(self) -> None:
        """ return the information for all files under a directory and generate a pretty table"""
        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        
        for key in self.files_summary:
            pt.add_row([self.directory+'\\'+key,
                        self.files_summary[key]['classes'],
                        self.files_summary[key]['functions'],
                        self.files_summary[key]['line'],
                        self.files_summary[key]['char']])
        print(f'Summary for {self.directory}')
        print(pt)
