from prisma.enums import OperatorFunction, OperatorRole


def get_operator_function(op_function: OperatorFunction) -> str:
    match op_function:
        case OperatorFunction.DOCTOR:
            return "Dr"
        case OperatorFunction.NURSE:
            return "Mr(d)"
        case OperatorFunction.PARAMEDIC:
            return "Mr(d)"
        case _:
            return ""
    pass


def get_operator_role(role: OperatorRole) -> str:

    match role:
        case OperatorRole.MAIN_OPERATOR:
            return "Opérateur principal"
        case OperatorRole.SECONDARY_OPERATOR:
            return "Aide opérateur"
        case OperatorRole.NURSE:
            return "Infirmier en salle"
        case OperatorRole.PARAMEDIC:
            return "Paramédical"
        case _:
            return ""
    pass
