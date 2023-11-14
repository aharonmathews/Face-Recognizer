import pickle

# Replace 'your_file.pkl' with the path to your pickle file
file_path = 'dataset/names.pkl'

try:
    # Open the pickle file for reading
    with open(file_path, 'rb') as file:
        # Load the data from the pickle file
        data = pickle.load(file)

        # Print the loaded data
        print("Data from the pickle file:")
        print(data)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"Error: Unable to load data from the pickle file. {e}")
