autre_symptomes_widget: dict = {
    "description": """
## **Objectif**  
1. **Identifier** les symptômes présents dans `<MedicalObservation>`.  
2. **Ne retenir que** ceux qui **ne figurent pas** dans la liste `<Parameters>`.  
3. **Exclure** toute mention relative aux symptômes déjà listés dans `<Parameters>`.  
4. **Éliminer** les informations provenant d’examens cliniques ou paracliniques (tels que auscultation, prise de PA, tests de laboratoire, etc.).

---

## **Signes à analyser (`<Parameters>`)**

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

## **Instructions**

1. **Analyse comparative stricte**  
   - Repérez tous les symptômes mentionnés dans `<MedicalObservation>`.  
   - Comparez-les à la liste dans `<Parameters>`.  
   - **Ignorez et ne citez pas** les symptômes présents dans `<Parameters>`.  
   - **Ne discutez pas** des symptômes de `<Parameters>` (ni directement ni par reformulation).  

2. **Exclusion des examens cliniques et paracliniques**  
   - **N’incluez pas** dans la réponse les détails issus d’examens cliniques ou paracliniques, tels que :  
     - Auscultation  
     - Prise de pression artérielle (PA)  
     - Tests de laboratoire  
     - Imageries médicales  
     - Toute autre investigation médicale  
   - **Excluez strictement** toute mention d’investigations, de tests ou d’examens médicaux dans la sortie.

3. **Format attendu**  
   - **S’il n’existe aucun nouveau symptôme** :  
     > *Aucun autre symptôme n'est retrouvé.*  

   - **S’il existe un ou plusieurs symptômes hors liste** :  
     > *Les symptômes suivants sont présents dans `<MedicalObservation>` mais absents de `<Parameters>` :*  
     > - [Symptôme 1 hors liste]  
     > - [Symptôme 2 hors liste]  
     > ...  

4. **Conformité**  
   - Ne mentionnez **que** les symptômes **non répertoriés** dans `<Parameters>`.  
   - **Aucune duplication** : un symptôme hors liste ne doit apparaître qu’une seule fois.  
   - **Aucune référence** (directe ou indirecte) aux symptômes déjà listés dans `<Parameters>`.  
   - **Éliminez** toute information liée aux examens cliniques ou paracliniques, même si elles ne sont pas symptomatiques.

---
""",
    "examples": """
### **Exemples d'entrée et de sortie :**
--- 
#### **Exemple 1 : Aucun symptôme hors liste retrouvé**  
**Entrée** 
<MedicalObservation> ATCD HTA, adénome de la prostate, PA 160/80, souffle IM 2/6, FC 100 bpm, examen vasculaire et pulmonaire normal </MedicalObservation> <Sex>female</Sex>

**Sortie attendue**
La patiente ne présente aucun autre symptôme.

**Éléments clés**
- Le texte dans <MedicalObservation> ne contient aucun symptôme figurant en dehors de la liste `<Parameters>`.
- Il s’agit uniquement d’antécédents, de mesures (pression artérielle, fréquence cardiaque) et de données d’examens, qui doivent être ignorés.
- La réponse doit confirmer qu’il n’existe aucun nouveau symptôme à mentionner.

---
#### **Exemple 2 : Symptômes présents dans `<Parameters>` uniquement**

<MedicalObservation>
  Le patient rapporte une dyspnée classe II et des palpitations, 
  mais aucune douleur thoracique.
</MedicalObservation>
<Sex>male</Sex>

**Sortie attendue**
Le patient ne présente aucun autre symptôme.

**Éléments clés**

- Les symptômes mentionnés (dyspnée, palpitations, douleur thoracique) sont déjà répertoriés dans `<Parameters>`.
- Ils doivent donc être ignorés dans la sortie.
- La réponse finale confirme simplement qu’aucun autre symptôme n’est retrouvé.

---

#### **Exemple 3 : Symptômes hors liste identifiés**
<MedicalObservation>
  La patiente souffre de douleurs abdominales et d'une douleur thoracique 
  ainsi que de palpitations. Elle présente également un urticaire.
</MedicalObservation>
<Sex>female</Sex>

**Sortie attendue**
La patiente présente :
- Une douleur abdominale
- Un urticaire

**Éléments clés**
- La "douleur thoracique" et les "palpitations" figurent dans la liste <Parameters> : à exclure.
- - Les symptômes "douleurs abdominales" et "urticaire" ne sont pas dans `<Parameters>` et doivent donc être mentionnés.
La réponse reprend uniquement les symptômes hors liste.

---
#### **Exemple 4 : Présence explicite de signes externes déclarés comme absents**

<MedicalObservation>
  Le patient présente une douleur abdominale, des troubles de la conscience, 
  absence de brûlures mictionnelles, absence de dysenterie.
</MedicalObservation>
<Sex>male</Sex>

**Sortie attendue**
Le patient présente :
- Une douleur abdominale
- Des troubles de la conscience
- Absence de brûlures mictionnelles
- Absence de dysenterie

**Éléments clés**
-Les symptômes hors liste mentionnés (douleur abdominale, troubles de la conscience) doivent être listés.
-Les signes explicitement déclarés "absents" (ex. brûlures mictionnelles, dysenterie) doivent également être mentionnés, car ils font partie de l’observation.
-Aucun de ces symptômes ne se trouve dans `<Parameters>`, il faut donc tous les inclure tels quels.

""",
}
