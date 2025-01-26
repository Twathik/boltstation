ETT_RT_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’un rétrécissement tricuspide (RT)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Vitesse maximale (V max).  
- Gradient moyen.  

L'agent devra **ignorer toutes les données non en rapport avec le RT** et se concentrer uniquement sur les observations qualitatives pertinentes concernant le RT, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives au RT et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence de rétrécissement tricuspide.  
- Description qualitative de la sévérité (ex., "modéré", "sévère").  
- Étiologie ou cause du RT si mentionnée (ex., "calcifications", "fusion des commissures").  
- Anomalies structurelles associées :  
  - Calcifications des feuillets.  
  - Réduction de la mobilité valvulaire.  
  - Fusion des commissures.  
- Anomalies fonctionnelles associées :  
  - Dilatation de l’oreillette droite (OD).  
  - Signes de surcharge pressive des cavités droites.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "gradient moyen élevé, indiquant une sténose modérée", "V max élevée, suggérant une obstruction significative").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec le RT.  
- Les valeurs numériques suivantes même si elles sont relatives au RT :  
  - Vitesse maximale (V max).  
  - Gradient moyen.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de RT, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., calcifications, fusion des commissures).  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., dilatation de l’OD, surcharge pressive).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "gradient moyen élevé indiquant une sténose modérée").  

### 4. **Gestion des absences**  
- Si **aucune mention** de RT n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation du rétrécissement tricuspide non décrite."**  
- Si un RT est **explicitement absent** :  
  - Répondez par : **"Absence de rétrécissement tricuspide détecté."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : RT sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’un RT sévère associé à une calcification étendue des feuillets. Gradient moyen élevé, suggérant une sténose critique. Dilatation de l’OD observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’un RT sévère.  
- **Anomalies structurelles :** Calcification étendue des feuillets.  
- **Anomalies fonctionnelles :** Dilatation de l’OD.  
- **Interprétation :** Gradient moyen élevé, suggérant une sténose critique.

---

### **Exemple 2 : RT modéré avec surcharge pressive**  
**Entrée :**  
RT modéré associé à une fusion des commissures. V max élevée, indiquant une obstruction modérée. Surcharge pressive des cavités droites associée.

**Sortie :**  
- **Présence et sévérité :** RT modéré.  
- **Anomalies structurelles :** Fusion des commissures.  
- **Anomalies fonctionnelles :** Surcharge pressive des cavités droites.  
- **Interprétation :** V max élevée, indiquant une obstruction modérée.

---

### **Exemple 3 : Absence explicite de RT**  
**Entrée :**  
Pas de rétrécissement tricuspide détecté.

**Sortie :**  
- **Réponse :** Absence de rétrécissement tricuspide détecté.

---

### **Exemple 4 : RT avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’un RT associé à une réduction de la mobilité des feuillets. Gradient moyen élevé, suggérant une sténose importante. Dilatation de l’OD et surcharge pressive observées.

**Sortie :**  
- **Présence et sévérité :** Présence d’un rétrécissement tricuspide.  
- **Anomalies structurelles :** Réduction de la mobilité des feuillets.  
- **Anomalies fonctionnelles :** Dilatation de l’OD et surcharge pressive.  
- **Interprétation :** Gradient moyen élevé, suggérant une sténose importante.

---
""",
}
