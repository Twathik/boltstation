ETT_CIA_widget: dict = {
    "description": """
---

## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à la Communication Interauriculaire (CIA)** tout en excluant rigoureusement les variables numériques suivantes :  
- Taille des berges.  
- Diamètre maximum de la CIA.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant la CIA, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire :  
- Présence ou absence d’une CIA.  
- Type de CIA :  
  - Ostium secundum.  
  - Ostium primum.  
  - Sinus veineux.  
  - Sinus coronaire.  
- Orientation du shunt associé (ex., gauche-droite, droite-gauche, bidirectionnel).  
- Description qualitative des berges (ex., "berges épaisses" ou "berges irrégulières").  
- Anomalies associées :  
  - Dilatation des cavités droites.  
  - Surcharge volumique.  
  - Hypertension pulmonaire associée.  
- Interprétation des valeurs numériques si rapportée (ex., "grand diamètre suggérant un shunt significatif").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Taille des berges.  
- Diamètre maximum de la CIA.  

### 3. **Structure obligatoire de la sortie**  
- **CIA :** Mentionnez la présence ou l'absence, le type de CIA, et l'orientation du shunt si rapportée.  
- **Berges :** Décrivez qualitativement l’aspect des berges si mentionné.  
- **Anomalies associées :** Incluez toute conséquence anatomique ou fonctionnelle (ex., dilatation des cavités droites, surcharge volumique).  
- **Interprétation :** Mentionnez l’interprétation des valeurs numériques si explicitement rapportée (ex., "diamètre suggérant un shunt significatif").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la CIA n’est présente dans le texte :  
  - Répondez par : **"Communication interauriculaire non décrite."**  
- Si une CIA est **explicitement absente** :  
  - Répondez par : **"Absence de communication interauriculaire détectée."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Présence d’une CIA avec anomalies associées**  
**Entrée :**  
"Présence d’une CIA de type ostium secundum avec shunt gauche-droite. Berges régulières. Dilatation des cavités droites observée."  

**Sortie :**  
- **CIA :** Communication interauriculaire (CIA) de type ostium secundum avec shunt gauche-droite.  
- **Berges :** Berges régulières.  
- **Anomalies associées :** Dilatation des cavités droites.

**Explication :**  
- Le type de CIA, l’orientation du shunt et l’état des berges sont rapportés.  
- Les anomalies associées (dilatation des cavités droites) sont incluses.  

---

### **Exemple 2 : Absence explicite de CIA**  
**Entrée :**  
"Absence de shunt intracardiaque détecté."  

**Sortie :**  
- **Réponse :** Absence de communication interauriculaire détectée.

**Explication :**  
- L’absence explicite de CIA est signalée conformément aux règles.

---

### **Exemple 3 : Absence de mention de la CIA**  
**Entrée :**  
"Aucune mention spécifique de communication interauriculaire dans le texte."  

**Sortie :**  
- **Réponse :** Communication interauriculaire non décrite.

**Explication :**  
- L’absence de mention est notifiée sans interprétation supplémentaire.

---

### **Exemple 4 : CIA avec interprétation des valeurs numériques**  
**Entrée :**  
"Large communication interauriculaire avec shunt gauche-droite. Berges épaisses. Grand diamètre suggérant un shunt significatif."  

**Sortie :**  
- **CIA :** Large communication interauriculaire avec shunt gauche-droite.  
- **Berges :** Berges épaisses.  
- **Interprétation :** Grand diamètre suggérant un shunt significatif.

**Explication :**  
- L’interprétation qualitative des valeurs numériques est incluse, mais les valeurs elles-mêmes sont ignorées.

---
""",
}
