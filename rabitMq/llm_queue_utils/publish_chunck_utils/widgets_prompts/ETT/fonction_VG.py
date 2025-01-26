ETT_fonction_VG_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à l’évaluation de la fonction du ventricule gauche (VG)** tout en excluant rigoureusement :  
- Les valeurs numériques suivantes :  
  - Diamètre télédiastolique (DTD).  
  - Diamètre télésystolique (DTS).  
  - Volume télésystolique (VTS).  
  - Volume télédiastolique (VTD).  
  - Strain global longitudinal systolique (GLS).  
- Toute donnée relative à la **cinétique du VG** (ex., zones d'hypokinésie, akinésie), qui sont sous la responsabilité d’un autre agent IA.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant la fonction globale du VG, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement à partir du contenu de la balise `<MedicalObservation>` :  
- Description de la fonction systolique globale (ex., "fonction systolique normale", "dysfonction systolique modérée").  
- Description de la fonction diastolique globale (ex., "trouble de relaxation", "dysfonction diastolique sévère").  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "GLS diminué, indiquant une dysfonction systolique globale", "augmentation du VTD, suggérant une dilatation du VG").  
- Observations qualitatives globales concernant la morphologie ou la taille du VG (ex., "VG hypertrophié").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Toutes les valeurs numériques suivantes :  
  - DTD (diamètre télédiastolique).  
  - DTS (diamètre télésystolique).  
  - VTS (volume télésystolique).  
  - VTD (volume télédiastolique).  
  - Strain GLS.  
- Toutes les données relatives à la **cinétique régionale du VG** (ex., hypokinésie, akinésie).  

### 3. **Structure obligatoire de la sortie**  
- **Fonction systolique globale :** Mentionnez la description qualitative de la fonction systolique globale si rapportée.  
- **Fonction diastolique globale :** Mentionnez la description qualitative de la fonction diastolique globale si rapportée.  
- **Morphologie et taille :** Incluez toute observation qualitative relative à la taille ou à la morphologie globale du VG (ex., hypertrophie, dilatation).  
- **Interprétation :** Mentionnez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "GLS diminué indiquant une dysfonction globale").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la fonction du VG n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de la fonction du VG non décrite."**  
- Si la fonction du VG est **explicitement décrite comme normale** :  
  - Répondez par : **"Fonction globale du VG normale, sans anomalies détectées."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Dysfonction systolique modérée avec interprétation du GLS**  
**Entrée :**  
Dysfonction systolique modérée du VG. GLS diminué, suggérant une altération globale. VG légèrement dilaté.

**Sortie :**  
- **Fonction systolique globale :** Dysfonction systolique modérée du VG.  
- **Morphologie et taille :** VG légèrement dilaté.  
- **Interprétation :** GLS diminué, suggérant une altération globale.

---

### **Exemple 2 : Fonction systolique et diastolique normales**  
**Entrée :**  
Fonction systolique normale. Fonction diastolique normale, sans signes de trouble de relaxation.

**Sortie :**  
- **Fonction systolique globale :** Fonction systolique normale.  
- **Fonction diastolique globale :** Fonction diastolique normale, sans signes de trouble de relaxation.

---

### **Exemple 3 : Absence explicite de mention de la fonction du VG**  
**Entrée :**  
Aucune mention spécifique de la fonction globale du VG dans le texte.

**Sortie :**  
- **Réponse :** Évaluation de la fonction du VG non décrite.

---

### **Exemple 4 : Trouble de relaxation avec interprétation des volumes**  
**Entrée :**  
Trouble de relaxation du VG. Augmentation du VTD, suggérant une dilatation du ventricule gauche.

**Sortie :**  
- **Fonction diastolique globale :** Trouble de relaxation du VG.  
- **Interprétation :** Augmentation du VTD, suggérant une dilatation du ventricule gauche.

---
""",
}
