ETT_VCI_widget: str = """
### **Contexte :**  
Analysez le contenu de la balise `<MedicalObservation>` pour **extraire les informations relatives à la veine cave inférieure (VCI)**, en excluant rigoureusement **toute mention du diamètre de la VCI**.  

L'agent devra extraire toutes les informations qualitatives et observations pertinentes concernant la VCI, à l’exception du diamètre. Structurez les résultats sous forme de paragraphe fluide.

---

### **Règles d’Extraction**  

#### 1. **Données autorisées :**  
- Présence ou absence de dilatation.  
- Aspects morphologiques : paroi épaissie, calcifications, irrégularités, etc.  
- Mobilité ou collapsibilité qualitative (ex. "collapsibilité réduite").  
- Toute mention d’obstruction, thrombus ou anomalies spécifiques (ex. "thrombus visible").  

#### 2. **Données interdites :**  
- Diamètre de la VCI.  

#### 3. **Structure obligatoire de la sortie :**  
- Décrivez qualitativement les observations sur la VCI, en mentionnant toute anomalie pertinente.  

#### 4. **Gestion des absences :**  
- Si **aucune référence** à la VCI n’est présente dans le texte :  
  - Répondez par : **"Structure non décrite."**  
- Si la VCI est **explicitement décrite comme normale** ou si aucune anomalie n’est décrite :  
  - Répondez par : **"VCI non dilatée, compliante."**

#### 5. **Respect strict des données fournies :**  
- Utilisez uniquement les informations présentes dans le texte fourni.  
- Reformulez légèrement pour adopter un style professionnel d’un échocardiographiste chevronné.  
- Ignorez rigoureusement toute mention du diamètre de la VCI.  

---
## **Exemples Entrée-Sortie :**

### **Exemple 1 : Descriptions détaillées**
**Entrée :**  
"Veine cave inférieure dilatée avec collapsibilité réduite. Présence d’un thrombus partiellement occlusif dans la portion proximale. Paroi régulière sans calcifications."

**Sortie :**  
- **Veine cave inférieure (VCI) :** La veine cave inférieure est dilatée, avec collapsibilité réduite. Présence d’un thrombus partiellement occlusif dans la portion proximale. Paroi régulière, sans calcifications.

**Explication :**  
- Les anomalies qualitatives (dilatation, collapsibilité réduite, thrombus) sont rapportées.  
- Toute mention du diamètre de la VCI est ignorée.  

---

### **Exemple 2 : VCI normale explicitement décrite**
**Entrée :**  
"VCI de calibre normal, sans thrombus ni anomalies visibles."

**Sortie :**  
- **Veine cave inférieure (VCI) :** VCI non dilatée, compliante.

**Explication :**  
- La normalité explicite de la VCI est traduite par une réponse professionnelle standard.  

---

### **Exemple 3 : Absence de mention de la VCI**
**Entrée :**  
"Aucune mention de la veine cave inférieure."

**Sortie :**  
- **Réponse :** Structure non décrite.

**Explication :**  
- L’absence de mention de la VCI est clairement signalée.  
- Le style reste conforme à un compte rendu professionnel.  

---

### **Exemple 4 : Absence d’anomalies décrites explicitement**
**Entrée :**  
"Aucune anomalie de la VCI n’est rapportée."

**Sortie :**  
- **Veine cave inférieure (VCI) :** VCI non dilatée, compliante.

**Explication :**  
- L’absence explicite d’anomalie est traduite par une réponse normalisée : "VCI non dilatée, compliante."
"""
