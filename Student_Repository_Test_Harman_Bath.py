import unittest
from HW08_Harman_Bath import file_reader
from HW08_Harman_Bath import FileAnalyzer

class FileReaderTest(unittest.TestCase):
    def test_file_reader(self):

        path = "C:\\Users\\hrmnv\\Desktop\\SSW_810\\Homework 8\\file_reader_test.csv"
        file1 = file_reader(path, 3, ' ')
        file2 = file_reader(path, 3, ' ', header = True)


        self.assertTrue(next(file1) == ('ABC', '0', '1'))
        self.assertTrue(next(file1) == ('DEF', '2', '3'))
        self.assertTrue(next(file1) == ('GHI', '4', '5'))

        self.assertTrue(next(file2) == ('DEF', '2', '3'))
        self.assertTrue(next(file2) == ('GHI', '4', '5'))


class FileAnalyzerTest(unittest.TestCase):
    def test_analyze(self):
        dir = "C:\\Users\\hrmnv\\Desktop\\SSW_810\\Homework 8"
        fs = FileAnalyzer(dir)
        files = fs.files_summary
        file_names = list(files.keys())

        self.assertEqual(file_names[0], '0_def.py')
        self.assertEqual(files[file_names[0]]['classes'], 0)
        self.assertEqual(files[file_names[0]]['functions'], 0)
        self.assertEqual(files[file_names[0]]['line'], 8)
        self.assertEqual(files[file_names[0]]['char'], 79)

        self.assertEqual(file_names[1], 'HW08_Harman_Bath.py')
        self.assertEqual(files[file_names[1]]['classes'], 1)
        self.assertEqual(files[file_names[1]]['functions'], 5)
        self.assertEqual(files[file_names[1]]['line'], 129)
        self.assertEqual(files[file_names[1]]['char'], 4803)



if __name__ == '__main__':
    unittest.main()