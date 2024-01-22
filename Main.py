import tkinter as tk
from pipelinecode_nik import *
'''
rows = 14
cols = 14

# Declare and initialize the 2D array of strings
pipeline_matrix = [["" for _ in range(cols)] for 
# Initialize some values in the matrix
pipeline_matrix[0][:4] = ["mov r1 #1", "[    F   ]", "[    D   ]", "[    E   ]"]
pipeline_matrix[1][:6] = ["add r1 r2", "", "[    F   ]", "[////////]", "[    D   ]", "[    E   ]"]
pipeline_matrix[2][:7] = ["mov r1 #9", "","", "", "[    F   ]", "[////////]", "[    D   ]", "[    E   ]"]
pipeline_matrix[3][:8] = ["mov r2 #2", "","", "", "","", "[    F   ]", "[    D   ]", "[    E   ]"]
pipeline_matrix[4][:9] = ["add r3 r2", "","", "", "", "","", "[    F   ]", "[////////]", "[    D   ]", "[    E   ]"]
pipeline_matrix[5][:10] = ["mov r1 #2", "","", "", "", "","","", "", "[    F   ]", "[    D   ]", "[    E   ]"]
pipeline_matrix[6][:11] = ["add r1 r2", "", "","", "", "", "", "","", "", "[    F   ]", "[////////]", "[    D   ]", "[    E   ]"]


pipeline_matrix = [
    ["mov r1 #1", "[    F   ]", "[    D   ]", "[    E   ]"],
    ["add r1 r2", "          ","[    F   ]", "[////////]", "[    D   ]", "[    E   ]"],
    ["mov r1 #9", "          ","          ","[    F   ]", "[////////]", "[    D   ]", "[    E   ]"],
    ["mov r2 #2", "          ","          ","          ","[    F   ]", "[    D   ]", "[    E   ]"],
    ["add r3 r2", "          ","          ","          ","          ","[    F   ]", "[////////]", "[    D   ]", "[    E   ]"],
    ["mov r1 #2", "          ","          ","          ","          ","          ","[    F   ]", "[    D   ]", "[    E   ]"],
    ["add r1 r2", "          ","          ","          ","          ","          ","          ","[    F   ]", "[////////]", "[    D   ]", "[    E   ]"]
]

'''




class PipelineGUI:
    def __init__(self,root,matrix):
        self.root = root
        self.root.title("Pipeline Matrix")

        self.canvas = tk.Canvas(self.root, width=1500, height=300, bg="white",scrollregion=(0,0,10000,5000))
        self.canvas.pack()

        self.draw_matrix(matrix)

    def draw_matrix(self, matrix):
        row_height = 25
        column_width = 75



        # Draw the column indices (t1, t2, t3, ...) in the first row
        for j in range(len(matrix[0])+3):
            x = (j + 1) * column_width  # Shift right by 1 column
            y = 0
            self.canvas.create_text(x + column_width / 2, y + row_height / 2, text="t" + str(j + 1), fill="black",
                                    font=("Arial", 10, "bold"))

        # Draw the matrix elements
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                x = (j + 1) * column_width  # Shift right by 1 column
                y = (i + 1) * row_height  # Shift down by 1 row

                # Determine the color and text properties based on the cell content
                color = "white"
                text = cell[1:-1]  # Remove brackets from the cell content
                bold = False

                if cell == "[    F   ]":
                    color = "lightblue"
                    bold = True
                    text = "Fetch"
                elif cell == "[    E   ]":
                    color = "lightcoral"
                    bold = True
                    text = "Execute"
                elif cell == "[    D   ]":
                    color = "lightgreen"
                    bold = True
                    text = "Decode"
                elif cell == "[////////]":
                    color = "darkgrey"
                    text = "///////"
                    bold = True
                elif cell == "[//ERROR//]":
                    color = "red"
                    text = "ERROR"
                    bold = True
                elif cell.strip():  # Check if the cell is not an empty string after removing leading/trailing whitespaces
                    color = "lightgrey"
                    text = cell
                    bold = True
                elif not cell.strip():  # Check if the cell is empty or contains only whitespaces
                    color = "white"
                    text = ""


                # Draw the colored rectangle
                self.canvas.create_rectangle(x, y, x + column_width, y + row_height, outline="black", fill=color)

                # Draw the text in the center of the rectangle
                text_id = self.canvas.create_text(x + column_width / 2, y + row_height / 2, text=text, fill="black",
                                                  font=("Arial", 10, "bold" if bold else "normal"))
        # Draw the row indices (serial numbers) in the first column
        for i in range(len(matrix)):
            x = 0
            y = (i + 1) * row_height  # Shift down by 1 row
            if matrix[i][0].strip():
                self.canvas.create_text(x + column_width / 2, y + row_height / 2, text="Instr " + str(i+1),fill="black", font=("Arial", 10, "bold"))

if __name__ == "__main__" :
    root: Tk = tk.Tk()
    app = PipelineGUI(root,pipeline_matrix)
    root.mainloop()
