ETT_Shunts_widget: dict = {
    "description": """
---

## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives aux shunts intracardiaques** tout en excluant rigoureusement les variables numériques suivantes :  
- Rapport QP/QS.  
- Valeur des résistances pulmonaires.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant les shunts intracardiaques, y compris l’interprétation des résistances pulmonaires si explicitement mentionnée, mais jamais leurs valeurs numériques. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire :  
- Présence ou absence d’un shunt intracardiaque.  
- Type de shunt :  
  - Communication interauriculaire (CIA).  
  - Communication interventriculaire (CIV).  
  - Canal atrioventriculaire.  
  - Autres types spécifiques (ex., foramen ovale perméable).  
- Orientation du shunt :  
  - Gauche-droite.  
  - Droite-gauche.  
  - Bidirectionnel.  
- Description qualitative des anomalies associées (ex., dilatation des cavités droites, surcharge volumique).  
- Interprétation qualitative des résistances pulmonaires si mentionnée explicitement (ex., "résistances pulmonaires augmentées, suggérant une hypertension pulmonaire").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Rapport QP/QS.  
- Valeur des résistances pulmonaires.

### 3. **Structure obligatoire de la sortie**  
- **Shunt intracardiaque :** Mentionnez le type et la direction du shunt, ainsi que la présence ou l'absence de bidirectionnalité si rapportée.  
- **Anomalies associées :** Décrivez toute conséquence anatomique ou fonctionnelle (ex., dilatation des cavités droites, surcharge volumique).  
- **Interprétation des résistances pulmonaires :** Mentionnez uniquement l’interprétation qualitative si elle est rapportée (ex., résistances augmentées).  

### 4. **Gestion des absences**  
- Si **aucune mention** de shunts intracardiaques n’est présente dans le texte :  
  - Répondez par : **"Shunts intracardiaques non décrits."**  
- Si un shunt intracardiaque est explicitement absent :  
  - Répondez par : **"Absence de shunts intracardiaques détectés."**

### 5. **Respect strict des données fournies**  
- Utilisez uniquement les informations présentes dans le texte fourni.  
- Reformulez légèrement pour adopter un style professionnel d’un échocardiographiste chevronné.  
- Ignorez rigoureusement les variables interdites mentionnées ci-dessus.

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Présence d’un shunt intracardiaque avec anomalies associées**  
**Entrée :**  
"Shunt intracardiaque de type communication interauriculaire (CIA) détecté, orienté gauche-droite. Dilatation des cavités droites et surcharge volumique observées. Résistances pulmonaires interprétées comme augmentées."  

**Sortie :**  
- **Shunt intracardiaque :** Communication interauriculaire (CIA) détectée, orientée gauche-droite.  
- **Anomalies associées :** Dilatation des cavités droites et surcharge volumique.  
- **Interprétation des résistances pulmonaires :** Résistances pulmonaires interprétées comme augmentées.

---

### **Exemple 2 : Absence explicite de shunts intracardiaques**  
**Entrée :**  
"Aucune anomalie détectée. Pas de shunts intracardiaques identifiés."  

**Sortie :**  
- **Réponse :** Absence de shunts intracardiaques détectés.

---

### **Exemple 3 : Absence de mention des shunts intracardiaques**  
**Entrée :**  
"Aucune mention spécifique des shunts intracardiaques dans le texte."  

**Sortie :**  
- **Réponse :** Shunts intracardiaques non décrits.

---

### **Exemple 4 : Shunt intracardiaque bidirectionnel sans anomalies associées**  
**Entrée :**  
"Un shunt bidirectionnel de type canal atrioventriculaire a été observé. Aucun autre signe d’anomalie associé n’est mentionné."  

**Sortie :**  
- **Shunt intracardiaque :** Canal atrioventriculaire bidirectionnel détecté.  
- **Anomalies associées :** Aucune anomalie associée rapportée.

---
""",
}
