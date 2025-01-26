ECG_analyse_rythme_widget: dict = {
    "description": """
**Contexte :**  
Analysez `<MedicalObservation>` pour **extraire uniquement les informations liées au rythme cardiaque observé sur l’ECG**, en excluant toutes les données non pertinentes ou non directement liées au rythme (complexe QRS, segments ST, espace PR, ondes T, anomalies de repolarisation, etc.). Structurez les résultats sous forme de paragraphe fluide sans mentionner de référence au patient (par exemple : "le patient" ou "la patiente").

---

### **Règles d’Extraction**

1. **Données autorisées :**  
   - **Origine du rythme :** Sinusal, auriculaire, jonctionnel, ventriculaire.  
   - **Fréquence cardiaque :** Exprimée en bpm.  
   - **Régularité du rythme :** Régulier ou irrégulier.  
   - **Relation onde P-QRS :** 1:1, dissociation auriculo-ventriculaire, ou autre.  
   - **Autres anomalies spécifiques liées au rythme :** Fibrillation auriculaire, flutter auriculaire, bigéminisme, etc.

2. **Données interdites :**  
   - **N’incluez aucune information liée aux éléments suivants, même si elles figurent dans `<MedicalObservation>` :**  
     - Complexes QRS (ex. élargissement, blocs de branche).  
     - Segments ST (ex. sus-décalage, sous-décalage).  
     - Ondes T ou P non spécifiquement liées à la description du rythme.  
     - Informations non liées au rythme (ex. hypertrophies, anomalies de conduction).  

3. **Structure obligatoire de la sortie :**  
   - **Origine du rythme :** Précisez si le rythme est sinusal, auriculaire, jonctionnel ou ventriculaire.  
   - **Fréquence cardiaque :** Indiquez la fréquence en bpm.  
   - **Régularité :** Précisez si le rythme est régulier ou irrégulier.  
   - **Relation onde P-QRS :** Décrivez la relation entre les ondes P et les complexes QRS (ex. 1:1, dissociation, conduction anormale).  
   - **Résumé des anomalies spécifiques du rythme (le cas échéant) :** Incluez uniquement les anomalies directement liées au rythme cardiaque.

4. **Gestion des absences :**  
   - Si aucune information sur le rythme n’est disponible dans `<MedicalObservation>`, la sortie doit être : **"Informations sur le rythme non disponibles."**

---

""",
    "examples": """
### ** Exemples d'entrées et sorties attendues :**

#### **Exemple 1**
**Entrée :**  
"Rythme sinusal à 82 bpm, bloc de branche droit complet (BBDc), sous-décalage ST en DII, DIII et aVF."  
**Sortie :**  
Rythme sinusal, avec une fréquence cardiaque de 82 bpm. Le rythme est régulier, avec une relation onde P-QRS normale.

**Explication :**  
- Le rythme est décrit comme sinusal avec une fréquence de 82 bpm, conformément à `<MedicalObservation>`.  
- Les informations sur le BBDc et le sous-décalage ST sont ignorées car elles ne concernent pas le rythme.

---

#### **Exemple 2**  
**Entrée :**  
"Fibrillation auriculaire avec réponse ventriculaire irrégulière à 120 bpm. Complexes QRS élargis à 140 ms."  
**Sortie :**  
Rythme irrégulier, caractérisé par une fibrillation auriculaire avec une fréquence ventriculaire de 120 bpm.

**Explication :**  
- La fibrillation auriculaire et la fréquence ventriculaire sont rapportées car elles concernent le rythme.  
- Les complexes QRS élargis sont ignorés car ils ne sont pas directement liés au rythme.

---

#### **Exemple 3**  
**Entrée :**  
"Bigéminisme ventriculaire avec fréquence sinusale à 70 bpm."  
**Sortie :**  
Rythme sinusal, avec une fréquence cardiaque de 70 bpm. Des épisodes de bigéminisme ventriculaire sont observés.

**Explication :**  
- Le rythme sinusal et la fréquence sont décrits, avec mention de l’anomalie spécifique liée au rythme (bigéminisme ventriculaire).

---

#### **Exemple 4**  
**Entrée :**  
"Aucune anomalie notable sur l’ECG."  
**Sortie :**  
Rythme sinusal, avec une fréquence cardiaque normale. Le rythme est régulier, avec une relation onde P-QRS normale.

**Explication :**  
- Aucune anomalie liée au rythme n’étant mentionnée, la sortie reflète un rythme sinusal normal.

---

#### **Exemple 5**  
**Entrée :**  
"Présence d’un flutter auriculaire à 150 bpm, conduction auriculo-ventriculaire 2:1."  
**Sortie :**  
Flutter auriculaire avec une fréquence de 150 bpm. Une conduction auriculo-ventriculaire 2:1 est observée.

**Explication :**  
- Le flutter auriculaire, sa fréquence, et la relation onde P-QRS (2:1) sont rapportés.

---

### **Rappel Important**
- **N’incluez aucune information ou interprétation non liée au rythme cardiaque.**  
- Tout élément mentionné dans `<MedicalObservation>` mais n’ayant pas de lien direct avec le rythme doit être ignoré.  
- La sortie ne doit pas contenir de référence au patient, comme "le patient" ou "la patiente".

---
""",
}
