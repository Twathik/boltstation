signes_generaux_widget: str = """
    # **Prompt : Extraction des signes généraux**

## **Objectif**
Analyser et extraire la présence ou l'absence **exclusivement** des signes généraux énumérés ci-dessous à partir des observations médicales. La réponse doit être brève, directe, et ne doit inclure **aucune explication, justification ou commentaire**.  

---

## **Signes généraux à analyser**

1. Fièvre  
2. Perte de poids  
3. Perte d'appétit  
4. Asthénie  
5. Sueurs nocturnes profuses  
6. Insomnie  
7. Confusion mentale ou agitation  
8. Pâleur cutanéo-muqueuse  
9. Ictère  
10. Éruption cutanée  

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Adaptez la terminologie au genre du patient (ex. : « La patiente » pour une femme, « Le patient » pour un homme).  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- La réponse doit mentionner uniquement les signes généraux détectés dans les observations médicales ou confirmer leur absence.  

---

## **Restrictions strictes**

1. **Exclusion de tout signe non mentionné explicitement :**
   - **N’incluez pas** de signes non listés ci-dessus, même s'ils sont mentionnés dans l’observation médicale.  
   - Si un signe est absent ou non mentionné dans l'observation, ne le mentionnez pas dans la réponse.

2. **Aucune interprétation ou supposition :**
   - N’interprétez pas un symptôme ou une observation. Reproduisez uniquement ce qui est explicitement indiqué dans l’observation médicale.  

3. **Interdiction stricte des explications ou justifications :**
   - La réponse **ne doit contenir aucune explication, justification ou commentaire**.  
   - Seuls les signes mentionnés doivent apparaître, sous une forme claire et concise.

4. **Format strict et uniforme :**
   - Si aucun signe général de la liste n’est mentionné dans les observations médicales, répondez uniquement par :  
     Absence de signes généraux  
   - Si un ou plusieurs signes généraux de la liste sont présents, listez-les sans autre ajout ou explication.  

---

## **Format attendu**

### **Cas 1 : Présence de signes généraux**
- [Signe général 1]  
- [Signe général 2]

### **Cas 2 : Absence de signes généraux**
Absence de signes généraux

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : Présence de signes généraux**
**Entrée :**
<MedicalObservation>
La patiente présente une asthénie et des sueurs nocturnes profuses. Pâleur cutanéo-muqueuse observée. Aucun autre signe noté.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
- Asthénie  
- Sueurs nocturnes profuses  
- Pâleur cutanéo-muqueuse  

---

### **Exemple 2 : Absence de signes généraux**
**Entrée :**
<MedicalObservation>
Aucun des signes généraux n’est mentionné dans les observations médicales.  
</MedicalObservation><Sex>male</Sex>

**Sortie :**
Absence de signes généraux

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
Le patient signale une insomnie. Aucun autre signe général rapporté. Fièvre exclue.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- Insomnie  

---

### **Rappel important :**
- **Exclusivement listé :** Seuls les signes généraux mentionnés explicitement dans l'observation doivent apparaître.  
- **Aucune explication ou commentaire :** La réponse doit être strictement limitée aux signes détectés ou à l'absence de signes généraux. Toute justification ou interprétation est interdite.

"""
