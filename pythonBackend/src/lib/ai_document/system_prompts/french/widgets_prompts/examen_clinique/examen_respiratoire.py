examen_respiratoire_widget: dict = {
    "description": """
## **Objectif**  
Analyser le contenu de `<MedicalObservation>` pour extraire toutes les informations relatives à **l’examen respiratoire**, en excluant les données liées à d’autres systèmes (par exemple : examen cardiaque ou vasculaire).  
Cet examen vise à évaluer les fonctions respiratoires du patient afin de détecter des signes de pathologies pulmonaires ou respiratoires, en se basant sur les observations cliniques suivantes : inspection, palpation, percussion et auscultation.  

## **Techniques d’examen respiratoire**  
- **Inspection**  
  - Rechercher des signes visibles de difficultés respiratoires, tels que :  
    - Dyspnée.  
    - Cyanose.  
    - Utilisation des muscles accessoires respiratoires.  

- **Palpation**  
  - Évaluer la symétrie de la cage thoracique.  
  - Détecter des masses ou douleurs thoraciques.  
  - Exclure toute information liée à la palpation des battements cardiaques ou des bruits précordiaux.  

- **Percussion**  
  - Analyser la résonance pulmonaire pour identifier des anomalies telles que :  
    - Épanchements pleuraux.  
    - Pneumonie.  

- **Auscultation**  
  - Écouter les bruits respiratoires pour détecter :  
    - Râles.  
    - Sibilances.  
    - Crépitements.  
    - Ronchis.  
  - Exclure tout élément lié aux bruits cardiaques (souffles, bruits du cœur, etc.).  

---

## **Instructions**  
1. Analysez les informations contenues dans `<MedicalObservation>`.  
2. Identifiez les données correspondant aux étapes suivantes : inspection, palpation, percussion et auscultation, en excluant :  
   - Toute information liée à la palpation des battements cardiaques ou des bruits précordiaux.  
   - Toute information liée à l’auscultation des bruits cardiaques (par exemple : souffles cardiaques ou bruits du cœur).  
3. Structurez les données extraites en suivant les catégories mentionnées dans l’objectif.  
4. Si des éléments sont absents dans `<MedicalObservation>`, ne rien mentionner à ce sujet.  
5. **En cas d’examen respiratoire normal**, la réponse doit être consolidée comme suit :  
   - **Inspection** : sans anomalies.  
   - **Palpation** : Symétrie thoracique normale.  
   - **Percussion** : Résonance pulmonaire normale.  
   - **Auscultation** : Aucun bruit anormal détecté.  
6. **En cas d'anomalies présentes uniquement dans certains temps de l'examen**, structurez la réponse comme suit :  
   - Chaque catégorie (Inspection, Palpation, Percussion, Auscultation) doit inclure les anomalies détectées.  
   - Les catégories sans anomalies doivent clairement indiquer un résultat normal.  
   - Exemple :  

### **Exemple (Anomalie à l’auscultation uniquement)**  
**Entrée :**  
`<MedicalObservation> Dyspnée modérée rapportée. Symétrie thoracique conservée, percussion normale. À l'auscultation : râles crépitants bilatéraux bas situés. </MedicalObservation><Sex>female</Sex>`  

**Sortie :**  
**Inspection**  
- Dyspnée modérée.  

**Palpation**  
- Symétrie thoracique normale.  

**Percussion**  
- Résonance pulmonaire normale.  

**Auscultation**  
- Présence de râles crépitants bilatéraux bas situés.  

7. Soyez clair et précis dans la présentation des informations.  

---

""",
    "examples": """
## **Exemples d'entrée et de sortie :**

### Exemple 1 (Examen normal)  
**Entrée :**  
`<MedicalObservation> Patient sans antécédents particuliers. Examen respiratoire normal : pas de cyanose, dyspnée ou utilisation des muscles accessoires. Symétrie thoracique normale, percussion claire, auscultation sans râles ni sibilances. </MedicalObservation><Sex>male</Sex>`

**Sortie :**  
**Inspection**  
- sans anomalies  

**Palpation**  
- Symétrie thoracique normale.  

**Percussion**  
- Résonance pulmonaire normale.  

**Auscultation**  
- Murmure vésiculaire bien ausculté dans les deux champs pulmonaires.  
---

### Exemple 2 (Anomalies non liée à l'appareil réspiratoire)
  **Entrée :**  
`<MedicalObservation> <MedicalObservation> Patient avec dyspnée modérée. À l'inspection : cyanose des lèvres et utilisation des muscles accessoires. À la palpation : symétrie thoracique conservée, mais choc de pointe perceptible. À la percussion : matité au niveau du lobe inférieur gauche. À l'auscultation : râles crépitants à la base gauche, souffle systolique au foyer mitral. </MedicalObservation>
<Sex>male</Sex>`

**Sortie :**  
**Inspection**  
- Cyanose des lèvres.
- Utilisation des muscles accessoires respiratoires. 

**Palpation**  
- Symétrie thoracique conservée.

**Percussion**  
- Matité au lobe inférieur gauche.  

**Auscultation**  
- Râles crépitants à la base gauche. 
---  

** Note**: Le choc de pointe perçu lors de la palpation est lié à l'examen cardiaque et a été exclu. Le souffle systolique au foyer mitral est un bruit cardiaque et a été exclu.

---
""",
}
