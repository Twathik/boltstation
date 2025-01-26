ETT_CIV_widget: dict = {
    "description": """
---

## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à la Communication Interventriculaire (CIV)** tout en excluant rigoureusement les variables numériques suivantes :  
- Vitesse maximale (V max).  
- Diamètre de la CIV.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant la CIV, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement à partir du contenu de la balise `<MedicalObservation>` :  
- Présence ou absence d’une CIV.  
- Type de CIV :  
  - Péri-membraneuse.  
  - Musculaire.  
  - Inlet.  
  - Outlet.  
- Orientation du shunt associé (ex., gauche-droite, droite-gauche, bidirectionnel).  
- Description qualitative des bords ou des berges (ex., "bords épaissis" ou "bords irréguliers").  
- Anomalies associées :  
  - Dilatation des cavités droites.  
  - Hypertension pulmonaire.  
  - Signes de surcharge volumique.  
- Interprétation qualitative des valeurs numériques si rapportée (ex., "V max élevée, suggérant un shunt significatif").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Vitesse maximale (V max).  
- Diamètre de la CIV.  

### 3. **Structure obligatoire de la sortie**  
- **CIV :** Mentionnez la présence ou l'absence, le type de CIV, et l'orientation du shunt si rapportée.  
- **Bords :** Décrivez qualitativement l’aspect des bords ou berges si mentionné.  
- **Anomalies associées :** Incluez toute conséquence anatomique ou fonctionnelle (ex., dilatation des cavités droites, surcharge volumique).  
- **Interprétation :** Mentionnez l’interprétation des valeurs numériques si explicitement rapportée (ex., "V max élevée suggérant un shunt significatif").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la CIV n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Communication interventriculaire non décrite."**  
- Si une CIV est **explicitement absente** :  
  - Répondez par : **"Absence de communication interventriculaire détectée."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Présence d’une CIV avec anomalies associées**  
**Entrée :**  
Présence d’une CIV péri-membraneuse avec shunt gauche-droite. Bords réguliers. Dilatation des cavités droites et signes de surcharge volumique observés.

**Sortie :**  
- **CIV :** Communication interventriculaire (CIV) péri-membraneuse avec shunt gauche-droite.  
- **Bords :** Bords réguliers.  
- **Anomalies associées :** Dilatation des cavités droites et surcharge volumique.

---

### **Exemple 2 : Absence explicite de CIV**  
**Entrée :**  
Absence de shunt interventriculaire détecté.

**Sortie :**  
- **Réponse :** Absence de communication interventriculaire détectée.

---

### **Exemple 3 : Absence de mention de la CIV**  
**Entrée :**  
Aucune mention spécifique de communication interventriculaire dans le texte.

**Sortie :**  
- **Réponse :** Communication interventriculaire non décrite.

---

### **Exemple 4 : CIV avec interprétation des valeurs numériques**  
**Entrée :**  
Large communication interventriculaire avec shunt gauche-droite. Bords irréguliers. V max élevée, suggérant un shunt significatif.

**Sortie :**  
- **CIV :** Large communication interventriculaire avec shunt gauche-droite.  
- **Bords :** Bords irréguliers.  
- **Interprétation :** V max élevée, suggérant un shunt significatif.

---
""",
}
