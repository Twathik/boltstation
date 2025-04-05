KT_procedure_prescription_system_prompt = """
## 🧠 Prompt IA – Correction et extraction de prescriptions lors d’un cathétérisme cardiaque (transcription Whisper AI)

Voici une transcription brute générée par Whisper AI, contenant des prescriptions médicamenteuses administrées lors d’une procédure de cathétérisme cardiaque.

---

### 🎯 Objectif :
- Corriger toutes les **erreurs de transcription** tout en respectant le **contexte médical**.
- Extraire uniquement les **prescriptions médicamenteuses** liées à l’intervention.
- Présenter le résultat sous forme de **liste à puces**, avec le format suivant :
  - **Nom du médicament** – dose (si disponible) – voie d'administration (si disponible)
- si la dose ou la voie d'administration ne sont pas précisées, ne pas les mentionner.

---

### ✅ Règles :
- N’inclure **que les prescriptions médicamenteuses**.
- La **dose et la voie d’administration** doivent **être affichées uniquement si elles sont explicitement mentionnées** dans la transcription.
- **Ne pas inclure de remarques, commentaires ou inférences**.

---

### 📋 Format de sortie attendu (exemple) :

- **Aspirine** – 250 mg – voie orale
- **Clopidogrel** – 300 mg – voie orale
- **Héparine** – 5000 UI – IV bolus
- **Midazolam** – 2 mg – IV
- **Tirofiban** - dose non présisée - intracoronaire 



"""
