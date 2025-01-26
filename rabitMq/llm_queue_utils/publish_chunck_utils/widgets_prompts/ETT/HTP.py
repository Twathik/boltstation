ETT_HTP_widget: dict = {
    "description": """
### **Contexte :**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à l’hypertension pulmonaire (HTP)**, en excluant rigoureusement les variables numériques suivantes :  
- Vitesse maximale de l’insuffisance tricuspide (vit max IT).  
- Pression artérielle pulmonaire diastolique (PAPD).  
- Pression artérielle pulmonaire moyenne (PAPM).  
- Temps d’accélération de l’artère pulmonaire (TAP).  
- Diamètre de l’artère pulmonaire (AP).  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant l’hypertension pulmonaire, à l’exception des variables citées. Structurez les résultats sous forme de paragraphe fluide.

---

### **Règles d’Extraction**  

#### 1. **Données autorisées :**  
- Mention d’une **présomption d’hypertension pulmonaire** (présente ou absente).  
- Description de l’aspect de l’artère pulmonaire : dilatée, normale, anomalies spécifiques.  
- Anomalies qualitatives en lien avec l’hypertension pulmonaire, par exemple :  
  - Régurgitation pulmonaire ou tricuspide.  
  - Déviation du septum interventriculaire liée à une surcharge droite.  
  - Dilatation des cavités droites associée.  

#### 2. **Données interdites :**  
- Vitesse maximale de l’insuffisance tricuspide (vit max IT).  
- Pression artérielle pulmonaire diastolique (PAPD).  
- Pression artérielle pulmonaire moyenne (PAPM).  
- Temps d’accélération de l’artère pulmonaire (TAP).  
- Diamètre de l’artère pulmonaire (AP).  

#### 3. **Structure obligatoire de la sortie :**  
- Mentionnez explicitement si une **présomption d’hypertension pulmonaire** est rapportée.  
- Décrivez qualitativement l’artère pulmonaire (ex. dilatée, normale).  
- Incluez toute observation clinique pertinente liée à l’hypertension pulmonaire.  

#### 4. **Gestion des absences :**  
- Si aucune mention de l’hypertension pulmonaire ou des observations associées n’est présente dans le texte :  
  - Répondez par : **"Hypertension pulmonaire non décrite."**  
- Si l’absence d’hypertension pulmonaire est explicitement rapportée :  
  - Répondez par : **"Absence de signes en faveur d’une hypertension pulmonaire."**

#### 5. **Respect strict des données fournies :**  
- Utilisez uniquement les informations présentes dans le texte fourni.  
- Reformulez légèrement pour adopter un style professionnel d’un échocardiographiste chevronné.  
- Ignorez rigoureusement les variables interdites mentionnées ci-dessus.  

---
""",
    "examples": """
### **Exemples Entrée-Sortie :**

#### **Exemple 1 : Présence d’hypertension pulmonaire avec anomalies associées**
**Entrée :**  
"Présence d’une hypertension pulmonaire présumée. L’artère pulmonaire est dilatée. Régurgitation tricuspide modérée avec déviation du septum interventriculaire vers la gauche."

**Sortie :**  
- **Hypertension pulmonaire :** Présomption d’hypertension pulmonaire rapportée.  
- **Artère pulmonaire :** Artère pulmonaire dilatée.  
- **Observations associées :** Régurgitation tricuspide modérée et déviation du septum interventriculaire vers la gauche.

**Explication :**  
- Les anomalies qualitatives (dilatation de l’artère pulmonaire, régurgitation, déviation du septum) sont rapportées.  
- Les variables numériques interdites (ex. vit max IT, TAP) sont ignorées.  

---

#### **Exemple 2 : Absence explicite d’hypertension pulmonaire**
**Entrée :**  
"Aucun signe d’hypertension pulmonaire rapporté. Artère pulmonaire de taille normale."

**Sortie :**  
- **Hypertension pulmonaire :** Absence de signes en faveur d’une hypertension pulmonaire.  
- **Artère pulmonaire :** Artère pulmonaire de taille normale.

**Explication :**  
- L’absence explicite d’hypertension pulmonaire est traduite dans un style professionnel.  

---

#### **Exemple 3 : Absence de mention de l’hypertension pulmonaire**
**Entrée :**  
"Aucune mention de l’hypertension pulmonaire."

**Sortie :**  
- **Réponse :** Hypertension pulmonaire non décrite.

**Explication :**  
- L’absence de mention de l’hypertension pulmonaire est signalée clairement.  

---

#### **Exemple 4 : Mention d’anomalies associées sans confirmation explicite**
**Entrée :**  
"Artère pulmonaire dilatée, avec régurgitation pulmonaire minime. Cavités droites dilatées."

**Sortie :**  
- **Hypertension pulmonaire :** Présence possible d’anomalies associées à l’hypertension pulmonaire.  
- **Artère pulmonaire :** Artère pulmonaire dilatée.  
- **Observations associées :** Régurgitation pulmonaire minime et cavités droites dilatées.

**Explication :**  
- Les anomalies qualitatives associées à l’hypertension pulmonaire sont rapportées.  
- Les variables numériques interdites ne sont pas considérées.

---
""",
}
