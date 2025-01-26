autre_symptomes_widget: str = """
# **Prompt : Extraction des autres signes fonctionnels**

## **Objectif**
Analyser et extraire **uniquement** les informations liées aux signes fonctionnels **non mentionnés** dans `<Parameters>` à partir des observations médicales. Les signes fonctionnels listés dans `<Parameters>` doivent être **strictement exclus** de la réponse. La réponse doit être concise, directe et ne doit inclure **aucune explication, justification ou commentaire**.

---

## **Signes fonctionnels à exclure**

<Parameters>  
1. **Douleurs thoraciques ou angor**  
2. **Dyspnée**  
3. **Palpitations**  
4. **Syncope ou lipothymie**  
5. **Œdèmes des membres inférieurs**  
6. **Claudication intermittente**  
7. **Toux chronique**  
8. **Cyanose**  
</Parameters>

---

## **Instructions générales**

### **Langue et style**
- Rédigez en **français** avec une terminologie médicale précise.  
- Maintenez un **ton professionnel et formel**, conforme au style d’un rapport clinique.  
- Adaptez la terminologie au genre du patient (ex. : « La patiente » pour une femme, « Le patient » pour un homme).  
- Ne faites jamais référence aux balises XML directement dans la réponse.

### **Organisation**
- Mentionnez uniquement les autres signes fonctionnels détectés ou confirmez leur absence avec la phrase standardisée :  
  - **Absence d'autres signes fonctionnels**  

---

## **Restrictions strictes**

1. **Exclusion des signes listés dans `<Parameters>` :**
   - Ignorez **strictement** les signes suivants, même s'ils sont mentionnés dans l’observation médicale :  
     - Douleurs thoraciques ou angor.  
     - Dyspnée.  
     - Palpitations.  
     - Syncope ou lipothymie.  
     - Œdèmes des membres inférieurs.  
     - Claudication intermittente.  
     - Toux chronique.  
     - Cyanose.  

2. **Exclusion des données non pertinentes :**
   - Ignorez les observations cliniques, les données d'auscultation cardiaque ou pulmonaire, et les informations relatives à l'examen vasculaire périphérique.

3. **Aucune interprétation ou supposition :**
   - Ne **déduisez pas** ou n’interprétez pas les résultats. Reproduisez uniquement les signes fonctionnels non exclus explicitement listés dans `<Parameters>`.

4. **Interdiction stricte des explications ou justifications :**
   - La réponse **ne doit contenir aucune explication, justification ou commentaire**.  

5. **Format uniforme :**
   - Listez uniquement les signes fonctionnels non mentionnés dans `<Parameters>` ou confirmez leur absence avec la phrase standardisée.  

---

## **Format attendu**

### **Cas 1 : Présence d'autres signes fonctionnels**
- [Signe fonctionnel 1]  
- [Signe fonctionnel 2]

### **Cas 2 : Absence d'autres signes fonctionnels**
Absence d'autres signes fonctionnels  

---

## **Exemples d’entrée et de sortie**

### **Exemple 1 : Présence d'autres signes fonctionnels**
**Entrée :**
<MedicalObservation>
Le patient présente une asthénie et des sueurs nocturnes. Cyanose des extrémités et œdèmes bilatéraux mentionnés, mais ignorés selon les consignes.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- Asthénie  
- Sueurs nocturnes  

---

### **Exemple 2 : Absence d'autres signes fonctionnels**
**Entrée :**
<MedicalObservation>
Aucun autre signe fonctionnel n’est mentionné dans les observations médicales, à l’exception de douleurs thoraciques et d’œdèmes des membres inférieurs, qui doivent être ignorés.
</MedicalObservation><Sex>female</Sex>

**Sortie :**
Absence d'autres signes fonctionnels  

---

### **Exemple 3 : Inclusion erronée corrigée**
**Entrée :**
<MedicalObservation>
Le patient présente une pâleur cutanéo-muqueuse. À l’auscultation pulmonaire : râles crépitants bilatéraux détectés. Cyanose mentionnée.
</MedicalObservation><Sex>male</Sex>

**Sortie :**
- Pâleur cutanéo-muqueuse  

"""
