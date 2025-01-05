ECG_segment_QT_widget: dict = {
    "description": """
**Contexte :**  
Analysez `<MedicalObservation>` pour **extraire uniquement les informations directement liées au segment QT**, en excluant rigoureusement toutes les données non pertinentes ou non liées (complexe QRS, espace PR, segments ST, ondes P ou T, information sur le rythme ou tout autre élément ECG). Le sexe du patient est indiqué dans `<Sex>` (par exemple : `<Sex>male</Sex>` ou `<Sex>female</Sex>`), et doit être utilisé pour interpréter les limites normales du QT corrigé (QTc). Structurez les résultats sous forme de paragraphe fluide sans inclure les balises XML dans la sortie.

---

### **Règles d’Extraction**

1. **Données autorisées :**  
   - **Durée du QT :** Mesure en ms, rapportée directement.  
   - **QT corrigé (QTc) :** Calculé si possible ou utilisé directement si fourni.  
   - **Interprétation des anomalies :** QT allongé ou raccourci, avec une mention des risques associés (ex. torsades de pointes).

2. **Calcul du QTc :**  
   - Si QT et FC sont fournis, calculez le QTc avec la formule de Bazett :  
     \[ QTc = QT / \sqrt{60 / FC} \]  
     Mentionnez que le calcul suit cette formule.  
   - Comparez le QTc calculé ou fourni aux limites normales, en fonction du sexe :  
     - **Pour un homme : QTc normal < 450 ms.**  
     - **Pour une femme : QTc normal < 460 ms.**  
   - Fournissez une interprétation complète :  
     - Si QTc est dans la normale, concluez : **"Absence d’anomalies du segment QT."**  
     - Si QTc est allongé ou raccourci, mentionnez cette anomalie et les implications cliniques possibles.  

3. **Données interdites :**  
   - **N’incluez aucune information liée aux éléments suivants, même si elles figurent dans `<MedicalObservation>` :**  
     - Complexe QRS (ex. blocs de branche, élargissement).  
     - Espace PR.  
     - Segments ST (ex. sus-décalage, sous-décalage).  
     - Ondes P ou autres anomalies ECG non liées au QT.  
     - Informations non liées au QT ou hors du contexte ECG.

4. **Gestion des absences :**  
   - Si aucune donnée QT/QTc n’est disponible : **"Données non disponibles."**  
   - Si aucune anomalie n’est détectée après analyse, concluez : **"Absence d’anomalies du segment QT."**

5. **Respect strict des données fournies :**  
   - Utilisez exclusivement les informations présentes dans `<MedicalObservation>` et `<Sex>`.  
   - Reformulez uniquement pour améliorer la fluidité, sans interprétation ni ajout.  
   - Ne faites pas référence aux balises XML dans la sortie.

---
""",
    "examples": """
### ** Exemples d'entrées et sorties attendues :**
---

#### **Exemple 2**  
**Entrée :**  
"QTc allongé à 480 ms. <Sex>female</Sex>"  
**Sortie :**  
Le QTc est de 480 ms, ce qui est supérieur aux limites normales pour une femme (< 460 ms). Cette valeur augmente le risque d’arythmies ventriculaires telles que les torsades de pointes.

**Explication :**  
- Le QTc est déjà fourni, donc aucun calcul n’est effectué.  
- La comparaison aux limites normales pour une femme est réalisée, et une interprétation clinique est ajoutée.

---

#### **Exemple 3**  
**Entrée :**  
"QT mesuré à 450 ms. <Sex>male</Sex>"  
**Sortie :**  
Le QT est mesuré à 450 ms. La fréquence cardiaque n’est pas fournie, il n’est pas possible de conclure sur le QT corrigé (QTc). Aucune anomalie détectée du segment QT.

**Explication :**  
- En l’absence de la FC, le QTc ne peut pas être calculé.  
- La conclusion mentionne l’absence d’anomalies détectées en l’état.

---

#### **Exemple 4**  
**Entrée :**  
"Aucune anomalie notable sur l’ECG. <Sex>male</Sex>"  
**Sortie :**  
Absence d’anomalies du segment QT.

**Explication :**  
- Aucune anomalie liée au segment QT n’est rapportée. La réponse reflète cela clairement.

---

#### **Exemple 5**  
**Entrée :**  
"Présence d’un sus-décalage ST en V3-V5. <Sex>female</Sex>"  
**Sortie :**  
Données non disponibles.

**Explication :**  
- Aucune information sur le segment QT ou QTc n’est mentionnée dans `<MedicalObservation>`. La sortie indique cela clairement.

---

### **Rappel Important**
- **N’incluez aucune information ou interprétation non liée au segment QT.**  
- Si un calcul du QTc est nécessaire, mentionnez qu’il a été réalisé selon la formule de Bazett.  
- Ne faites jamais référence aux balises XML directement dans la sortie, utilisez uniquement les informations qu’elles contiennent.
---
""",
}
