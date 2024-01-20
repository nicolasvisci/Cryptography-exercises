def cifrario_cesare(stringa, chiave):
    """
    Applica il cifrario di Cesare alla stringa data spostandosi di tante posizioni quante indica la chiave.
    """
    # definizione dell'alfabeto di riferimento
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    # stringa che conterrà la versione cifrata della stringa in input
    cifrata = ''

    for carattere in stringa:
        # verifichiamo che il carattere sia effettivamente una lettera minuscola
        if carattere.lower() in alfabeto:
            # recuperiamo l'indice della lettera nell'alfabeto
            indice = alfabeto.index(carattere.lower())
            # calcoliamo il nuovo indice a cui corrisponde la lettera cifrata
            nuovo_indice = (indice + chiave) % 26
            # aggiungiamo la lettera cifrata alla stringa cifrata, mantenendo la maiuscola/minuscola dell'originale
            cifrata += alfabeto[nuovo_indice] if carattere.islower() else alfabeto[nuovo_indice].upper()
        else:
            # se il carattere non è una lettera minuscola, lo aggiungiamo così com'è alla stringa cifrata
            cifrata += carattere

    return cifrata

stringa_in_chiaro = input("Inserisci una stringa da cifrare: ") 
chiave_da_applicare = input("inserisci la chiave da applicare: ") 
print("Stringa cifrata: " + cifrario_cesare(stringa_in_chiaro, int(chiave_da_applicare)))