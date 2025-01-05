Examen_vasculaire_perepherique_widget: dict = {
    "description": """
   ## **Objectif**  
Analyser le contenu de `<MedicalObservation>` pour extraire toutes les informations relatives à l’examen vasculaire périphérique, en excluant les données liées à l'examen cardiaque. Cet examen vise à évaluer l’état des artères et des veines des membres supérieurs et inférieurs afin de détecter des anomalies circulatoires.  

Les éléments clés à inclure sont :  
- **Inspection** :  
  Rechercher des signes visibles de troubles circulatoires, tels que :  
  - Varices.  
  - Œdèmes.  
  - Cyanose des membres.  
  - Ulcères ou troubles trophiques (ex. : peau sèche, dépilation, plaies chroniques).  

- **Palpation** :  
  Identifier et évaluer la qualité des pouls périphériques :  
  - Pouls radial, brachial, fémoral, poplité, tibial postérieur, pédieux.  
  - Détecter des asymétries ou des absences de pouls pouvant indiquer une obstruction ou une insuffisance artérielle.  
  - Vérifier la température des membres :  
    - Rechercher des anomalies de température, telles que la froideur ou la chaleur excessive, qui peuvent indiquer une mauvaise circulation sanguine ou une inflammation.

- **Auscultation** :  
  Écouter les bruits vasculaires pour identifier :  
  - Souffles artériels ou veineux suggérant des sténoses ou des plaques athérosclérotiques.  
  - Toute anomalie sonore pouvant signaler un flux turbulent.  

*Les données liées à l'examen cardiaque, telles que les souffles cardiaques ou les bruits du cœur, doivent être exclues de l'analyse.*

Si les résultats de l'examen vasculaire sont normaux (sans anomalies), la réponse doit refléter cette normalité de manière consolidée, comme dans l'exemple suivant.

---

## **Instructions**  
1. Analysez les informations contenues dans `<MedicalObservation>`.  
2. Identifiez les données correspondant aux étapes suivantes : inspection, palpation et auscultation, en excluant les éléments relatifs à l'examen cardiaque.  
3. Structurez les données extraites en suivant les catégories mentionnées dans l’objectif.  
4. Si des éléments sont absents dans `<MedicalObservation>`, ne rien mentionner à ce sujet.  
5. En cas d'anomalie des pouls ou de la température des membres, indiquez la présence de l'anomalie et mentionnez explicitement l'absence d'anomalies sur les autres trajets vasculaires et dans la température des autres membres (comme dans l'exemple 2).  
6. En cas d'examen vasculaire normal, la réponse doit être concise et consolidée dans le format suivant :  
   - **Inspection** : sans anomalies  
   - **Palpation** : Pouls présents sur tous les trajets vasculaires. Température des membres normale.  
   - **Auscultation** : Absence de souffles sur tous les trajets vasculaires.  

---

## **Format attendu pour la sortie**  
Votre réponse doit être structurée comme suit :  

**1. Inspection**  
_(Listez tous les signes visibles identifiés, tels que varices, œdèmes, ulcères, etc. Mentionnez uniquement les anomalies observées.)_  

**2. Palpation**  
_(Listez les pouls périphériques évalués, leur qualité, présence ou absence, et toute asymétrie constatée. Mentionnez également la température des membres uniquement si une anomalie est détectée, par exemple froideur ou chaleur excessive.)_  

**3. Auscultation**  
_(Listez les bruits vasculaires détectés, avec une précision sur leur localisation et leur signification potentielle, à l'exclusion des bruits cardiaques)_  

---

""",
    "examples": """
 ## **Exemples d'entrée et de sortie :**

### Exemple 1  
**Entrée :**  
`<MedicalObservation> atcd HTA, adénome de la prostate, PA 160/80, souffle IM 2/6, FC 100 bpm, examen vasculaire et pulmonaire normal </MedicalObservation><Sex>female</Sex>`

**Sortie :**  
**1. Inspection**  
- sans anomalies  

**2. Palpation**  
- Pouls présents sur tous les trajets vasculaires.  

**3. Auscultation**  
- Absence de souffles sur tous les trajets vasculaires  

### Exemple 2  
**Entrée :**  
`<MedicalObservation> œdème des membres inférieurs, varices visibles aux membres inférieurs, pouls pédieux absent, souffle aortique 3/6, examen pulmonaire normal, membre inférieur gauche froid </MedicalObservation><Sex>male</Sex>`

**Sortie :**  
**1. Inspection**  
- Œdème des membres inférieurs  
- Varices visibles aux membres inférieurs  

**2. Palpation**  
- Pouls pédieux absent  
- Autres pouls présents et sans anomalies  
- Membre inférieur gauche froide

**3. Auscultation**  
- Absence de souffles sur les trajets vasculaires

### Exemple 3 (Examen vasculaire normal)  
**Entrée :**  
`<MedicalObservation> examen vasculaire normal, aucune anomalie constatée sur les membres inférieurs et supérieurs </MedicalObservation><Sex>female</Sex>`

**Sortie :**  
**1. Inspection**  
- sans anomalies  

**2. Palpation**  
- Pouls présents sur tous les trajets vasculaires.  

**3. Auscultation**  
- Absence de souffles sur tous les trajets vasculaires

---  

""",
}
