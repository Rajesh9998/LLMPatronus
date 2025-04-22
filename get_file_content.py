def read_file_contents(file_name):
   try:
        with open(file_name, 'r') as file:
           content = file.read()
        return content
   except IOError as e:
        print(f"Error reading  {e}\n")

    

