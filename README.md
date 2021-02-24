# Slide-Parser
 Python Script that will take an image as an input and generate component images as an output

 # Set-up and Use

1. Create a new folder with the following folder structure:

        Image-Parser
            |-app.py
            |-inputs (folder)
            |-outputs(folder)

2. Drop the file that you want to parse into slides into the inputs folder.
    - image must have a .jpg extension

3. Open a Command window at the folder.
    - For Windows: Open Command Prompt and navigate to the directory using the command 'cd filepath/Image=Parser'
    - For Mac: Open Terminal and navigate to the directory using the command 'cd filepath/Image=Parser'

4. Once you are at the directory use the command 'python3.8 app.py' to initiate the image parsing.

5. Verify that the program has created the desired output slides.

6. Remove the files from the 'outputs' folder and deposit them in another repository.

# Troubleshooting

1. If parser is having difficulty identifying slides, make sure that the starting image is framed well on the slide book, with border space betweeen the slides and the edge of the image frame, and little contrast between the slide book and the background its being photographed on
