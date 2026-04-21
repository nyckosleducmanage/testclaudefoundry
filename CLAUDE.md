# Conventions de review

## Priorités
1. Sécurité (secrets hardcodés, injections, permissions excessives)
2. Bugs de régression
3. Qualité du code (PEP 8 pour Python, ESLint pour JS/TS, Terraform fmt pour HCL)

## À signaler systématiquement
- Secrets, clés API, mots de passe en clair dans le code
- Utilisation de MD5/SHA1 pour du hashing cryptographique
- Blocs `except:` nus, `eval()`, `os.system()` avec input non sanitisé
- Injections SQL / command injection
- Tests manquants sur le code critique

## À ignorer
- Style purement subjectif (single vs double quotes, etc.)
- Commentaires TODO/FIXME existants
- Fichiers de fixtures, mocks, données de test

## Format des commentaires
- Factuel et concis
- Pas de blabla introductif
- Proposer un fix quand c'est évident
- Préfixer par la sévérité : 🔴 critique / 🟡 important / 🔵 suggestion
