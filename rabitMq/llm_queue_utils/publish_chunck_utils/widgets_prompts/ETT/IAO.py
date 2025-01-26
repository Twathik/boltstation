ETT_IAO_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’une insuffisance aortique (IAO)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Surface de l’Orifice Régurgitant (SOR).  
- Volume Régurgitant (VR).  
- Pressure Half-Time (PHT).  
- Vitesse télésystolique isthmique.  
- Vena contracta.  

L'agent devra **ignorer toutes les données non en rapport avec l’IAO** et se concentrer uniquement sur les observations qualitatives pertinentes concernant l’IAO, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives à l’IAO et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence d’une IAO.  
- Description qualitative de la sévérité (ex., "modérée", "sévère").  
- Étiologie ou cause de l’IAO si mentionnée (ex., "déchirure valvulaire", "dilatation de l’aorte ascendante").  
- Anomalies structurelles associées :  
  - Calcifications valvulaires.  
  - Déchirures des cuspides.  
  - Épaississement valvulaire.  
  - Dilatation de l’aorte ascendante ou de la racine aortique.  
- Anomalies fonctionnelles associées :  
  - Hypertrophie du ventricule gauche (VG).  
  - Dilatation du VG.  
  - Signes de surcharge volumique ou pressive.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "SOR augmenté suggérant une IAO sévère", "VR élevé indiquant une régurgitation importante").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec l’IAO.  
- Les valeurs numériques suivantes même si elles sont relatives à l’IAO :  
  - Surface de l’Orifice Régurgitant (SOR).  
  - Volume Régurgitant (VR).  
  - Pressure Half-Time (PHT).  
  - Vitesse télésystolique isthmique.  
  - Vena contracta.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de l’IAO, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées.  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., hypertrophie ou dilatation du VG).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "SOR augmenté suggérant une régurgitation sévère").  

### 4. **Gestion des absences**  
- Si **aucune mention** de l’IAO n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de l’insuffisance aortique non décrite."**  
- Si une IAO est **explicitement absente** :  
  - Répondez par : **"Absence d’insuffisance aortique détectée."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : IAO sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’une IAO sévère associée à une déchirure valvulaire. SOR augmenté, suggérant une régurgitation sévère. Hypertrophie du VG observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une IAO sévère.  
- **Étiologie :** Déchirure valvulaire.  
- **Anomalies fonctionnelles :** Hypertrophie du VG.  
- **Interprétation :** SOR augmenté, suggérant une régurgitation sévère.

---

### **Exemple 2 : IAO modérée avec surcharge volumique**  
**Entrée :**  
IAO modérée associée à une dilatation de l’aorte ascendante. VR élevé indiquant une régurgitation modérée. Surcharge volumique observée.

**Sortie :**  
- **Présence et sévérité :** IAO modérée.  
- **Anomalies structurelles :** Dilatation de l’aorte ascendante.  
- **Anomalies fonctionnelles :** Surcharge volumique.  
- **Interprétation :** VR élevé, indiquant une régurgitation modérée.

---

### **Exemple 3 : Absence explicite d’IAO**  
**Entrée :**  
Pas d’insuffisance aortique détectée.

**Sortie :**  
- **Réponse :** Absence d’insuffisance aortique détectée.

---

### **Exemple 4 : IAO avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’une IAO associée à une réduction de la mobilité des cuspides. PHT prolongé, suggérant une régurgitation importante. Dilatation du VG observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une insuffisance aortique.  
- **Anomalies structurelles :** Réduction de la mobilité des cuspides.  
- **Anomalies fonctionnelles :** Dilatation du VG.  
- **Interprétation :** PHT prolongé, suggérant une régurgitation importante.

---
""",
}
