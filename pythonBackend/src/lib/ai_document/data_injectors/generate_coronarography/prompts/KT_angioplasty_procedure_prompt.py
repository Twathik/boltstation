angioplasty_procedure_prompt = """
## 🎯 Reformulation d’une procédure d’angioplastie coronaire
Reformule la description médicale suivante en français, en respectant **strictement** les consignes ci-dessous :

---

### ✅ Règles générales :
1. Conserver **toutes les informations médicales** présentes dans le texte source (instruments, mesures, vaisseaux, complications, etc.).
2. Éviter **toute répétition inutile** :
   - Si un matériel contient déjà les paramètres sous la forme *(diamètre X longueur)*, ne pas répéter les dimensions en toutes lettres.
3. Améliorer la **fluidité, la précision et la clarté** du texte, dans un style **formel, technique et professionnel**, adapté à un **compte rendu opératoire de cardiologie interventionnelle**.
4. Ne **pas commencer** par une phrase introductive (ex. « Suite à... »). Le texte doit débuter directement par l'action ou l'observation médicale.
5. Ne **pas ajouter** d'informations nouvelles ni modifier les données cliniques fournies.
6. Le résultat doit être rédigé en **français uniquement**.

---

### 🧾 Mise en forme :
7. Le **matériel utilisé** (ex. ballons, stents, cathéters, etc.) doit être affiché en **gras**.
8. La **pression d’inflation**, exprimée en **ATM**, doit être affichée en **gras**.

---

### 💬 Terminologie technique :
9. Utiliser des termes techniques corrects :
   - Employer « **ballon** » au lieu de « ballonet ».
   - Employer « **stent** » au lieu de tout autre terme moins spécifique.
   - Employer les désignations précises pour les dispositifs médicaux (ex. cathéter, microcathéter, guide, etc.).
10. Le terme **extension-Kt** doit être interprété comme une **extension de cathéter guide** et formulé comme tel dans le texte.

---

### 🧠 Interprétation anatomique :
11. Lorsqu’une chaîne de segments artériels est mentionnée avec un tiret (ex. `IVA1 proximale -> IVA2 proximale - 1ère diagonale`) :
   - Le premier segment correspond au **vaisseau principal**.
   - Les segments suivants (après le tiret) sont à considérer comme **branches filles** ou **segments successifs**.
   - La formulation doit refléter le **trajet anatomique et interventionnel** logique, de façon fluide et cohérente (ex. : *de l’IVA1 proximale à l’IVA2 proximale en passant par la 1ère diagonale*).

---
"""
