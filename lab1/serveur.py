import socket,time,json


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 5000))
s.listen()

compteur = 0
paiements_traites = {}

print("Serveur en attente sur le port 5000")

while True:
    conn, addr = s.accept()

    try:
        data = json.loads(conn.recv(1024).decode())
        paiement_id = data["id"]
        montant = data["montant"]

        if paiement_id in paiements_traites:
            print("Doublon ignoré :", paiement_id)
            resultat = paiements_traites[paiement_id]
        else:
            compteur += 1
            print("Paiements exécutés :", compteur)

            resultat = {
                "id": paiement_id,
                "statut": "OK",
                "montant": montant
            }

            # Enregistrer avant de simuler le traitement long
            paiements_traites[paiement_id] = resultat
            time.sleep(3)

        conn.sendall(json.dumps(resultat).encode())

    except (ValueError, KeyError, OSError) as e:
        print("Erreur :", e)

    finally:
        conn.close()
