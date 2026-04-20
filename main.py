from models.salle import Salle

s1 = Salle("303", "Salle Francais", "Classe", 40)
s1.afficher_infos()



from services.services_salle import ServiceSalle
from models.salle import Salle


service = ServiceSalle()


s = Salle("A206", "Salle Service", "Bureau", 7)
print(service.ajouter_salle(s)[1])


s.libelle = "Salle Service Modifiée"
s.capacite = 10
print(service.modifier_salle(s)[1])


res = service.rechercher_salle("A206")
if res:
    res.afficher_infos()



for salle in service.recuperer_salles():
    salle.afficher_infos()

service.supprimer_salle("A206")
print("Salle supprimée")

