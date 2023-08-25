import pandas as pd

# Read data from the CSV file into a DataFrame
df = pd.read_csv('train_solution_bounding_boxes.csv')

# Iterate through each row in the DataFrame
for index, fila in df.iterrows():

    # Create a text file name based on the image name from the CSV
    file_name = fila['image'] + '.txt'

    # Open the text file in write mode
    with open(file_name, 'w') as archivo_txt:

        # Write bounding box coordinates to the text file
        # Convert numerical values to strings using str() function
        archivo_txt.write(
            str(fila['xmin']) + ',' +
            str(fila['ymin']) + ',' +
            str(fila['xmax']) + ',' +
            str(fila['ymax'])
        )
