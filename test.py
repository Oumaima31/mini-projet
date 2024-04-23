import unittest
from unittest.mock import patch
from ToDoList import tasks, addTask, listTask, deleteTask

class TestTasks(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    @patch('builtins.input', return_value='Go to the store')
    def test_add_task(self, mock_input):
        addTask()
        self.assertEqual(tasks, ['Go to the store'])

    @patch('builtins.input', side_effect=[1, 'Go to the store'])
    def test_delete_task(self, mock_input):
        tasks.append('Clean the house')
        tasks.append('Go to the store')
        deleteTask()
        self.assertEqual(tasks, ['Clean the house'])

    @patch('builtins.input', side_effect=[3])
    def test_delete_task_not_found(self, mock_input):
        deleteTask()
        self.assertEqual(tasks, [])

@patch('builtins.input', side_effect=['3\n', 'Go to the store\n', '4\n'])
def test_list_tasks(self, mock_input):
    listTask()
    self.assertEqual(mock_input.call_args_list, [('',), ('',), ('',)])

if __name__ == '__main__':
    unittest.main()