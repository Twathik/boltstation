signes_fonctionnels_cardiovasculaires_widget: dict = {
    "description": """
    ## **Objectif**

    Analyser le texte contenu dans `<MedicalObservation>` pour identifier **uniquement** la présence ou l'absence des signes énumérés dans `<Parameters>`. **Aucune autre information ou symptôme non mentionné dans cette liste ne doit être inclus.**

    ## **Signes à analyser (<Parameters>)**
<Parameters>
    1. **Douleurs thoraciques**
    - Typiques : douleur rétrosternale oppressante (angor, infarctus).
    - Atypiques : douleur épigastrique, irradiations (bras, mâchoire, dos).
    - L'angor est classé de I à IV selon la CCS.
    - les autres sièges de douleurs ne sont pas inclus.

    2. **Dyspnée**
    - D'effort (liée à une insuffisance cardiaque).
    - De repos ou orthopnée (dyspnée en position allongée).
    - Dyspnée paroxystique nocturne (réveil brutal).
    - Classée de I à IV selon la NYHA.

    3. **Palpitations**
    - Sensation de battements rapides, irréguliers ou forts.
    - Liées à des troubles du rythme (extrasystoles, fibrillation auriculaire, tachycardies).

    4. **Syncope ou lipothymie**
    - Syncope : perte de connaissance brutale, souvent liée à une bradycardie, une tachycardie ou une sténose aortique.
    - Lipothymie : sensation de malaise sans perte de conscience.

    5. **Œdèmes des membres inférieurs**
    - Bilatéraux : évocateurs d'insuffisance cardiaque droite.

    6. **Claudication intermittente**
    - Douleur musculaire à l’effort (membres inférieurs), souvent due à une insuffisance artérielle périphérique.


    7. **Toux chronique**
    - Souvent liée à une congestion pulmonaire (insuffisance cardiaque gauche).

    8. **Cyanose**
        - Coloration bleutée des extrémités (hypoxie périphérique).
</Parameters>
    ---

    ## **Instructions pour l'extraction**

    1. **Analyse restreinte :**
    - Limitez l’analyse aux signes mentionnés dans `<Parameters>`.
    - **Ne mentionnez aucun signe ou symptôme extérieur à cette liste.**

    2. **Réponse en cas d'absence d'information :**
    - Si aucun signe de `<Parameters>` n’est mentionné dans `<MedicalObservation>`, répondez avec la phrase suivante :  
        **"Le patient/La patiente ne présente aucun signe fonctionnel."**
    - **Important :** N’ajoutez aucune autre information.

    3. **Réponse en cas de présence d'information :**
    - Si des informations sur un ou plusieurs signes de `<Parameters>` sont identifiées :  
        - Rédigez une réponse en commençant par **"Le patient/La patiente présente : "**.
        - Incluez la liste des signes présents et/ou absents dans `<MedicalObservation>`, mais uniquement ceux de `<Parameters>`.
        - Organisez les information retrouvées sous forme de **liste à puces**.
        - Ignorez toute autre information non pertinente.
        - Toutes les information sur les signes de `<Parameters>` doivent figurer dans le rapport.

    4. **Conformité stricte :**
    - Assurez-vous que la réponse respecte rigoureusement ces consignes. Aucune information ou mention en dehors de `<Parameters>` ne doit apparaître.

    5. **Format attendu :**
    - Si aucun signe n’est retrouvé :  
        
        Le patient/La patiente ne présente aucun signe fonctionnel.
        
    - Si des signes sont retrouvés :  
        
        Le patient/La patiente présente : 
        - [Description du signe 1]
        - [Description du signe 2]
        

    
""",
    "examples": """
    ## **Exemples d'entrée et de sortie :**

    ### Exemple 1 : Aucun signe retrouvé
    **Entrée :**  
    `<MedicalObservation> atcd HTA adenome de la prostate, PA 160/80, souffle IM 2/6, fc 100 bpm, examen vasculaire et pulmonaire normal </MedicalObservation><Sex>female</Sex>`

    **Sortie :**  
    La patiente ne présente aucun signe fonctionnel cardiovasculaire.
    
    **Note :** aucun signe listé dans <Parameters> n'est retrouvé, la reponse doit donc contenir "Le patient/La patiente ne présente aucun signe fonctionnel cardiovasculaire".

    ---

    ### Exemple 2 : Signes retrouvés
    **Entrée :**  
    `<MedicalObservation> Le patient rapporte une dyspnée classe II et des palpitations, mais aucune douleur thoracique. </MedicalObservation><Sex>male</Sex>`

    **Sortie :**  
    Le patient présente : 
        - Une dyspnée classe II de la NYHA
        - Des palpitations
        - Absence de douleur thoracique
    
     **Note :** des informations sur la dyspnée, les palpitations et la douleur thoracique sont presentes dans <MedicalObservation> et doivent donc etre incluses.

    ---

    ### Exemple 3 : Aucun signe de la liste mais d'autres symptômes mentionnés
    **Entrée :**  
    `<MedicalObservation> La patiente souffre de douleurs abdominales et d'une douleur thoracique et des palpitations. </MedicalObservation><Sex>female</Sex>`

    **Sortie :**  
    La patient présente : 
        - Une douleur thoracique
        - Des palpitations
    
    **Note :** Ne mentionnez pas "douleurs abdominales", car ils ne font pas partie des signes listés.

    ---

    ### Exemple 4 : Inclusion de signes externes declarés comme absents
    **Entrée :**  
    `<MedicalObservation> Le patient présente une dyspnée classe II. pas de palpitations, ni d'angor.</MedicalObservation><Sex>male</Sex>`

    **Sortie :**  
    Le patient présente : 
        - Une dyspnée classe II de la NYHA
        - Des palpitations
        - Absence d'angor
""",
}
