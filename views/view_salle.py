import customtkinter as ctk
from tkinter import ttk
from models.salle import Salle
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service = ServiceSalle()

        self.frameInfo = ctk.CTkFrame(self)
        self.frameInfo.pack(pady=10)

        self.entry_code = ctk.CTkEntry(self.frameInfo, placeholder_text="Code")
        self.entry_code.grid(row=0, column=0, padx=5, pady=5)

        self.entry_libelle = ctk.CTkEntry(self.frameInfo, placeholder_text="Libellé")
        self.entry_libelle.grid(row=0, column=1, padx=5, pady=5)

        self.entry_type = ctk.CTkEntry(self.frameInfo, placeholder_text="Type")
        self.entry_type.grid(row=1, column=0, padx=5, pady=5)

        self.entry_capacite = ctk.CTkEntry(self.frameInfo, placeholder_text="Capacité")
        self.entry_capacite.grid(row=1, column=1, padx=5, pady=5)

        self.frameBtn = ctk.CTkFrame(self)
        self.frameBtn.pack(pady=10)

        ctk.CTkButton(self.frameBtn, text="Ajouter", command=self.ajouter).grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.frameBtn, text="Modifier", command=self.modifier).grid(row=0, column=1, padx=5)
        ctk.CTkButton(self.frameBtn, text="Supprimer", command=self.supprimer).grid(row=0, column=2, padx=5)
        ctk.CTkButton(self.frameBtn, text="Rechercher", command=self.rechercher).grid(row=0, column=3, padx=5)