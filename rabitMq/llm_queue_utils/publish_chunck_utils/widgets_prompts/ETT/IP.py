ETT_IP_widget: dict = {
    "description": """
---

## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’une insuffisance pulmonaire (IP)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Temps de décélération.  
- Pressure Half-Time (PHT).  
- Index de régurgitation.  

L'agent devra **ignorer toutes les données non en rapport avec l’IP** et se concentrer uniquement sur les observations qualitatives pertinentes concernant l’IP, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives à l’IP et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence d’une IP.  
- Description qualitative de la sévérité (ex., "modérée", "sévère").  
- Étiologie ou cause de l’IP si mentionnée (ex., "dilatation de l’anneau pulmonaire", "dysfonction valvulaire").  
- Anomalies structurelles associées :  
  - Dilatation de l’anneau pulmonaire.  
  - Calcifications ou épaississement des cuspides.  
  - Dysfonction valvulaire.  
- Anomalies fonctionnelles associées :  
  - Dilatation du ventricule droit (VD).  
  - Surcharge volumique des cavités droites.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "index de régurgitation élevé, indiquant une régurgitation sévère", "temps de décélération court, suggérant une régurgitation importante").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec l’IP.  
- Les valeurs numériques suivantes même si elles sont relatives à l’IP :  
  - Temps de décélération.  
  - Pressure Half-Time (PHT).  
  - Index de régurgitation.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence d’IP, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., dilatation de l’anneau pulmonaire, épaississement des cuspides).  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., surcharge volumique des cavités droites).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "temps de décélération court, indiquant une régurgitation importante").  

### 4. **Gestion des absences**  
- Si **aucune mention** d’IP n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de l’insuffisance pulmonaire non décrite."**  
- Si une IP est **explicitement absente** :  
  - Répondez par : **"Absence d’insuffisance pulmonaire détectée."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : IP sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’une IP sévère associée à une dilatation de l’anneau pulmonaire. Temps de décélération court, indiquant une régurgitation sévère. Dilatation du VD observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une IP sévère.  
- **Anomalies structurelles :** Dilatation de l’anneau pulmonaire.  
- **Anomalies fonctionnelles :** Dilatation du VD.  
- **Interprétation :** Temps de décélération court, indiquant une régurgitation sévère.

---

### **Exemple 2 : IP modérée avec surcharge volumique**  
**Entrée :**  
IP modérée due à un épaississement des cuspides. Index de régurgitation élevé, indiquant une régurgitation modérée. Surcharge volumique des cavités droites associée.

**Sortie :**  
- **Présence et sévérité :** IP modérée.  
- **Étiologie :** Épaississement des cuspides.  
- **Anomalies fonctionnelles :** Surcharge volumique des cavités droites.  
- **Interprétation :** Index de régurgitation élevé, indiquant une régurgitation modérée.

---

### **Exemple 3 : Absence explicite d’IP**  
**Entrée :**  
Pas d’insuffisance pulmonaire détectée.

**Sortie :**  
- **Réponse :** Absence d’insuffisance pulmonaire détectée.

---

### **Exemple 4 : IP avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’une IP associée à un épaississement valvulaire. PHT prolongé, suggérant une régurgitation importante. Dilatation des cavités droites observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’une insuffisance pulmonaire.  
- **Anomalies structurelles :** Épaississement valvulaire.  
- **Anomalies fonctionnelles :** Dilatation des cavités droites.  
- **Interprétation :** PHT prolongé, suggérant une régurgitation importante.

---
""",
}
