from data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not all([salle.code, salle.libelle, salle.type, salle.capacite]):
            return False, "Tous les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "Capacité invalide"

        self.dao.insert_salle(salle)
        return True, "Salle ajoutée"

    def modifier_salle(self, salle):
        if not all([salle.code, salle.libelle, salle.type, salle.capacite]):
            return False, "Champs invalides"

        if int(salle.capacite) < 1:
            return False, "Capacité invalide"

        self.dao.update_salle(salle)
        return True, "Salle modifiée"

    def supprimer_salle(self, code):
        self.dao.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao.get_salle(code)