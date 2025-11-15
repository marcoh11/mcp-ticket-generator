from enum import Enum

class DeploymentType(str, Enum):
    INCIDENCIA = "Incidencia"
    REQUERIMIENTO = "Requerimiento"
    NUEVO_SERVICIO = "Nuevo Servicio"
    HOTFIX = "Hotfix"
    OTROS = "Otros"

class ComponentType(str, Enum):
    PIPELINE = "Pipeline"
    LEGACY = "Legacy"

class ScriptType(str, Enum):
    DML = "DML"
    DDL = "DDL"
