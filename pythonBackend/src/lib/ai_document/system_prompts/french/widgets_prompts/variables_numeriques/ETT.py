ETT_variables_numerics_description = [
    {
        "name": "Aorte_Diam_Anneau",
        "description": "Diamètre mesuré au niveau de l’anneau aortique, en diastole, exprimé en millimètres (mm). Ce diamètre représente la dimension interne de l’anneau valvulaire. Rechercher explicitement la mention 'anneau aortique' ou une équivalence dans le texte",
    },
    {
        "name": "Aorte_Diam_Sinus_Valsalva",
        "description": "Diamètre des sinus de Valsalva, mesuré en diastole, exprimé en millimètres (mm). Rechercher les termes 'sinus de Valsalva' ou 'sinus aortiques'. Si plusieurs mesures sont données, extraire la dernière valeur.",
    },
    {
        "name": "Aorte_Diam_Jonction_Sino_Tubulaire",
        "description": "Diamètre de la jonction sino-tubulaire mesuré en diastole, exprimé en millimètres (mm). Ce paramètre correspond à la zone de transition entre les sinus de Valsalva et l’aorte ascendante.",
    },
    {
        "name": "Aorte_Diam_Tubulaire",
        "description": "Diamètre de l’aorte tubulaire mesuré en diastole, exprimé en millimètres (mm). Cette mesure évalue la portion tubulaire de l’aorte ascendante pour détecter des anomalies structurelles comme des dilatations.",
    },
    {
        "name": "Diam_tele_diast_VG",
        "description": "Diamètre télédiastolique du ventricule gauche mesuré à la fin de la diastole, exprimé en millimètres (mm). Cette mesure évalue la taille du ventricule gauche lorsqu’il est rempli de sang.",
    },
    {
        "name": "Diam_tele_syst_VG",
        "description": "Diamètre télésystolique du ventricule gauche mesuré à la fin de la systole, exprimé en millimètres (mm). Il reflète la taille du ventricule gauche après l’éjection du sang vers l’aorte.",
    },
    {
        "name": "Volum_tele_syst_VG",
        "description": "Volume télésystolique du ventricule gauche mesuré à la fin de la systole, exprimé en millilitres (mL). Cette valeur évalue le volume sanguin restant dans le ventricule après la contraction.",
    },
    {
        "name": "Volum_tele_diast_VG",
        "description": "Volume télédiastolique du ventricule gauche mesuré à la fin de la diastole, exprimé en millilitres (mL). Cette mesure évalue la capacité de remplissage du ventricule gauche.",
    },
    {
        "name": "FE_Simpson",
        "description": "Fraction d'éjection (FE) mesurée par la méthode Simpson en pourcentage (%). Elle est calculée comme le rapport entre le volume éjecté et le volume télédiastolique pour évaluer la fonction systolique du ventricule gauche.",
    },
    {
        "name": "FE_3D",
        "description": "Fraction d'éjection mesurée par échocardiographie tridimensionnelle (3D), exprimée en pourcentage (%). Ne pas attribuer de valeur si le texte ne mentionne pas explicitement les termes 'échocardiographie 3D', 'FE mesurée en 3D' ou 'fraction d’éjection tridimensionnelle'. Ignorer les valeurs associées à la méthode Simpson ou d'autres techniques. Exemple attendu dans le texte : 'Fraction d’éjection mesurée par 3D : 58 %'.",
    },
    {
        "name": "Strain_GLS",
        "description": "Strain longitudinal global (GLS) du ventricule gauche mesuré en pourcentage (%), évaluant la déformation longitudinale myocardique pendant la systole. Des valeurs normales se situent autour de -16 % à -22 %.",
    },
    {
        "name": "VD_diam_basal",
        "description": "Diamètre basal du ventricule droit mesuré en diastole, exprimé en millimètres (mm). Il évalue la largeur de la base du ventricule droit.",
    },
    {
        "name": "VD_diam_moy",
        "description": "Diamètre moyen du ventricule droit, mesuré en millimètres (mm), correspondant à la largeur médiane entre la base et l’apex. Extraire uniquement si des termes explicites tels que 'diamètre moyen du VD', 'diamètre médian' ou équivalents sont présents dans le texte. En l’absence de mention, retourner null.",
    },
    {
        "name": "VD_diam_longitudinal",
        "description": "Diamètre longitudinal du ventricule droit mesuré entre la base et l’apex, en millimètres (mm). Rechercher les mentions spécifiques de 'diamètre longitudinal', 'longueur VD' ou 'longueur ventriculaire droite'. Si ces termes ne sont pas présents dans le texte, retourner null.",
    },
    {
        "name": "VD_TAPSE",
        "description": "TAPSE (excursion systolique de l’anneau tricuspide) mesuré en millimètres (mm). Il évalue la fonction systolique longitudinale du ventricule droit.",
    },
    {
        "name": "VD_Pic_S",
        "description": "Pic de l'onde S mesuré par Doppler tissulaire au niveau de l’anneau tricuspide, exprimé en centimètres par seconde (cm/s). Cette valeur reflète la vélocité systolique longitudinale du ventricule droit.",
    },
    {
        "name": "VD_FAC",
        "description": "Fraction de surface d’acourcissement (FAC) mesurée en pourcentage (%). Elle évalue la fonction systolique globale du ventricule droit.",
    },
    {
        "name": "VD_strain_GLS",
        "description": "Strain longitudinal global du ventricule droit mesuré en pourcentage (%), évaluant la déformation longitudinale du ventricule droit pendant la systole.",
    },
    {
        "name": "OG_Diam",
        "description": "Diamètre de l'oreillette gauche mesuré en diastole, exprimé en millimètres (mm). Il évalue la taille de l’oreillette gauche.",
    },
    {
        "name": "OG_Surface",
        "description": "Surface de l'oreillette gauche mesurée en centimètres carrés (cm²). Elle reflète la taille bidimensionnelle de l’oreillette gauche.",
    },
    {
        "name": "OG_Volume",
        "description": "Volume de l’oreillette gauche, exprimé en millilitres (mL). Rechercher les termes spécifiques comme 'volume OG', 'volume auriculaire gauche', 'volume de l’oreillette gauche' ou équivalents. Ne pas attribuer de valeur si le texte mentionne uniquement des dimensions ou une surface de l’oreillette gauche. Exemple attendu dans le texte : 'Volume de l’oreillette gauche : 34 mL.'",
    },
    {
        "name": "OG_volume_indexe",
        "description": "Volume indexé de l'oreillette gauche rapporté à la surface corporelle, exprimé en millilitres par mètre carré (mL/m²). Il évalue la taille relative de l’oreillette gauche.",
    },
    {
        "name": "OG_Strain",
        "description": "Strain de l’oreillette gauche mesuré en pourcentage (%), exprimant la déformation auriculaire pendant le cycle cardiaque. Les mentions spécifiques comme 'strain auriculaire gauche' ou 'OG strain' doivent être présentes pour extraire une valeur.",
    },
    {
        "name": "Mitrale_surface_anatomique",
        "description": "Surface anatomique de la valve mitrale mesurée en diastole, exprimée en centimètres carrés (cm²). Elle reflète la taille structurelle de la valve mitrale.",
    },
    {
        "name": "Mitrale_surface_fonctionnelle",
        "description": "Surface fonctionnelle de la valve mitrale, mesurée en centimètres carrés (cm²). Ce paramètre est généralement associé à des mesures par Doppler ou à l’évaluation de l’orifice effectif de la valve.",
    },
    {
        "name": "Aorte_surface_fonctionnelle",
        "description": "Surface fonctionnelle de l'orifice valvulaire aortique (AVA), exprimée en centimètres carrés (cm²). Cette mesure doit être extraite uniquement si le texte mentionne explicitement des termes comme 'surface fonctionnelle', 'AVA', 'aire valvulaire aortique' ou 'surface valvulaire aortique'. Ne pas inférer de valeur si le terme est absent. Exemple attendu dans le texte : 'Surface fonctionnelle de l’aorte mesurée à 1,5 cm².'",
    },
    {
        "name": "Mitral_gradient_moyen",
        "description": "Gradient mitral moyen mesuré par Doppler, exprimé en millimètres de mercure (mmHg). Il reflète la pression moyenne entre l’oreillette gauche et le ventricule gauche pendant la diastole, calculé en intégrant la pression au cours du temps (aire sous la courbe). Les seuils sont : léger (< 5 mmHg), modéré (5-10 mmHg) et sévère (> 10 mmHg).",
    },
    {
        "name": "Mitral_gradient_max",
        "description": "Gradient mitral maximal mesuré par Doppler, exprimé en millimètres de mercure (mmHg). Il correspond à la pression maximale entre l’oreillette gauche et le ventricule gauche pendant la diastole, calculé à partir de la vitesse maximale du flux mitral. Les seuils sont : léger (< 10 mmHg), modéré (10-20 mmHg) et sévère (> 20 mmHg).",
    },
    {
        "name": "Mitrale_SOR",
        "description": "Surface de l'Orifice Régurgitant (SOR) mesurée en centimètres carrés (cm²). Elle quantifie la zone par laquelle le sang régurgite anormalement à travers la valve mitrale. Les seuils sont : léger (< 0,2 cm²), modéré (0,2-0,39 cm²) et sévère (≥ 0,4 cm²).",
    },
    {
        "name": "Mitrale_VR",
        "description": "Volume Régurgité (VR) mesuré en millilitres (mL), représentant le volume de sang régurgitant à travers la valve mitrale pendant la systole. Les seuils sont : léger (< 30 mL), modéré (30-59 mL) et sévère (≥ 60 mL).",
    },
    {
        "name": "Mitrale_rapport_ITV",
        "description": "Rapport des Intégrales Temps-Vitesse (ITV), sans unité, qui compare l’ITV du flux mitral régurgitant à celui du flux aortique. Il permet d’évaluer la sévérité de l’insuffisance mitrale : léger (< 0,2), modéré (0,2-0,5) et sévère (> 0,5).",
    },
    {
        "name": "Mitrale_vena_contracta",
        "description": "Vena Contracta mesurée en millimètres (mm), représentant la largeur maximale du jet régurgitant au niveau de l’orifice mitral. Les seuils sont : léger (< 3 mm), modéré (3-6,9 mm) et sévère (≥ 7 mm).",
    },
    {
        "name": "Prothese_Mitrale_Vmax",
        "description": "Vmax mesurée en mètres par seconde (m/s), correspondant à la vitesse maximale du flux à travers une prothèse mitrale. Elle évalue le fonctionnement hémodynamique de la prothèse.",
    },
    {
        "name": "Prothese_Aorte_Vmax",
        "description": "Vmax mesurée en mètres par seconde (m/s), représentant la vitesse maximale du flux à travers une prothèse aortique. Elle est utilisée pour évaluer la performance de la prothèse et détecter un éventuel dysfonctionnement.",
    },
    {
        "name": "Aorte_surface_fonctionnelle",
        "description": "Surface fonctionnelle (AVA) mesurée en centimètres carrés (cm²), représentant la surface effective de l’orifice valvulaire aortique. Les seuils sont : léger (≥ 1,5 cm²), modéré (1,0-1,49 cm²), sévère (< 1,0 cm²) et critique (< 0,6 cm²).",
    },
    {
        "name": "Aorte_grad_max",
        "description": "Gradient maximal (Grad max) mesuré en millimètres de mercure (mmHg), représentant la pression maximale entre le ventricule gauche et l’aorte pendant la systole. Les seuils sont : léger (< 36 mmHg), modéré (36-64 mmHg) et sévère (≥ 64 mmHg).",
    },
    {
        "name": "Prothese_Aorte_grad_Moyen",
        "description": "Gradient moyen mesuré par Doppler à travers une prothèse aortique, exprimé en millimètres de mercure (mmHg). Il évalue la pression moyenne exercée par le flux sanguin durant la systole. Une valeur élevée peut indiquer une sténose ou un dysfonctionnement de la prothèse.",
    },
    {
        "name": "Prothese_Aorte_IP",
        "description": "Indice de perméabilité mesuré comme le rapport entre la vitesse d'éjection transvalvulaire (VTI) dans le tractus d'éjection du ventricule gauche et la vitesse transprothétique. Ce paramètre sans unité est utilisé pour détecter une sténose ou un dysfonctionnement de la prothèse.",
    },
    {
        "name": "IAO_SOR",
        "description": "Surface de l'Orifice Régurgitant (SOR) mesurée en centimètres carrés (cm²) pour l'insuffisance aortique (IAO). Extraire uniquement si le texte mentionne explicitement 'SOR de l’insuffisance aortique', 'surface régurgitante aortique' ou des termes similaires. Exemple attendu dans le texte : 'SOR mesurée à 0,3 cm².'",
    },
    {
        "name": "IAO_VR",
        "description": "Volume Régurgité (VR) mesuré en millilitres (mL), représentant la quantité de sang régurgitant de l’aorte vers le ventricule gauche par cycle. Un VR supérieur à 60 mL est associé à une IAO sévère.",
    },
    {
        "name": "IAO_PHT",
        "description": "Temps de demi-pression (PHT) mesuré en millisecondes (ms) par Doppler, représentant le temps nécessaire pour que la pression aortique diminue de moitié pendant la diastole. Une valeur inférieure à 200 ms indique une IAO sévère.",
    },
    {
        "name": "IAO_Vena_Contracta",
        "description": "Vena Contracta mesurée en centimètres (cm), correspondant à la largeur maximale du jet régurgitant au niveau de la valve aortique. Une largeur supérieure à 0,6 cm est indicative d’une IAO sévère.",
    },
    {
        "name": "IAO_V_isthmique_telediastolique",
        "description": "Vitesse isthmique télé-diastolique mesurée en centimètres par seconde (cm/s) par Doppler, utilisée pour évaluer la dynamique du flux sanguin dans l’isthme aortique en fin de diastole. Une valeur élevée peut indiquer une insuffisance aortique significative.",
    },
    {
        "name": "RT_V_MAX",
        "description": "Vélocité maximale (Vmax) mesurée par Doppler à travers la valve tricuspide pendant la diastole, exprimée en mètres par seconde (m/s). Une Vmax supérieure à 1 m/s est indicative d’un rétrécissement tricuspide (RT) significatif.",
    },
    {
        "name": "RT_Gradient_moyent",
        "description": "Gradient moyen transvalvulaire mesuré par Doppler, exprimé en millimètres de mercure (mmHg). Il reflète la pression moyenne entre l’oreillette droite et le ventricule droit pendant la diastole. Une valeur supérieure à 5 mmHg indique un RT significatif.",
    },
    {
        "name": "IT_SOR",
        "description": "Surface de l’Orifice Régurgitant (SOR) de l’insuffisance tricuspide (IT) mesurée en centimètres carrés (cm²). Une SOR supérieure à 0,4 cm² est indicative d’une IT sévère.",
    },
    {
        "name": "IT_VR",
        "description": "Volume Régurgité (VR) de l’insuffisance tricuspide (IT) mesuré en millilitres (mL), représentant la quantité de sang régurgitant dans le ventricule droit. Un VR supérieur à 45 mL indique une IT sévère.",
    },
    {
        "name": "IT_flux_veineux_sous_hepatique",
        "description": "Profil du flux sanguin dans les veines sus-hépatiques mesuré par Doppler. Extraire uniquement si le texte mentionne des observations spécifiques sur le flux veineux sous-hépatique, comme une inversion ou une diminution associée à une insuffisance tricuspide sévère.",
    },
    {
        "name": "IT_Vitesse_Onde_E",
        "description": "Vitesse maximale de l’onde E mesurée en centimètres par seconde (cm/s) par Doppler pulsé. Elle reflète le remplissage ventriculaire passif pendant la diastole précoce. Une valeur élevée peut indiquer une élévation des pressions de remplissage ventriculaire.",
    },
    {
        "name": "RP_Vmax",
        "description": "Vélocité maximale (Vmax) mesurée en mètres par seconde (m/s) du flux rétrograde à travers la valve pulmonaire pendant la diastole. Une Vmax élevée peut indiquer une régurgitation pulmonaire significative.",
    },
    {
        "name": "RP_Grad_Moy",
        "description": "Gradient moyen du reflux pulmonaire (RP) mesuré par Doppler, exprimé en millimètres de mercure (mmHg). Une valeur élevée peut indiquer une régurgitation pulmonaire significative.",
    },
    {
        "name": "IP_TD",
        "description": "Temps de décélération (TD) mesuré en millisecondes (ms) par Doppler pulsé, évaluant la durée de réduction du flux pulmonaire après son pic. Une valeur basse peut indiquer une insuffisance pulmonaire sévère.",
    },
    {
        "name": "IP_PHT",
        "description": "Temps de demi-pression (PHT) de l’insuffisance pulmonaire mesuré en millisecondes (ms). Une valeur inférieure à 100 ms est associée à une insuffisance pulmonaire sévère.",
    },
    {
        "name": "IP_indice_regurgitation",
        "description": "Indice de régurgitation exprimé en pourcentage (%), représentant le rapport entre la durée du flux de régurgitation pulmonaire et la durée totale du cycle cardiaque. Une valeur inférieure à 50 % est indicative d’une insuffisance pulmonaire significative.",
    },
    {
        "name": "IP_diam_reg__diam_anneau",
        "description": "Rapport entre le diamètre de régurgitation et le diamètre de l'anneau pulmonaire, exprimé en pourcentage (%). Cette mesure permet d'évaluer la sévérité de l'insuffisance pulmonaire : une valeur supérieure à 50 % est indicative d'une insuffisance pulmonaire sévère.",
    },
    {
        "name": "Prothese_Mitrale_Vmax",
        "description": "Vmax mesurée en mètres par seconde (m/s), représentant la vitesse maximale du flux sanguin à travers une prothèse mitrale. Cette mesure évalue le fonctionnement hémodynamique de la prothèse et peut indiquer une sténose ou un dysfonctionnement en cas de valeur élevée.",
    },
    {
        "name": "Prothese_Mitrale_Grad_Max",
        "description": "Gradient maximal mesuré par Doppler à travers une prothèse mitrale, exprimé en millimètres de mercure (mmHg). Il représente la pression maximale générée par le flux sanguin pendant la diastole. Une valeur élevée peut indiquer une sténose ou un dysfonctionnement.",
    },
    {
        "name": "Prothese_Mitrale_Grad_Moy",
        "description": "Gradient moyen mesuré par Doppler à travers une prothèse mitrale, exprimé en millimètres de mercure (mmHg). Il reflète la pression moyenne exercée par le flux sanguin durant la diastole. Une valeur élevée peut indiquer une sténose ou un dysfonctionnement de la prothèse.",
    },
    {
        "name": "Prothese_Mitrale_Surface_Fonctionnelle",
        "description": "Surface fonctionnelle (ou aire effective d'orifice) mesurée en centimètres carrés (cm²), représentant la surface d'ouverture effective de la prothèse mitrale pendant la diastole. Une valeur réduite peut indiquer une sténose prothétique ou un dysfonctionnement.",
    },
    {
        "name": "Prothese_Mitrale_Rapport_ITV",
        "description": "Rapport des Intégrales Temps-Vitesse (ITV) calculé entre le flux transprothétique et celui du tractus d'éjection du ventricule gauche (TEVG). Ce paramètre, sans unité, aide à détecter un dysfonctionnement valvulaire, tel qu'une sténose prothétique.",
    },
    {
        "name": "Prothese_Mitrale_PHT",
        "description": "Pressure Half-Time (PHT) mesuré en millisecondes (ms), représentant le temps nécessaire pour que la pression transvalvulaire diminue de moitié après le pic initial. Une valeur prolongée peut indiquer une sténose prothétique.",
    },
    {
        "name": "Prothese_Aorte_Vmax",
        "description": "Vmax mesurée en mètres par seconde (m/s), correspondant à la vitesse maximale du flux sanguin à travers une prothèse aortique. Une valeur élevée peut indiquer une sténose ou un dysfonctionnement.",
    },
    {
        "name": "Prothese_Aorte_grad_Moyen",
        "description": "Gradient moyen mesuré par Doppler à travers une prothèse aortique, exprimé en millimètres de mercure (mmHg). Il reflète la pression moyenne exercée par le flux sanguin durant la systole. Une valeur élevée peut indiquer une sténose ou un dysfonctionnement de la prothèse.",
    },
    {
        "name": "Prothese_Aorte_Grad_max",
        "description": "Gradient maximal mesuré par Doppler à travers une prothèse aortique, exprimé en millimètres de mercure (mmHg). Cette mesure évalue la pression maximale générée pendant la systole. Une valeur élevée peut indiquer une sténose ou un dysfonctionnement.",
    },
    {
        "name": "Prothese_Aorte_Surface_Fonctionnelle",
        "description": "Surface fonctionnelle (ou aire effective d’orifice) mesurée en centimètres carrés (cm²) pour une prothèse aortique. Extraire uniquement si le texte mentionne 'surface fonctionnelle de la prothèse aortique', 'aire effective de la prothèse aortique' ou des termes équivalents. Ne pas inclure de valeur inférée ou implicite. Exemple attendu dans le texte : 'Surface fonctionnelle de la prothèse aortique : 1,2 cm².'",
    },
    {
        "name": "Prothese_Aorte_Temps_Acceleration",
        "description": "Temps d'accélération mesuré en millisecondes (ms), correspondant à la durée nécessaire pour atteindre la vitesse maximale (Vmax) à travers une prothèse aortique. Une valeur prolongée peut indiquer un rétrécissement ou un dysfonctionnement de la prothèse.",
    },
    {
        "name": "Prothese_Aorte_IP",
        "description": "Indice de perméabilité calculé comme le rapport entre la vitesse d'éjection transvalvulaire (VTI) du tractus d'éjection du ventricule gauche et la vitesse d'éjection transprothétique. Ce paramètre sans unité aide à évaluer l'efficacité hémodynamique de la prothèse.",
    },
    {
        "name": "PAPS",
        "description": "Pression artérielle pulmonaire systolique (PAPS) mesurée en millimètres de mercure (mmHg). Elle est calculée à partir de la vitesse maximale de l'insuffisance tricuspide (IT) et est essentielle pour évaluer l'hypertension pulmonaire.",
    },
    {
        "name": "PAPD",
        "description": "Pression artérielle pulmonaire diastolique (PAPd) mesurée en millimètres de mercure (mmHg). Elle reflète la pression dans l'artère pulmonaire à la fin de la diastole, souvent utilisée pour évaluer la circulation pulmonaire.",
    },
    {
        "name": "PAPM",
        "description": "Pression artérielle pulmonaire moyenne (PAPm) mesurée en millimètres de mercure (mmHg). Cette mesure reflète la pression moyenne dans l'artère pulmonaire au cours du cycle cardiaque et est utilisée pour diagnostiquer l'hypertension pulmonaire.",
    },
    {
        "name": "IT_Vmax",
        "description": "Vélocité maximale (Vmax) mesurée en mètres par seconde (m/s), représentant la vitesse maximale du flux rétrograde à travers la valve tricuspide. Rechercher explicitement les mentions 'IT Vmax' ou 'vélocité maximale de l’insuffisance tricuspide'.",
    },
    {
        "name": "Temps_Acceleration_AP",
        "description": "Temps d'accélération de l'artère pulmonaire (TAc AP) mesuré en millisecondes (ms), représentant la durée nécessaire pour atteindre le pic de vitesse du flux systolique. Une diminution peut indiquer une pression pulmonaire élevée.",
    },
    {
        "name": "Diametre_AP",
        "description": "Diamètre de l'artère pulmonaire (AP) mesuré en millimètres (mm) par échocardiographie bidimensionnelle. Cette mesure, effectuée en diastole sur une vue parasternal grand axe ou suprasternale, permet de détecter des dilatations associées à l'hypertension pulmonaire ou d'autres pathologies pulmonaires. Une valeur normale est inférieure à 25 mm chez l'adulte.",
    },
    {
        "name": "VCI_Diam",
        "description": "Diamètre de la veine cave inférieure (VCI) mesuré en millimètres (mm) par échocardiographie sous-costale. Cette mesure, réalisée en fin d'expiration et d'inspiration, évalue la taille et la variabilité respiratoire de la VCI. Une valeur normale est inférieure à 21 mm avec une variation respiratoire supérieure à 50 %, permettant d'estimer la pression veineuse centrale et l'état volémique.",
    },
    {
        "name": "QP__QS",
        "description": "Rapport des débits (Qp/Qs) utilisé pour évaluer les shunts intracardiaques ou extracardiaques. Ce ratio, calculé à partir des surfaces des voies d'éjection et des vitesses intégrées mesurées par Doppler, reflète le flux sanguin pulmonaire (Qp) par rapport au flux systémique (Qs). Une valeur normale est de 1:1. Un rapport supérieur à 1,5 indique un shunt gauche-droite, tandis qu'un rapport inférieur à 1 suggère un shunt droite-gauche.",
    },
    {
        "name": "Resistances_Pulmonaires",
        "description": "Résistances pulmonaires (RP) calculées pour évaluer la résistance au flux sanguin dans la circulation pulmonaire. Exprimées en unités Wood (UW) ou dyn·s·cm⁻⁵, elles sont obtenues en divisant le gradient de pression transpulmonaire par le débit cardiaque. Une valeur normale est inférieure à 2 UW. Cette mesure est essentielle pour diagnostiquer et surveiller l’hypertension pulmonaire.",
    },
    {
        "name": "CIA_Berge_Ant",
        "description": "Berge antérieure de la communication interauriculaire (CIA), située en avant de l'orifice septal reliant les oreillettes droite et gauche. Elle est visualisée en échocardiographie bidimensionnelle ou tridimensionnelle, souvent proche de la racine aortique. Son évaluation est cruciale pour éviter les shunts pathologiques ou planifier une fermeture percutanée.",
    },
    {
        "name": "CIA_berge_Posterieure",
        "description": "Berge postérieure de la communication interauriculaire (CIA), située en arrière de l'orifice septal entre les oreillettes droite et gauche. Elle est visualisée en échocardiographie dans des vues apicales ou transœsophagiennes et est essentielle pour évaluer la taille et la localisation de la CIA, ainsi que pour guider les interventions.",
    },
    {
        "name": "CIA_berge_Sup",
        "description": "Berge supérieure de la communication interauriculaire (CIA), localisée à la limite supérieure de l'orifice septal près de la veine cave supérieure. Elle est évaluée en échocardiographie transœsophagienne ou sous-costale pour déterminer son intégrité et planifier une fermeture percutanée ou chirurgicale.",
    },
    {
        "name": "CIA_berge_Inf",
        "description": "Berge inférieure de la communication interauriculaire (CIA), située à la limite inférieure de l'orifice septal, en relation avec la veine cave inférieure. Elle est visualisée en échocardiographie sous-costale ou transœsophagienne et est essentielle pour évaluer l’anatomie de la CIA et planifier son traitement.",
    },
    {
        "name": "CIA_Diam_Max",
        "description": "Diamètre maximal de la communication interauriculaire (CIA) mesuré en millimètres (mm) dans le plan où l'ouverture est la plus large. Cette mesure, obtenue par échocardiographie transœsophagienne ou sous-costale, permet d’évaluer la gravité du shunt interauriculaire et de planifier une intervention.",
    },
    {
        "name": "CIV_Vmax",
        "description": "Vitesse maximale (Vmax) du flux à travers une communication interventriculaire (CIV), mesurée en mètres par seconde (m/s). Cette mesure Doppler évalue le gradient de pression entre les ventricules gauche et droit et aide à diagnostiquer des shunts gauche-droite ou des pathologies associées.",
    },
    {
        "name": "CIV_Diametre",
        "description": "Diamètre de la communication interventriculaire (CIV) mesuré en millimètres (mm), représentant la taille de l'orifice reliant les ventricules gauche et droit. Cette mesure est utilisée pour évaluer la gravité du shunt et planifier les interventions thérapeutiques.",
    },
    {
        "name": "CIV_Nombre",
        "description": "Nombre total de communications interventriculaires (CIV) détectées dans le septum interventriculaire. Cette évaluation, réalisée par échocardiographie en utilisant plusieurs vues, permet d'estimer l'impact hémodynamique et de planifier la prise en charge adaptée.",
    },
]
