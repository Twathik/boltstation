ETT_prothese_mitrale_widget: dict = {
    "description": """
## **Contexte**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à l’évaluation d’une prothèse mitrale mécanique ou d’une bioprothèse**, tout en excluant rigoureusement les variables numériques suivantes :  
- Vitesse maximale mitrale (V max).  
- Gradient maximal.  
- Gradient moyen.  
- Surface fonctionnelle mitrale.  
- Rapport des ITV (intégrales temporelles des vitesses).  
- PHT (Pressure Half-Time).  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant l’évaluation de ces dispositifs, y compris l’interprétation des valeurs numériques mentionnées explicitement, mais jamais les valeurs elles-mêmes. Structurez les résultats sous forme de paragraphe fluide.

---

## **Règles d’Extraction**

### 1. **Données autorisées**  
L'agent doit extraire uniquement à partir du contenu de la balise `<MedicalObservation>` :  
- Type de dispositif évalué :  
  - Prothèse mitrale mécanique.  
  - Bioprothèse mitrale.  
- Présence ou absence de dysfonctionnement :  
  - Sténose.  
  - Régurgitation paraprothétique ou intra-prothétique.  
  - Thrombose, pannus ou obstruction par un matériel thrombotique.  
  - Dégénérescence structurelle.  
- Description qualitative des anomalies fonctionnelles (ex., "diminution de l’ouverture", "flux accéléré").  
- Anomalies structurelles observées (ex., "calcifications", "mobilité restreinte des feuillets").  
- Interprétation qualitative des valeurs numériques si mentionnée explicitement (ex., "gradient moyen élevé suggérant une sténose significative", "PHT prolongé indiquant une dysfonction prothétique").  

### 2. **Données interdites**  
L'agent doit **ignorer** les éléments suivants :  
- Vitesse maximale mitrale (V max).  
- Gradient maximal.  
- Gradient moyen.  
- Surface fonctionnelle mitrale.  
- Rapport des ITV.  
- PHT (Pressure Half-Time).  

### 3. **Structure obligatoire de la sortie**  
- **Type de dispositif :** Mentionnez le type de prothèse ou dispositif évalué.  
- **Dysfonctionnement :** Décrivez qualitativement toute anomalie ou dysfonctionnement observé (ex., sténose, régurgitation).  
- **Anomalies structurelles :** Mentionnez les observations qualitatives concernant la structure du dispositif.  
- **Interprétation :** Incluez les interprétations qualitatives des valeurs numériques si explicitement rapportées (ex., "gradient moyen élevé suggérant une sténose significative").  

### 4. **Gestion des absences**  
- Si **aucune mention** de la prothèse mitrale n’est présente dans le contenu de la balise `<MedicalObservation>` :  
  - Répondez par : **"Évaluation de la prothèse mitrale non décrite."**  
- Si une prothèse mitrale est **explicitement décrite comme normale** :  
  - Répondez par : **"Prothèse mitrale fonctionnant normalement, sans anomalies détectées."**

---
""",
    "examples": """
## **Exemples Entrée-Sortie**

### **Exemple 1 : Dysfonctionnement d’une prothèse mitrale mécanique**  
**Entrée :**  
Prothèse mitrale mécanique présentant une diminution de l’ouverture avec flux accéléré. Gradient moyen élevé, suggérant une sténose significative. Régurgitation paraprothétique modérée observée.

**Sortie :**  
- **Type de dispositif :** Prothèse mitrale mécanique.  
- **Dysfonctionnement :** Diminution de l’ouverture avec flux accéléré. Régurgitation paraprothétique modérée.  
- **Interprétation :** Gradient moyen élevé, suggérant une sténose significative.

---

### **Exemple 2 : Bioprothèse mitrale sans anomalies**  
**Entrée :**  
Bioprothèse mitrale correctement positionnée et fonctionnant normalement. Absence de sténose ou de régurgitation.

**Sortie :**  
- **Type de dispositif :** Bioprothèse mitrale.  
- **Dysfonctionnement :** Aucun dysfonctionnement observé.  
- **Interprétation :** Fonctionnement normal sans sténose ni régurgitation.

---

### **Exemple 3 : Absence explicite de mention de prothèse mitrale**  
**Entrée :**  
Aucune mention de la prothèse mitrale.

**Sortie :**  
- **Réponse :** Évaluation de la prothèse mitrale non décrite.

---

### **Exemple 4 : Prothèse mitrale avec interprétation des valeurs numériques**  
**Entrée :**  
Bioprothèse mitrale présentant une mobilité restreinte des feuillets et un PHT prolongé, suggérant un dysfonctionnement. Flux légèrement accéléré.

**Sortie :**  
- **Type de dispositif :** Bioprothèse mitrale.  
- **Dysfonctionnement :** Mobilité restreinte des feuillets et flux légèrement accéléré.  
- **Interprétation :** PHT prolongé, suggérant un dysfonctionnement.

---
""",
}
