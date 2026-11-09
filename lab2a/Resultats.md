Étape 1 — Le paiement avec l’identifiant lab2-ralphd12-20261109 a été accepté une fois. En le répétant, le serveur a répondu « deja_traite: true ». L’identifiant p1 était déjà présent dans la base, alors j’ai utilisé un nouvel identifiant.
Étape 2 — Avec une instance : 200 requêtes, 0 erreur, 97 req/s et 75,4 ms de latence moyenne.
Étape 3 — Monolithe arrêté : 200 erreurs sur 200 requêtes. Cela montre le point unique de panne.
Étape 4 — Avec deux instances et le répartiteur : 200 requêtes, 0 erreur, 99,4 req/s et 76,4 ms.
Étape 5 — Après l’arrêt de l’instance 5002, le service a continué : 200 requêtes, 0 erreur, 88,6 req/s et 91,1 ms.
Étape 6 — Les soldes étaient différents : 989300 sur 5001 et 999900 sur 5002. Les bases SQLite des deux instances ne sont pas synchronisées.
Conclusion — Le répartiteur améliore la disponibilité, mais les instances ne synchronisent pas leurs données. Le gain de débit est faible car elles partagent le même Codespace.