signes_generaux_widget: dict = {
    "description": """
    **Objectif**: Analyser le texte contenu dans `<MedicalObservation>` pour identifier la présence ou l'absence **exclusivement** des signes énumérés dans `<Parameters>`. **Aucune autre information** ne doit être incluse. l'information peut etre soit la presence du signe ou son absence.
    <Parameters>
        - fièvre
        - perte de poids
        - perte d'appétit
        - asthénie
        - sueurs nocturnes profuses
        - insomnie
        - confusion mentale ou agitation
        - pâleur cutanéo-muqueuse
        - ictère
        - éruption cutanée
    </Parameters>
    **Instructions pour l'extraction*:*
    
    1. **Analyse restreinte :**  
    Vous devez **strictement** analyser les information portants sur les signes énumérés dans `<Parameters>`. **Ne mentionnez aucun signe en dehors de cette liste**.

    2. **Réponse en cas d'absence d'information** :  
   - **Si aucune information portant sur un signe de la liste `<Parameters>` n'est retrouvé** dans `<MedicalObservation>`, répondre **uniquement** par la phrase suivante :  
     **"Le patient/La patiente ne présente aucun signe général."**
     
     **Important :** Ne donnez aucune autre information, et surtout **ne faites pas référence à d'autres symptômes** non listés dans `<Parameters>`. La réponse doit être concise et précise.

    3. **Réponse en cas de presence d'information** :  
   - **Si un ou plusieurs informations portant sur un signe de `<Parameters>` sont présents**, rédigez une réponse sous la forme suivante :
     - Commencez par **"Le patient/La patiente présente : "** suivi par les informations retrouvés.
     - **N'incluez que les informations portant sur les signes de la liste `<Parameters>`**, même s'il y a d'autres symptômes dans `<MedicalObservation>`.

    4. **Conformité stricte :**  
    Assurez-vous que votre réponse soit **strictement conforme** à ces règles. **Aucune inclusion d'éléments supplémentaires** ou d'informations non demandées ne doit apparaître.

    5. **Format de sortie attendu :**  
    Produisez la réponse en suivant exactement le format ci-dessous :  
    - **Si aucun signe n'est retrouvé :**  
        `Le patient/La patiente ne présente aucun signe général.`
    - **Si au moins un signe est retrouvé**  
        `Le patient/La patiente présente : [liste des informations portant sur les signes retrouvés].`  

    
""",
    "examples": """
    ## **Exemples d'entrée et de sortie :**

    ### Exemple 1 : Aucun signe retrouvé
    **Entrée :**  
    `<MedicalObservation> atcd HTA adenome de la prostate, PA 160/80, souffle IM 2/6, fc 100 bpm, examen vasculaire et pulmonaire normal </MedicalObservation><Sex>female</Sex>`

    **Sortie :**  
    La patiente ne présente aucun signe général.
    
    **Note :** aucun signe listé dans <Parameters> n'est retrouvé, la reponse doit donc contenir "Le patient/La patiente ne présente aucun signe général".

    ---

    ### Exemple 2 : Signes retrouvés
    **Entrée :**  
    `<MedicalObservation> Le patient rapporte une asthénie et une perte de poids, mais aucun signe de fièvre ou d'insomnie. </MedicalObservation><Sex>male</Sex>`

    **Sortie :**  
    Le patient présente : une asthénie, une perte de poids. absence de fievre ou d'insomnie.
    
     **Note :** une information sur l'asthenie, la perte de poids, la fievre et l'insomnie est presente dans <MedicalObservation> et doit donc etre incluse.

    ---

    ### Exemple 3 : Aucun signe de la liste mais d'autres symptômes mentionnés
    **Entrée :**  
    `<MedicalObservation> La patiente souffre de douleurs abdominales et d'une douleur thoracique et des palpitations. </MedicalObservation><Sex>female</Sex>`

    **Sortie :**  
    La patiente ne présente aucun signe général.
    
    **Note :** Ne mentionnez pas "douleurs abdominales" ou "douleur thoracique" et "palpitations", car ils ne font pas partie des signes listés.

    ---

    ### Exemple 4 : Inclusion de signes externes declarés comme absents
    **Entrée :**  
    `<MedicalObservation> Le patient présente une éruption cutanée et de la fièvre. pas d'ictère </MedicalObservation><Sex>male</Sex>`

    **Sortie :**  
    Le patient présente : une éruption cutanée, une fièvre. Absence d'ictère

    
""",
}
