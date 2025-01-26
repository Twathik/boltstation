donnee_ecg_widget: str = """### Objectif
# **Prompt : Extraction des données ECG**

## **Objectif**
Analyser et extraire **uniquement** les informations liées aux données ECG telles qu’explicitement mentionnées dans l’observation médicale. Les données doivent être rapportées sans **interprétation, omission ou modification**. La réponse doit être concise, directe et **ne doit inclure aucune explication, justification ou commentaire**.

---

## **Informations à analyser**

### **1. Rythme cardiaque :**
- Type de rythme (sinusal, fibrillation auriculaire, etc.).  
- Fréquence cardiaque (bpm).  

### **2. Onde P :**
- Morphologie, amplitude, durée.  
- Anomalies spécifiques : hypertrophie auriculaire gauche (HAG), hypertrophie auriculaire droite (HAD).  

### **3. Complexe QRS :**
- Durée et morphologie (élargi, normal).  
- Anomalies spécifiques : blocs de branche (BBG, BBGc, BBGi, BBD, BBDc, BBDi).  

### **4. Segment ST :**
- Anomalies spécifiques :  
  - ST+ : Sus-décalage du segment ST (lésion sous-épicardique).  
  - ST- : Sous-décalage du segment ST (lésion sous-endocardique).  

### **5. Segment QT :**
- Durée corrigée (QTc).  
- Anomalies : allongement ou raccourcissement du QT.  

### **6. Espace PR :**
- Durée (ms).  
- Présence ou absence d’anomalies significatives.  

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- La réponse doit être structurée en catégories correspondant aux différents paramètres ECG.  
- **Chaque donnée doit être rapportée exactement comme elle apparaît dans l'observation médicale.**  
- Si une catégorie est normale ou sans anomalie détectée, mentionnez explicitement qu’elle est normale.  

---

## **Restrictions strictes**

1. **Exclusion des données non pertinentes :**
   - Ignorez les observations cliniques ou paracliniques non liées à l’ECG.  

2. **Aucune interprétation ou modification :**
   - **Ne reformulez pas, n’interprétez pas et ne modifiez pas** les données explicitement mentionnées dans l’observation.  
   - Reproduisez fidèlement les informations présentes, y compris les abréviations ou termes techniques (ex. : BBG pour bloc de branche gauche).

3. **Interdiction stricte des omissions :**
   - **Aucune donnée ECG mentionnée dans l’observation ne doit être omise**. Toutes les catégories doivent être rapportées si elles sont présentes.  

4. **Interdiction stricte des explications, justifications et redondances :**
   - La réponse **ne doit contenir aucune explication, justification ou commentaire**.  

5. **Format strict et uniforme :**
   - Mentionnez chaque catégorie ECG dans l’ordre suivant, une seule fois :  
     - **Rythme cardiaque**  
     - **Onde P**  
     - **Complexe QRS**  
     - **Segment ST**  
     - **Segment QT**  
     - **Espace PR**  

---

## **Format attendu**

### **Cas 1 : ECG avec anomalies**
- **Rythme cardiaque** : [Type de rythme, fréquence]  
- **Onde P** : [Description des anomalies]  
- **Complexe QRS** : [Description des anomalies]  
- **Segment ST** : [Description des anomalies]  
- **Segment QT** : [Description des anomalies]  
- **Espace PR** : [Durée, anomalies ou absence d’anomalies]  

### **Cas 2 : ECG normal**
- **Rythme cardiaque** : Régulier  
- **Onde P** : Normale  
- **Complexe QRS** : Normal  
- **Segment ST** : Absence d’anomalies  
- **Segment QT** : Normal  
- **Espace PR** : Normal  

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : ECG avec anomalies**
**Entrée :**
<MedicalObservation>
L’ECG montre un rythme sinusal a 100 bpm avec des QRS élargis et un bloc de branche gauche complet. Le segment ST est normal. L’espace PR est à 160 ms, sans anomalies significatives.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- **Rythme cardiaque** : Sinusal, 100 bpm  
- **Onde P** : Normale  
- **Complexe QRS** : Élargi, bloc de branche gauche complet  
- **Segment ST** : Normal  
- **Segment QT** : Normal  
- **Espace PR** : 160 ms, sans anomalies significatives  

---

### **Exemple 2 : ECG normal**
**Entrée :**
<MedicalObservation>
L’ECG est normal, sans anomalies détectées.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
- **Rythme cardiaque** : Régulier  
- **Onde P** : Normale  
- **Complexe QRS** : Normal  
- **Segment ST** : Absence d’anomalies  
- **Segment QT** : Normal  
- **Espace PR** : Normal  

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
Rythme irrégulier avec fibrillation auriculaire. Segment ST sans anomalies. QT corrigé normal.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- **Rythme cardiaque** : Irrégulier, fibrillation auriculaire  
- **Onde P** : Absente  
- **Complexe QRS** : Normal  
- **Segment ST** : Absence d’anomalies  
- **Segment QT** : Normal  
- **Espace PR** : Non disponible  

---

### **Rappel important**
- **Aucune interprétation ou omission :** Les données ECG doivent être rapportées fidèlement, sans modification ni omission.  
- **Exclusivement listé :** Mentionnez uniquement les données ECG mentionnées explicitement.  
- **Aucune explication ou commentaire :** La réponse doit être strictement limitée aux anomalies détectées ou à l’absence d’anomalies, sans justification ou interprétation.

"""
