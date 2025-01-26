examen_respiratoire_widget: str = """
# **Prompt : Extraction des informations de l’examen respiratoire**

## **Objectif**
Analyser et extraire les informations **exclusivement** liées à l’examen respiratoire à partir des observations médicales. La réponse doit être concise, directe et ne doit inclure **aucune explication, justification ou commentaire.**

---

## **Informations à analyser**

### **1. Inspection**
- Signes visibles de difficultés respiratoires :  
  - Dyspnée.  
  - Cyanose.  
  - Utilisation des muscles accessoires respiratoires.  

### **2. Palpation**
- Symétrie de la cage thoracique.  
- Douleurs ou masses thoraciques.  

### **3. Percussion**
- Anomalies de résonance pulmonaire :  
  - Épanchements pleuraux.  
  - Pneumonie.  

### **4. Auscultation**
- Anomalies des bruits respiratoires :  
  - Râles.  
  - Sibilances.  
  - Crépitements.  
  - Ronchis.  

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Adaptez la terminologie au genre du patient (ex. : « La patiente » pour une femme, « Le patient » pour un homme).  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- Structurez la réponse sous forme de catégories correspondant aux techniques d’examen : Inspection, Palpation, Percussion, Auscultation.  
- Si aucune anomalie n’est détectée, mentionnez explicitement que l’examen est normal dans chaque catégorie.  

---

## **Restrictions strictes**

1. **Exclusion de tout élément non lié à l’examen respiratoire :**
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
     - **Percussion**  
     - **Auscultation**  
   - Si aucune anomalie n’est détectée, utilisez le format standard suivant :  
     - **Inspection** : sans anomalies  
     - **Palpation** : cage thoracique symétrique, absence de masses ou douleurs.  
     - **Percussion** : résonance pulmonaire normale.  
     - **Auscultation** : absence de bruits anormaux  

---

## **Format attendu**

### **Cas 1 : Anomalies détectées**
- **Inspection**  
  [Liste des anomalies détectées]  

- **Palpation**  
  [Liste des anomalies détectées : asymétrie, douleurs, masses]  

- **Percussion**  
  [Liste des anomalies détectées : anomalies de résonance pulmonaire]  

- **Auscultation**  
  [Liste des anomalies détectées : râles, sibilances, crépitements, ronchis]  

### **Cas 2 : Examen normal**
- **Inspection** : sans anomalies  
- **Palpation** : cage thoracique symétrique, absence de masses ou douleurs.  
- **Percussion** : résonance pulmonaire normale.  
- **Auscultation** : absence de bruits anormaux  

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : Anomalies détectées**
**Entrée :**
<MedicalObservation>
La patiente présente une dyspnée et une cyanose. À la palpation : cage thoracique symétrique, sans douleur. Percussion : matité au niveau basal droit. À l'auscultation : râles crépitants à droite et sibilances bilatérales.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
- **Inspection**  
  - Dyspnée  
  - Cyanose  

- **Palpation**  
  - Cage thoracique symétrique, absence de douleurs  

- **Percussion**  
  - Matité au niveau basal droit  

- **Auscultation**  
  - Râles crépitants à droite  
  - Sibilances bilatérales  

---

### **Exemple 2 : Examen normal**
**Entrée :**
<MedicalObservation>
Aucun signe respiratoire anormal rapporté dans les observations médicales.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- **Inspection** : sans anomalies  
- **Palpation** : cage thoracique symétrique, absence de masses ou douleurs.  
- **Percussion** : résonance pulmonaire normale.  
- **Auscultation** : absence de bruits anormaux  

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
Le patient présente une cyanose et des râles crépitants bilatéraux. Aucun autre signe respiratoire mentionné.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- **Inspection**  
  - Cyanose  

- **Auscultation**  
  - Râles crépitants bilatéraux  

---

### **Rappel important :**
- **Exclusivement listé :** Mentionnez uniquement les informations directement liées à l’examen respiratoire.  
- **Aucune explication ou commentaire :** La réponse doit être strictement limitée aux anomalies détectées ou à l’absence d’anomalies, sans justification ou interprétation.

"""
