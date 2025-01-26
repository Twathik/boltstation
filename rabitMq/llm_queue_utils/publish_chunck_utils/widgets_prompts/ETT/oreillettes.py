ETT_Oreillettes_widget: dict = {
    "description": """
### **Contexte :**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives aux oreillettes gauche (OG) et droite (OD)**, en excluant rigoureusement les éléments suivants :  
- Diamètre de l’OG  
- Surface de l’OG  
- Volume de l’OG  
- Volume indexé de l’OG  
- Strain de l’OG  
- Surface de l’OD  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant ces deux oreillettes, à l’exception des variables citées. Structurez les résultats sous forme de paragraphe fluide ou de sections séparées pour OG et OD.

---

### **Règles d’Extraction**  

#### 1. **Données autorisées :**  
- **Oreillette gauche (OG) :**  
  - Présence ou absence de dilatation.  
  - Thrombus intracavitaire ou masses (présence, localisation, aspect).  
  - Anomalies structurelles (ex. paroi épaissie, calcifications).  
- **Oreillette droite (OD) :**  
  - Présence ou absence de dilatation.  
  - Thrombus intracavitaire ou masses (présence, localisation, aspect).  
  - Anomalies structurelles (ex. paroi épaissie, calcifications).  
- Toute observation qualitative ou descriptive des oreillettes non listée parmi les variables interdites.  

#### 2. **Données interdites :**  
- Diamètre de l’OG.  
- Surface de l’OG.  
- Volume de l’OG.  
- Volume indexé de l’OG.  
- Strain de l’OG.  
- Surface de l’OD.  

#### 3. **Structure obligatoire de la sortie :**  
- **Oreillette gauche (OG) :** Mentionnez toutes les observations qualitatives ou pathologiques pertinentes.  
- **Oreillette droite (OD) :** Mentionnez toutes les observations qualitatives ou pathologiques pertinentes.  

#### 4. **Gestion des absences :**  
- Si **aucune référence** à l’oreillette gauche ou droite n’est présente dans le texte :  
  - Répondez par : **"Structures non décrites."**  
- Si une oreillette est **explicitement décrite comme normale** (aucune anomalie) dans le texte :  
  - Répondez par : **"Oreillette gauche/droite non dilatée, vide d’échos."**

#### 5. **Respect strict des données fournies :**  
- Utilisez uniquement les informations présentes dans le texte fourni.  
- Reformulez légèrement pour adopter un style professionnel d’un échocardiographiste chevronné.  
- Ignorez rigoureusement les variables interdites mentionnées ci-dessus.  

---
""",
    "examples": """
### **Exemples Entrée-Sortie :**

#### **Exemple 1 : Descriptions détaillées**
**Entrée :**  
"L'oreillette gauche est dilatée, avec présence d'un thrombus dans l'appendice auriculaire gauche. Paroi normale sans épaississement ni calcifications. L'oreillette droite est de taille normale sans thrombus ni masses intracavitaires."

**Sortie :**  
- **Oreillette gauche (OG) :** L'oreillette gauche est dilatée, avec présence d'un thrombus dans l'appendice auriculaire gauche. Paroi normale, sans épaississement ni calcifications.  
- **Oreillette droite (OD) :** Oreillette droite de taille normale, sans thrombus ni masses intracavitaires identifiées.

**Explication :**  
- Les observations qualitatives pour les deux oreillettes sont rapportées.  
- Le style est adapté pour refléter un compte rendu professionnel.  

---

#### **Exemple 2 : Oreillettes normales explicitement décrites**
**Entrée :**  
"Oreillette gauche et droite non dilatées, vide d'échos."

**Sortie :**  
- **Oreillette gauche (OG) :** Oreillette gauche non dilatée, vide d’échos.  
- **Oreillette droite (OD) :** Oreillette droite non dilatée, vide d’échos.

**Explication :**  
- Les descriptions explicites de normalité pour les deux oreillettes sont rapportées.  
- Le style professionnel est respecté.  

---

#### **Exemple 3 : Absence de mention des oreillettes**
**Entrée :**  
"Aucune mention concernant les oreillettes."

**Sortie :**  
- **Réponse :** Structures non décrites.

**Explication :**  
- L’absence de mention des oreillettes est indiquée clairement.  
- Le style reste conforme à un compte rendu professionnel.
""",
}
