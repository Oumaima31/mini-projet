import unittest
from unittest.mock import patch

from ToDoList import tasks, addTask, listTask, deleteTask


class TestToDoListApp(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    @patch('builtins.input', return_value="Task 1")
    def test_add_task(self, mock_input):
        addTask()
        self.assertEqual(len(tasks), 1)
        self.assertIn("Task 1", tasks[0])
        mock_input.assert_called_with("Please enter a task :")

@patch('builtins.input')
def test_list_tasks(self, mock_input):
        tasks.append("Task 1")
        tasks.append("Task 2")
        mock_input.return_value = "3"
        listTask()
        self.assertEqual(len(tasks), 2)
        mock_input.assert_called_with("Enter your choice :")
        self.assertIn("Task #'1'. 'Task 1'", mock_input.call_args_list[1].args[1])
        self.assertIn("Task #'2'. 'Task 2'", mock_input.call_args_list[1].args[1])

@patch('builtins.input')
def test_delete_task(self, mock_input):
        tasks.append("Task 1")
        tasks.append("Task 2")
        mock_input.side_effect = ["2", "0", "5", "4", ""]
        deleteTask()
        self.assertEqual(len(tasks), 2)
        mock_input.assert_called_with("Enter your choice :")
        mock_input.assert_called_with("Enter the # to delete : ")
        mock_input.call_args_list[1].args[0].assertIsInstance(mock_input.call_args_list[1].args[0], int)
        mock_input.call_args_list[2].args[0].assertIsInstance(mock_input.call_args_list[2].args[0], int)
        self.assertIn("task 0 has been removed.", mock_input.call_args_list[1].args[1])
        self.assertIn("task 5 was not found.", mock_input.call_args_list[2].args[1])
        self.assertIn("Goodbye", mock_input.call_args_list[3].args[0])
    

if __name__ == '__main__':
    unittest.main()