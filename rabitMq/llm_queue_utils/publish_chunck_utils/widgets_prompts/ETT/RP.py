ETT_RP_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’un rétrécissement pulmonaire (RP)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Vitesse maximale (V max).  
- Gradient maximal.  
- Gradient moyen.  

L'agent devra **ignorer toutes les données non en rapport avec le RP** et se concentrer uniquement sur les observations qualitatives pertinentes concernant le RP, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives au RP et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence de rétrécissement pulmonaire.  
- Description qualitative de la sévérité (ex., "modéré", "sévère").  
- Étiologie ou cause du RP si mentionnée (ex., "fusion des commissures", "calcifications").  
- Anomalies structurelles associées :  
  - Calcifications des cuspides.  
  - Réduction de la mobilité des cuspides.  
  - Fusion des commissures.  
- Anomalies fonctionnelles associées :  
  - Hypertrophie du ventricule droit (VD).  
  - Surcharge pressive ou volumique des cavités droites.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "gradient moyen élevé, indiquant une sténose modérée", "V max élevée, suggérant une obstruction significative").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec le RP.  
- Les valeurs numériques suivantes même si elles sont relatives au RP :  
  - Vitesse maximale (V max).  
  - Gradient maximal.  
  - Gradient moyen.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de RP, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., calcifications, fusion des commissures).  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., surcharge pressive des cavités droites).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "gradient moyen élevé indiquant une sténose modérée").  

### 4. **Gestion des absences**  
- Si **aucune mention** de RP n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation du rétrécissement pulmonaire non décrite."**  
- Si un RP est **explicitement absent** :  
  - Répondez par : **"Absence de rétrécissement pulmonaire détecté."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : RP sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’un RP sévère associé à une calcification étendue des cuspides. Gradient moyen élevé, suggérant une sténose critique. Hypertrophie du VD observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’un RP sévère.  
- **Anomalies structurelles :** Calcification étendue des cuspides.  
- **Anomalies fonctionnelles :** Hypertrophie du VD.  
- **Interprétation :** Gradient moyen élevé, suggérant une sténose critique.

---

### **Exemple 2 : RP modéré avec surcharge pressive**  
**Entrée :**  
RP modéré avec une réduction de la mobilité des cuspides. V max élevée, indiquant une obstruction modérée. Surcharge pressive des cavités droites associée.

**Sortie :**  
- **Présence et sévérité :** RP modéré.  
- **Anomalies structurelles :** Réduction de la mobilité des cuspides.  
- **Anomalies fonctionnelles :** Surcharge pressive des cavités droites.  
- **Interprétation :** V max élevée, indiquant une obstruction modérée.

---

### **Exemple 3 : Absence explicite de RP**  
**Entrée :**  
Pas de rétrécissement pulmonaire détecté.

**Sortie :**  
- **Réponse :** Absence de rétrécissement pulmonaire détecté.

---

### **Exemple 4 : RP avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’un RP associé à une fusion des commissures. Gradient moyen élevé, suggérant une sténose importante. Dilatation des cavités droites observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’un rétrécissement pulmonaire.  
- **Anomalies structurelles :** Fusion des commissures.  
- **Anomalies fonctionnelles :** Dilatation des cavités droites.  
- **Interprétation :** Gradient moyen élevé, suggérant une sténose importante.

---
""",
}
