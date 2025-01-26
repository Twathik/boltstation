ETT_RM_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à l’évaluation d’un rétrécissement mitral (RM)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Pressure Half-Time (PHT).  
- Gradient moyen.  
- Gradient maximal.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant le RM, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Toutes les autres données relatives au RM doivent être incluses dans l'extraction. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement à partir du contenu de la balise `<MedicalObservation>` :  
- Présence ou absence de rétrécissement mitral.  
- Étiologie ou cause si mentionnée (ex., "calcifications", "épaississement valvulaire").  
- Description qualitative de la sévérité (ex., "modéré", "sévère").  
- Anomalies structurelles associées :  
  - Calcifications.  
  - Épaississement des feuillets.  
  - Fusion des commissures.  
  - Réduction de la mobilité valvulaire.  
- Anomalies fonctionnelles associées :  
  - Dilatation de l’oreillette gauche (OG).  
  - Hypertension pulmonaire secondaire.  
  - Surcharge volumique.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "PHT prolongé suggérant un RM sévère", "gradient moyen élevé indiquant un rétrécissement significatif").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Pressure Half-Time (PHT).  
- Gradient moyen.  
- Gradient maximal.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de RM, ainsi que sa sévérité si rapportée.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., calcifications, épaississement des feuillets).  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., dilatation de l’OG, hypertension pulmonaire secondaire).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "PHT prolongé suggérant un RM sévère").  

### 4. **Gestion des absences**  
- Si **aucune mention** de RM n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation du rétrécissement mitral non décrite."**  
- Si un RM est **explicitement absent** :  
  - Répondez par : **"Absence de rétrécissement mitral détecté."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : RM sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’un RM sévère associé à un épaississement valvulaire et des calcifications. PHT prolongé, suggérant un RM significatif. Hypertension pulmonaire secondaire observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’un RM sévère.  
- **Anomalies structurelles :** Épaississement valvulaire et calcifications.  
- **Anomalies fonctionnelles :** Hypertension pulmonaire secondaire.  
- **Interprétation :** PHT prolongé, suggérant un RM significatif.

---

### **Exemple 2 : RM modéré avec OG dilatée**  
**Entrée :**  
Rétrécissement mitral modéré avec dilatation de l’oreillette gauche. Gradient moyen élevé, indiquant une obstruction significative.

**Sortie :**  
- **Présence et sévérité :** Rétrécissement mitral modéré.  
- **Anomalies fonctionnelles :** Dilatation de l’oreillette gauche.  
- **Interprétation :** Gradient moyen élevé, indiquant une obstruction significative.

---

### **Exemple 3 : Absence explicite de RM**  
**Entrée :**  
Pas de rétrécissement mitral détecté.

**Sortie :**  
- **Réponse :** Absence de rétrécissement mitral détecté.

---

### **Exemple 4 : RM avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’un RM associé à des calcifications et une réduction de la mobilité valvulaire. OG dilatée avec surcharge volumique. Gradient maximal élevé, suggérant un RM significatif.

**Sortie :**  
- **Présence et sévérité :** Présence d’un rétrécissement mitral.  
- **Anomalies structurelles :** Calcifications et réduction de la mobilité valvulaire.  
- **Anomalies fonctionnelles :** OG dilatée avec surcharge volumique.  
- **Interprétation :** Gradient maximal élevé, suggérant un RM significatif.

---
""",
}
