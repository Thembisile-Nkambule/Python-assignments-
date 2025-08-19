filename = input("Please enter the file name you want to read? (e.g flie.txt) ")
file_name = filename.lower()

try:
    with open(file_name,"r") as file:
        data = file.read()
        
    #Spit the words in input.txt
    split_data =data.split()
    #Calculate the number of words
    num_data = len(split_data)
    #Make text to uppercase
    upper_data = data.upper()
    
    #writing and creating a new file
    with open("output.txt", "w") as file:
        file.write(upper_data +"\n\n")
        file.write(f"Word count: {num_data}")
        print("Text successfully added on output.txt!!")

except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Error: You don't have permission to read/write one of the files.")
