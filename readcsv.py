import pandas as pd

df = pd.read_csv('train_solution_bounding_boxes.csv')
for index, fila in df.iterrows():
    nombre_archivo_txt = fila['image']+'.txt'
    with open(nombre_archivo_txt, 'w') as archivo_txt:
        
        archivo_txt.write(str(fila['xmin']) + ',' +
        str(fila['ymin']) + ',' +
        str(fila['xmax']) + ',' +
        str(fila['ymax']))