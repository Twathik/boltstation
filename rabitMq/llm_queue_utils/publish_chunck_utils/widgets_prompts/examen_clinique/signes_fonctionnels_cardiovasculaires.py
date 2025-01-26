signes_fonctionnels_cardiovasculaires_widget: str = """
    # **Prompt : Extraction des signes fonctionnels cardiovasculaires**

## **Objectif**
Analyser et extraire **uniquement** les informations liées aux signes fonctionnels cardiovasculaires énumérés ci-dessous à partir des observations médicales. Toute information non listée doit être **strictement exclue**. La réponse doit être concise, directe et ne doit inclure **aucune explication, justification ou commentaire**.

---

## **Signes fonctionnels cardiovasculaires à analyser**

1. **Douleurs thoraciques**  
   - Typiques : douleur rétrosternale oppressante (angor, infarctus).  
   - Atypiques : douleur épigastrique, irradiations (bras, mâchoire, dos).  

2. **Dyspnée**  
   - D’effort.  
   - De repos ou orthopnée (dyspnée en position allongée).  
   - Dyspnée paroxystique nocturne (réveil brutal).  

3. **Palpitations**  
   - Sensation de battements rapides, irréguliers ou forts.  

4. **Syncope ou lipothymie**  
   - Syncope : perte de connaissance brutale.  
   - Lipothymie : sensation de malaise sans perte de conscience.  

5. **Œdèmes des membres inférieurs**  
   - Bilatéraux, évocateurs d'insuffisance cardiaque droite.  

6. **Claudication intermittente**  
   - Douleur musculaire à l’effort, souvent due à une insuffisance artérielle périphérique.  

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Adaptez la terminologie au genre du patient (ex. : « La patiente » pour une femme, « Le patient » pour un homme).  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- La réponse doit mentionner uniquement les signes fonctionnels cardiovasculaires détectés ou confirmer leur absence avec la phrase standardisée :  
  - **Absence de signes fonctionnels cardiovasculaires**  

---

## **Restrictions strictes**

1. **Exclusion de tout élément non pertinent :**
   - Ignorez strictement les informations ne figurant pas dans la liste des signes fonctionnels cardiovasculaires ci-dessus.  
   - Excluez les données d’auscultation, de l’examen vasculaire périphérique ou d’autres systèmes.

2. **Aucune interprétation ou supposition :**
   - Ne **déduisez pas** ou n’interprétez pas les résultats. Reproduisez uniquement ce qui est explicitement mentionné.

3. **Interdiction stricte des explications ou justifications :**
   - La réponse **ne doit contenir aucune explication, justification ou commentaire**.  

4. **Format uniforme :**
   - Listez uniquement les signes fonctionnels cardiovasculaires présents ou confirmez leur absence avec la phrase standardisée.  

---

## **Format attendu**

### **Cas 1 : Présence de signes fonctionnels cardiovasculaires**
- [Signe fonctionnel 1]  
- [Signe fonctionnel 2]

### **Cas 2 : Absence de signes fonctionnels cardiovasculaires**
Absence de signes fonctionnels cardiovasculaires  

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : Présence de signes fonctionnels**
**Entrée :**
<MedicalObservation>
Le patient présente des douleurs thoraciques rétrosternales survenant à l’effort et une dyspnée d’effort de grade II selon la NYHA. Aucun œdème des membres inférieurs rapporté.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- Douleurs thoraciques rétrosternales survenant à l’effort  
- Dyspnée d’effort de grade II  

---

### **Exemple 2 : Absence de signes fonctionnels**
**Entrée :**
<MedicalObservation>
Aucun des signes fonctionnels cardiovasculaires n’est mentionné dans les observations médicales.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
Absence de signes fonctionnels cardiovasculaires  

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
Le patient présente une claudication intermittente. Cyanose des extrémités observée. À l’auscultation cardiaque : souffle systolique détecté.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- Claudication intermittente  

"""
