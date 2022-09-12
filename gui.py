import tkinter as tk
import pandas as pand
import json
from tkinter import END, ttk
from tkinter import Text

#lire fichier csv et convertir en json
csv_file = pand.DataFrame(pand.read_csv("list.csv", sep = ";", header = 0, index_col = False))
csv_file.to_json("list.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

#lire données fichier json
database = "list.json"
data = json.loads(open(database).read())
#print(data)

#mettre en place l'interface graphique
app = tk.Tk()
app.title('MAINTENANCE DISTRIBUTEUR STATION SERVICE')
app.geometry("350x200")

# box 1
box1 = tk.Label(app, bg="#B8405E", fg="white")
box1.pack(ipadx=10, ipady=10, fill=tk.BOTH, expand=True, side=tk.LEFT)

# label 1
label1 = ttk.Label(box1,background="#B8405E",foreground="white", text="Symptome:")
label1.pack()

# box 2
box2 = tk.Label(app, bg="#2EB086", fg="white")
box2.pack(ipadx=10, ipady=10, fill=tk.BOTH, expand=True, side=tk.RIGHT)

# label 2
label2 = ttk.Label(box2, background="#2EB086",foreground="white", text="Solutions:")
label2.pack()

# textbox
text = Text(box2, height=8)
text.pack()

# créer options
cmb = ttk.Combobox(box1, values=("Fuite sur la pompe","Tuyau rigide","Court circuit","Echauffement"))
cmb.pack()

# texte à afficher suivant le choix
def checkcmbo():
    text.delete("1.0",END)
    #loop through the csv list
    for i in data:
        if i['symptome'] == cmb.get():
            text.insert("1.0", i['solutions'])
            break      
        
#cmb.bind('<<ComboboxSelected>>', checkcmbo)
# créer bouton pour afficher résultat de recherche
ttk.Button(box1, text= "VALIDER", command=checkcmbo).pack(pady=50)
    
app.mainloop()











































#Lee© 2022