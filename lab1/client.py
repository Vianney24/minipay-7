import socket,json,uuid,time


# Un identifiant unique pour cette opération de paiement
paiement_id = str(uuid.uuid4())

message = json.dumps({
    "id": paiement_id,
    "montant": 5000
}).encode()

for essai in range(2):
    try:
        c = socket.create_connection(
            ("127.0.0.1", 5000),
            timeout=2
        )
        c.settimeout(2)
        c.sendall(message)

        reponse = c.recv(1024).decode()
        print("Réponse du serveur :", reponse)
        c.close()
        break

    except OSError as e:
        print("Essai", essai + 1, "échoué :", e)

    finally:
        try:
            c.close()
        except (OSError, NameError):
            pass

    time.sleep(0.2)

print("Identifiant du paiement :", paiement_id)


