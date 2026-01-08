# Projet Docker - Guide simple

## Prerequis
- Docker Desktop (avec `docker compose` v2)
- Git

## Lancement rapide
1. Creer le fichier `.env` a partir du modele :
   ```
   cp .env.example .env
   ```
2. Demarrer la stack :
   ```
   docker compose up -d --build
   ```
3. Ouvrir le dashboard :
   - http://localhost:8080

## Arret
```
docker compose down
```

## Reinitialiser la base (rejouer les scripts SQL)
```
docker compose down -v
docker compose up -d
```
