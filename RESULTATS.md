Étape 2 : serveur arrêté, le client reçoit « Connection refused » en 6 ms.
Étape 2 : adresse injoignable, le client reçoit « timed out » après environ 2012 ms.
Étape 3 : les deux tentatives du client expirent ; le compteur du serveur atteint 2.
Conclusion : une réponse tardive peut pousser le client à renvoyer un paiement déjà exécuté.