import logging


def debug_log(fonction):

    # logger specifique a ce decorateur
    dblogger = logging.getLogger("DEBUGLOG")
    dblogger.setLevel(logging.DEBUG)
    dblogger.addHandler(logging.StreamHandler())

    def wrapper(*args, **kwargs):
        dblogger.debug(f"[DEBUG] Debut : {fonction.__name__} avec args={args}, kwargs={kwargs}")
        resultat = fonction(*args, **kwargs)
        dblogger.debug(f"[DEBUG] Fin : {fonction.__name__} resultat {resultat}")
        return resultat
    return wrapper