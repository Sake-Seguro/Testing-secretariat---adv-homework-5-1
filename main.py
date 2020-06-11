
import app
import unittest
from unittest.mock import patch



class SecretariatTester(unittest.TestCase):

    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def testing_check_document_existance(self):
        presence = app.check_document_existance('2207 876234')
        self.assertTrue(presence)
        presence = app.check_document_existance('2207876234')
        self.assertFalse(presence)

    def testing_get_doc_owner_name(self):
        correct_name = self.docs[0]['name']
        with patch('app.input', return_value='2207 876234'):
            name_to_check = app.get_doc_owner_name()
        self.assertIs(name_to_check, correct_name)

    def testing_get_all_doc_owner_names(self):
        persons_list = [self.docs[0]['name'], self.docs[1]['name'], self.docs[2]['name']]
        checked_names = (app.get_all_doc_owners_names())
        self.assertIs(len(checked_names), len(persons_list))

    def testing_get_doc_shelf(self):
        correct_number = '2'
        with patch('app.input', return_value=f'{self.dirs["2"][0]}'):
            shelf_to_check = app.get_doc_shelf()
        self.assertIs(correct_number, shelf_to_check)

    def testing_delete(self):
        pre_eliminated = len(self.docs)
        with patch('app.input', return_value='11-2'):
            app.delete_doc()
        self.assertLess(len(self.docs), pre_eliminated)

    def testing_add(self):
        pre_added = len(self.docs)
        with patch('app.input', size_effect=['12345', 'passport', 'testUser', '1']):
            app.add_new_doc()
        self.assertGreater(len(self.docs), pre_added)

    def testing_move_doc_to_shelf(self):
        with patch('app.input', side_effect=['10006', '3']):
            app.move_doc_to_shelf()
        self.assertIn('10006', self.dirs['3'])
        self.assertNotIn('10006', self.dirs['2'])

    def testing_add_new_shelf(self):
        with patch('app.input', return_value='testNum'):
            app.add_new_shelf()
        self.assertIs(len(app.directories), 4)


if __name__ == '__main__':

    unittest.main()


