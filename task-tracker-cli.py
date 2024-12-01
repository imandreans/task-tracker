import cmd, json
from datetime import datetime

class TaskTracker(cmd.Cmd):
    prompt = 'task-cli '
    filename = 'task.json'

    def do_add(self, description):
        """
            Add new task
        """
        try:
            #if exist, read the file
            data = self.__fetch_list()
        except FileNotFoundError:
            #make new array if no file
            data = []
        #initialize new data 
        if len(description) == 0:
            print('Please type your Task!')
            return

        new_data = {'id' : len(data)+1, #id is equal to array's length
                    'description': description, 
                    'status': 'todo',
                    'createdAt': datetime.now().strftime('%x %X'),
                    'updatedAt': datetime(1976, 1, 1, 0, 0).strftime('%x %X')}
        
        #push new data to data
        data.append(new_data)

        #write it 
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def do_update(self, args):
        """
            Update a Task
        """
        args_list = args.split()
        if len(args_list) != 2:
            print("Please type Task ID or Description")

        task_id, description = args_list
        try:
            data = self.__fetch_list()
            data[int(task_id)-1]['description'] = description
            data[int(task_id)-1]['updatedAt'] = datetime.now().strftime('%x %X')
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(e)

    def do_delete(self, task_id):
        """
            Delete task
        """

        try:
            if int(task_id) < 1:
                print("ID task must be 1 or greater.")
                
            data = self.__fetch_list()
            data.pop(int(task_id)-1)
            for i, _ in enumerate(data):
                data[i]['id'] = i+1

            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except ValueError:
            print('Please input the ID of task you want to delete!')
        except Exception as e:
            print(e) 
    
    def __fetch_list(self):
        """
            Fetch data from task.json
        """
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    def do_list(self, status):
        """
            Show table contains a list of task
        """
        data = self.__fetch_list()
        # if status is provided
        if status!='':
            data = [i for i in data if i['status']==status] #filter data
        
        # if parameter isn't todo, in-progress, or done
        if status not in ['', 'todo', 'in-progress', 'done']: 
            print(f"{status} isn't status in this task tracker")

        # #print table that contains list of task
        print(f"|{'='*91}|")
        print(f"|{'id':^5}|{'The Task':^30}|{'Status':^14}|{'Created Time':^20}|{'Updated Time':^18}|")
        print(f"|{'='*91}|")
        for i in data:
            print(f"|{i['id']:^5}|{i['description']:<30}|{i['status']:^14}|{i['createdAt']:^20}|{i['updatedAt']:^18}|")
        print(f"|{'='*91}|")   

    def __change_status(self, task_id: int, status):
        try:
            data = self.__fetch_list()
            data[int(task_id)-1]['status'] = status
            data[int(task_id)-1]['updatedAt'] = datetime.now().strftime('%x %X')
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except ValueError:
            print('Please input the ID of task you want to mark')
        except Exception as e:
            print(e)

    def do_mark_in_progress(self, task_id: int):
        self.__change_status(task_id, 'in-progress')

    def do_mark_done(self, task_id: int):
        self.__change_status(task_id, 'in-progress')


    def do_quit(self, line):
        """
            Exit the cmd
        """
        return True
if __name__ == '__main__':
    taskTracker = TaskTracker()
    taskTracker.cmdloop()