"""
This file contains the bot interactions.
"""

BOT_INTERACTIONS_DICT = {
    "/start": "Benvenuto {name}",
    "help": [
        (
            "Ciao frat a me, questo bot serve per tenere sotto controllo"
            "il database dei prodotti che la macchinetta degli oggetti"
            " aggiorna ogni giorno"
        ),
        (
            "Da questo bot puoi direttamente controllare la macchinetta degli"
            "oggetti, ma fai attenzione perché rischi di spaccare tutto"
            "fortissimo."
        ),
        (
            "Ecco una lista dei comandi che puoi utilizzare, notare che il"
            "comando e' solo ed esclusivamente la parola senza il trattino"
            "e i due punti"
            "(non si sa mai sono abituato a lavorare coi sarchiaponi):"
        ),
        (
            "- /start: inizia la conversazione con il bot\n"
            "- help: mostra questa lista di comandi\n"
            "- search by name: cerca nel database dei prodotti usando come"
            " chiave di match il nome\n"
            "- search by price_range: cerca nel database dei prodotti usando"
            " come chiave di match un range di prezzo\n"
            "- search by category: cerca nel database dei prodotti usando"
            " come chiave di match la categoria\n"
            "- download db: scarica tutto il database dei prodotti"
            " in formato csv (attento io non so quanto e' grosso"
            " e nemmeno tu)\n"
            "- download updates: scarica il database dei prodotti di oggi"
            " (csv)\n"
            "- updates on: attiva la notifica giornaliera dei prodotti"
            "- updates settings: imponi un filtro sul tipo di prodotti"
            " che ti vengono notificati (poi attivali con updates on)\n"
            "- updates off: disattiva la notifica giornaliera dei prodotti\n"
            "- developer on: attiva la modalita' sviluppatore per controllare"
            " la macchinetta degli oggetti\n"
            "- developer off: disattiva la modalita' sviluppatore\n"
            "- about: mostra informazioni sul bot\n"
        )
    ],
    "search by name": "Sto cercando il prodotto che mi hai chiesto...",
    "search by price_range": "Sto cercando il prodotto che mi hai chiesto...",
    "search by category": (
        "Io non ho diviso la roba in categoria,"
        " chi so Kant"
    ),
    "download db": "Sto scaricando il database dei prodotti...",
    "download updates": "Sto scaricando il database dei prodotti...",
    "updates on": "Notifiche attivate",
    "updates settings": (
        "dimmi il range di prezzo dei prodotti per i quali"
        " vuoi essere notificato, usa questa notazione: (30 - 50)",
        "dimmi quanto deve essere recente l'annuncio, usa questa notazione:\n"
        "- 3h -> mi stai chiendo annunci non piu vecchi di 3 ore fa\n"
        "- 3d \n"
        "- 3m \n"
        "- 3y \n,"
        "Tutte le altre sono autoevidenti, te prego nun ce mette er trattino"
    ),
    "updates off": "Notifiche disattivate",
    "developer on": "Modalita' sviluppatore attivata",
    "developer off": "Modalita' sviluppatore disattivata",
    "about": (
        "Macchinetta degli oggetti v1.0.0\n"
        "Running entirely on python 3.11.0, .csv files, padnas and an "
        "old laptop mounting Arch Linux"
    )
}
