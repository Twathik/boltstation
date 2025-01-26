auscultation_widget: str = """
# **Prompt : Extraction des données de l’auscultation cardiaque**

## **Objectif**
Analyser et extraire **uniquement** les informations liées à l’auscultation cardiaque à partir des observations médicales. Les données relatives à l’auscultation d’autres appareils (ex. : pulmonaire) doivent être **excluses**. La réponse doit être concise, directe et ne doit inclure **aucune explication, justification ou commentaire**.

---

## **Informations à analyser pour l’auscultation cardiaque**

1. Présence de souffles :  
   - Localisation : mitral, aortique, pulmonaire, tricuspide.  
   - Intensité : grade 1 à 6.  
   - Type : systolique, diastolique, continu.  
   - Irradiation éventuelle.  

2. Présence de frottements péricardiques.  
3. Présence de bruits de galop (B3 ou B4).  
4. Qualité des bruits cardiaques : normaux, diminués ou renforcés.  

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Adaptez la terminologie au genre du patient (ex. : « La patiente » pour une femme, « Le patient » pour un homme).  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- Si aucune anomalie n’est détectée, mentionnez explicitement que l’auscultation cardiaque est normale.  

---

## **Restrictions strictes**

1. **Exclusion des données non liées à l’auscultation cardiaque :**
   - **Ignorez** toute information relative à d’autres appareils ou systèmes, y compris l’auscultation pulmonaire.  
   - Si des informations concernant d'autres appareils sont mentionnées dans les observations médicales, elles ne doivent **pas** apparaître dans la réponse.

2. **Aucune interprétation ou supposition :**
   - Ne **déduisez pas** ou n’interprétez pas les résultats. Reproduisez uniquement ce qui est explicitement indiqué dans l’observation.

3. **Interdiction stricte des explications ou justifications :**
   - La réponse **ne doit contenir aucune explication, justification ou commentaire**.  
   - Mentionnez uniquement les informations demandées de manière concise et claire.

4. **Format strict et uniforme :**
   - Si aucune anomalie n’est détectée, utilisez le format standard suivant :  
     - **Auscultation cardiaque** : absence de souffles ou de bruits surajoutés  

---

## **Format attendu**

### **Cas 1 : Anomalies détectées**
[Liste des anomalies détectées : souffles, frottements, galops, bruits diminués/renforcés]  

### **Cas 2 : Auscultation normale**
- absence de souffles ou de bruits surajoutés  

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : Anomalies détectées**
**Entrée :**
<MedicalObservation>
À l’auscultation cardiaque, souffle systolique au foyer mitral, grade 4/6, irradiant vers l’aisselle gauche. Bruits de galop (B3) présents. À l’auscultation pulmonaire : murmures vésiculaires normaux.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
  - Souffle systolique au foyer mitral, grade 4/6, irradiant vers l’aisselle gauche  
  - Bruits de galop (B3)  

---

### **Exemple 2 : Auscultation normale**
**Entrée :**
<MedicalObservation>
L’auscultation cardiaque est normale, sans anomalies détectées. À l’auscultation pulmonaire, présence de râles crépitants bilatéraux.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- absence de souffles ou de bruits surajoutés  

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
À l’auscultation cardiaque : souffle diastolique au foyer aortique. À l’auscultation pulmonaire : râles crépitants bilatéraux.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
  - Souffle diastolique au foyer aortique  

---

### **Rappel important :**
- **Exclusivement listé :** Mentionnez uniquement les informations liées à l’auscultation cardiaque.  
- **Aucune explication ou commentaire :** La réponse doit être strictement limitée aux anomalies détectées ou à l’absence d’anomalies, sans justification ou interprétation.  
- **Exclusion stricte des données d’autres appareils** : Les observations sur l’auscultation pulmonaire ou d’autres systèmes doivent être ignorées.

"""
