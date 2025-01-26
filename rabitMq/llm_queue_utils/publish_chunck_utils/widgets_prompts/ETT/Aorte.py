ETT_Aorte_widget: dict = {
    "description": """
---

## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire exclusivement les informations relatives à l’évaluation de la racine de l’aorte**, tout en excluant rigoureusement les valeurs numériques suivantes :  
- Diamètre de l’anneau aortique.  
- Diamètre des sinus de Valsalva.  
- Diamètre de la jonction sino-tubulaire.  
- Diamètre de l’aorte ascendante.  

L'agent devra **ignorer toutes les données non en rapport avec l’évaluation de la racine de l’aorte** et se concentrer uniquement sur les observations qualitatives pertinentes concernant cette structure, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement les informations suivantes relatives à l’évaluation de la racine de l’aorte et présentes dans la balise `<MedicalObservation>` :  
- Présence ou absence d’anomalies de la racine de l’aorte.  
- Description qualitative de la taille ou de la morphologie globale (ex., "racine aortique dilatée", "aorte ascendante normale").  
- Étiologie ou cause des anomalies si mentionnée (ex., "maladie bicuspide", "syndrome de Marfan").  
- Anomalies structurelles associées :  
  - Dilatation des sinus de Valsalva.  
  - Épaississement ou calcification de l’anneau aortique.  
  - Anomalies congénitales (ex., "valve bicuspide").  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "diamètre augmenté suggérant une dilatation importante").  

### 2. **Données interdites**  
L'agent doit **ignorer** :  
- Toute information non en rapport avec l’évaluation de la racine de l’aorte.  
- Les valeurs numériques suivantes même si elles sont relatives à l’évaluation de la racine de l’aorte :  
  - Diamètre de l’anneau aortique.  
  - Diamètre des sinus de Valsalva.  
  - Diamètre de la jonction sino-tubulaire.  
  - Diamètre de l’aorte ascendante.  

### 3. **Structure obligatoire de la sortie**  
- **Présence et description :** Mentionnez la présence ou l'absence d’anomalies, ainsi qu’une description qualitative si rapportée (ex., "dilatation significative des sinus de Valsalva").  
- **Étiologie :** Décrivez la cause ou le mécanisme sous-jacent si mentionné.  
- **Anomalies structurelles :** Décrivez qualitativement les anomalies structurelles observées (ex., dilatation, épaississement).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "diamètre augmenté suggérant une dilatation importante").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la racine de l’aorte n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de la racine de l’aorte non décrite."**  
- Si la racine de l’aorte est **explicitement décrite comme normale** :  
  - Répondez par : **"Racine de l’aorte normale, sans anomalies détectées."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Dilatation des sinus de Valsalva avec anomalies structurelles**  
**Entrée :**  
Racine de l’aorte présentant une dilatation significative des sinus de Valsalva. Diamètre augmenté, indiquant une dilatation importante. Aucune anomalie congénitale observée.

**Sortie :**  
- **Présence et description :** Dilatation significative des sinus de Valsalva.  
- **Interprétation :** Diamètre augmenté, indiquant une dilatation importante.

---

### **Exemple 2 : Aorte ascendante normale**  
**Entrée :**  
Aorte ascendante normale sans signes de dilatation ou d’épaississement.

**Sortie :**  
- **Présence et description :** Aorte ascendante normale, sans signes de dilatation ou d’épaississement.

---

### **Exemple 3 : Absence explicite de mention d’anomalies de la racine de l’aorte**  
**Entrée :**  
Pas d’anomalies détectées au niveau de la racine de l’aorte.

**Sortie :**  
- **Réponse :** Racine de l’aorte normale, sans anomalies détectées.

---

### **Exemple 4 : Racine de l’aorte dilatée avec étiologie sous-jacente**  
**Entrée :**  
Présence d’une dilatation de la racine de l’aorte associée à une valve aortique bicuspide. Diamètre des sinus de Valsalva augmenté, suggérant une dilatation significative.

**Sortie :**  
- **Présence et description :** Dilatation de la racine de l’aorte.  
- **Étiologie :** Valve aortique bicuspide.  
- **Interprétation :** Diamètre des sinus de Valsalva augmenté, suggérant une dilatation significative.

---
""",
}
