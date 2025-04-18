import logging

dblogger = logging.getLogger("DEBUGLOG")

def debug_log(fonction):
    def wrapper(*args, **kwargs):
        dblogger(f"[DEBUG] Appel : {fonction.__name__} avec args={args}, kwargs={kwargs}")
        resultat = fonction(*args, **kwargs)
        dblogger(f"[DEBUG] Fin : {fonction.__name__}")
        return resultat
    return wrapper

# Décorateur 2 : empêcher les réservations en double
def unique_reservation(fonction):
    def wrapper(self, trajet):
        if trajet in self._reservations:
            print("⛔ Trajet déjà réservé.")
            return
        return fonction(self, trajet)
    return wrapper
