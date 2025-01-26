ETT_RAO_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation d’un rétrécissement aortique (RAO)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Vitesse maximale aortique (V max).  
- Surface fonctionnelle aortique.  
- Gradient maximal.  
- Gradient moyen.  
- Index de perméabilité.  

L'agent devra **ignorer toutes les données non en rapport avec le RAO** et se concentrer uniquement sur les observations qualitatives pertinentes concernant le RAO, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives au RAO et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence de rétrécissement aortique.  
- Description qualitative de la sévérité (ex., "modéré", "sévère").  
- Étiologie ou cause du RAO si mentionnée (ex., "calcifications étendues", "valve aortique bicuspide").  
- Anomalies structurelles associées :  
  - Calcifications des cuspides.  
  - Réduction de la mobilité des cuspides.  
  - Fusion des commissures.  
- Anomalies fonctionnelles associées :  
  - Hypertrophie du ventricule gauche (VG).  
  - Signes de surcharge pressive.  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "surface fonctionnelle réduite suggérant une sténose critique", "gradient moyen élevé indiquant une obstruction sévère").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec le RAO.  
- Les valeurs numériques suivantes même si elles sont relatives au RAO :  
  - Vitesse maximale aortique (V max).  
  - Surface fonctionnelle aortique.  
  - Gradient maximal.  
  - Gradient moyen.  
  - Index de perméabilité.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et sévérité :** Mentionnez la présence ou l'absence de RAO, ainsi que sa sévérité si rapportée.  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., calcifications, fusion des commissures).  
- **Anomalies fonctionnelles :** Mentionnez les conséquences fonctionnelles associées (ex., hypertrophie du VG, surcharge pressive).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "gradient moyen élevé indiquant une sténose sévère").  

### 4. **Gestion des absences**  
- Si **aucune mention** de RAO n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation du rétrécissement aortique non décrite."**  
- Si un RAO est **explicitement absent** :  
  - Répondez par : **"Absence de rétrécissement aortique détecté."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : RAO sévère avec anomalies structurelles**  
**Entrée :**  
Présence d’un RAO sévère avec calcifications étendues des cuspides. Surface fonctionnelle réduite, suggérant une sténose critique. Hypertrophie du VG observée.

**Sortie :**  
- **Présence et sévérité :** Présence d’un RAO sévère.  
- **Anomalies structurelles :** Calcifications étendues des cuspides.  
- **Anomalies fonctionnelles :** Hypertrophie du VG.  
- **Interprétation :** Surface fonctionnelle réduite, suggérant une sténose critique.

---

### **Exemple 2 : RAO modéré avec surcharge pressive**  
**Entrée :**  
RAO modéré associé à une fusion des commissures. Gradient moyen élevé, indiquant une obstruction modérée.

**Sortie :**  
- **Présence et sévérité :** RAO modéré.  
- **Anomalies structurelles :** Fusion des commissures.  
- **Interprétation :** Gradient moyen élevé, indiquant une obstruction modérée.

---

### **Exemple 3 : Absence explicite de RAO**  
**Entrée :**  
Pas de rétrécissement aortique détecté.

**Sortie :**  
- **Réponse :** Absence de rétrécissement aortique détecté.

---

### **Exemple 4 : RAO avec anomalies structurelles et fonctionnelles**  
**Entrée :**  
Présence d’un RAO associé à une réduction de la mobilité des cuspides. V max élevée, indiquant une sténose significative. Hypertrophie du VG et surcharge pressive observées.

**Sortie :**  
- **Présence et sévérité :** Présence d’un rétrécissement aortique.  
- **Anomalies structurelles :** Réduction de la mobilité des cuspides.  
- **Anomalies fonctionnelles :** Hypertrophie du VG et surcharge pressive.  
- **Interprétation :** V max élevée, indiquant une sténose significative.

---
""",
}
