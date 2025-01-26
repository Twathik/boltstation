from src.lib.ai_document.system_prompts.french.widgets_prompts.variables_numeriques.ETT import (
    ETT_variables_numerics_description,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.variables_numeriques.Examen_clinique import (
    Examen_clinique_variables_numerics_description,
)


numerical_variables_descriptions = [
    *ETT_variables_numerics_description,
    *Examen_clinique_variables_numerics_description,
]
