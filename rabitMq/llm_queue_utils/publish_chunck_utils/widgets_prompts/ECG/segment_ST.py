ECG_segment_ST_widget: dict = {
    "description": """
**Contexte :**  
Analysez `<MedicalObservation>` pour **extraire uniquement les informations liées aux anomalies de repolarisation et du segment ST observées sur l’ECG**, en excluant rigoureusement toutes les données non pertinentes ou non directement liées à la repolarisation ou au segment ST. Structurez les résultats sous forme de paragraphe fluide.

---

### **Règles d’Extraction**

1. **Données autorisées :**  
   - Anomalies du segment ST :  
     - Sus-décalage (ST+), sous-décalage (ST-), normal.  
   - Anomalies des ondes T :  
     - Ondes T négatives, aplaties, ou hypervoltage.  
   - Interprétations spécifiques liées à ces anomalies :  
     - Ischémie, lésion sous-épicardique, infarctus aigu, etc.

2. **Données interdites :**  
   - **N’incluez aucune information liée aux éléments suivants, même si elles figurent dans `<MedicalObservation>` :**  
     - Complexe QRS (ex. élargissement, blocs de branche).  
     - Espace PR.  
     - Segment QT ou QT corrigé (QTc).  
     - Ondes P ou autres anomalies ECG non liées à la repolarisation.  
     - Informations non liées à la repolarisation ou au segment ST.

3. **Structure obligatoire de la sortie :**  
   - **Anomalies du segment ST :** Mentionnez les sus-décalages ou sous-décalages avec les dérivations concernées.  
   - **Anomalies des ondes T :** Décrivez les anomalies (ex. T négatives, aplaties) et les dérivations concernées.  
   - **Interprétation clinique (le cas échéant) :** Fournissez une interprétation uniquement en lien avec les anomalies rapportées (ex. ischémie, lésion sous-épicardique).  

4. **Gestion des absences :**  
   - Si aucune anomalie de repolarisation ou du segment ST n’est rapportée : **"Absence d’anomalies de la repolarisation et du segment ST."**

5. **Respect strict des données fournies :**  
   - Utilisez exclusivement les informations présentes dans `<MedicalObservation>`.  
   - Reformulez uniquement pour améliorer la fluidité, sans interprétation ni ajout.  
   - Ignorez rigoureusement toutes les données non liées aux anomalies de repolarisation et du segment ST.

---
""",
    "examples": """
### ** Exemples d'entrées et sorties attendues :**

#### **Exemple 1**
**Entrée :**  
"Rythme sinusal à 82 bpm, bloc de branche droit complet (BBDc), sous-décalage ST en V2-V5. Ondes T négatives en DII et aVF."  
**Sortie :**  
Un sous-décalage du segment ST est observé en V2-V5. Ondes T négatives en DII et aVF, évoquant une ischémie sous-épicardique.

**Explication :**  
- Les anomalies du segment ST et des ondes T sont rapportées avec leur interprétation clinique.  
- Les mentions sur le rythme sinusal et le BBDc sont ignorées.

---

#### **Exemple 2**  
**Entrée :**  
"Sus-décalage ST en DII, DIII et aVF. QTc allongé à 480 ms."  
**Sortie :**  
Un sus-décalage du segment ST est observé en DII, DIII et aVF, compatible avec un syndrome coronarien aigu.

**Explication :**  
- Les anomalies du segment ST sont rapportées avec leur interprétation clinique.  
- Le QTc allongé est ignoré car il n’est pas lié aux anomalies de repolarisation.

---

#### **Exemple 3**  
**Entrée :**  
"Rythme irrégulier avec fibrillation auriculaire. Sus-décalage ST en V1-V3, ondes T aplaties en V4-V6."  
**Sortie :**  
Un sus-décalage du segment ST est observé en V1-V3. Ondes T aplaties en V4-V6.

**Explication :**  
- Les anomalies du segment ST et des ondes T sont rapportées.  
- Les informations sur le rythme irrégulier et la fibrillation auriculaire sont ignorées.

---

#### **Exemple 4**  
**Entrée :**  
"Aucune anomalie notable sur l’ECG."  
**Sortie :**  
Absence d’anomalies de la repolarisation et du segment ST.

**Explication :**  
- Aucune anomalie liée à la repolarisation ou au segment ST n’est rapportée. La sortie reflète cela.

---

#### **Exemple 5**  
**Entrée :**  
"Présence d’un sous-décalage ST en V2-V4. Complexes QRS élargis à 160 ms."  
**Sortie :**  
Un sous-décalage du segment ST est observé en V2-V4.

**Explication :**  
- Le sous-décalage ST est rapporté.  
- Les complexes QRS élargis sont ignorés car ils ne concernent pas la repolarisation.

---

### **Rappel Important**
- **N’incluez aucune information ou interprétation non liée aux anomalies de repolarisation ou du segment ST.**  
- Tout élément mentionné dans `<MedicalObservation>` mais n’ayant pas de lien direct avec la repolarisation doit être ignoré.
- La sortie ne doit pas contenir de référence au patient, comme "le patient" ou "la patiente".

---
""",
}
