from unittest import TestCase, mock
from database import Citations
import command_line

class TestCommandLine(TestCase):

    @mock.patch('command_line.input', create=True)
    def test_get_article_info(self, mocked_input):
        mocked_input.side_effect = ["John Doe", "Sample Article", "Journal of Testing", "2023"]
        result = command_line.get_article_info()
        self.assertEqual(result, """@article{Doe2023,\n\tauthor = "John Doe",\n\ttitle = "Sample Article",\n\tjournal = "Journal of Testing",\n\tyear = "2023"\n}""")

    @mock.patch("command_line.print", create=True)
    @mock.patch('command_line.input', create=True)
    def test_start(self, mocked_input, mocked_print):
        mocked_input.side_effect = ["new", "John Doe", "Sample Article", "Journal of Testing", "2023", "list", "quit"]
        db = Citations()
        command_line.start(db)
        self.assertListEqual(mocked_print.mock_calls, [mock.call('Welcome to the citation database!'), 
                                                        mock.call('Commands: new, list, quit'), 
                                                        mock.call('Article Information:'), 
                                                        mock.call('@article{Doe2023,\n\tauthor = "John Doe",\n\ttitle = "Sample Article",\n\tjournal = "Journal of Testing",\n\tyear = "2023"\n}')])
        
        self.assertListEqual(mocked_input.mock_calls, [mock.call("Enter a command: "), 
                                                        mock.call("Enter the article title: "), 
                                                        mock.call('Enter the author(s): '), 
                                                        mock.call('Enter the journal name: '), 
                                                        mock.call('Enter the publication year: '), 
                                                        mock.call('Enter a command: '), 
                                                        mock.call('Enter a command: ')])