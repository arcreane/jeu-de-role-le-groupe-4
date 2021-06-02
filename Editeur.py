from tkinter import *
import os


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="registration successful", fg="green", font=("Calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("success")
    screen3.geometry("150x100")
    Label(screen3, text="Login successful").pack()
    Button(screen3, text="OK", command=session).pack()

def session():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("histoires")
    screen6.geometry("400x400")
    Label(screen6, text = "Bienvenue a l'Editor").pack()
    Label(screen6, text = "").pack()
    Label(screen6, text="").pack()

    Button(screen6, text = "Creer une histoire", command = creer_histoire).pack()
    Label(screen6, text = "").pack()
    Label(screen6, text="").pack()

    Button(screen6, text = "Modifier une histoire", command = modifier_histoire).pack()
    Label(screen6, text = "").pack()
    Label(screen6, text="").pack()
    Button(screen6, text = "Supprimer une histoire", command = supprimer_histoire).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Jouer une histoire", command=jouer_histoire).pack()



def creer_histoire():
    global raw_titre1
    raw_titre1 = StringVar()
    global raw_paragraph
    raw_paragraph = StringVar()
    global raw_choix1
    raw_choix1 = StringVar()
    global raw_choix2
    raw_choix2 = StringVar()
    global raw_paragraph1
    raw_paragraph1 = StringVar()
    global raw_choix3
    raw_choix3 = StringVar()
    global raw_choix4
    raw_choix4 = StringVar()
    global raw_paragraph2
    raw_paragraph2 = StringVar()
    global raw_choix5
    raw_choix5 = StringVar()
    global raw_choix6
    raw_choix6 = StringVar()
    global raw_paragraph3
    raw_paragraph3 = StringVar()
    global raw_paragraph4
    raw_paragraph4 = StringVar()
    global raw_paragraph5
    raw_paragraph5 = StringVar()
    global raw_paragraph6
    raw_paragraph6 = StringVar()
    global titre1
    global paragraph
    global choix1
    global choix2
    global paragraph1
    global choix3
    global choix4
    global paragraph2
    global choix5
    global choix6
    global paragraph3
    global paragraph4
    global paragraph5
    global paragraph6

    global screen7
    screen7 = Toplevel(screen)
    screen7.title("creer une histoire")
    screen7.geometry("800x800")
    Label(screen7, text = "on recommande d'ecrire les textes autre part et de copier coller").pack()
    Label(screen7, text="titre de l'histoire").pack()
    titre1 = Entry(screen7, textvariable=raw_titre1)
    titre1.pack()
    Label(screen7, text="paragraph ").pack()
    paragraph = Entry(screen7, width = 150, textvariable=raw_paragraph)
    paragraph.pack()
    Label(screen7, text="choix 1").pack()
    choix1 = Entry(screen7, textvariable=raw_choix1)
    choix1.pack()
    Label(screen7, text="choix 2").pack()
    choix2 = Entry(screen7, textvariable=raw_choix2)
    choix2.pack()
    Label(screen7, text="paragraph1").pack()
    paragraph1 = Entry(screen7, width = 150, textvariable = raw_paragraph1)
    paragraph1.pack()
    Label(screen7, text = "choix3").pack()
    choix3 = Entry(screen7, textvariable=raw_choix3)
    choix3.pack()
    Label(screen7, text="choix4").pack()
    choix4 = Entry(screen7, textvariable=raw_choix4)
    choix4.pack()
    Label(screen7, text="paragraph2").pack()
    paragraph2 = Entry(screen7, width=150, textvariable=raw_paragraph2)
    paragraph2.pack()
    Label(screen7, text="choix5").pack()
    choix5 = Entry(screen7, textvariable=raw_choix5)
    choix5.pack()
    Label(screen7, text="choix6").pack()
    choix6 = Entry(screen7, textvariable=raw_choix6)
    choix6.pack()
    Label(screen7, text="paragraph3").pack()
    paragraph3 = Entry(screen7, width=150, textvariable=raw_paragraph3)
    paragraph3.pack()
    Label(screen7, text="paragraph4").pack()
    paragraph4 = Entry(screen7, width=150, textvariable=raw_paragraph4)
    paragraph4.pack()
    Label(screen7, text="paragraph5").pack()
    paragraph5 = Entry(screen7, width=150, textvariable=raw_paragraph5)
    paragraph5.pack()
    Label(screen7, text="paragraph6").pack()
    paragraph6 = Entry(screen7, width=150, textvariable=raw_paragraph6)
    paragraph6.pack()
    Button(screen7, text = "save", width = 10, height = 1, command=save_hist).pack()


def save_hist():

    titre_info = raw_titre1.get()
    paragraph_info = raw_paragraph.get()
    choix1_info = raw_choix1.get()
    choix2_info = raw_choix2.get()
    paragraph1_info = raw_paragraph1.get()
    choix3_info = raw_choix3.get()
    choix4_info = raw_choix4.get()
    paragraph2_info = raw_paragraph2.get()
    choix5_info = raw_choix5.get()
    choix6_info = raw_choix6.get()
    paragraph3_info = raw_paragraph3.get()
    paragraph4_info = raw_paragraph4.get()
    paragraph5_info = raw_paragraph5.get()
    paragraph6_info = raw_paragraph6.get()
    file_hist = open(titre_info+".txt", "w")
    file_hist.write(titre_info + "\n")
    file_hist.write(paragraph_info + "\n")
    file_hist.write(choix1_info + "\n")
    file_hist.write(choix2_info + "\n")
    file_hist.write(paragraph1_info + "\n")
    file_hist.write(choix3_info + "\n")
    file_hist.write(choix4_info + "\n")
    file_hist.write(paragraph2_info + "\n")
    file_hist.write(choix5_info + "\n")
    file_hist.write(choix6_info + "\n")
    file_hist.write(paragraph3_info + "\n")
    file_hist.write(paragraph4_info + "\n")
    file_hist.write(paragraph5_info + "\n")
    file_hist.write(paragraph6_info)

    titre1.delete(0, END)
    paragraph.delete(0, END)
    choix1.delete(0, END)
    choix2.delete(0, END)
    paragraph1.delete(0, END)
    choix3.delete(0, END)
    choix4.delete(0, END)
    paragraph2.delete(0, END)
    choix5.delete(0, END)
    choix6.delete(0, END)
    paragraph3.delete(0, END)
    paragraph4.delete(0, END)
    paragraph5.delete(0, END)
    paragraph6.delete(0, END)

    Label(screen7, text = "histoire sauvegarde avec succes", fg="green", font=("Calibri",12)).pack()

def modifier_histoire():
    print("a faire")


def supprimer_histoire():
    print("a faire")

def jouer_histoire():
    print("a faire")










def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("error")
    screen4.geometry("150x100")
    Label(screen4, text="pass error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def delete3():
    screen4.destroy()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("error")
    screen5.geometry("150x100")
    Label(screen5, text="pass error").pack()
    Button(screen5, text="OK", command=delete4).pack()


def delete4():
    screen5.destroy()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Entrez les details ci-dessous").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="entrez les details ci-dessous").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="username * ").pack()
    global username_entry1
    global password_entry1
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("S'identifier")
    Label(text="S'identifier", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()




