Examen_vasculaire_perepherique_widget: str = """
   # **Prompt : Extraction des informations de l’examen vasculaire périphérique**

## **Objectif**
Analyser et extraire les informations **exclusivement** liées à l’examen vasculaire périphérique à partir des observations médicales. La réponse doit être concise, directe et ne doit inclure **aucune explication, justification ou commentaire**.

---

## **Informations à analyser**

### **1. Inspection :**
- Varices.  
- Œdèmes.  
- Cyanose des membres.  
- Ulcères ou troubles trophiques (ex. : peau sèche, dépilation, plaies chroniques).  

### **2. Palpation :**
- Qualité des pouls périphériques (radial, brachial, fémoral, poplité, tibial postérieur, pédieux) :  
  - Présence, absence, asymétrie.  
- Température des membres :  
  - Anomalies telles que froideur ou chaleur excessive.  

### **3. Auscultation :**
- Bruits vasculaires :  
  - Souffles artériels ou veineux indiquant des sténoses ou plaques athérosclérotiques.  

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Adaptez la terminologie au genre du patient (ex. : « La patiente » pour une femme, « Le patient » pour un homme).  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- Structurez la réponse sous forme de catégories correspondant aux techniques d’examen : Inspection, Palpation, Auscultation.  
- Si aucune anomalie n’est détectée, mentionnez explicitement que l’examen est normal dans chaque catégorie.  

---

## **Restrictions strictes**

1. **Exclusion de tout élément non lié à l’examen vasculaire périphérique :**
   - **N’incluez pas** d’informations concernant d’autres systèmes ou examens.  
   - Ignorez toute donnée non mentionnée explicitement dans les observations médicales.

2. **Aucune interprétation ou supposition :**
   - Ne **déduisez pas** ou n’interprétez pas les résultats. Reproduisez uniquement ce qui est explicitement indiqué dans l’observation.

3. **Interdiction stricte des explications ou justifications :**
   - La réponse **ne doit contenir aucune explication, justification ou commentaire**.  
   - Mentionnez uniquement les informations demandées de manière concise et claire.

4. **Format strict et uniforme :**
   - Organisez la réponse en catégories :  
     - **Inspection**  
     - **Palpation**  
     - **Auscultation**  
   - Si aucune anomalie n’est détectée, utilisez le format standard suivant :  
     - **Inspection** : sans anomalies  
     - **Palpation** : pouls présents sur tous les trajets vasculaires. Température des membres normale.  
     - **Auscultation** : absence de souffles vasculaires  

---

## **Format attendu**

### **Cas 1 : Anomalies détectées**
- **Inspection**  
  [Liste des anomalies détectées]  

- **Palpation**  
  [Liste des anomalies détectées : pouls absents/asymétriques, anomalies de température]  

- **Auscultation**  
  [Liste des anomalies détectées : souffles vasculaires]  

### **Cas 2 : Examen normal**
- **Inspection** : sans anomalies  
- **Palpation** : pouls présents sur tous les trajets vasculaires. Température des membres normale.  
- **Auscultation** : absence de souffles vasculaires  

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : Anomalies détectées**
**Entrée :**
<MedicalObservation>
Le patient présente des varices au membre inférieur droit et des œdèmes bilatéraux. Palpation : absence de pouls pédieux bilatéraux. Température des membres inférieure à la normale. Aucun souffle vasculaire détecté à l’auscultation.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- **Inspection**  
  - Varices au membre inférieur droit  
  - Œdèmes bilatéraux  

- **Palpation**  
  - Absence de pouls pédieux bilatéraux  
  - Température des membres inférieure à la normale  

- **Auscultation**  
  - Absence de souffles vasculaires  

---

### **Exemple 2 : Examen normal**
**Entrée :**
<MedicalObservation>
Aucun signe d’anomalie vasculaire rapporté dans les observations médicales.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
- **Inspection** : sans anomalies  
- **Palpation** : pouls présents sur tous les trajets vasculaires. Température des membres normale.  
- **Auscultation** : absence de souffles vasculaires  

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
Le patient présente des ulcères au niveau des membres inférieurs. Aucun souffle vasculaire détecté. Palpation normale pour les trajets vasculaires.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- **Inspection**  
  - Ulcères au niveau des membres inférieurs  

- **Palpation**  
  - Pouls présents sur tous les trajets vasculaires  

- **Auscultation**  
  - Absence de souffles vasculaires  

---

### **Rappel important :**
- **Exclusivement listé :** Mentionnez uniquement les informations directement liées à l’examen vasculaire périphérique.  
- **Aucune explication ou commentaire :** La réponse doit être strictement limitée aux anomalies détectées ou à l’absence d’anomalies, sans justification ou interprétation.


"""
