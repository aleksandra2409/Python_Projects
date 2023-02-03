import imageio
import os

video=os.path.abspath('_import_609115c00e5a15.53371416.mp4')

print(video)

def gifMaker(inputPath, targetFormat):
    outputPath=os.path.splitext(inputPath)[0] + targetFormat
    

    print(f'converting {inputPath} to {outputPath}')

    reader=imageio.get_reader(inputPath) 
    fps=reader.get_meta_data()['fps'] 

    writer=imageio.get_writer(outputPath,fps=fps)

    for image in reader:  
        writer.append_data(image)
        print(f'Frame {image}')
    
    print('Done!')
    writer.close()

gifMaker(video,'.gif')
