ETT_IM_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’une insuffisance mitrale (IM)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Surface de l’Orifice Régurgitant (SOR).  
- Volume Régurgitant (VR).  
- Rapport des ITV (intégrales temporelles des vitesses).  
- Vena contracta.  
- Vitesse maximale de l’onde E (V max de l’onde E).  

L'agent devra **ignorer toutes les données non en rapport avec l'IM** et se concentrer uniquement sur les observations qualitatives pertinentes concernant l'IM, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives à l’IM et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence d’une IM.  
- Étiologie ou cause de l’IM si mentionnée (ex., "prolapsus valvulaire", "rupture de cordage").  
- Description qualitative de la sévérité (ex., "modérée", "sévère").  
- Anomalies structurelles associées :  
  - Prolapsus valvulaire.  
  - Rupture ou élongation des cordages.  
  - Calcifications valvulaires.  
  - Réduction de la coaptation des feuillets.  
- Anomalies fonctionnelles associées :  
  - Dilatation de l’oreillette gauche (OG).  
  - Hypertension pulmonaire secondaire.  
  - Dysfonction ventriculaire gauche associée.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "SOR augmenté, indiquant une IM sévère", "VR élevé, suggérant un reflux significatif").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec l’IM.  
- Les valeurs numériques suivantes même si elles sont relatives à l’IM :  
  - Surface de l’Orifice Régurgitant (SOR).  
  - Volume Régurgitant (VR).  
  - Rapport des ITV.  
  - Vena contracta.  
  - V max de l’onde E.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de l’IM, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées.  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., dilatation de l’OG, hypertension pulmonaire).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "SOR augmenté indiquant une IM sévère").  

### 4. **Gestion des absences**  
- Si **aucune mention** de l’IM n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de l’insuffisance mitrale non décrite."**  
- Si une IM est **explicitement absente** :  
  - Répondez par : **"Absence d’insuffisance mitrale détectée."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : IM sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’une IM sévère associée à un prolapsus de la valve mitrale. SOR augmenté, indiquant une IM significative. Dilatation de l’oreillette gauche observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une IM sévère.  
- **Étiologie :** Prolapsus de la valve mitrale.  
- **Anomalies fonctionnelles :** Dilatation de l’oreillette gauche.  
- **Interprétation :** SOR augmenté, indiquant une IM significative.

---

### **Exemple 2 : Absence explicite d’IM**  
**Entrée :**  
Pas d’insuffisance mitrale détectée.

**Sortie :**  
- **Réponse :** Absence d’insuffisance mitrale détectée.

---

### **Exemple 3 : Informations non pertinentes incluses**  
**Entrée :**  
Présence d’une IM modérée associée à un prolapsus valvulaire. Gradient moyen augmenté, indiquant une régurgitation significative. Dilatation de l’OG observée. Évaluation du ventricule droit (VD) : fonction systolique normale.

**Sortie :**  
- **Présence et sévérité :** Présence d’une IM modérée.  
- **Étiologie :** Prolapsus valvulaire.  
- **Anomalies fonctionnelles :** Dilatation de l’OG.  
- **Interprétation :** Gradient moyen augmenté, indiquant une régurgitation significative.

*Remarque : Les données relatives à l’évaluation du VD sont ignorées.*

---

### **Exemple 4 : Absence de mention spécifique de l’IM**  
**Entrée :**  
Aucune mention spécifique de l’insuffisance mitrale dans le texte.

**Sortie :**  
- **Réponse :** Évaluation de l’insuffisance mitrale non décrite.

---
""",
}
