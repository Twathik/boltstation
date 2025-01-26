ETT_fonction_VD_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à l’évaluation de la fonction du ventricule droit (VD)** tout en excluant rigoureusement les valeurs numériques suivantes :  
- Diamètres du VD.  
- TAPSE (excursion systolique de l'anneau tricuspide).  
- Pic de l’onde S (onde systolique de l’anneau tricuspide).  
- FAC (Fractional Area Change).  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant la fonction globale du VD, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement à partir du contenu de la balise `<MedicalObservation>` :  
- Description de la fonction systolique globale du VD (ex., "fonction systolique normale", "dysfonction systolique modérée").  
- Description de la morphologie ou de la taille globale du VD (ex., "VD dilaté", "hypertrophie du VD").  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "FAC diminué, indiquant une altération systolique", "TAPSE bas suggérant une dysfonction systolique").  
- Présence ou absence de surcharge volumique ou pressive (ex., "surcharge volumique associée").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Diamètres du VD.  
- TAPSE.  
- Pic de l’onde S.  
- FAC.  

### 3. **Structure obligatoire de la sortie**  
- **Fonction systolique globale :** Mentionnez la description qualitative de la fonction systolique globale si rapportée.  
- **Morphologie et taille :** Mentionnez toute observation qualitative relative à la taille ou à la morphologie globale du VD (ex., dilatation, hypertrophie).  
- **Surcharge :** Mentionnez toute surcharge volumique ou pressive si rapportée.  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "FAC diminué indiquant une dysfonction systolique").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la fonction du VD n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de la fonction du VD non décrite."**  
- Si la fonction du VD est **explicitement décrite comme normale** :  
  - Répondez par : **"Fonction globale du VD normale, sans anomalies détectées."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Dysfonction systolique avec interprétation du FAC**  
**Entrée :**  
Dysfonction systolique modérée du VD. FAC diminué, suggérant une altération globale. VD légèrement dilaté.

**Sortie :**  
- **Fonction systolique globale :** Dysfonction systolique modérée du VD.  
- **Morphologie et taille :** VD légèrement dilaté.  
- **Interprétation :** FAC diminué, suggérant une altération globale.

---

### **Exemple 2 : Fonction systolique normale sans surcharge**  
**Entrée :**  
Fonction systolique normale. Absence de surcharge volumique ou pressive.

**Sortie :**  
- **Fonction systolique globale :** Fonction systolique normale.  
- **Surcharge :** Absence de surcharge volumique ou pressive.

---

### **Exemple 3 : Absence explicite de mention de la fonction du VD**  
**Entrée :**  
Aucune mention spécifique de la fonction globale du VD dans le texte.

**Sortie :**  
- **Réponse :** Évaluation de la fonction du VD non décrite.

---

### **Exemple 4 : VD dilaté avec interprétation du TAPSE**  
**Entrée :**  
VD dilaté avec TAPSE diminué, suggérant une dysfonction systolique globale.

**Sortie :**  
- **Morphologie et taille :** VD dilaté.  
- **Interprétation :** TAPSE diminué, suggérant une dysfonction systolique globale.

---
""",
}
