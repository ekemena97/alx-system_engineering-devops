#!/usr/bin/python3
import requests
import  sys

def get_employee_todo_progress(employee_id):
   

   base_url = "https://jsonplaceholder.typicode.com/users"
   api_url = f"{base_url}/{employee_id}"
   todo_url = f"{api_url}/todos"

   try:
       # Get employee information
       response = requests.get(api_url)
       response.raise_for_status()  # Raise an exception for non-200 status codes

       employee_data = response.json()
       employee_name = employee_data.get("name")

       # Get Todo list tasks
       todo_response = requests.get(todo_url)
       todo_response.raise_for_status()

       tasks = todo_response.json()
       completed_tasks = [task for task in tasks if task.get("completed")]

       # Display Todo list progress
       print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{len(tasks)}):")
       for task in completed_tasks:
           print(f"\t{task.get('title')}")

   except requests.exceptions.RequestException as err:
       print(f"Error: Unable to fetch data. {err}")

if __name__ == "__main__":
   import sys

   # Check for employee ID as a command-line argument
   if len(sys.argv) != 2:
       print("Usage: python todo_progress.py <employee_id>")
       sys.exit(1)

   employee_id = int(sys.argv[1])
   get_employee_todo_progress(employee_id)
