import tkinter
from tkinter import messagebox

def status(file):
    """Lees de validation af uit het bestand door,
    elke keer op dezelfde positie, op een andere regel.
    Zet de validation in een lijst.
    Input: file - csv bestand - genen annotatie
    Output: data_list - lijst met  statussen
    """
    info_list = []
    data_list = []
    open_file = open(file)
    open_file.readline()
    for i in open_file:
        line = i.replace("\n", "").split(",")
        info_list.append(line)
        # In iedere regel, tweede positie.
        validation = line[1]
        data_list.append(validation)

    open_file.close()

    return data_list

def gene_status(data_list):
    """Telt het aantal van iedere validation status.
    Input: data_list
    Output: count_list
    """
    validation_list = []
    count_list = []
    count = 0
    for j in data_list:
        if j not in validation_list:
            validation_list.append(j)
        else:
            continue
    length = len(validation_list)
    print(validation_list)

    # r is aantal verschillende validation.
    # i voor elk woord in de lijst.
    # als het woord gelijk is als het woord van validation tel bij op.
    for r in range(length):
        for i in data_list:
            if i == validation_list[r]:
                count += 1
        if count != 0:
            count_list.append(count)
            count = 0

    return count_list

# def stacked_bar(med_a_mg, med_b_mg):
#     labels = ['G1', 'G2', 'G3', 'G4', 'G5']
#     med_a = med_a_mg
#     med_b = med_b_mg
#     med_a_std = [2, 3, 4, 1, 2]
#     med_b_std = [3, 5, 2, 3, 3]
#     width = 0.35  # the width of the bars: can also be len(x) sequence
#     fig, ax = plt.subplots()
#     ax.bar(labels, med_a, width, yerr=med_a_std, label='med_a')
#
#     ax.bar(labels, med_b, width, yerr=med_b_std, bottom=med_a,
#            label='med_b')
#
#     ax.set_ylabel('Hoeveelheid medicijn')
#     ax.set_title('medicijnen a en b')
#     ax.legend()
#     plt.show()

class GUI:
    def __init__(self):
        # Creeer de main window
        self.main_window = tkinter.Tk()

        # Maak de twee frames voor checkbox en de buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Maak labels aan.
        self.label1 = tkinter.Label(self.top_frame)

        # Pack items
        # Frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.label1.pack()
        # Geef de main window weer
        tkinter.mainloop()

    # def showresults(self):
    #     self.message = "
    #



def main():
    data_list = status("yeast_genes.csv")
    count_list = gene_status(data_list)
    print(count_list)
    gui = GUI()

main()
 