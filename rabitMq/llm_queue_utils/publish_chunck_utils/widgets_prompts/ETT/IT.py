ETT_IT_widget: dict = {
    "description": """
---

## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’une insuffisance tricuspide (IT)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Surface de l’Orifice Régurgitant (SOR).  
- Volume Régurgitant (VR).  
- Flux veineux sous-hépatique.  
- Vitesse de l’onde E.  

L'agent devra **ignorer toutes les données non en rapport avec l’IT** et se concentrer uniquement sur les observations qualitatives pertinentes concernant l’IT, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives à l’IT et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence d’une IT.  
- Description qualitative de la sévérité (ex., "modérée", "sévère").  
- Étiologie ou cause de l’IT si mentionnée (ex., "dilatation de l’anneau tricuspide", "rupture de cordage").  
- Anomalies structurelles associées :  
  - Dilatation de l’anneau tricuspide.  
  - Malformation ou dysfonctionnement des feuillets valvulaires.  
  - Calcifications.  
- Anomalies fonctionnelles associées :  
  - Dilatation de l’oreillette droite (OD).  
  - Hypertension pulmonaire secondaire.  
  - Surcharge volumique ou pressive des cavités droites.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "SOR augmenté, suggérant une IT sévère", "VR élevé, indiquant une régurgitation importante").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec l’IT.  
- Les valeurs numériques suivantes même si elles sont relatives à l’IT :  
  - Surface de l’Orifice Régurgitant (SOR).  
  - Volume Régurgitant (VR).  
  - Flux veineux sous-hépatique.  
  - Vitesse de l’onde E.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de l’IT, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., dilatation de l’anneau tricuspide, calcifications).  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., surcharge volumique des cavités droites).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "SOR augmenté suggérant une régurgitation sévère").  

### 4. **Gestion des absences**  
- Si **aucune mention** de l’IT n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de l’insuffisance tricuspide non décrite."**  
- Si une IT est **explicitement absente** :  
  - Répondez par : **"Absence d’insuffisance tricuspide détectée."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : IT sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’une IT sévère associée à une dilatation de l’anneau tricuspide. SOR augmenté, indiquant une régurgitation sévère. Hypertension pulmonaire secondaire observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une IT sévère.  
- **Anomalies structurelles :** Dilatation de l’anneau tricuspide.  
- **Anomalies fonctionnelles :** Hypertension pulmonaire secondaire.  
- **Interprétation :** SOR augmenté, indiquant une régurgitation sévère.

---

### **Exemple 2 : IT modérée avec surcharge volumique**  
**Entrée :**  
IT modérée avec dilatation de l’OD. VR élevé, suggérant une régurgitation modérée. Surcharge volumique des cavités droites associée.

**Sortie :**  
- **Présence et sévérité :** IT modérée.  
- **Anomalies fonctionnelles :** Dilatation de l’OD et surcharge volumique des cavités droites.  
- **Interprétation :** VR élevé, suggérant une régurgitation modérée.

---

### **Exemple 3 : Absence explicite d’IT**  
**Entrée :**  
Pas d’insuffisance tricuspide détectée.

**Sortie :**  
- **Réponse :** Absence d’insuffisance tricuspide détectée.

---

### **Exemple 4 : IT avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’une IT associée à un prolapsus valvulaire. Flux veineux sous-hépatique inversé, indiquant une régurgitation importante. Dilatation de l’OD observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une insuffisance tricuspide.  
- **Anomalies structurelles :** Prolapsus valvulaire.  
- **Anomalies fonctionnelles :** Dilatation de l’OD.  
- **Interprétation :** Flux veineux sous-hépatique inversé, indiquant une régurgitation importante.

---
""",
}
