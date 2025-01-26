ETT_prothese_aortique_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à l’évaluation d’une prothèse aortique, bioprothèse aortique ou TAVI**, tout en excluant rigoureusement les variables numériques suivantes :  
- Vitesse maximale aortique (V max).  
- Gradient maximal.  
- Gradient moyen.  
- Surface fonctionnelle aortique.  
- Temps d'accélération.  
- Indice de perméabilité.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant l’évaluation de ces dispositifs, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement à partir du contenu de la balise `<MedicalObservation>` :  
- Type de dispositif évalué :  
  - Prothèse aortique mécanique.  
  - Bioprothèse aortique.  
  - TAVI (Transcatheter Aortic Valve Implantation).  
- Présence ou absence de dysfonctionnement :  
  - Sténose.  
  - Régurgitation paraprothétique ou intra-prothétique.  
  - Thrombose ou pannus.  
  - Dégénérescence structurelle.  
- Description des anomalies fonctionnelles (ex., "diminution de l’ouverture", "flux accéléré").  
- Anomalies structurelles observées (ex., "calcifications", "déchirures").  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "V max élevée, suggérant une sténose significative", "surface fonctionnelle réduite, indiquant un dysfonctionnement").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Vitesse maximale aortique (V max).  
- Gradient maximal.  
- Gradient moyen.  
- Surface fonctionnelle aortique.  
- Temps d'accélération.  
- Indice de perméabilité.  

### 3. **Structure obligatoire de la sortie**  
- **Type de dispositif :** Mentionnez le type de prothèse ou dispositif évalué.  
- **Dysfonctionnement :** Décrivez qualitativement toute anomalie ou dysfonctionnement observé (ex., sténose, régurgitation).  
- **Anomalies structurelles :** Mentionnez les observations qualitatives concernant la structure du dispositif.  
- **Interprétation :** Incluez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "gradient moyen élevé suggérant une sténose significative").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la prothèse, bioprothèse ou TAVI n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de la prothèse aortique non décrite."**  
- Si une prothèse aortique est **explicitement décrite comme normale** :  
  - Répondez par : **"Prothèse aortique fonctionnant normalement, sans anomalies détectées."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Dysfonctionnement d’une bioprothèse aortique**  
**Entrée :**  
Bioprothèse aortique avec diminution de l’ouverture et flux accéléré. Présence de régurgitation intra-prothétique modérée. Gradient moyen élevé, suggérant une sténose significative.

**Sortie :**  
- **Type de dispositif :** Bioprothèse aortique.  
- **Dysfonctionnement :** Diminution de l’ouverture et flux accéléré. Régurgitation intra-prothétique modérée.  
- **Interprétation :** Gradient moyen élevé, suggérant une sténose significative.

---

### **Exemple 2 : TAVI sans anomalies**  
**Entrée :**  
TAVI correctement positionné. Fonctionnement normal sans sténose ni régurgitation.

**Sortie :**  
- **Type de dispositif :** TAVI.  
- **Dysfonctionnement :** Aucun dysfonctionnement observé.  
- **Interprétation :** Fonctionnement normal sans sténose ni régurgitation.

---

### **Exemple 3 : Absence explicite de mention de prothèse aortique**  
**Entrée :**  
Aucune mention de la prothèse aortique.

**Sortie :**  
- **Réponse :** Évaluation de la prothèse aortique non décrite.

---

### **Exemple 4 : Prothèse aortique avec interprétation des valeurs numériques**  
**Entrée :**  
Prothèse aortique mécanique présentant des flux élevés et une surface fonctionnelle réduite, indiquant un possible dysfonctionnement. Régurgitation paraprothétique légère.

**Sortie :**  
- **Type de dispositif :** Prothèse aortique mécanique.  
- **Dysfonctionnement :** Flux élevés et surface fonctionnelle réduite, indiquant un possible dysfonctionnement.  
- **Interprétation :** Surface fonctionnelle réduite, suggérant un possible dysfonctionnement.

---
""",
}
