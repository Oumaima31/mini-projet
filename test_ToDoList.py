
import pytest
from unittest.mock import patch
from ToDoList import tasks,addTask,listTask,deleteTask

#we are tesing 'ToDoList' application  :
       
def test_addTask(capsys):
    #  we are adding a fake task called'Doing something'
    with patch('builtins.input',return_val='Doing something'):
        addTask()
    #  then testing if task has added
    assert tasks==['Doing something']
    out, _ = capsys.readouterr()
    assert out.strip() == "Task 'Doing something' added to the list."

       
def test_listTask(capsys):
        # we tested if there is no task:
    with capsys.disabled():
        listTask()
        cap=capsys.readouterr()
        assert cap.out.strip()== "there are no tasks currently."

       # then we added a task and verified if it does  exist or not:
    tasks.append("task 1")
    assert cap.out.strip()=="current tasks: task #1 :task 1 \n task #2 : task 2 "


def test_deledteTask(capsys,monkeypatch):

        #we addet 3 tasks to the list:
    tasks.append(["task 1","task 2","task 3"])

        #we deleted 'task 2' :
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: '2')
        deleteTask(tasks)
        #we tested if the task had deleted successefully:
    assert tasks==["task 1","task 3"]
    cap= capsys.readouterr()
    assert cap.out.strip() == "task 2 has been removed."